# 2Pair Integrated v0.1 — stored-field map

Every stored field maps to an already-existing Calibration metric, Wave 1 field, consent/privacy operation, or technical provenance. No new psychological construct is stored.

## Session

| Field | Existing purpose |
|---|---|
| `session_uuid` | Wave 1 participant/session pseudonymous identifier |
| `release_id` | Calibration release provenance |
| `run_type` | Calibration technical/research separation; integrated values are `TECHNICAL` / `RESEARCH` |
| `protocol_version` | Wave 1 + Calibration protocol provenance |
| `stimulus_set_version` | Calibration/Wave 1 stimulus provenance |
| `training_set_version` | Calibration training provenance |
| `language` | Wave 1 v0.4 language field |
| `device_category` | Calibration coarse device diagnostic |
| `consent_version` | Calibration consent provenance |
| `research_consent` | Calibration affirmative consent evidence |
| `age_18_confirmed` | Calibration 18+ declaration |
| `deletion_token_hash` | Calibration participant-rights mechanism |
| `received_at` | collection / retention provenance |

## Block / attempt

`block_index`, `form_id`, `block_budget_ms`, `technical_preload_ok`, `clean_primary`, `exclusion_reason`, `attempt_number`, `block_elapsed_ms_final`, `block_timed_out`, `page_hidden_during_block` are direct equivalents of existing Calibration mechanics, extended only with `block_index` because one integrated session contains two complementary blocks.

## Pair event

- `pair_id`, A/B asset identity and top/bottom position: existing Wave 1 / Calibration provenance.
- `session_presentation_index`: existing Wave 1 presentation index, now 1–6 across the two blocks.
- `pair_presented`, ready elapsed, choice latency, block elapsed, remaining budget, page hidden: existing Calibration timing variables.
- `choice_identity`: existing A/B rapid choice plus Wave 1 `no_clear_choice`; `timeout` remains the Calibration missingness state.

## Reflection

- `free_text`: Wave 1 optional free-text reason.
- `intensity`: Wave 1 optional ordinal 1–5 reaction intensity; null for `no_clear_choice`.
- `hard_to_identify`: Wave 1 independent reason-identification state.

Only reflections anchored to a PRIMARY-attempt completed response are stored for research analysis. This preserves the Calibration rule that retries are diagnostic and avoids inventing a retry-to-Wave-1 inclusion rule.
