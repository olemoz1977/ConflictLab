# ConflictLab — Future Session Implementation Baseline Status v0.6

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Base:** `44426f715103a90bc79967d2655b75c1f33bbd2c`  
**PR:** Draft PR #2  
**Status:** F1 COMPLETE + F2 PILOT MECHANICS COMPLETE + TIMING GATE READY + DRAFT REASON MAP COMPLETE

## Current gate state

```text
M1-M7 architecture decisions       CLOSED
F1 exact stimulus identity          COMPLETE AS DRAFT
F2 rapid presentation mechanics     COMPLETE FOR PILOT
6000 ms budget                      PILOT HYPOTHESIS, NOT VALIDATED
Timing calibration gate             READY
reason-map architecture             CLOSED
reason-map content                  48 DRAFT ITEMS / REVIEW REQUIRED
Gate D                              NONE
Gate E                              NONE
Reflection UI                       BLOCKED pending reason-content review
production deploy                   NOT AUTHORIZED
```

## Draft reason catalog

Source of truth:

```text
config/future-session/reason-map-v1.json
```

Bound to:

```text
stimulus_set_version = stimulus-set-v1
```

Current shape:

```text
6 pairs
x A/B anchor
x 4 options
= 48 items
```

Every anchor has:

```text
R01  intended-family-consistent wording
R02  cross-load or concrete confound wording
R03  Another reason + optional LOCAL-ONLY free text
R04  Unresolved / hard to say exactly why
```

Internal interpretation classes are not participant-facing.

## Content boundary

`DOMAIN_CONSISTENT_REASON` is only a coding label for the wording of the reason option. It does not validate the pair, assign A/B polarity, prove a participant motive, or create a trait claim.

All six F1 pair mappings remain:

```text
Gate D = NONE
```

and Gate E remains NONE for CS and CR.

## Draft review record

Semantic/content review source:

```text
docs/architecture/FUTURE_SESSION_REASON_MAP_DRAFT_REVIEW_v0.1.md
```

The review explicitly separates:

- intended-family-consistent R01 wording;
- cross-domain R02 wording;
- aesthetics/composition/utility R02 confounds;
- local-only open-text path;
- unresolved response path.

## Automated contract

Test:

```text
tests/reason_map_contract.test.mjs
```

It enforces:

- reason-map stays DRAFT;
- exact stimulus-set binding;
- 48 total items;
- 4 items for every pair+anchor;
- unique pair+anchor-specific reason IDs;
- exactly one DOMAIN_CONSISTENT and one UNRESOLVED item per anchor;
- exactly one LOCAL-ONLY free-text option per anchor;
- allowed interpretation classes only;
- no direct `you are / you need / tu esi / tau reikia` trait or need language;
- participant-facing class labels remain hidden.

## Reflection data boundary

Current server rule remains unchanged:

```text
reason_id -> explicit research consent only
free text -> LOCAL ONLY
```

Because `reason-map-v1` is DRAFT, the future-session ingestion layer still fails closed for production reason telemetry.

## Reason-map release blockers

Before `reason-map-v1` can become RELEASED:

1. human LT wording review;
2. EN parity review;
3. manual exact-asset visual check for all R01/R02 descriptions;
4. review of six CROSS_DOMAIN_REASON codings;
5. confirmation that four choices per anchor is acceptable UX;
6. confirmation of local-only open text;
7. green contract CI.

## Timing work remains parallel

The 6000 ms timing hypothesis remains independent from reason-map content.

Real pilot timing data are still required until the calibration floor is reached:

```text
20 clean primary blocks
```

Synthetic tests validate evaluator behavior only.

## Still deliberately not done

- no live Wave 1 changes;
- no production DB migration;
- no stimulus RELEASED status;
- no reason-map RELEASED status;
- no Gate D mapping;
- no Gate E aggregation;
- no Reflection UI wiring;
- no production LLM call;
- no persistent participant identifier;
- no server storage of free text, intensity or personal result snapshot;
- no merge/deploy decision.

## Next gate

The next action is **reason-content human/visual review**, not Reflection UI implementation.

Only after the wording/classification review is accepted should the Reflection UI be wired to `reason-map-v1`.
