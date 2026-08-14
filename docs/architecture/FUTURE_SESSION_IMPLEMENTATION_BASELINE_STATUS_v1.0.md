# ConflictLab — Future Session Implementation Baseline Status v1.0

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**PR:** Draft PR #2  
**Status:** PRODUCT-SHAPED PILOT IMPLEMENTED IN REPOSITORY / HOSTINGER PATCH PENDING / PUBLIC SWITCH NOT AUTHORIZED

Detailed decisions and owner findings are maintained in:

`docs/architecture/FUTURE_SESSION_WORKLOG.md`

## Current state

```text
M1-M7 architecture decisions       CLOSED
F1 exact stimulus identity          COMPLETE AS DRAFT
F2 rapid mechanics                  COMPLETE FOR PILOT
Stage 0 training                    IMPLEMENTED / EXCLUDED FROM CALIBRATION
mobile rapid viewport fit           IMPLEMENTED / OWNER VISIBILITY PASS
Hostinger versioned LAB             DEPLOYED / PREVIOUS LAB BUILD CURRENTLY LIVE
Hostinger JS compatibility          RESOLVED (.js deployment modules + index.php)
calibration DB                      CREATED / ISOLATED FROM WAVE1
calibration API                     END-TO-END OWNER SMOKE PASS
calibration admin v2                DEPLOYED / OWNER VERIFIED
run classification                  TECHNICAL vs CALIBRATION IMPLEMENTED
collection mode                     TECHNICAL
calibration N/20                    0 / 20 at last owner check
6000 ms timing gate                 INSUFFICIENT_DATA / REAL DATA PENDING
product-shaped pilot code           IMPLEMENTED IN REPOSITORY
LT / EN                              IMPLEMENTED IN PRODUCT-SHAPED BUILD
reason -> intensity 1-5             IMPLEMENTED / SEQUENTIAL
visual choice latency               IMPLEMENTED / SERVER TIMING TELEMETRY
reason response latency             IMPLEMENTED / LOCAL ONLY
intensity response latency          IMPLEMENTED / LOCAL ONLY
reflection total elapsed            IMPLEMENTED / LOCAL ONLY
Calculation Engine                  WIRED INTO PILOT
Evidence Engine                     WIRED INTO PILOT
participant result                  FAIL-CLOSED / NOT_ESTIMABLE
Gate D                              NONE
Gate E                              NONE
owner product-pilot smoke           PENDING AFTER HOSTINGER PATCH
owner public approval               NOT GRANTED
public /wave1 switch                NOT AUTHORIZED
omesg360.eu root                    UNCHANGED
live /wave1                         UNCHANGED
production product deployment       NOT AUTHORIZED
```

## Product-shaped pilot flow

Repository LAB release now implements:

```text
LT / EN language selection
-> Stage 0 training
-> rapid A/B block / shared 6000 ms candidate budget
-> timing-only server save
-> reason reflection
-> intensity 1-5
-> local Calculation Engine
-> local Evidence Engine
-> fail-closed result screen
```

Language is selected before training and remains fixed for that session. The reason map already supplies paired LT/EN participant text.

## Three independent response-time channels

The pilot keeps the three timings separate:

```text
visual_choice_latency_ms
  pair visually ready -> A/B choice

reason_response_latency_ms
  selected image + reason controls visually ready -> final reason selection

intensity_response_latency_ms
  selected image + intensity controls visually ready -> 1-5 selection
```

`reflection_total_elapsed_ms` is retained as a local UX/process diagnostic.

Reason and intensity stages have no time limit. Their controls remain disabled until the selected image is decoded and the UI is visually ready, so their clocks cannot begin before the participant can actually respond.

No latency value is allowed to imply confidence, impulsivity, depth, decisiveness or another psychological characteristic without separate validation.

## Reflection / intensity semantics

Reason and intensity are sequential. Current local response model distinguishes:

```text
reason_status     = ANSWERED | SKIPPED | NOT_REACHED
intensity_status  = ANSWERED | SKIPPED | NOT_REACHED
```

Reaction intensity is an independent self-report channel and does not enter Directional Balance.

Current calculation invariants remain:

```text
intensity never enters directional balance
latency never enters directional balance
retry events never enter directional balance
reflection class never changes direction
```

The rapid timing save occurs before reflection, so incomplete reflection does not automatically invalidate otherwise eligible timing evidence.

## Local-first / server boundary

Calibration server continues to receive only the mechanical timing fields required for the 6000 ms decision plus coarse device category.

It does **not** receive:

```text
reason selection
reflection free text
reason_response_latency_ms
intensity 1-5
intensity_response_latency_ms
reflection_total_elapsed_ms
derived participant result
persistent participant ID
```

Those product-shaped reflection/result channels are local-first in this build.

## Result pipeline boundary

The pilot now executes the actual Calculation Engine and Evidence Engine locally after reflection.

Current Gate D config remains:

```text
lifecycle = DRAFT
mappings = []
Gate D = NONE
```

Current Gate E config remains:

```text
CS = NONE
CR = NONE
```

Therefore the real participant result is intentionally:

```text
NOT_ESTIMABLE
```

The result screen explains that no directional/psychological conclusion is available yet. Synthetic/fixture cases may be used to develop result-processing and presentation behavior without treating real participant direction as validated.

## Timing calibration boundary

At least 20 clean primary `CALIBRATION` blocks are still required before the 6000 ms candidate can produce:

```text
KEEP_6000
ADJUST_AND_RETEST
REJECT_6000
```

`TECHNICAL` owner runs never enter N/20. Current server mode remains `TECHNICAL` until an explicit switch after owner product-pilot smoke testing.

## Hostinger state

The isolated LAB path remains:

```text
https://omesg360.eu/conflictlab/releases/calibration-v0.1/
```

The currently deployed bytes predate the product-shaped pilot changes in this status. A validated overwrite patch must be applied to this versioned LAB path before owner testing of LT/EN + reason/intensity + result-shell behavior.

No DB migration is required for this product-shaped patch because the newly added reflection/intensity channels remain local-only and the existing timing API/schema are unchanged.

## Public safety

Still untouched:

```text
https://omesg360.eu/
https://omesg360.eu/wave1/
current Wave1 API and response storage
frozen deploy/wave1-hostinger mirror
Pair P0 source files and paths
```

No merge, public switch or production product deployment is authorized.

## Immediate next gate

1. package the CI-validated product-shaped LAB overwrite patch;
2. owner uploads it only to `/conflictlab/releases/calibration-v0.1/`;
3. keep `collection_mode = TECHNICAL`;
4. owner smoke-tests LT and EN flows;
5. verify admin gains only TECHNICAL runs and N/20 stays 0;
6. record owner UX findings in the worklog;
7. only then decide whether the data-collection boundary is sufficient for the planned research hypotheses before switching to `CALIBRATION`.
