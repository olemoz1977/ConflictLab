# OWNER LT product-shaped pilot smoke test

**Date:** 2026-08-14  
**Environment:** Hostinger versioned LAB  
**Path:** `/conflictlab/releases/calibration-v0.1/`  
**Mode:** `TECHNICAL`

## Outcome

The owner completed one full Lithuanian product-shaped pilot flow on mobile after the Hostinger overwrite.

Observed participant flow:

```text
LT language selection
-> Stage 0 training
-> measured 3-pair rapid block
-> sequential reason reflection
-> intensity 1-5
-> local Calculation/Evidence pipeline
-> fail-closed result
```

Result screen correctly reported:

```text
Gate D = NONE
Gate E = NONE
NOT_ESTIMABLE
```

and confirmed that technical timing data were saved while reflection reason/intensity and their response-time data were not sent to the calibration DB.

## Admin verification

Admin after the LT smoke test showed:

```text
SERVER MODE: TECHNICAL
calibration eligible: 0 / 20
technical / owner runs: 2
excluded calibration runs: 0
decision: INSUFFICIENT_DATA
```

New owner run:

```text
run_id: 2
run_type: TECHNICAL
form: F2-B
device: mobile
primary elapsed: 4257 ms
retry: no
page hidden: no
```

Pair timing events:

```text
P1 CR-FS-01  latency 1306 ms  elapsed 1306 ms  remaining 6000 ms
P2 CS-RE-01  latency 1365 ms  elapsed 2672 ms  remaining 4693 ms
P3 CS-PR-01  latency 1584 ms  elapsed 4257 ms  remaining 3327 ms
```

All three pairs were presented and received `choice` responses.

This run is engineering evidence only and must never enter calibration N/20 because it is owner-operated and run_type is `TECHNICAL`.

## UX note

The Lithuanian result copy contains the English phrase `response-time`. This is a copy-quality issue only and should be localized before broader participant use.

## Next gate

1. owner smoke-test the complete EN flow;
2. verify the new run remains TECHNICAL and calibration N/20 remains 0;
3. record EN UX/copy findings;
4. keep collection mode TECHNICAL until the research-collection scope/consent decision is closed.
