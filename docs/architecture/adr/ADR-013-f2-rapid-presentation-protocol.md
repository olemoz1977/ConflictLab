# ADR-013 — F2 rapid presentation protocol

**Date:** 2026-08-14  
**Status:** ACCEPTED FOR PILOT IMPLEMENTATION  
**Scope:** future-session presentation mechanics only

## Context

F1 fixed the exact identity of the six current Wave 1 candidate pairs and twelve source assets. The next gate is how those six factual pair identities are presented in the future three-pair shared-budget rapid protocol.

Presentation mechanics must not create avoidable confounds and must not depend on a participant's earlier choice, timeout or retry outcome.

This ADR does **not** validate CS/CR meaning, Gate D direction, Gate E aggregation, reflection reasons or the 6000 ms budget as a validated threshold.

## Decision

### 1. One session contains one rapid block

```text
1 session
= 1 rapid block
= 3 sequential pairs
```

Reflection follows that block according to the separate reflection architecture.

### 2. The six F1 pairs form two complementary three-pair forms

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

The grouping is operational. `CS-*` / `CR-*` are source-family provenance labels only and do not authorize participant interpretation.

Across the two forms:

- every F1 pair appears exactly once;
- each form contains three pairs;
- one form contains one CS-provenance and two CR-provenance pairs;
- the other contains two CS-provenance and one CR-provenance pair;
- the current repository asset payload is distributed reasonably across the two forms rather than concentrating both largest pairs into one form.

### 3. Two-session local cycle

For a device-local cycle:

```text
Session 1 -> random F2-A or F2-B
Session 2 -> the complementary unused form
Session 3 -> begins a new cycle
```

Therefore under normal local continuity no pair repeats in the first two sessions.

Timeout, retry, choice or missingness **must not change the next form assignment**. Adapting future stimulus selection to prior participant behavior would create an additional experimental condition.

The cycle state is local only. It is not a persistent server participant identifier. Clearing storage or using another device breaks local continuity; the server must not infer or reconstruct it through fingerprinting.

### 4. Pair order

At the start of a new logical block, the three pair identities in the selected form receive a uniform random permutation.

```text
primary attempt -> randomized order
retry attempt   -> exact same order
new cycle       -> may reshuffle
```

Retry does not introduce another order manipulation.

### 5. A/B screen position

The future rapid protocol uses one presentation geometry across device categories:

```text
vertical top / bottom
```

Desktop does not switch the experiment to left/right merely because horizontal space is available.

Within a three-pair block, stable asset A is placed at the top for exactly one or two pairs, never zero and never all three.

For the first two sessions in a local cycle:

```text
if session 1 has A-top count = 1
session 2 has A-top count = 2

if session 1 has A-top count = 2
session 2 has A-top count = 1
```

Thus the six first-cycle presentations contain exactly three A-top and three A-bottom assignments.

Which concrete pairs receive A-top is randomized within the block.

Retry reuses the exact primary A/B positions.

Always:

```text
A != top
B != bottom
A != +1
B != -1
```

The event records concrete top/bottom placement separately from stable A/B identity.

### 6. Preload and readiness

All six image assets required by the selected three-pair form must be fetched and decoded into memory **before the rapid block may start**.

The participant cannot start the timed block while any selected asset is unresolved.

The monotonic block clock begins only when the first pair is interactive after successful preload.

The timed interaction path must not depend on a network request after block start.

### 7. Preload failure is not participant timeout

If any selected asset cannot be fetched/decoded during preflight:

```text
technical preload failure
!=
participant timeout
```

No research block attempt starts and no rapid timeout event is created.

The UI may offer another preload attempt. That technical retry does not consume one of the three allowed rapid block attempts.

This prevents network/cache failure from entering Coverage or missingness as if the participant saw a pair and failed to answer.

### 8. Shared budget

Pilot configuration remains:

```text
6000 ms total for the three-pair block
```

But the status is explicitly:

```text
PILOT_HYPOTHESIS_NOT_VALIDATED
```

F2 accepts the mechanics required to test this condition. It does not claim that 6000 ms is the final valid research budget.

Existing ADR rules continue to apply:

- client monotonic time adjudicates the deadline;
- page backgrounding does not pause the clock;
- retry uses up to three total attempts;
- same order and same positions are retained on retry;
- never-presented pairs remain distinct from shown timeouts.

## Machine-readable source of truth

The pilot presentation contract is stored in:

```text
config/future-session/rapid-presentation-v1.json
```

The pure planning implementation is:

```text
src/future_session/presentation_plan.mjs
```

## Consequences

### Positive

- first two local sessions cover all six F1 pair identities without repetition;
- domain-provenance families are not concentrated into one homogeneous block;
- A/B identity is position-balanced without implying direction;
- retry is a re-exposure condition rather than a new order/position experiment;
- asset/network readiness is moved outside the timed condition;
- participant timeout is not contaminated by technical preload failure;
- server anonymity remains session-scoped.

### Limitations

- sample-level pair-order balance is randomized, not centrally assigned;
- local two-session balance cannot survive storage clearing or device switching;
- the 6000 ms budget still requires empirical calibration;
- a future release may require a new protocol version if F2 pilot data show serial depletion, excessive timeout or device-specific rendering effects.

## Explicitly not decided here

- Gate D directional mapping;
- Gate E domain aggregation;
- reflection reason wording;
- interpretation of latency or timeout;
- final training-pair count;
- production deployment.
