# ConflictLab — Future Session Implementation Baseline Status v0.5

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Base:** `44426f715103a90bc79967d2655b75c1f33bbd2c`  
**PR:** Draft PR #2  
**Status:** F1 COMPLETE + F2 PILOT MECHANICS COMPLETE + 6000 MS CALIBRATION GATE READY

## Current gate state

```text
M1-M7 architecture decisions       CLOSED
F1 exact stimulus identity          COMPLETE AS DRAFT
F2 rapid presentation mechanics     COMPLETE FOR PILOT
6000 ms budget                      PILOT HYPOTHESIS, NOT VALIDATED
Timing calibration gate             READY
Gate D                              NONE
Gate E                              NONE
reason-map                          EMPTY
Reflection UI                       NOT STARTED
production deploy                   NOT AUTHORIZED
```

## 6000 ms calibration source of truth

Machine-readable criteria:

```text
config/future-session/timing-calibration-v1.json
```

Decision record:

```text
docs/architecture/adr/ADR-014-rapid-budget-calibration-gate.md
```

Offline evaluator:

```text
src/future_session/timing_calibration.mjs
```

Tests:

```text
tests/timing_calibration.test.mjs
```

`rapid-presentation-v1.json` now explicitly references `timing-calibration-v1`.

## Calibration question

The gate answers only:

> Does the shared 6000 ms budget allow the intended three-pair rapid interaction without creating excessive primary missingness or systematic depletion of block position 3?

It does not validate:

- Gate D mapping;
- Gate E aggregation;
- latency meaning;
- psychological interpretation;
- participant traits;
- reason-map content.

## Inclusion rules

Only clean primary attempts enter the timing decision:

```text
block_attempt_number = 1
is_training = false
page_hidden_during_block = false
block_budget_ms = 6000
exactly 3 logical pair outcomes available
```

Preload failure is technical and creates no research attempt.

Retry attempts remain diagnostic only.

## Minimum evidence floor

No KEEP/ADJUST/REJECT decision before:

```text
20 clean primary blocks
```

This is an operational pilot floor, not a statistical-power or population-validity claim.

Pair-specific threshold checks require at least 8 primary appearances for that pair.

## Decision states

```text
INSUFFICIENT_DATA
KEEP_6000
ADJUST_AND_RETEST
REJECT_6000
```

### KEEP_6000 requires all estimable green criteria

```text
primary block completion rate                  >= 80%
position 3 never-presented rate                <= 10%
position 3 missing rate                        <= 20%
position 3 minus position 1 missing gradient   <= 10 percentage points
single-pair missing rate, n >= 8               <= 30%
```

### REJECT_6000 if any red criterion is crossed

```text
primary block completion rate                  < 60%
position 3 never-presented rate                > 25%
position 3 missing rate                        > 40%
position 3 minus position 1 missing gradient   > 20 percentage points
single-pair missing rate, n >= 8               > 50%
```

If the data floor is met, no red criterion is crossed, but one or more green criteria fail:

```text
ADJUST_AND_RETEST
```

No new budget value is chosen automatically.

## Diagnostics preserved but not used as psychological evidence

The evaluator reports:

- retry rate;
- page-hidden rate;
- latency by block position;
- remaining budget at pair start;
- completion by device category;
- device completion gap when estimable;
- pair-specific missingness.

Latency is descriptive process telemetry only.

## Implementation safety

Nothing in this calibration layer changes the working Wave 1 deployment.

Still untouched:

```text
deploy/wave1-hostinger
current Wave 1 API
existing Wave 1 responses table
production database
```

The future-session branch remains isolated and Draft.

## Next gate

The next methodological/content task can proceed in parallel with timing data collection:

```text
DRAFT pair+anchor-specific reason catalog
```

However, Reflection UI should only be wired after the reason-map text and interpretability classes are separately reviewed.

The 6000 ms timing decision itself requires real future-session pilot telemetry; synthetic tests prove evaluator behavior only, not budget validity.
