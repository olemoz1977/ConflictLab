# ConflictLab — Future Session Implementation Baseline Status v0.2

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Base:** `44426f715103a90bc79967d2655b75c1f33bbd2c`  
**PR:** Draft PR #2  
**Status:** IMPLEMENTATION BASELINE — REFLECTION CONTENT BLOCKED BY STIMULUS FREEZE

## 1. Decision gate

The seven blocking implementation decisions from `RESULT_CALCULATION_ARCH_v0.2_IMPLEMENTATION_REVIEW.md` are resolved by ADR-010.

```text
M1  block timer authority          CLOSED
M2  retry limit                    CLOSED
M3  reflection trigger             CLOSED
M4  reason catalog architecture    CLOSED
    reason catalog content         PENDING STIMULUS FREEZE
M5  Gate D / Gate E storage        CLOSED
M6  session vs participant ID      CLOSED
M7  reflection server purpose      CLOSED
```

Binding ADRs:

- `ADR-010-future-session-execution-boundary.md`
- `ADR-011-timeout-presentation-semantics.md`
- `ADR-012-monotonic-timing-quantization.md`

Where ADR-010 conflicts with the earlier implementation-review recommendation, ADR-010 is authoritative.

## 2. Important audit corrections now encoded

The implementation baseline explicitly prevents several failure modes that were still possible in the review document:

1. **Client monotonic time is authoritative.** Server receive time never adjudicates whether a tap beat the deadline.
2. **No ACK wait in the rapid block.** A choice is captured locally, the next pair can advance immediately, and upload happens asynchronously through the outbox.
3. **Backgrounding does not pause the experimental clock.** It is logged as context only.
4. **Retry identity is explicit.** A logical `block_id` may contain up to three distinct `block_attempt_id` values.
5. **Shown timeout != non-exposure.** A pair never made interactive before the shared deadline does not enter the Coverage presentation denominator.
6. **Exposure number counts actual exposures, not attempt numbers.** A pair first shown on retry can have `block_attempt_number = 2` and `pair_exposure_number = 1`.
7. **A/B are stable asset identities, not screen positions.** Raw events preserve both asset IDs and their concrete randomized/counterbalanced positions.
8. **Gate D is bound to exact stimulus identity.** A mapping cannot silently carry across a changed stimulus-set version or changed A/B assets.
9. **Full precision decides, integer ms are stored.** `performance.now()` is compared before quantization; persisted elapsed telemetry is floored to integer milliseconds.
10. **409 is true idempotency only.** Same immutable ID with different persisted content is a 422 conflict, never an acknowledged duplicate.

## 3. Implemented client layers

### Rapid block core

`src/future_session/rapid_block_core.mjs`

- exactly three pairs per rapid block;
- monotonic deadline;
- maximum three total attempts;
- timeout/non-exposure provenance;
- actual exposure numbering;
- page-hidden diagnostics without timer pause;
- primary-first reflection anchor provenance;
- stable asset IDs separate from positions.

### Local-first transport

`src/future_session/event_outbox.mjs`  
`src/future_session/http_transport.mjs`

- IndexedDB durable outbox;
- canonical immutable message identity;
- exponential retry backoff;
- network/5xx/429 retry;
- permanent 4xx rejected for diagnostics;
- concurrent flush de-duplication;
- no coupling between network ACK and participant interaction timing.

### Calculation Engine

`src/future_session/calculation_engine.mjs`

- first-attempt, non-training evidence only;
- retry never fills primary directional evidence;
- Gate D VALIDATED mappings only;
- exact stimulus-set + asset identity match required;
- shown timeout affects Coverage but not direction;
- non-exposure is not counted as presentation;
- no intensity, latency, reason, or retry weighting.

### Evidence Engine

`src/future_session/evidence_engine.mjs`

- claim-limiting layer only;
- never modifies direction or Coverage;
- single observation remains claim level 0;
- repeated pair-specific observation before Gate E remains level 1;
- Gate E VALID may authorize level 2 domain language;
- retry divergence, missingness, position strategy and retry-anchored reflection become narrative constraints, not score modifiers.

### LLM boundary

`src/future_session/llm_contract.mjs`

- whitelist-built depersonalized generation contract;
- no session/event/asset IDs, raw latency, intensity or free text;
- exact allowed claim level passed through;
- explicit forbidden-output instructions;
- `LOCAL_ONLY_BY_DEFAULT` delivery policy;
- no LLM provider/API call is implemented in this baseline.

### Local result pipeline

`src/future_session/result_pipeline.mjs`

