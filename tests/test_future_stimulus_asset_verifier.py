import hashlib
import importlib.util
import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "verify_future_stimulus_assets.py"
SPEC = importlib.util.spec_from_file_location("verify_future_stimulus_assets", MODULE_PATH)
verifier = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(verifier)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def base_config():
    return {
        "schema": "conflictlab.stimulus-set.v1",
        "stimulus_set_version": "stimulus-set-test",
        "lifecycle": "DRAFT",
        "content_status": "PENDING_STIMULUS_FREEZE",
        "released_at": None,
        "required_pair_fields": [
            "pair_id",
            "asset_a_id",
            "asset_b_id",
            "asset_a_path",
            "asset_b_path",
            "asset_a_sha256",
            "asset_b_sha256",
            "asset_a_mime_type",
            "asset_b_mime_type",
            "is_training",
            "source_family",
        ],
        "allowed_mime_types": ["image/webp", "image/png", "image/jpeg"],
        "pairs": [],
    }


def write_asset(root: Path, rel: str, data: bytes) -> str:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return digest(data)


def add_pair(config, root: Path):
    a = b"synthetic-webp-A"
    b = b"synthetic-webp-B"
    hash_a = write_asset(root, "assets/future-session/test/P1-A.webp", a)
    hash_b = write_asset(root, "assets/future-session/test/P1-B.webp", b)
    config["pairs"] = [
        {
            "pair_id": "P1",
            "asset_a_id": "P1-A",
            "asset_b_id": "P1-B",
            "asset_a_path": "assets/future-session/test/P1-A.webp",
            "asset_b_path": "assets/future-session/test/P1-B.webp",
            "asset_a_sha256": hash_a,
            "asset_b_sha256": hash_b,
            "asset_a_mime_type": "image/webp",
            "asset_b_mime_type": "image/webp",
            "is_training": False,
            "source_family": "CS-PR",
        }
    ]
    return hash_a, hash_b


def test_empty_draft_catalog_is_valid_baseline(tmp_path):
    result = verifier.verify_config(base_config(), tmp_path)
    assert result["status"] == "PASS"
    assert result["verified_pair_count"] == 0
    assert result["verified_asset_count"] == 0


def test_released_catalog_cannot_be_empty(tmp_path):
    config = base_config()
    config.update(lifecycle="RELEASED", content_status="FROZEN", released_at="2026-08-14")
    with pytest.raises(verifier.VerificationError, match="at least one pair"):
        verifier.verify_config(config, tmp_path)


def test_exact_bytes_and_hashes_pass(tmp_path):
    config = base_config()
    hash_a, hash_b = add_pair(config, tmp_path)
    result = verifier.verify_config(config, tmp_path)
    assert result["verified_pair_count"] == 1
    assert result["verified_asset_count"] == 2
    assert result["pairs"][0]["asset_a"]["sha256"] == hash_a
    assert result["pairs"][0]["asset_b"]["sha256"] == hash_b


def test_released_frozen_catalog_with_exact_assets_passes(tmp_path):
    config = base_config()
    add_pair(config, tmp_path)
    config.update(lifecycle="RELEASED", content_status="FROZEN", released_at="2026-08-14")
    result = verifier.verify_config(config, tmp_path)
    assert result["lifecycle"] == "RELEASED"
    assert result["verified_pair_count"] == 1


def test_changed_bytes_fail_same_filename(tmp_path):
    config = base_config()
    add_pair(config, tmp_path)
    path = tmp_path / config["pairs"][0]["asset_a_path"]
    path.write_bytes(b"different-pixels-under-same-name")
    with pytest.raises(verifier.VerificationError, match="SHA-256 mismatch"):
        verifier.verify_config(config, tmp_path)


def test_missing_asset_fails(tmp_path):
    config = base_config()
    add_pair(config, tmp_path)
    (tmp_path / config["pairs"][0]["asset_b_path"]).unlink()
    with pytest.raises(verifier.VerificationError, match="file not found"):
        verifier.verify_config(config, tmp_path)


def test_remote_and_parent_paths_fail(tmp_path):
    config = base_config()
    add_pair(config, tmp_path)
    config["pairs"][0]["asset_a_path"] = "https://example.com/A.webp"
    with pytest.raises(verifier.VerificationError, match="remote URLs are forbidden"):
        verifier.verify_config(config, tmp_path)

    config = base_config()
    add_pair(config, tmp_path)
    config["pairs"][0]["asset_a_path"] = "../A.webp"
    with pytest.raises(verifier.VerificationError, match="parent traversal"):
        verifier.verify_config(config, tmp_path)


def test_mime_extension_mismatch_fails(tmp_path):
    config = base_config()
    add_pair(config, tmp_path)
    config["pairs"][0]["asset_a_mime_type"] = "image/png"
    with pytest.raises(verifier.VerificationError, match="MIME/extension mismatch"):
        verifier.verify_config(config, tmp_path)


def test_identical_ab_bytes_fail_even_with_different_ids(tmp_path):
    config = base_config()
    same = b"same-image"
    hash_a = write_asset(tmp_path, "assets/future-session/test/P1-A.webp", same)
    hash_b = write_asset(tmp_path, "assets/future-session/test/P1-B.webp", same)
    config["pairs"] = [
        {
            "pair_id": "P1",
            "asset_a_id": "P1-A",
            "asset_b_id": "P1-B",
            "asset_a_path": "assets/future-session/test/P1-A.webp",
            "asset_b_path": "assets/future-session/test/P1-B.webp",
            "asset_a_sha256": hash_a,
            "asset_b_sha256": hash_b,
            "asset_a_mime_type": "image/webp",
            "asset_b_mime_type": "image/webp",
            "is_training": False,
            "source_family": "CS-PR",
        }
    ]
    with pytest.raises(verifier.VerificationError, match="A/B asset bytes are identical"):
        verifier.verify_config(config, tmp_path)


def test_same_asset_id_cannot_point_to_different_bytes(tmp_path):
    config = base_config()
    add_pair(config, tmp_path)
    first = config["pairs"][0]
    a2 = b"another-A"
    b2 = b"another-B"
    hash_a2 = write_asset(tmp_path, "assets/future-session/test/P2-A.webp", a2)
    hash_b2 = write_asset(tmp_path, "assets/future-session/test/P2-B.webp", b2)
    config["pairs"].append(
        {
            "pair_id": "P2",
            "asset_a_id": first["asset_a_id"],
            "asset_b_id": "P2-B",
            "asset_a_path": "assets/future-session/test/P2-A.webp",
            "asset_b_path": "assets/future-session/test/P2-B.webp",
            "asset_a_sha256": hash_a2,
            "asset_b_sha256": hash_b2,
            "asset_a_mime_type": "image/webp",
            "asset_b_mime_type": "image/webp",
            "is_training": False,
            "source_family": "CS-CO",
        }
    )
    with pytest.raises(verifier.VerificationError, match="reused with different provenance"):
        verifier.verify_config(config, tmp_path)


def test_cli_current_repo_draft_config_passes_without_assets():
    config = json.loads((ROOT / "config/future-session/stimulus-set-v1.json").read_text())
    result = verifier.verify_config(config, ROOT)
    assert result["lifecycle"] == "DRAFT"
    assert result["verified_pair_count"] == 0
