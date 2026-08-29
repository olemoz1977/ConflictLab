# 2Pair / ConflictLab — Human Wave 1 data review

**Date:** 2026-08-29  
**Status:** descriptive evidence checkpoint  
**Scope:** Wave 1 v0.3 / v0.4 exports supplied by owner; no raw participant data committed

## Method boundary

This checkpoint follows `WAVE1_ANALYSIS_RUNBOOK_v0.1.md` and remains descriptive only.

```text
signal_mapping_status = NONE
Gate D = NONE
Gate E = NONE
```

No CS/CR direction is inferred from asset choice. Latency is not interpreted psychologically. No automatic KEEP / REVISE / REJECT verdict is issued.

Different participant UUIDs across protocol versions are counted as participant IDs, not proven unique humans.

## Export counts

### wave1-v0.3

```text
rows: 12
participant IDs: 2
complete 6/6 participant IDs: 2
incomplete participant IDs: 0
free-text rows: 1
```

### wave1-v0.4

```text
rows: 48
participant IDs: 10
complete 6/6 participant IDs: 7
incomplete participant IDs: 3
free-text rows: 20
language: 4 LT participant IDs, 6 EN participant IDs
complete: 4/4 LT, 3/6 EN
```

The v0.3 and v0.4 exports are not silently pooled because v0.4 added participant-facing language/privacy changes.

## v0.4 pair-level descriptive signals

Among the 7 complete 6/6 participant IDs, all six pairs remained close to balanced in chosen-asset counts (4:3 or 3:4). This is only a descriptive observation and does not establish construct validity.

`CS-PR-01` is the clearest pair-level review flag in the current small dataset:

```text
complete-session exposures: 7
hard_to_identify: 3/7 (42.9%)
median latency: 12,543 ms
chosen assets: 4 vs 3
```

For comparison, the other five pairs showed `hard_to_identify` rates of 0% or 14.3% among complete-session exposures.

This is a **review flag, not a REVISE verdict**. The existing methodology requires post-hoc reason/confound coding before a family decision.

## Completion / UX signal

For wave1-v0.4:

```text
10 participant IDs started
7 completed 6/6
3 stopped after 1, 2, or 3 saved responses
```

Cause is unknown from the export alone. These rows must not be described as proven boredom, friction, technical failure, or loss of interest without additional evidence.

The incompletion pattern is still a legitimate UX question for the next review, especially in light of the product-experience principle that the stimulus process itself should be engaging.

## Next action

Follow the frozen Wave 1 decision path rather than redesigning stimuli immediately:

```text
current exports
-> reproducible descriptive report
-> blind post-hoc coding of available free-text reasons
-> unblind coding summary
-> human KEEP / REVISE / REJECT decision by family
-> only then create second exemplars / revised variants for surviving families
```

There are 21 non-empty free-text rows across the two supplied exports (1 in v0.3, 20 in v0.4). This is enough to begin the planned blind-coding stage, but not enough to claim psychometric validation.

## Product / UX separation

Do not alter the active Calibration research core merely to make it more entertaining.

The previously recorded 2Pair experience direction (more visual rhythm, stronger payoff, optional Explore layer) should be prototyped separately from the frozen research core so UX experimentation does not contaminate current measurement evidence.
