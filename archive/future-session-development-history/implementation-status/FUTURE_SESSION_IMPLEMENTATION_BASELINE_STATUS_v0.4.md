# ConflictLab — Future Session Implementation Baseline Status v0.4

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Base:** `44426f715103a90bc79967d2655b75c1f33bbd2c`  
**PR:** Draft PR #2  
**Status:** F1 ASSET IDENTITY COMPLETE + F2 PILOT PRESENTATION MECHANICS COMPLETE — TIMING CALIBRATION PENDING

## Decision gate

```text
M1  block timer authority          CLOSED
M2  retry limit                    CLOSED
M3  reflection trigger             CLOSED
M4  reason catalog architecture    CLOSED
    reason catalog content         PENDING
M5  Gate D / Gate E storage        CLOSED
M6  session vs participant ID      CLOSED
M7  reflection server purpose      CLOSED

F1  exact stimulus identity        COMPLETE (DRAFT set)
F2  presentation mechanics         COMPLETE FOR PILOT
    6000 ms budget validity        CALIBRATION REQUIRED
```

## F1 source-of-truth

`config/future-session/stimulus-set-v1.json` contains the six exact Wave 1 pair identities and twelve repository-resident assets with stable neutral A/B IDs, repository paths, SHA-256 and MIME provenance.

The set remains `DRAFT`. F1 identity does not authorize Gate D or Gate E interpretation.

## F2 machine-readable protocol

Added:

```text
config/future-session/rapid-presentation-v1.json
```

Current pilot protocol:

```text
1 session = 1 rapid block = 3 pairs
2 complementary forms cover all 6 F1 pairs
first two local sessions contain no repeated pair
session 1 form chosen 50/50
session 2 uses complementary form
session 3 begins a new cycle
```

Forms:

```text
F2-A
  CS-CA-01
  CR-PZ-01
  CR-PO-01

F2-B
  CS-PR-01
  CS-RE-01
  CR-FS-01
```

This grouping is operational only. Source-family labels do not authorize psychological interpretation.

## F2 pair order and retry

For each new logical block:

```text
pair order = randomized permutation of the selected form
```

Retry retains:

```text
same three pair identities
same pair order
same A/B top-bottom assignments
```

Participant choice, timeout, retry outcome or missingness never changes which complementary form is scheduled next. This prevents adaptive stimulus scheduling from becoming an unplanned experimental condition.

## F2 position balance

The pilot uses one geometry across device categories:

```text
vertical top / bottom
```

Within each three-pair block, stable A appears at the top exactly once or twice.

Across the first two local sessions:

```text
A-top count = 3 of 6 presentations
A-bottom count = 3 of 6 presentations
```

Concrete pair assignments are randomized. Stable A/B identity remains distinct from screen position and from any future Gate D direction.

## F2 preload boundary

Added:

```text
src/future_session/asset_preloader.mjs
```

Before a rapid block can start:

```text
all 6 assets for the selected three pairs
-> fetch
-> Blob
-> object URL
-> decode
-> hold in memory
```

The timed path therefore does not depend on a network request after block start.

If preload fails:

```text
TechnicalPreloadError
```

No rapid research attempt starts and no participant timeout event is created. A technical preload retry does not consume one of the three allowed rapid block attempts.

## F2 planner

Added:

```text
src/future_session/presentation_plan.mjs
```

It validates the F2 config against the exact F1 stimulus set and creates a two-session local presentation cycle.

The cycle state is local-only and is not sent as a persistent participant identifier. Storage clearing or device switching may break local balancing; no fingerprint-based reconstruction is permitted.

## Binding decision record

Added:

```text
docs/architecture/adr/ADR-013-f2-rapid-presentation-protocol.md
```

Status:

```text
ACCEPTED FOR PILOT IMPLEMENTATION
```

## Timing status

The pilot remains configured for:

```text
6000 ms shared budget for three sequential pairs
```

This is **not validated**.

Its status is explicitly:

```text
PILOT_HYPOTHESIS_NOT_VALIDATED
```

The next empirical calibration must inspect at minimum:

```text
block completion rate
retry rate
pair timeout rate
never-presented rate
position-in-block missingness
remaining budget at pair start
latency distribution by block position
mobile/tablet/desktop differences
page-hidden rate
```

A high completion rate alone is insufficient if position 3 is systematically depleted or device categories differ materially.

## CI state

Current active checks pass:

```text
legacy behavior-translation Python       PASS
future architecture/stimulus Python     PASS
exact asset verifier                    PASS
rapid presentation planner              PASS
asset preloader                         PASS
rapid block core                        PASS
Calculation Engine                      PASS
Evidence Engine                         PASS
outbox / HTTP transport                 PASS
LLM generation contract                 PASS
local result pipeline                   PASS
PHP validation/persistence contracts    PASS
```

## Interpretation boundary remains closed

Still unchanged:

```text
Gate D mappings        empty / NONE
Gate E CS              NONE
Gate E CR              NONE
reason-map items       empty
stimulus lifecycle     DRAFT
rapid protocol         DRAFT pilot
```

F2 does not assign meaning to:

```text
pair ID
A/B identity
top/bottom position
latency
timeout
retry
```

## Next work

Two workstreams can now proceed without changing the working Wave 1 application:

1. define the 6000 ms pilot calibration / accept-reject criteria;
2. author the first DRAFT pair+anchor-specific reason catalog for the six F1 pairs, keeping reflection content separate from Gate D mapping.

Reflection UI should consume only reviewed reason-map content and should not be deployed before the rapid pilot flow is independently tested.

## Still deliberately not done

- no change to live Wave 1 UI/API;
- no production DB migration;
- no stimulus or rapid-protocol `RELEASED` status;
- no Gate D mapping;
- no Gate E aggregation;
- no reason-map content;
- no Reflection UI integration;
- no production LLM provider call;
- no persistent participant identifier;
- no merge/deploy decision.
