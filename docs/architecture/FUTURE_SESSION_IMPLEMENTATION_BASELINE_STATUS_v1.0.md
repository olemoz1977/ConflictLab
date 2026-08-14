# ConflictLab — Future Session Implementation Baseline Status v1.0

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**PR:** Draft PR #2  
**Status:** VERSIONED HOSTINGER LAB DEPLOYED / TECHNICAL MODE / PUBLIC SWITCH NOT AUTHORIZED

Detailed decisions, owner findings, rejected alternatives and next-gate context are maintained in:

`docs/architecture/FUTURE_SESSION_WORKLOG.md`

## Current state

```text
M1-M7 architecture decisions       CLOSED
F1 exact stimulus identity          COMPLETE AS DRAFT
F2 rapid mechanics                  COMPLETE FOR PILOT
Stage 0 training                    IMPLEMENTED
training calibration eligibility    EXCLUDED
mobile rapid viewport fit           IMPLEMENTED / OWNER VISIBILITY PASS
6000 ms timing gate                 READY / clean real data pending
Hostinger LAB                       DEPLOYED AT VERSIONED PATH
Hostinger JS compatibility          RESOLVED FOR LAB (.js deploy modules / index.php)
calibration DB                      CREATED / ISOLATED FROM WAVE1
calibration API                     END-TO-END OWNER SMOKE TEST PASS
calibration admin v2                DEPLOYED / OWNER VERIFIED
run classification                  TECHNICAL vs CALIBRATION IMPLEMENTED
collection mode                     TECHNICAL
technical owner runs                >= 1
calibration N/20                    0 / 20 at last owner check
product-shaped pilot                NEXT DEVELOPMENT GATE
LT                                  CURRENT LAB AVAILABLE
EN                                  REQUIRED BEFORE REAL COLLECTION
Gate D                              NONE
Gate E                              NONE
owner public approval               NOT GRANTED
public /wave1 switch                NOT AUTHORIZED
omesg360.eu root                    UNCHANGED
live /wave1                         UNCHANGED
production product deployment       NOT AUTHORIZED
```

## Release routing boundary

The already-published URL remains a stable entrypoint:

```text
https://omesg360.eu/wave1/
```

It has not been changed.

Versioned LAB releases use:

```text
/conflictlab/releases/<release-id>/
```

Current owner-operated LAB deployment:

```text
https://omesg360.eu/conflictlab/releases/calibration-v0.1/
```

Promotion remains explicit:

```text
LAB
-> OWNER APPROVAL of exact deployed release
-> separate PUBLIC switch authorization
-> optional ROLLBACK to previous public entrypoint
```

`OWNER_APPROVED` never implies `PUBLIC`.

## Current Hostinger LAB boundary

The LAB package uses an isolated future-session calibration database and does not reuse Wave1 response storage.

Tables:

```text
cl_calibration_runs
cl_calibration_attempts
cl_calibration_pair_events
```

The initial owner end-to-end smoke run confirmed:

```text
browser
-> preload
-> Stage 0 training
-> measured 3-pair rapid block
-> calibration API
-> MySQL
-> Reflection
-> finish
```

That owner run is retained as `run_type = TECHNICAL` and cannot enter calibration N/20.

Server collection mode remains:

```text
TECHNICAL
```

Only fresh-participant collection may use:

```text
CALIBRATION
```

and that switch requires an intentional owner action after the next pilot gate is complete.

## Calibration admin v2

Admin v2 separates engineering runs from calibration evidence.

It reports:

- server mode;
- calibration-eligible clean `N / 20`;
- technical/owner run count;
- excluded calibration run count;
- primary completion;
- P3 missing;
- P3 never presented;
- P3-P1 missingness gradient;
- retry diagnostic;
- filters by run type, form, device and status;
- per-run primary elapsed/retry state;
- detailed attempts and P1/P2/P3 timing events;
- pair missingness and positional diagnostics from eligible calibration runs only.

At the last owner check the dashboard correctly showed:

```text
SERVER MODE: TECHNICAL
technical runs: 1
calibration eligible: 0 / 20
excluded calibration: 0
decision: INSUFFICIENT_DATA
```

## Timing gate

The shared 6000 ms budget remains an unvalidated pilot hypothesis.

At least 20 clean primary CALIBRATION blocks are required before the timing gate may produce:

```text
KEEP_6000
ADJUST_AND_RETEST
REJECT_6000
```

Primary timeout is evidence about the budget, not automatically an exclusion. Page-hidden primary remains excluded. Retries are diagnostic only.

Timing/latency must not be interpreted as confidence, impulsivity, depth, decisiveness or another psychological characteristic without separate validation.

## Product-shaped pilot — next development gate

Because fresh testers are scarce, the next step is **not** to start N/20 immediately.

The current LAB should first evolve into a product-shaped pilot so each fresh participant contributes to multiple independent validation layers in one coherent future-product flow.

Target flow:

```text
LT / EN language selection
-> Stage 0 training
-> rapid A/B block
-> reason reflection
-> intensity 1-5
-> local calculation pipeline
-> evidence gate
-> result / fail-closed presentation
```

Three response-time channels should remain distinct:

```text
visual_choice_latency_ms
reason_response_latency_ms
intensity_response_latency_ms
```

`reflection_total_elapsed_ms` may be retained as UX/process telemetry.

Reason and intensity should be sequential so their response latencies remain separable.

## Calculation and local-first boundary

The current v0.2 calculation constraints remain unchanged:

```text
intensity never enters directional balance
latency never enters directional balance
retry events never enter directional balance
reflection class never changes direction
```

Reaction intensity remains an independent self-report channel. Reflection reasons/free text, intensity and derived personal results remain local-first by default.

Rapid timing eligibility and reflection completeness are separate dimensions. A participant who finishes the rapid block but abandons reflection does not automatically invalidate otherwise eligible timing evidence.

## Gate and interpretation boundary

Still unchanged:

```text
Gate D pair mapping          NONE
Gate E aggregation           NONE
stimulus lifecycle           DRAFT
reason-map lifecycle         DRAFT
participant directional claim NOT AUTHORIZED
psychological result claim   NOT AUTHORIZED
```

Real participant result presentation therefore remains fail-closed while Gate D/E are NONE. Calculation Engine / Evidence Engine / result UX can be developed using fixtures/synthetic cases without treating real participant direction as validated.

## Immediate next operational step

Do not change `/wave1/` and do not switch collection mode to `CALIBRATION` yet.

Next development sequence:

1. add complete LT/EN participant flow;
2. add sequential reason -> intensity 1-5 reflection;
3. record visual-choice, reason-response and intensity-response latencies independently;
4. preserve local-first boundary for reason/intensity;
5. wire the real Calculation Engine / Evidence Engine / fail-closed result shell;
6. test scoring/result paths with fixtures/synthetic cases;
7. owner smoke-test the complete product-shaped pilot in `TECHNICAL` mode;
8. only after owner approval switch to `CALIBRATION` and begin fresh-participant N/20 collection.

## Production safety

Still untouched:

```text
omesg360.eu root
live /wave1/ entrypoint
frozen deploy/wave1-hostinger source mirror
current Wave1 API
existing Wave1 response storage
Pair P0 source files and paths
```

No merge or public/production switch is authorized.
