#!/usr/bin/env python3
"""Import the six factual Wave 1 F0 candidate assets into a future stimulus-set draft.

This tool performs byte identity/provenance work only. It never writes Gate D or Gate E
interpretation and never marks a stimulus set RELEASED.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

from verify_future_stimulus_assets import VerificationError, sha256_file, verify_config


MIME_BY_SUFFIX = {
    ".webp": "image/webp",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
}


class ImportError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ImportError(message)


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ImportError(f"cannot load {path}: {exc}") from exc
    _require(isinstance(data, dict), f"{path}: JSON object required")
    return data


def validate_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    _require(
        manifest.get("schema") == "conflictlab.future-stimulus-candidate-manifest.v1",
        "unsupported candidate manifest schema",
    )
    _require(manifest.get("status") == "F0_CANDIDATE_INVENTORY", "manifest must be F0 inventory")
    pairs = manifest.get("pairs")
    _require(isinstance(pairs, list) and pairs, "candidate manifest must contain pairs")

    seen_pairs: set[str] = set()
    seen_asset_ids: set[str] = set()
    seen_source_names: set[str] = set()

    required = {
        "pair_id",
        "source_family",
        "source_asset_a_filename",
        "source_asset_b_filename",
        "asset_a_id",
        "asset_b_id",
        "is_training",
    }

    for index, pair in enumerate(pairs):
        _require(isinstance(pair, dict), f"pairs[{index}] must be an object")
        missing = required.difference(pair)
        _require(not missing, f"pairs[{index}] missing {sorted(missing)[0]}")

        pair_id = pair["pair_id"]
        _require(isinstance(pair_id, str) and pair_id, f"pairs[{index}].pair_id invalid")
        _require(pair_id not in seen_pairs, f"duplicate pair_id: {pair_id}")
        seen_pairs.add(pair_id)

        _require(isinstance(pair["is_training"], bool), f"{pair_id}.is_training must be boolean")
        _require(isinstance(pair["source_family"], str) and pair["source_family"],
                 f"{pair_id}.source_family invalid")

        for side in ("a", "b"):
            source_name = pair[f"source_asset_{side}_filename"]
            asset_id = pair[f"asset_{side}_id"]
            _require(isinstance(source_name, str) and Path(source_name).name == source_name,
                     f"{pair_id}: source filename must be a basename")
            _require(source_name not in seen_source_names, f"source filename reused: {source_name}")
            seen_source_names.add(source_name)
            _require(isinstance(asset_id, str) and asset_id, f"{pair_id}: asset ID required")
            _require(asset_id not in seen_asset_ids, f"asset ID reused: {asset_id}")
            seen_asset_ids.add(asset_id)

        _require(pair["asset_a_id"] != pair["asset_b_id"], f"{pair_id}: A/B asset IDs must differ")

    return pairs


def build_import_plan(
    *,
    manifest: dict[str, Any],
    source_dir: Path,
    repo_root: Path,
    canonical_dir: str = "assets/future-session/stimulus-set-v1",
) -> list[dict[str, Any]]:
    pairs = validate_manifest(manifest)
    source_dir = source_dir.resolve()
    repo_root = repo_root.resolve()
    canonical_root = (repo_root / canonical_dir).resolve()
    _require(canonical_root.is_relative_to(repo_root), "canonical destination escapes repository root")

    plan: list[dict[str, Any]] = []
    for pair in pairs:
        item: dict[str, Any] = {
            "pair_id": pair["pair_id"],
            "source_family": pair["source_family"],
            "is_training": pair["is_training"],
        }
        for side in ("a", "b"):
            source_name = pair[f"source_asset_{side}_filename"]
            source = source_dir / source_name
            _require(source.is_file(), f"missing source asset: {source_name}")
            suffix = source.suffix.lower()
            mime = MIME_BY_SUFFIX.get(suffix)
            _require(mime is not None, f"unsupported source image extension: {source_name}")

            asset_id = pair[f"asset_{side}_id"]
            destination = canonical_root / f"{asset_id}{suffix}"
            rel_destination = destination.relative_to(repo_root).as_posix()

            item[f"asset_{side}_id"] = asset_id
            item[f"asset_{side}_source"] = source
            item[f"asset_{side}_destination"] = destination
            item[f"asset_{side}_path"] = rel_destination
            item[f"asset_{side}_sha256"] = sha256_file(source)
            item[f"asset_{side}_mime_type"] = mime

        _require(
            item["asset_a_sha256"] != item["asset_b_sha256"],
            f"{pair['pair_id']}: A/B source assets are byte-identical",
        )
        plan.append(item)

    return plan


def build_draft_config(template: dict[str, Any], plan: list[dict[str, Any]]) -> dict[str, Any]:
    _require(template.get("schema") == "conflictlab.stimulus-set.v1", "invalid stimulus-set template")
    _require(template.get("lifecycle") == "DRAFT", "import target must remain DRAFT")
    _require(not template.get("released_at"), "DRAFT import target cannot carry released_at")

    result = json.loads(json.dumps(template))
    result["lifecycle"] = "DRAFT"
    result["content_status"] = "PENDING_STIMULUS_FREEZE"
    result["released_at"] = None
    result["pairs"] = []

    for item in plan:
        result["pairs"].append(
            {
                "pair_id": item["pair_id"],
                "asset_a_id": item["asset_a_id"],
                "asset_b_id": item["asset_b_id"],
                "asset_a_path": item["asset_a_path"],
                "asset_b_path": item["asset_b_path"],
                "asset_a_sha256": item["asset_a_sha256"],
                "asset_b_sha256": item["asset_b_sha256"],
                "asset_a_mime_type": item["asset_a_mime_type"],
                "asset_b_mime_type": item["asset_b_mime_type"],
                "is_training": item["is_training"],
                "source_family": item["source_family"],
            }
        )

    return result


def materialize(plan: list[dict[str, Any]]) -> None:
    for item in plan:
        for side in ("a", "b"):
            source: Path = item[f"asset_{side}_source"]
            destination: Path = item[f"asset_{side}_destination"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            if sha256_file(destination) != item[f"asset_{side}_sha256"]:
                raise ImportError(f"copy verification failed: {destination}")


def main(argv: list[str] | None = None) -> int:
    repo_root_default = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", required=True, help="directory containing the 12 source images")
    parser.add_argument(
        "--manifest",
        default="config/future-session/wave1-candidate-manifest-v0.1.json",
    )
    parser.add_argument(
        "--template",
        default="config/future-session/stimulus-set-v1.json",
    )
    parser.add_argument(
        "--output",
        default="config/future-session/stimulus-set-v1.json",
    )
    parser.add_argument(
        "--canonical-dir",
        default="assets/future-session/stimulus-set-v1",
    )
    parser.add_argument("--repo-root", default=str(repo_root_default))
    parser.add_argument(
        "--write",
        action="store_true",
        help="copy canonical assets and write DRAFT config; without this flag only print the plan",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="allow replacing an existing non-empty DRAFT output config",
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    manifest_path = Path(args.manifest)
    template_path = Path(args.template)
    output_path = Path(args.output)
    if not manifest_path.is_absolute():
        manifest_path = repo_root / manifest_path
    if not template_path.is_absolute():
        template_path = repo_root / template_path
    if not output_path.is_absolute():
        output_path = repo_root / output_path

    try:
        manifest = load_json(manifest_path)
        template = load_json(template_path)
        plan = build_import_plan(
            manifest=manifest,
            source_dir=Path(args.source_dir),
            repo_root=repo_root,
            canonical_dir=args.canonical_dir,
        )
        config = build_draft_config(template, plan)

        if not args.write:
            printable = {
                "status": "DRY_RUN",
                "pair_count": len(plan),
                "asset_count": len(plan) * 2,
                "output": str(output_path),
                "pairs": config["pairs"],
            }
            print(json.dumps(printable, ensure_ascii=False, indent=2))
            return 0

        if output_path.exists() and not args.force:
            existing = load_json(output_path)
            if existing.get("pairs"):
                raise ImportError("output config already contains pairs; use --force only after review")
            if existing.get("lifecycle") != "DRAFT":
                raise ImportError("refusing to overwrite non-DRAFT output config")

        materialize(plan)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        verify_config(config, repo_root)
        print(json.dumps({
            "status": "IMPORTED_DRAFT",
            "pair_count": len(plan),
            "asset_count": len(plan) * 2,
            "output": str(output_path),
        }, ensure_ascii=False))
        return 0
    except (ImportError, VerificationError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
