import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "future-session"
SCHEMA = ROOT / "docs" / "architecture" / "FUTURE_SESSION_SERVER_SCHEMA_v0.2.sql"


def load_json(name):
    with (CONFIG / name).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def test_gate_d_starts_non_interpretive():
    gate_d = load_json("gate-d-v1.json")
    assert gate_d["mapping_version"] == "gate-d-v1"
    assert gate_d["lifecycle"] == "DRAFT"
    assert gate_d["mappings"] == []
    assert set(gate_d["allowed_domains"]) == {"CS", "CR"}


def test_gate_e_blocks_domain_interpretation_by_default():
    gate_e = load_json("gate-e-v1.json")
    assert gate_e["aggregation_gate_version"] == "gate-e-v1"
    assert gate_e["domains"]["CS"]["status"] == "NONE"
    assert gate_e["domains"]["CR"]["status"] == "NONE"


def test_reason_map_waits_for_stimulus_freeze():
    reason_map = load_json("reason-map-v1.json")
    assert reason_map["content_status"] == "PENDING_STIMULUS_FREEZE"
    assert reason_map["items"] == []
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


def test_reason_server_table_is_structured_opt_in_only():
    sql = SCHEMA.read_text(encoding="utf-8")
    assert "CREATE TABLE reflection_reason_events" in sql
    assert "reason_id" in sql
    assert "consent_version" in sql
