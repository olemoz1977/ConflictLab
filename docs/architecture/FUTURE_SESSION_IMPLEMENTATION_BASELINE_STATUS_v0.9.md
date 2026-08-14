# ConflictLab — Future Session Implementation Baseline Status v0.9

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**PR:** Draft PR #2  
**Revision:** Stage 0 familiarization + owner calibration-quality telemetry implemented  
**Status:** ISOLATED END-TO-END FUTURE SESSION PREVIEW READY FOR OWNER UX RUN 002; NO DEPLOYMENT

## Current state

```text
M1-M7 architecture decisions       CLOSED
F1 exact stimulus identity          COMPLETE AS DRAFT
F2 rapid mechanics                  COMPLETE FOR PILOT
Stage 0 training                    IMPLEMENTED
training source                     P0-001 / P0-002 / P0-003 IN-PLACE REFERENCES
training calibration eligibility    EXCLUDED
6000 ms timing gate                 READY / real clean data pending
owner telemetry export              IMPLEMENTED / v2
reason-map                          48 DRAFT ITEMS
exact-asset review                  COMPLETE
Reflection model/UI                 IMPLEMENTED AS DRAFT
session orchestration               IMPLEMENTED
end-to-end pilot preview            IMPLEMENTED / SERVER-ISOLATED
OWNER_UX_RUN_001                    EXCLUDED
OWNER_UX_RUN_002                    NEXT MANUAL GATE
Gate D                              NONE
Gate E                              NONE
production deploy                   NOT AUTHORIZED
```

## Stage 0 familiarization correction

`OWNER_UX_RUN_001` demonstrated that a measured-looking block without prior familiarization mixes interaction learning with the timing condition. Run 001 remains retained for provenance but contributes zero to the 6000 ms calibration N.

The preview now requires a successful training stage before the fresh measured block.

Training config:

```text
config/future-session/training-set-v1.json
```

Training planner:

```text
src/future_session/training_plan.mjs
```

The training set references existing Pair P0 assets without moving, renaming or rewriting them:

```text
P0-001 -> docs/experiments/pair-p0/images/p0-001-a.png / p0-001-b.png
P0-002 -> docs/experiments/pair-p0/images/p0-002-a.png / p0-002-b.png
P0-003 -> docs/experiments/pair-p0/images/p0-003-a.png / p0-003-b.png
```

The manifest records the existing P0 Git blob SHAs so the familiarization source identity is explicit.

Training boundary:

```text
is_training = true
analysis_eligible = false
timing_calibration_eligible = false
Gate D = NOT_APPLICABLE
Gate E = NOT_APPLICABLE
server_upload = false
participant_result = NONE
```

The training block uses the same three sequential vertical A/B interaction and the same shared 6000 ms pilot hypothesis only to teach the mechanic. A timeout may be retried. Three failed training attempts require a fresh training cycle; training never falls through into Reflection.

## End-to-end path now implemented

Internal preview:

`docs/experiments/future-session-pilot-preview.html`

Composition:

```text
training-set-v1 (P0-001/002/003, local-only)
↓
preload/decode training + selected measured assets
↓
Stage 0 training
↓
explicit training-complete transition
↓
stimulus-set-v1 + rapid-presentation-v1
↓
two-session presentation planner
↓
fresh selected 3-pair measured session
↓
FutureSessionOrchestrator
↓
RapidBlockAttempt (shared 6000 ms hypothesis)
↓
retry with same order + same positions when required
↓
deriveReflectionAnchors
↓
reason-map-v1
↓
Reflection model + UI
↓
local-only owner telemetry export
```

No participant result is calculated or displayed.

## Orchestration invariants

Source:

`src/future_session/session_orchestrator.mjs`

Measured blocks preserve the existing invariants:

- one stable logical `blockId` per measured block;
- new `blockAttemptId` per attempt;
- exact session plan preserved on retry;
- prior exposure counts passed into retries;
- PRIMARY reflection anchors preferred;
- FIRST_COMPLETED_RETRY used only when primary lacks A/B;
- page-hidden diagnostics do not pause the clock;
- deadline reached during `markPairReady()` settles as timeout.

Training adds a strict mode:

- `isTraining=true` is propagated into attempt summaries and every rapid event;
- successful training ends at `COMPLETE`, never `REFLECTION_READY`;
- training cannot request reflection anchors or mark Reflection complete;
- third timeout ends at `TRAINING_RESTART_REQUIRED`, not Reflection.

## Owner telemetry export v2

The completion screen can download a local JSON export with schema:

```text
conflictlab.owner-ux-export.v2
```

It includes:

- training completion state and training-run telemetry;
- measured session plan;
- complete measured attempt summaries and rapid events;
- existing event timing fields such as `pairReadyElapsedMs`, `remainingBudgetAtPairStartMs`, `visualChoiceLatencyMs`, `blockElapsedMsAtEvent`, `pairPresented`, timeout and page-hidden fields;
- viewport/screen/device context captured locally at start and finish;
- Reflection selections;
- explicit `calibrationAssessment = NOT_EVALUATED_IN_UI`.

The preview does not decide whether a run is clean enough for calibration. That decision remains outside the UI and under `timing-calibration-v1`.

## Pilot preview boundaries

The preview deliberately:

- preloads/decode all training assets and selected measured assets before training starts;
- requires training completion before the fresh measured block;
- starts each monotonic shared budget only after pair 1 becomes interactive;
- keeps the pair layout vertical top/bottom on every viewport;
- permits only A/B taps during rapid blocks;
- performs no server/API calls;
- keeps training excluded from analysis and calibration;
- reuses preloaded in-memory object URLs for Reflection;
- uses DRAFT configs only through explicit DRAFT preview paths;
- does not assign Gate D/E meaning.

## What remains unvalidated

```text
6000 ms budget                 UNVALIDATED until clean real telemetry
Gate D pair mapping            NONE
Gate E aggregation             NONE
reason-map lifecycle           DRAFT
stimulus lifecycle             DRAFT
training-set lifecycle         DRAFT
participant result claims      NOT AUTHORIZED
```

## Next owner action — OWNER_UX_RUN_002

Open the updated isolated pilot preview on the intended phone/browser and complete:

```text
Stage 0 training
→ explicit transition
→ fresh measured 3-pair block
→ retry only if needed
→ Reflection
→ download owner UX telemetry JSON
```

For Run 002, judge:

1. whether the training makes the shared-timer mechanic clear before measurement;
2. whether the transition from training to measured block is unmistakable;
3. whether the measured three-pair interaction is technically usable;
4. whether retry behavior is understandable;
5. whether Reflection wording and mobile fit remain natural;
6. whether any participant-facing wording feels leading.

After Run 002, inspect the exported JSON before deciding whether it is a clean calibration candidate. One owner run still does not decide the 6000 ms hypothesis.

## CI

Commit `427e0a6f4b9ad04883c2775789849d3e9bfef174` passed all four workflow jobs. The future-js job now explicitly includes Training plan and Training orchestrator tests in addition to the existing future-session suite.

## Production safety

Still untouched:

```text
deploy/wave1-hostinger
current Wave 1 API
existing Wave 1 responses table
production database
Pair P0 source files and paths
```

No merge or production deploy is authorized.
