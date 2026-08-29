# ConflictLab — Timing Export Schema v0.1

**Schema ID:** `timing-export-v0.1`  
**Scope:** authenticated admin export of server-side mechanical timing research data only.  
**Release family:** `calibration-v0.1`

## 1. Purpose

Provide a reproducible CSV for timing-calibration analysis without direct database access and without exporting local-only reflection content.

The export is generated on demand by authenticated `server/data_admin.php` and streamed directly to the browser. No CSV file is intentionally persisted in the public web directory.

## 2. Explicit exclusions

The export MUST NOT contain:

```text
participant name
participant email
phone
employer
precise location
IP/access-log data
full user-agent
delection_token_hash
message_id
session_id
A/B selected asset identity
reason_id
open reflection text
reaction intensity
reason-response latency
intensity-response latency
derived directional result
CS/CR person score or label
```

## 3. Columns

CSV columns in order:

```text
export_schema_version
run_id
received_at
run_type
clean_primary
exclusion_reason
form_id
device_category
release_id
protocol_version
stimulus_set_version
block_budget_ms
consent_version
research_consent
age_18_confirmed
attempt_number
block_elapsed_ms_final
block_timed_out
page_hidden_during_block
pair_id
position_in_block
pair_exposure_number
pair_presented
pair_ready_elapsed_ms
response_status
visual_choice_latency_ms
block_elapsed_ms_at_event
remaining_budget_at_pair_start_ms
page_hidden_before_event
```

`run_id` is a database-local analysis key. It is not a persistent cross-study participant identifier.

## 4. Filters

The authenticated export UI supports:

```text
run_type: ALL | TECHNICAL | CALIBRATION
form: ALL | F2-A | F2-B
device: ALL | mobile | tablet | desktop | unknown
status: ALL | ELIGIBLE | EXCLUDED
```

`ELIGIBLE` means:

```text
run_type = CALIBRATION
AND clean_primary = 1
```

The export does not itself decide the 6000 ms outcome. Decision logic remains defined by the frozen timing-calibration specification/preregistration.

## 5. Versioning

Any column addition/removal, semantic change, eligibility semantic change, or newly exportable data class requires a new export schema version.

A cosmetic filename/UI change does not require a new schema version if the CSV semantics are unchanged.

## 6. Privacy boundary

This schema exists because the server timing dataset is deliberately narrower than the local product experience.

```text
LOCAL REFLECTION DATA
!=
SERVER TIMING RESEARCH DATA
!=
ADMIN TIMING EXPORT
```

No later feature may silently broaden this export merely because additional local data exist in the participant interface.
