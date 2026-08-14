# ConflictLab — Future Session Implementation Baseline Status v0.9

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**PR:** Draft PR #2  
**Revision:** Stage 0 familiarization + owner telemetry + mobile rapid viewport fit  
**Status:** OWNER MOBILE VISIBILITY PASSED; CLEAN TIMING CALIBRATION DATA STILL PENDING; NO DEPLOYMENT

## Current state

```text
M1-M7 architecture decisions       CLOSED
F1 exact stimulus identity          COMPLETE AS DRAFT
F2 rapid mechanics                  COMPLETE FOR PILOT
Stage 0 training                    IMPLEMENTED
training source                     P0-001 / P0-002 / P0-003 IN-PLACE REFERENCES
training calibration eligibility    EXCLUDED
mobile rapid viewport fit           IMPLEMENTED / OWNER VISIBILITY PASS
6000 ms timing gate                 READY / clean real data pending
owner telemetry export              IMPLEMENTED / owner-ux-export.v2
reason-map                          48 DRAFT ITEMS
exact-asset review                  COMPLETE
Reflection model/UI                 IMPLEMENTED AS DRAFT
session orchestration               IMPLEMENTED
end-to-end pilot preview            IMPLEMENTED / RESPONSE-WRITE-ISOLATED
OWNER_UX_RUN_001                    EXCLUDED
OWNER_UX_RUN_002                    MOBILE VISIBILITY PASS / CALIBRATION EXCLUDED
broader owner UX approval           PENDING EXPLICIT WORDING / TRANSITION SIGN-OFF
Gate D                              NONE
Gate E                              NONE
production deploy                   NOT AUTHORIZED
```

## Stage 0 familiarization

`OWNER_UX_RUN_001` demonstrated that a measured-looking block without prior familiarization mixes interaction learning with the timing condition. Run 001 remains retained for provenance but contributes zero to the 6000 ms calibration N.

The preview requires a successful training stage before the measured block.

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

## Owner Run 002 review

Run 001 exposed the F2-B research pairs, so Run 002 used the owner/debug-only `?form=F2-A` override to avoid immediately reusing F2-B. The override does not modify `rapid-presentation-v1.json`, form-cycle policy, Gate D/E, or production behavior.

The owner completed the F2-A standalone flow on a mobile viewport of approximately `392 x 727` CSS pixels. The first Run 002 snapshot exposed a mobile-layout issue: square images plus the explanatory header could require scrolling, so both alternatives were not guaranteed to be visible simultaneously.

The rapid mobile layout was then changed to:

```text
100dvh rapid shell
intro/brand hidden only during timed rapid presentation
body overflow hidden during rapid presentation
vertical top/bottom layout preserved
two equal minmax(0, 1fr) image rows
object-fit: contain
no source image resize or recompression
```

The owner repeated the mobile-fit snapshot and explicitly confirmed that **everything was visible**. This closes the mobile visibility/layout issue for the tested viewport.

The repeated mobile-fit standalone run was diagnostic only:

```text
training primary             COMPLETE / 3192 ms
measured F2-A primary        COMPLETE / 3471 ms
measured pairs               3/3 presented and completed
page hidden                  false
```

These timings do not validate the 6000 ms hypothesis. The standalone owner snapshot did not provide the same explicit measured-asset preload/decode guarantee as the canonical repository preview, and F2-A had already been exposed in the earlier Run 002 pass. Therefore all standalone Run 002 timing data remain excluded from the clean calibration N.

## Canonical mobile rapid layout

Internal canonical preview:

`docs/experiments/future-session-pilot-preview.html`

The canonical preview now applies the validated mobile-fit presentation behavior during both training and measured rapid blocks. It changes only CSS/layout presentation size; exact stimulus asset bytes and A/B identities remain unchanged.

The canonical preview still performs this preload step before training begins:

```text
preloadPathsForTraining(trainingPlan)
+ preloadPathsForSession(sessionPlan)
-> preloadAssetBundle(...)
```

Therefore both training and selected measured assets are fetched and decoded before the timed flow begins, preserving the F2 preload boundary.

## End-to-end path

```text
training-set-v1 (P0-001/002/003, local-only)
↓
preload/decode training + selected measured assets
↓
Stage 0 training
↓
explicit training-complete transition
↓
measured 3-pair rapid block
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

Static configs and image assets must load for the browser preview to run, but responses and telemetry remain local unless explicitly exported to the device.

## What remains unvalidated

```text
6000 ms budget                 UNVALIDATED until >=20 clean primary blocks
Gate D pair mapping            NONE
Gate E aggregation             NONE
reason-map lifecycle           DRAFT
stimulus lifecycle             DRAFT
training-set lifecycle         DRAFT
participant result claims      NOT AUTHORIZED
```

## Next gate

No further owner timing repetition with F2-A/F2-B should be used to build calibration N because the owner has now seen both research forms.

The next timing step is collection of **clean primary blocks from new participants** using the canonical preview and the `timing-calibration-v1` inclusion rules. The timing gate remains `INSUFFICIENT_DATA` until at least 20 clean primary blocks exist.

Separately, broader owner UX approval remains open only for participant-facing wording / transition / Reflection fit if the owner wants further changes. Mobile rapid visibility itself is passed.

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
