import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

VERIFY_SPEC = importlib.util.spec_from_file_location(
    "verify_future_stimulus_assets", TOOLS / "verify_future_stimulus_assets.py"
)
verify = importlib.util.module_from_spec(VERIFY_SPEC)
assert VERIFY_SPEC.loader is not None
VERIFY_SPEC.loader.exec_module(verify)
sys.modules["verify_future_stimulus_assets"] = verify

IMPORT_SPEC = importlib.util.spec_from_file_location(
    "import_wave1_future_candidates", TOOLS / "import_wave1_future_candidates.py"
)
importer = importlib.util.module_from_spec(IMPORT_SPEC)
assert IMPORT_SPEC.loader is not None
IMPORT_SPEC.loader.exec_module(importer)


def manifest():
    return json.loads(
        (ROOT / "config/future-session/wave1-candidate-manifest-v0.1.json").read_text(encoding="utf-8")
    )


def template():
    return json.loads(
        (ROOT / "config/future-session/stimulus-set-v1.json").read_text(encoding="utf-8")
    )


def make_source_files(source_dir: Path, candidate_manifest: dict):
    source_dir.mkdir(parents=True, exist_ok=True)
    counter = 0
    for pair in candidate_manifest["pairs"]:
        for side in ("a", "b"):
            counter += 1
            name = pair[f"source_asset_{side}_filename"]
            # Unique deterministic bytes; the asset verifier is about provenance/hash identity,
            # not image decoding in this unit test.
            (source_dir / name).write_bytes(f"candidate-{counter}-{name}".encode())


def test_manifest_contains_exactly_six_pairs_and_twelve_unique_source_files():
    data = manifest()
    pairs = importer.validate_manifest(data)
    assert len(pairs) == 6
    source_files = {
        pair[key]
        for pair in pairs
        for key in ("source_asset_a_filename", "source_asset_b_filename")
    }
    assert len(source_files) == 12
    assert {pair["pair_id"] for pair in pairs} == {
        "CS-PR-01",
        "CS-CO-01",
        "CS-OC-01",
        "CR-PZ-01",
        "CR-SY-01",
        "CR-OR-01",
    }


def test_full_import_materializes_canonical_assets_and_verified_draft(tmp_path):
    data = manifest()
    source_dir = tmp_path / "source"
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    make_source_files(source_dir, data)

    plan = importer.build_import_plan(
        manifest=data,
        source_dir=source_dir,
        repo_root=repo_root,
    )
    assert len(plan) == 6

    config = importer.build_draft_config(template(), plan)
    assert config["lifecycle"] == "DRAFT"
    assert config["released_at"] is None
    assert config["content_status"] == "PENDING_STIMULUS_FREEZE"
    assert len(config["pairs"]) == 6

    serialized = json.dumps(config)
    for forbidden in (
        "signal_mapping_status",
        "asset_a_direction",
        "asset_b_direction",
        "mapping_status",
    ):
        assert forbidden not in serialized

    importer.materialize(plan)
    result = verify.verify_config(config, repo_root)
    assert result["status"] == "PASS"
    assert result["verified_pair_count"] == 6
    assert result["verified_asset_count"] == 12

    for pair in config["pairs"]:
        assert pair["asset_a_path"].startswith("assets/future-session/stimulus-set-v1/")
        assert pair["asset_b_path"].startswith("assets/future-session/stimulus-set-v1/")
        assert (repo_root / pair["asset_a_path"]).is_file()
        assert (repo_root / pair["asset_b_path"]).is_file()
        assert len(pair["asset_a_sha256"]) == 64
        assert len(pair["asset_b_sha256"]) == 64


def test_missing_source_file_blocks_import(tmp_path):
    data = manifest()
    source_dir = tmp_path / "source"
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    make_source_files(source_dir, data)
    missing = source_dir / data["pairs"][0]["source_asset_a_filename"]
    missing.unlink()

    with pytest.raises(importer.ImportError, match="missing source asset"):
        importer.build_import_plan(
            manifest=data,
            source_dir=source_dir,
            repo_root=repo_root,
        )


def test_byte_identical_ab_pair_blocks_import(tmp_path):
    data = manifest()
    source_dir = tmp_path / "source"
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    make_source_files(source_dir, data)

    first = data["pairs"][0]
    same = b"same-exact-asset"
    (source_dir / first["source_asset_a_filename"]).write_bytes(same)
    (source_dir / first["source_asset_b_filename"]).write_bytes(same)

    with pytest.raises(importer.ImportError, match="byte-identical"):
        importer.build_import_plan(
            manifest=data,
            source_dir=source_dir,
            repo_root=repo_root,
        )


def test_import_does_not_release_template():
    data = template()
    data["lifecycle"] = "RELEASED"
    data["content_status"] = "FROZEN"
    data["released_at"] = "2026-08-14"
    with pytest.raises(importer.ImportError, match="must remain DRAFT"):
        importer.build_draft_config(data, [])
