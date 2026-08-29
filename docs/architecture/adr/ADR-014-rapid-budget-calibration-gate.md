# ADR-014 — Rapid shared-budget calibration gate

**Date:** 2026-08-14  
**Status:** ACCEPTED FOR PILOT  
**Scope:** future-session rapid visual block timing only

## Context

The future rapid protocol currently uses a working hypothesis of:

```text
3 sequential pairs
6000 ms shared block budget
```

The budget is intentionally a time-pressure manipulation. A high overall completion rate alone is not enough to accept it because a shared budget can create serial depletion: later positions may receive materially less usable time or may never be shown.

The calibration question is therefore mechanical:

> Does 6000 ms permit the intended three-pair interaction without producing excessive missingness or systematic depletion of the third block position?

This is not a psychometric validity test and cannot validate Gate D, Gate E, latency interpretation, personality inference, or trait language.

## Inclusion set

Calibration uses only clean primary research attempts:

```text
block_attempt_number = 1
is_training = false
page_hidden_during_block = false
exactly three logical pair outcomes are present
```

Technical preload failure creates no research attempt and therefore cannot be counted as participant timeout.

Retry attempts are diagnostic context only and do not enter the primary 6000 ms completion denominator.

## Minimum evidence floor

Do not make a KEEP/ADJUST/REJECT decision before:

```text
20 clean primary blocks
```

This is an operational pilot floor, not a claim of statistical power or population validation.

Pair-level missingness thresholds are evaluated only when that pair has at least 8 eligible primary appearances.

Device-category differences are reported only when each compared group has at least 5 clean primary blocks; they remain diagnostic in this calibration version.

## Green criteria — KEEP candidate

`KEEP_6000` requires all estimable green criteria to pass:

```text
primary block completion rate                  >= 0.80
position 3 never-presented rate                <= 0.10
position 3 missing-choice rate                 <= 0.20
(position 3 missing rate - position 1 rate)    <= 0.10
single-pair missing rate, where n >= 8          <= 0.30
```

A completed block means all three primary pair outcomes are A/B choices before the shared deadline.

`missing` includes both:

```text
shown but no A/B before deadline
never presented because shared budget expired
```

The separate never-presented metric preserves ADR-011 provenance.

## Red criteria — reject current budget

`REJECT_6000` is triggered when any estimable red criterion is crossed:

```text
primary block completion rate                  < 0.60
position 3 never-presented rate                > 0.25
position 3 missing-choice rate                 > 0.40
(position 3 missing rate - position 1 rate)    > 0.20
single-pair missing rate, where n >= 8          > 0.50
```

These thresholds are operational stop rules for the pilot protocol. They are not psychological cutoffs.

## Amber region

If the evidence floor is met, no red criterion is crossed, but one or more green criteria fail:

```text
ADJUST_AND_RETEST
```

The system must not silently choose a new budget. Any new candidate budget must be versioned and retested under the same F2 presentation mechanics.

## Insufficient data

If fewer than 20 clean primary blocks remain after inclusion rules:

```text
INSUFFICIENT_DATA
```

No timing decision is permitted.

## Diagnostics that do not independently decide the budget

Always preserve and review:

- retry rate;
- page-hidden rate;
- latency by block position;
- remaining budget at pair start by position;
- completion by device category;
- device completion gap;
- pair-specific missingness.

Latency has no directional or psychological meaning in this gate.

## Decision states

```text
INSUFFICIENT_DATA
KEEP_6000
ADJUST_AND_RETEST
REJECT_6000
```

## Consequences

- 6000 ms remains `PILOT_HYPOTHESIS_NOT_VALIDATED` until a real calibration dataset reaches this gate.
- F1 stimulus identity and F2 presentation mechanics remain independent from timing acceptance.
- Gate D, Gate E and reason-map remain independent from this calibration decision.
- A later budget change requires a new protocol/config version or explicitly versioned timing revision; historical raw events retain the budget actually used.

Machine-readable thresholds live in:

```text
config/future-session/timing-calibration-v1.json
```
