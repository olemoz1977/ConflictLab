# 2Pair Integrated v0.1 — Technical Readiness Record

**Date:** 2026-08-29  
**Status:** TECHNICAL CANDIDATE — OWNER DEPLOY DECISION NOT YET GIVEN  
**Branch:** `feature/2pair-integrated-v0.1`

## Scope

This record covers repository readiness only. It does not authorize Hostinger deployment, external research collection, a public privacy activation, merge, Gate D/E, or any psychological interpretation.

## Preserved analysis contract

```text
TIMING / UX         -> existing Calibration-style mechanical metrics
STIMULUS VALIDATION -> existing Wave 1 descriptive / blind-coding method
```

No combined `choice + latency + intensity` score is implemented.

Wave 1-compatible rows are emitted only after a reflection submission exists for the primary rapid-choice event. A rapid choice uploaded before reflection remains available to Timing/UX evidence but does not masquerade as a completed historical Wave 1 response row.

Retry rate in the Timing/UX admin uses the same clean-primary denominator as the other clean-primary block metrics.

## Exact stimulus reuse

All 12 research image files in the integrated package match the existing frozen Wave 1 source bytes exactly.

All 6 training image files match the existing P0 training source bytes exactly.

This was checked both by Git blob identity during repository audit and by byte-for-byte `cmp` in GitHub Actions.

## Automated evidence

GitHub Actions workflow:

```text
2Pair Integrated v0.1
```

Run #1 (`33240745226`) completed successfully on commit:

```text
566715794192f4349a270fe8321882d4317aa709
```

Successful checks:

```text
Integrated rapid-core tests
JavaScript syntax checks
Exact stimulus byte reuse
Analysis-boundary contract
PHP syntax checks
```

Subsequent documentation-only readiness commits are subject to the same workflow before the deployment decision.

## Repository isolation

Comparison against `arch/result-v0.2-implementation-baseline` shows the feature branch is ahead only; no historical file is modified or deleted by the integrated implementation. The new package lives under:

```text
deploy/2pair-integrated-v0.1/
```

Historical `/wave1/` and `calibration-v0.1` package sources remain untouched.

## Remaining operational gates

Before external RESEARCH collection:

```text
owner TECHNICAL deploy decision
Hostinger TECHNICAL deployment
new isolated integrated tables
TECHNICAL LT/EN/mobile smoke
both export verification against real smoke rows
deletion / retention verification
integrated privacy notice approval + live publication
exact release identity record
explicit owner RESEARCH activation authorization
TECHNICAL -> RESEARCH server switch
```

The next owner gate is only:

> Deploy `2pair-integrated-v0.1` to Hostinger in `TECHNICAL` mode?
