# ADR-011 — Timeout and presentation semantics

**Date:** 2026-08-14  
**Status:** ACCEPTED  
**Scope:** future-session rapid visual block

## Context

A shared block budget can expire in two materially different conditions:

1. a pair was already interactive, but the participant did not select A/B before the deadline;
2. the deadline expired before a later pair was ever presented.

Representing both conditions only as `choice = timeout` would conflate response missingness with non-exposure and would corrupt the denominator used for Coverage.

## Decision

Every logical position in an attempted block receives an append-only pair outcome, but the outcome must explicitly record whether the pair was actually presented.

Required semantics:

```text
pair_presented = true
  both assets reached interactive ready state before block deadline

pair_presented = false
  block budget expired before that pair became interactive
```

For a shown pair with no selection before deadline:

```text
choice = timeout
pair_presented = true
pair_ready_elapsed_ms != null
visual_choice_latency_ms = null
```

For a later pair never shown because the shared budget was already exhausted:

```text
choice = timeout
pair_presented = false
pair_ready_elapsed_ms = null
visual_choice_latency_ms = null
remaining_budget_at_pair_start_ms = null
```

For A/B selections:

```text
choice = A | B
pair_presented = true
```

## Coverage consequence

`n_eligible_presentations` counts only events where:

```text
Gate D mapping is eligible
AND pair_presented = true
AND is_training = false
```

A never-presented pair is missing exposure, not a failed participant choice, and must not enter the Coverage denominator as though the participant saw it.

Primary directional evidence remains restricted to first-attempt A/B selections.

## Telemetry

Store relative monotonic timing only:

```text
pair_ready_elapsed_ms
block_elapsed_ms_at_event
remaining_budget_at_pair_start_ms
```

Do not store absolute client timestamps server-side.

## Consequence for retry analysis

A retry may expose a pair that was never exposed in the primary attempt. That retry remains secondary process evidence; it does not retroactively create primary directional evidence for the missing primary exposure.
