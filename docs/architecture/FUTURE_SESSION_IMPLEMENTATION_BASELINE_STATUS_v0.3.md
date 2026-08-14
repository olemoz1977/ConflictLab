# ConflictLab — Future Session Implementation Baseline Status v0.3

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Base:** `44426f715103a90bc79967d2655b75c1f33bbd2c`  
**PR:** Draft PR #2  
**Status:** IMPLEMENTATION BASELINE + F1 ASSET IDENTITY COMPLETE — F2 PRESENTATION REVIEW NEXT

## Decision gate

The seven implementation decisions from the v0.2 review remain closed by ADR-010/011/012.

```text
M1  block timer authority          CLOSED
M2  retry limit                    CLOSED
M3  reflection trigger             CLOSED
M4  reason catalog architecture    CLOSED
    reason catalog content         PENDING F2 / stimulus presentation freeze
M5  Gate D / Gate E storage        CLOSED
M6  session vs participant ID      CLOSED
M7  reflection server purpose      CLOSED
```

## Implemented architecture

The future-session baseline remains isolated from the working Wave 1 deployment and includes:

```text
Rapid Block Core
-> durable local outbox
-> isolated HTTP transport
-> fail-closed server ingestion prototype
-> deterministic Calculation Engine
-> Evidence Engine
-> depersonalized LLM generation contract
-> local result pipeline
```

No network ACK participates in rapid choice timing. Server receive time never adjudicates deadline compliance.

## F1 stimulus identity — COMPLETE as DRAFT

`config/future-session/stimulus-set-v1.json` now contains all six pairs currently used by `wave1-v0.3`:

```text
CS-PR-01
CS-RE-01
CS-CA-01
CR-PZ-01
CR-FS-01
CR-PO-01
```

The exact 12 source assets are already repository-resident under:

```text
docs/experiments/stimulus-validation/assets/<pair_id>/
```

Every configured asset is bound by:

```text
stable neutral asset ID
repository-relative path
SHA-256 of exact bytes
MIME type
is_training = false
source-family provenance
```

Independent source provenance is recorded by:

```text
config/future-session/wave1-candidate-manifest-v0.2.json
```

which also binds source commit and Git blob SHA.

F1 decision record:

```text
docs/architecture/FUTURE_SESSION_STIMULUS_F1_DECISION_v0.1.md
```

## F1 verification

CI now runs:

```text
python -m pytest -q \
  tests/test_future_session_baseline.py \
  tests/test_future_stimulus_asset_verifier.py

python tools/verify_future_stimulus_assets.py
```

Required current result:

```text
lifecycle = DRAFT
verified_pair_count = 6
verified_asset_count = 12
```

Current branch result: PASS.

All four active CI jobs pass:

```text
legacy-python   PASS
baseline-python PASS
future-js       PASS
future-php      PASS
```

## Interpretation boundary remains closed

F1 proves exact stimulus identity only.

Current methodological state remains:

```text
Gate D mappings        empty / NONE
Gate E CS              NONE
Gate E CR              NONE
reason-map items       empty
stimulus lifecycle     DRAFT
```

Therefore no `+1/-1`, domain score, trait inference or participant-facing interpretation is authorized by the F1 decision.

## Clean-up after corrected asset discovery

The earlier external-asset recovery hypothesis was false because the exact Wave 1 binaries were already in the repository.

The obsolete active-tree artifacts created for that hypothesis were removed:

```text
tools/import_wave1_future_candidates.py
tests/test_import_wave1_future_candidates.py
config/future-session/wave1-candidate-manifest-v0.1.json
docs/architecture/FUTURE_SESSION_STIMULUS_F1_RUNBOOK_v0.1.md
```

Their history remains available in Git; they are no longer active source-of-truth material.

## Next gate — F2 presentation/protocol review

The next task is not further asset work.

Review and freeze how the six F1 candidates are used in the future rapid protocol:

1. define how six candidate pairs are distributed across three-pair rapid blocks/sessions;
2. define pair-order randomization/counterbalancing;
3. define A/B screen-position counterbalancing;
4. define asset preload/readiness before monotonic timing begins;
5. define what happens if one asset cannot become ready;
6. define whether a pair can repeat across sessions and under what balancing rule;
7. retain Wave 1 choice concentration, no-clear-choice and top/bottom diagnostics as descriptive stimulus QA, not scoring;
8. keep `stimulus-set-v1` DRAFT until F2 is reviewed.

Only after F2 should pair+anchor-specific reason content be authored and Reflection UI implemented.

## Still deliberately not done

- no change to live Wave 1 UI/API;
- no production DB migration;
- no stimulus RELEASED status;
- no Gate D mapping;
- no Gate E aggregation;
- no reason-map content;
- no Reflection UI;
- no production LLM provider call;
- no persistent participant identifier;
- no server storage of personal result snapshots;
- no merge/deploy decision.
