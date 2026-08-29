# ConflictLab — Future Session Implementation Baseline Status v1.0

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**PR:** Draft PR #2  
**Status:** PRODUCT-SHAPED PILOT IMPLEMENTED IN REPOSITORY / HOSTINGER PATCH PENDING / PUBLIC SWITCH NOT AUTHORIZED

Detailed decisions and owner findings are maintained in:

`docs/architecture/FUTURE_SESSION_WORKLOG.md`

Detailed product-shaped implementation record:

`docs/architecture/worklog/2026-08-14_PRODUCT_SHAPED_PILOT_IMPLEMENTATION.md`

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
research collection scope           REVIEW REQUIRED BEFORE CALIBRATION MODE
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

Language is selected before training and remains fixed for that session.

## Three independent response-time channels

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

Current local response model distinguishes:

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
A/B identity in the timing dataset
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

### Research-collection decision before CALIBRATION mode

Because scarce fresh testers are intended to contribute to more than timing UX, the current timing-only server boundary must be reviewed before real participant collection.

Do not silently broaden the calibration API. Explicitly decide which hypotheses require aggregate research data and whether a separately consented research channel is justified. Candidate channels to evaluate later include A/B response identity and reason metadata; intensity requires its own explicit purpose/consent decision. Free text remains local-first by default.

Until that decision is closed, keep `collection_mode = TECHNICAL`.

## Result pipeline boundary

The pilot executes the actual Calculation Engine and Evidence Engine locally after reflection.

Current Gate D:

```text
lifecycle = DRAFT
mappings = []
Gate D = NONE
```

Current Gate E:

```text
CS = NONE
CR = NONE
```

Therefore real participant result is intentionally:

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

`TECHNICAL` owner runs never enter N/20.

## Hostinger state

The isolated LAB path remains:

```text
https://omesg360.eu/conflictlab/releases/calibration-v0.1/
```

The currently deployed bytes predate the product-shaped pilot changes. Use an exact-head successful push CI artifact to overwrite this versioned LAB path before owner testing of the new flow.

No DB migration is required for this product-shaped UI update. Existing secret `server/config.php` must remain in place and `collection_mode` must remain `TECHNICAL`.

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

1. obtain the exact-head successful push CI artifact;
2. owner extracts it only into `/conflictlab/releases/calibration-v0.1/` with overwrite;
3. preserve `server/config.php` and keep `collection_mode = TECHNICAL`;
4. owner smoke-tests LT and EN flows;
5. verify admin gains only TECHNICAL runs and N/20 stays 0;
6. record owner UX findings;
7. close the explicit research-collection scope/consent decision;
8. only then consider switching to `CALIBRATION` for fresh participants.
