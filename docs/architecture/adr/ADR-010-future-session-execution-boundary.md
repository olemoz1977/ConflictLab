# ADR-010 — Future-session execution and data boundary

**Date:** 2026-08-14  
**Status:** ACCEPTED  
**Scope:** post-Wave-1 / future-session architecture  
**Resolves:** M1–M7 in `RESULT_CALCULATION_ARCH_v0.2_IMPLEMENTATION_REVIEW.md`

## Context

The v0.2 implementation review identified seven decisions that had to be resolved before implementation. Two review recommendations also conflict with the rapid-block experimental model:

1. using server receive time as timeout authority would mix network latency into participant response timing;
2. waiting for server ACK before advancing would make network conditions part of the shared block budget.

This ADR is the binding resolution. The implementation review remains an audit record and is not rewritten retrospectively. Where this ADR conflicts with a recommendation in that review, this ADR supersedes it.

## Decisions

### M1 — Block timer authority

**Decision: client monotonic elapsed time is authoritative for the interaction clock.**

- Use `performance.now()` (or an equivalent monotonic browser clock) for elapsed timing.
- Do not use wall-clock timestamps to decide whether a tap beat the deadline.
- Server receive time is ingestion/audit metadata only.
- A tap recorded before the local monotonic deadline remains a choice even if the network request reaches the server after the budget expires.
- Events are recorded locally first and uploaded asynchronously.
- Advancing to the next pair MUST NOT wait for server ACK.
- `pendingEvents[]` uses idempotent retry keyed by `event_id`.
- When the page becomes hidden, the block clock continues; log `page_hidden_during_block=true`. Do not pause the experimental budget.

Rationale: network latency and backgrounding must not grant or remove response time.

### M2 — Retry limit

**Decision: maximum three total block attempts.**

```text
attempt 1 = primary
attempt 2 = retry 1
attempt 3 = retry 2
MAX_BLOCK_ATTEMPTS = 3
```

- Retry uses the same pair order.
- All events are append-only.
- Only attempt 1 is eligible for primary directional evidence.
- Retry choices never fill missing primary directional evidence.

### M3 — Reflection trigger

**Decision: reflection starts after the first fully completed attempt, or after the final allowed attempt.**

- Attempt 1 complete → reflection immediately.
- Attempt 1 incomplete, attempt 2 complete → reflection after attempt 2.
- Attempt 2 incomplete, attempt 3 complete → reflection after attempt 3.
- Attempt 3 incomplete → stop retrying and enter reflection only for pairs with a valid anchor.
- A pair with no completed A/B choice across all attempts receives no reflection item.

Anchor provenance remains:

```text
primary choice exists        → PRIMARY
otherwise first retry choice → FIRST_COMPLETED_RETRY
```

### M4 — `reason_id` catalog

**Decision: architecture is fixed; content remains blocked until the stimulus set is frozen.**

Reason IDs are pair- and anchor-specific. Required fields:

```text
pair_id
anchor_choice
reason_id
text_lt
text_en
interpretability_class
reason_map_version
```

Allowed interpretation classes:

```text
DOMAIN_CONSISTENT_REASON
CROSS_DOMAIN_REASON
OTHER_REASON
UNRESOLVED
```

The absence of catalog content does **not** block DB/event schema, rapid-block state machine, Calculation Engine or Evidence Engine. It blocks only the Reflection UI that depends on concrete reasons.

### M5 — Gate D / Gate E storage

**Decision: immutable versioned JSON artifacts are the methodological source of truth.**

Canonical paths:

```text
config/future-session/gate-d-v1.json
config/future-session/gate-e-v1.json
config/future-session/reason-map-v1.json
```

Lifecycle rule:

- DRAFT artifacts may change before release.
- Once marked `RELEASED`, a version is immutable.
- Methodological changes create a new version (`v2`, `v3`, ...), never overwrite a released version.
- Server may cache/serve these files, but a mutable DB table is not the source of truth.

This preserves historical result reproduction by explicit config version.

### M6 — Session identity and longitudinal continuity

**Decision: anonymous session-scoped UUID by default.**

- Generate a new `session_id` for every session.
- No persistent `participant_id` is sent to the server in the default protocol.
- Cross-session continuity may exist locally on-device.
- Longitudinal server-side linkage requires a separate explicit research consent flow and a random `study_link_id` introduced by that study protocol.
- Do not derive continuity from browser/device fingerprinting.

### M7 — Server-side reflection data

**Decision: strict local-first minimum.**

Default server exclusions:

```text
free_text
reaction_intensity
self-report responses
derived personal result
published result snapshot
```

`reason_id` may be transmitted only under explicit opt-in consent for a defined research purpose, initially:

> Evaluate whether structured reason selections across specific visual pairs support or constrain Gate D interpretation.

Free text and intensity remain local-only in the v0.2 baseline. Future server collection requires a new documented research purpose and consent revision.

## Consequences

### Client

The client owns experimental timing, local event capture, the pending upload queue, Calculation Engine, Evidence Engine and participant-facing result snapshots.

### Server

The server is a research telemetry collector and public config host. It does not calculate personal results in the v0.2 baseline.

### Database

The future-session server schema contains no persistent participant identity and no personal reflection text/intensity fields. Gate D/E and reason-map methodological definitions are not stored as mutable DB source-of-truth tables.

### Wave 1

The existing Wave 1 `responses` table, deployed application and collected data remain unchanged.

## Implementation gate

M1, M2, M3, M5, M6 and M7 are **CLOSED**.

M4 is **ARCHITECTURE CLOSED / CONTENT PENDING** and blocks only Reflection UI content implementation.

Implementation may proceed with schema/config skeleton, rapid-block infrastructure and deterministic engines without waiting for reason catalog content.
