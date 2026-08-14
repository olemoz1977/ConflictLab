import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "future-session"
SCHEMA = ROOT / "docs" / "architecture" / "FUTURE_SESSION_SERVER_SCHEMA_v0.2.sql"


def load_json(name):
    with (CONFIG / name).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def test_stimulus_set_binds_six_current_wave1_pairs_without_releasing_them():
    stimulus = load_json("stimulus-set-v1.json")
    assert stimulus["stimulus_set_version"] == "stimulus-set-v1"
    assert stimulus["lifecycle"] == "DRAFT"
    assert stimulus["content_status"] == "PENDING_STIMULUS_FREEZE"
    assert stimulus["f1_asset_identity_status"] == "COMPLETE"
    assert stimulus["released_at"] is None
    assert stimulus["source_protocol"] == "wave1-v0.3"
    assert stimulus["source_manifest_version"] == "wave1-candidates-v0.2"
    assert len(stimulus["pairs"]) == 6
    assert {p["pair_id"] for p in stimulus["pairs"]} == {
        "CS-PR-01",
        "CS-RE-01",
        "CS-CA-01",
        "CR-PZ-01",
        "CR-FS-01",
        "CR-PO-01",
    }
    assert all(p["is_training"] is False for p in stimulus["pairs"])
    assert set(stimulus["required_pair_fields"]) == {
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
    }


def test_gate_d_starts_non_interpretive():
    gate_d = load_json("gate-d-v1.json")
    assert gate_d["mapping_version"] == "gate-d-v1"
    assert gate_d["stimulus_set_version"] is None
    assert gate_d["lifecycle"] == "DRAFT"
    assert gate_d["mappings"] == []
    assert set(gate_d["allowed_domains"]) == {"CS", "CR"}


def test_gate_e_blocks_domain_interpretation_by_default():
    gate_e = load_json("gate-e-v1.json")
    assert gate_e["aggregation_gate_version"] == "gate-e-v1"
    assert gate_e["domains"]["CS"]["status"] == "NONE"
    assert gate_e["domains"]["CR"]["status"] == "NONE"


def test_reason_map_is_bound_to_f1_stimulus_set_but_remains_draft():
    reason_map = load_json("reason-map-v1.json")
    assert reason_map["stimulus_set_version"] == "stimulus-set-v1"
    assert reason_map["lifecycle"] == "DRAFT"
    assert reason_map["content_status"] == "DRAFT_CONTENT_REVIEW_REQUIRED"
    assert reason_map["released_at"] is None
    assert len(reason_map["items"]) == 48
    assert reason_map["content_policy"]["other_reason_free_text"] == "LOCAL_ONLY_OPTIONAL"
    assert reason_map["content_policy"]["participant_facing_labels_hidden"] is True
    assert set(reason_map["allowed_interpretability_classes"]) == {
        "DOMAIN_CONSISTENT_REASON",
        "CROSS_DOMAIN_REASON",
        "OTHER_REASON",
        "UNRESOLVED",
    }


def test_server_schema_has_no_persistent_participant_identity_or_personal_reflection_fields():
    sql = SCHEMA.read_text(encoding="utf-8")
    executable_sql = "\n".join(
        line for line in sql.splitlines() if not line.lstrip().startswith("--")
    )

    assert "participant_id" not in executable_sql
    assert "free_text" not in executable_sql
    assert "reaction_intensity" not in executable_sql
    assert "derived_results" not in executable_sql
    assert "gate_d_mappings" not in executable_sql


def test_retry_schema_supports_multiple_attempts_per_logical_block():
    sql = SCHEMA.read_text(encoding="utf-8")
    assert "block_attempt_id" in sql
    assert "UNIQUE KEY uq_block_attempt (block_id, block_attempt_number)" in sql
    assert "CHECK (block_attempt_number BETWEEN 1 AND 3)" in sql


def test_raw_pair_events_preserve_stable_assets_and_separate_position():
    sql = SCHEMA.read_text(encoding="utf-8")
    assert "asset_a_id" in sql
    assert "asset_b_id" in sql
    assert "asset_a_position" in sql
    assert "asset_b_position" in sql
    assert "CHECK (asset_a_id <> asset_b_id)" in sql
    assert "CHECK (asset_a_position <> asset_b_position)" in sql


def test_timeout_and_non_exposure_are_distinguishable():
    sql = SCHEMA.read_text(encoding="utf-8")
    assert "pair_presented" in sql
    assert "pair_exposure_number                  TINYINT UNSIGNED NULL" in sql
    assert "pair_ready_elapsed_ms" in sql
    assert "CHECK (choice = 'timeout' OR pair_presented = 1)" in sql
    assert "CHECK (pair_presented = 1 OR pair_exposure_number IS NULL)" in sql
    assert "CHECK (pair_presented = 1 OR pair_ready_elapsed_ms IS NULL)" in sql
    assert "CHECK (pair_presented = 1 OR visual_choice_latency_ms IS NULL)" in sql


def test_page_hidden_semantics_are_block_summary_plus_event_snapshot():
    sql = SCHEMA.read_text(encoding="utf-8")
    assert "page_hidden_during_block" in sql
    assert "page_hidden_before_event" in sql
    rapid_pair_section = sql.split("CREATE TABLE rapid_pair_events", 1)[1].split(
        "CREATE TABLE reflection_reason_events", 1
    )[0]
    assert "page_hidden_during_block" not in rapid_pair_section


def test_reason_server_table_is_structured_opt_in_only_and_versioned():
    sql = SCHEMA.read_text(encoding="utf-8")
    reason_section = sql.split("CREATE TABLE reflection_reason_events", 1)[1].split(
        ") ENGINE=InnoDB", 1
    )[0]
    assert "reason_id" in reason_section
    assert "consent_version" in reason_section
    assert "stimulus_set_version" in reason_section
    assert "reason_map_version" in reason_section
    assert "protocol_version" in reason_section
    assert "free_text" not in reason_section
    assert "reaction_intensity" not in reason_section