The required derivation path is composed as:

```text
RAW EVENTS
  -> Calculation Engine
  -> Evidence Engine
  -> depersonalized generation contract
```

This prevents a future UI from bypassing the Evidence Engine and narrating a stronger claim directly from a numeric balance.

## 4. Implemented config/source-of-truth layer

`config/future-session/`

- `stimulus-set-v1.json`
- `gate-d-v1.json`
- `gate-e-v1.json`
- `reason-map-v1.json`

All current v1 artifacts are deliberately `DRAFT` / non-interpretive.

Current safety state:

```text
stimulus set content   PENDING_STIMULUS_FREEZE
Gate D mappings        empty
Gate E CS              NONE
Gate E CR              NONE
reason-map items       empty
```

A RELEASED version is immutable. Any methodological change after release requires a new versioned artifact.

## 5. Implemented server prototype

`server/future-session/`

- `validation.php`
- `persistence.php`
- `api_v2.php`
- `config.example.php`
- `README.md`

This is isolated from the current Wave 1 deployment.

The ingestion prototype:

- accepts only `rapid_pair_event`, `rapid_block_attempt`, and explicitly consented `reflection_reason_event`;
- rejects persistent participant identity and personal/local-only reflection fields;
- requires RELEASED stimulus/reason configuration;
- validates stable asset identity and training status against the released stimulus set;
- uses prepared, fixed SQL statements;
- implements immutable idempotency checks;
- stores only session-scoped telemetry;
- never calculates personal results;
- never uses server receive time to re-adjudicate the rapid deadline.

`FS_ALLOWED_REASON_CONSENT_VERSIONS` is empty in the example config, so structured reflection telemetry is fail-closed by default.

## 6. Server schema baseline

`docs/architecture/FUTURE_SESSION_SERVER_SCHEMA_v0.2.sql`

New future-session tables:

```text
rapid_block_attempts
rapid_pair_events
reflection_reason_events
```

The existing Wave 1 `responses` table is not modified or migrated.

No server table is introduced for:

```text
persistent participant_id
free_text
reaction_intensity
self-report responses
derived personal results
published result snapshots
mutable Gate D / Gate E truth
```

## 7. Test / CI state

GitHub Actions workflow:

`.github/workflows/future-session-baseline.yml`

The baseline continuously checks:

- existing active behavior-translation Python tests;
- future-session architecture/schema/config invariants;
- rapid-block JS tests;
- Calculation Engine tests;
- Evidence Engine tests;
- outbox tests;
- HTTP transport tests;
- LLM contract tests;
- local result pipeline tests;
- PHP syntax;
- API validation contract;
- persistence contract.

Archived v0.7 integration files are deliberately not collected as active pytest tests. A previous broad `pytest -q` attempt failed because an archived test imports an obsolete module; this was a test-discovery problem, not a regression in the active engine.

At this baseline point all active CI jobs pass.

## 8. Deliberately not implemented

The following are intentionally outside this baseline:

- no changes to the live Wave 1 UI;
- no deployment/migration of the future-session DB schema;
- no production `config.php` or DB credentials;
- no stimulus-set release;
- no Gate D validation claims;
- no Gate E validation claims;
- no concrete participant-facing `reason_id` texts;
- no Reflection UI using reason options;
- no LLM provider/API integration;
- no server storage of personal result snapshots;
- no persistent cross-session participant identifier;
- no longitudinal study linkage;
- no admin/research dashboard.

## 9. Current real blocker

The next implementation step is **not more generic infrastructure**.

Before participant-facing Reflection UI can be built, the future stimulus set must be frozen sufficiently to define stable:

```text
pair_id
asset_a_id
asset_b_id
is_training
```

Only then can pair- and anchor-specific reason content be authored:

```text
pair_id
anchor_choice
reason_id
text_lt
text_en
interpretability_class
reason_map_version
```

Creating those texts before stimulus freeze would couple reflection semantics to provisional images and risk invalidating provenance when a visual changes.

## 10. Next allowed sequence

```text
1. Freeze candidate future stimulus set
2. Populate stimulus-set-v1.json
3. Review/freeze pair identity and training status
4. Author pair+anchor-specific reason-map content
5. Review reason language for semantic leakage / demand characteristics
6. Only then implement Reflection UI
7. Integrate the local result pipeline into an isolated future-session UI
8. Create immutable local published-result snapshot handling
9. Perform deployment/migration review
10. Only after review consider merging/deploying future-session work
```

Until step 1 is completed, the branch should remain a draft implementation baseline and must not replace the working Wave 1 application.
