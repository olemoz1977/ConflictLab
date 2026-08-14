#!/usr/bin/env python3
"""Verify future-session stimulus asset identity against repository bytes.

The verifier is intentionally local/repository-based. It never downloads assets and never
infers psychological signal. It only checks factual identity/provenance required for F1/F2
stimulus freeze.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ID_RE = re.compile(r"^[A-Za-z0-9._:-]+$")
MIME_BY_SUFFIX = {
    ".webp": "image/webp",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
}


class VerificationError(ValueError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def _safe_repo_path(repo_root: Path, raw: Any, field: str) -> Path:
    _require(isinstance(raw, str) and raw != "", f"{field}: non-empty path required")
    _require("\\" not in raw, f"{field}: use repository POSIX path separators")
    _require("://" not in raw, f"{field}: remote URLs are forbidden")

    posix = PurePosixPath(raw)
    _require(not posix.is_absolute(), f"{field}: absolute path is forbidden")
    _require(".." not in posix.parts, f"{field}: parent traversal is forbidden")
    _require("." not in posix.parts, f"{field}: dot path segments are forbidden")

    path = (repo_root / Path(*posix.parts)).resolve()
    root = repo_root.resolve()
    _require(path.is_relative_to(root), f"{field}: path escapes repository root")
    return path


def _validate_asset(
    *,
    repo_root: Path,
    pair_id: str,
    side: str,
    pair: dict[str, Any],
    allowed_mime: set[str],
    seen_ids: dict[str, tuple[str, str]],
    seen_paths: dict[str, str],
) -> dict[str, str]:
    prefix = f"asset_{side}"
    asset_id = pair.get(f"{prefix}_id")
    raw_path = pair.get(f"{prefix}_path")
    expected_hash = pair.get(f"{prefix}_sha256")
    mime = pair.get(f"{prefix}_mime_type")

    _require(isinstance(asset_id, str) and ID_RE.fullmatch(asset_id) is not None,
             f"{pair_id}.{prefix}_id: invalid stable asset ID")
    _require(isinstance(expected_hash, str) and SHA256_RE.fullmatch(expected_hash) is not None,
             f"{pair_id}.{prefix}_sha256: lowercase SHA-256 required")
    _require(isinstance(mime, str) and mime in allowed_mime,
             f"{pair_id}.{prefix}_mime_type: unsupported MIME type")

    path = _safe_repo_path(repo_root, raw_path, f"{pair_id}.{prefix}_path")
    _require(path.is_file(), f"{pair_id}.{prefix}_path: file not found: {raw_path}")

    suffix_mime = MIME_BY_SUFFIX.get(path.suffix.lower())
    _require(suffix_mime is not None,
             f"{pair_id}.{prefix}_path: unsupported image extension {path.suffix}")
    _require(suffix_mime == mime,
             f"{pair_id}.{prefix}: MIME/extension mismatch ({mime} vs {path.suffix})")

    actual_hash = sha256_file(path)
    _require(actual_hash == expected_hash,
             f"{pair_id}.{prefix}: SHA-256 mismatch expected={expected_hash} actual={actual_hash}")

    prior_id = seen_ids.get(asset_id)
    if prior_id is not None:
        prior_path, prior_hash = prior_id
        _require(prior_path == str(raw_path) and prior_hash == actual_hash,
                 f"asset ID {asset_id} is reused with different provenance")
    else:
        seen_ids[asset_id] = (str(raw_path), actual_hash)

    prior_asset_for_path = seen_paths.get(str(raw_path))
    _require(prior_asset_for_path in (None, asset_id),
             f"path {raw_path} is assigned to multiple asset IDs: {prior_asset_for_path}, {asset_id}")
    seen_paths[str(raw_path)] = asset_id

    return {
        "asset_id": asset_id,
        "path": str(raw_path),
        "sha256": actual_hash,
        "mime_type": mime,
    }


def verify_config(config: dict[str, Any], repo_root: Path) -> dict[str, Any]:
    _require(config.get("schema") == "conflictlab.stimulus-set.v1",
             "unsupported stimulus-set schema")
    version = config.get("stimulus_set_version")
    _require(isinstance(version, str) and ID_RE.fullmatch(version) is not None,
             "invalid stimulus_set_version")

    lifecycle = config.get("lifecycle")
    _require(lifecycle in {"DRAFT", "RELEASED"}, "lifecycle must be DRAFT or RELEASED")

    required_fields = config.get("required_pair_fields")
    _require(isinstance(required_fields, list) and all(isinstance(x, str) for x in required_fields),
             "required_pair_fields must be a string array")

    allowed_mime_raw = config.get("allowed_mime_types")
    _require(isinstance(allowed_mime_raw, list) and len(allowed_mime_raw) > 0,
             "allowed_mime_types must be a non-empty array")
    allowed_mime = set(allowed_mime_raw)
    _require(allowed_mime.issubset(set(MIME_BY_SUFFIX.values())),
             "allowed_mime_types contains unsupported verifier MIME")

    pairs = config.get("pairs")
    _require(isinstance(pairs, list), "pairs must be an array")

    if lifecycle == "RELEASED":
        _require(config.get("content_status") == "FROZEN",
                 "RELEASED stimulus set requires content_status=FROZEN")
        _require(isinstance(config.get("released_at"), str) and config["released_at"],
                 "RELEASED stimulus set requires released_at")
        _require(len(pairs) > 0, "RELEASED stimulus set must contain at least one pair")

    seen_pair_ids: set[str] = set()
    seen_ids: dict[str, tuple[str, str]] = {}
    seen_paths: dict[str, str] = {}
    verified_pairs: list[dict[str, Any]] = []

    for index, pair in enumerate(pairs):
        _require(isinstance(pair, dict), f"pairs[{index}] must be an object")
        missing = [field for field in required_fields if field not in pair]
        _require(not missing, f"pairs[{index}] missing required field: {missing[0]}")

        pair_id = pair.get("pair_id")
        _require(isinstance(pair_id, str) and ID_RE.fullmatch(pair_id) is not None,
                 f"pairs[{index}].pair_id invalid")
        _require(pair_id not in seen_pair_ids, f"duplicate pair_id: {pair_id}")
        seen_pair_ids.add(pair_id)

        _require(isinstance(pair.get("is_training"), bool),
                 f"{pair_id}.is_training must be boolean")
        source_family = pair.get("source_family")
        _require(isinstance(source_family, str) and ID_RE.fullmatch(source_family) is not None,
                 f"{pair_id}.source_family invalid")

        asset_a = _validate_asset(
            repo_root=repo_root,
            pair_id=pair_id,
            side="a",
            pair=pair,
            allowed_mime=allowed_mime,
            seen_ids=seen_ids,
            seen_paths=seen_paths,
        )
        asset_b = _validate_asset(
            repo_root=repo_root,
            pair_id=pair_id,
            side="b",
            pair=pair,
            allowed_mime=allowed_mime,
            seen_ids=seen_ids,
            seen_paths=seen_paths,
        )
        _require(asset_a["asset_id"] != asset_b["asset_id"],
                 f"{pair_id}: A/B asset IDs must differ")
        _require(asset_a["sha256"] != asset_b["sha256"],
                 f"{pair_id}: A/B asset bytes are identical")

        verified_pairs.append({
            "pair_id": pair_id,
            "is_training": pair["is_training"],
            "source_family": source_family,
            "asset_a": asset_a,
            "asset_b": asset_b,
        })

    return {
        "status": "PASS",
        "stimulus_set_version": version,
        "lifecycle": lifecycle,
        "verified_pair_count": len(verified_pairs),
        "verified_asset_count": len(seen_ids),
        "pairs": verified_pairs,
    }


def load_config(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
        data = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        raise VerificationError(f"cannot load config: {exc}") from exc
    _require(isinstance(data, dict), "stimulus config must be a JSON object")
    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        default="config/future-session/stimulus-set-v1.json",
        help="repository-relative or absolute stimulus-set JSON path",
    )
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="repository root used to resolve canonical asset paths",
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = repo_root / config_path

    try:
        result = verify_config(load_config(config_path), repo_root)
    except VerificationError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1

    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
