# ADR-012 — Monotonic timing precision and telemetry quantization

**Date:** 2026-08-14  
**Status:** ACCEPTED  
**Scope:** future-session rapid visual block

## Context

ADR-010 makes client monotonic elapsed time authoritative for the rapid-block deadline. Browser `performance.now()` commonly returns fractional milliseconds, while the future-session server schema intentionally stores millisecond durations as integer values.

If quantization is left to the API or database driver, the participant-facing decision and stored research telemetry can diverge unpredictably across clients or server implementations.

## Decision

### Deadline decision

The client uses the full available monotonic precision for all deadline comparisons:

```text
elapsed_precise = performance.now() - block_start

elapsed_precise < block_budget_ms  -> choice may be accepted
elapsed_precise >= block_budget_ms -> timeout
```

Do not round before the deadline comparison.

### Persisted telemetry

Non-negative elapsed-duration telemetry is quantized on the client with `Math.floor()` before it enters the transport/storage contract:

```text
pair_ready_elapsed_ms
visual_choice_latency_ms
block_elapsed_ms_at_event
remaining_budget_at_pair_start_ms
block_elapsed_ms_final
```

The configured `block_budget_ms` is an integer.

Rationale for floor rather than round: a valid tap at `5999.9 ms` in a `6000 ms` block remains represented as `5999 ms`, rather than appearing in stored telemetry to occur exactly at the timeout boundary.

### Timeout events

A timeout event records:

```text
block_elapsed_ms_at_event = block_budget_ms
block_elapsed_ms_final = block_budget_ms
```

regardless of how late the JavaScript callback that observes the expired deadline actually runs.

### Interpretation boundary

The server MUST NOT re-adjudicate whether a choice beat the deadline from quantized telemetry. The client decision made from full-precision monotonic elapsed time is authoritative under ADR-010.

Absolute client timestamps remain excluded from server telemetry.
