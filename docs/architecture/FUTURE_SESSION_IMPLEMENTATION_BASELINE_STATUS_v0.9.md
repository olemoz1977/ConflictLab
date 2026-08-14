# ConflictLab — Future Session Implementation Baseline Status v0.9

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**PR:** Draft PR #2  
**Revision:** Stage 0 familiarization + owner calibration-quality telemetry + fresh-form Run 002  
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
owner telemetry export              IMPLEMENTED / owner-ux-export.v2
reason-map                          48 DRAFT ITEMS
exact-asset review                  COMPLETE
Reflection model/UI                 IMPLEMENTED AS DRAFT
session orchestration               IMPLEMENTED
end-to-end pilot preview            IMPLEMENTED / RESPONSE-WRITE-ISOLATED
OWNER_UX_RUN_001                    EXCLUDED
OWNER_UX_RUN_002                    NEXT MANUAL GATE / FORCE F2-A
Gate D                              NONE
Gate E                              NONE
production deploy                   NOT AUTHORIZED
```

## Stage 0 familiarization

`OWNER_UX_RUN_001` demonstrated that a measured-looking block without prior familiarization mixes interaction learning with the timing condition. Run 001 remains retained for provenance but contributes zero to the 6000 ms calibration N.

The preview now requires a successful training stage before the fresh measured block.

Training config:

`config/future-session/training-set-v1.json`

Training planner:

`src/future_session/training_plan.mjs`

The training set references existing Pair P0 assets without moving, renaming or rewriting them:

```text
P0-001 -> docs/experiments/pair-p0/images/p0-001-a.png / p0-001-b.png
P0-002 -> docs/experiments/pair-p0/images/p0-002-a.png / p0-002-b.png
P0-003 -> docs/experiments/pair-p0/images/p0-003-a.png / p0-003-b.png
```

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

Training uses the same three sequential vertical A/B interaction and the same shared 6000 ms pilot hypothesis only to teach the mechanic. A timeout may be retried. Three failed training attempts require a fresh training cycle; training never falls through into Reflection.

## Run 002 freshness rule

Run 001 exposed the F2-B research pairs:

```text
CS-PR-01
CS-RE-01
CR-FS-01
```

Therefore Run 002 must not use F2-B as its fresh measured primary block. The internal preview now supports an **owner/debug-only** form override through the query parameter:

```text
?form=F2-A
```

For Run 002 this selects the still-unexposed complementary form:

```text
CS-CA-01
CR-PZ-01
CR-PO-01
```

This override is recorded in the local owner export as `ownerFormOverride`. It does not modify `rapid-presentation-v1.json`, form-cycle policy, Gate D/E, or production behavior.

## End-to-end path

Internal preview:

`docs/experiments/future-session-pilot-preview.html`

```text
training-set-v1 (P0-001/002/003, local-only)
↓
preload/decode training + selected measured assets
↓
Stage 0 training
↓
explicit training-complete transition
↓
fresh F2-A measured block for OWNER_UX_RUN_002
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

## Owner telemetry export v2

The completion screen can download local JSON schema:

`conflictlab.owner-ux-export.v2`

It includes:

- training completion state and training-run telemetry;
- measured session plan and optional owner form override;
- complete measured attempt summaries and rapid events;
- `pairReadyElapsedMs`, `remainingBudgetAtPairStartMs`, `visualChoiceLatencyMs`, `blockElapsedMsAtEvent`, `pairPresented`, timeout and page-hidden fields;
- viewport/screen/device context captured locally at start and finish;
- Reflection selections;
- `calibrationAssessment = NOT_EVALUATED_IN_UI`.

The UI does not decide whether a run is clean enough for calibration. That decision remains outside the UI under `timing-calibration-v1`.

## Network/data boundary

The preview is **response-write-isolated**, not network-free:

```text
static config/image reads        YES / read-only
response upload                  NO
telemetry upload                 NO
server write                     NO
participant result write         NO
```

Participant-facing wording now reflects this distinction. Static configs and image assets must load for the browser preview to run, but responses and telemetry remain local unless the owner explicitly exports the JSON file to the device.

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

Open the isolated preview with the owner-only fresh-form override and complete:

```text
?form=F2-A
Stage 0 training
→ explicit transition
→ fresh F2-A measured 3-pair block
→ retry only if needed
→ Reflection
→ download owner UX telemetry JSON
```

Judge:

1. whether training makes the shared-timer mechanic clear before measurement;
2. whether the transition from training to measured block is unmistakable;
3. whether the measured three-pair interaction is technically usable;
4. whether retry behavior is understandable;
5. whether Reflection wording and mobile fit remain natural;
6. whether any participant-facing wording feels leading.

After Run 002, inspect the exported JSON before deciding whether its measured primary attempt is a clean calibration candidate. One owner run still does not decide the 6000 ms hypothesis.

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
