# ConflictLab — Future Session Implementation Baseline Status v0.9

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**PR:** Draft PR #2  
**Status:** ISOLATED END-TO-END FUTURE SESSION PREVIEW IMPLEMENTED; NO DEPLOYMENT

## Current state

```text
M1-M7 architecture decisions       CLOSED
F1 exact stimulus identity          COMPLETE AS DRAFT
F2 rapid mechanics                  COMPLETE FOR PILOT
6000 ms timing gate                 READY / real data pending
reason-map                          48 DRAFT ITEMS
exact-asset review                  COMPLETE
Reflection model/UI                 IMPLEMENTED AS DRAFT
session orchestration               IMPLEMENTED
end-to-end pilot preview            IMPLEMENTED / SERVER-ISOLATED
owner UX approval                   PENDING
Gate D                              NONE
Gate E                              NONE
production deploy                   NOT AUTHORIZED
```

## End-to-end path now implemented

Internal preview:

`docs/experiments/future-session-pilot-preview.html`

Composition:

```text
stimulus-set-v1
+ rapid-presentation-v1
↓
two-session presentation planner
↓
selected 3-pair session
↓
six-asset preload + decode
↓
FutureSessionOrchestrator
↓
RapidBlockAttempt (shared 6000 ms hypothesis)
↓
retry with same order + same positions when required
↓
deriveReflectionAnchors
↓
reason-map-v1
↓
Reflection model + UI
↓
local-only completion/debug view
```

No participant result is calculated or displayed in this preview.

## Orchestration invariants

Source:

`src/future_session/session_orchestrator.mjs`

The orchestrator:

- keeps one stable logical `blockId`;
- creates a new `blockAttemptId` per attempt;
- preserves the exact session plan on retry;
- passes prior exposure counts into retries;
- appends attempt events only after the attempt is terminal;
- preserves PRIMARY reflection anchors when a retry later differs;
- uses FIRST_COMPLETED_RETRY only when primary A/B is missing;
- carries page-hidden diagnostics without pausing the clock;
- settles a timeout even when `markPairReady()` itself reaches the deadline;
- exposes structured telemetry without networking.

## Pilot preview boundaries

The preview deliberately:

- preloads and decodes all six selected-form assets before Start becomes enabled;
- starts the monotonic budget only after pair 1 becomes interactive;
- reads the budget from `rapid-presentation-v1.json` rather than hardcoding it;
- keeps the pair layout vertical top/bottom on every viewport;
- displays no numeric countdown;
- permits only A/B taps during the rapid block;
- uses no `no_clear_choice`;
- performs no server/API calls;
- reuses preloaded in-memory object URLs for reflection;
- shows internal telemetry only inside a post-session debug disclosure;
- uses DRAFT configs only through explicit `allowDraft=true`.

## What remains unvalidated

```text
6000 ms budget                 unvalidated until real telemetry
Gate D pair mapping            NONE
Gate E aggregation             NONE
reason-map lifecycle           DRAFT
stimulus lifecycle             DRAFT
participant result claims      not authorized
```

## Next owner action

The next meaningful manual gate is to open the isolated pilot preview on the intended phone/browser and judge:

1. whether the 3-pair rapid interaction feels technically usable;
2. whether retry transition is understandable without coaching the choice;
3. whether Reflection wording feels natural after the actual rapid experience;
4. whether the selected image + four reason options fit comfortably on mobile;
5. whether any participant-facing wording feels leading.

That UX review may change presentation wording, but it must not silently change timing, stimulus identity, Gate D/E or data semantics.

## Production safety

Still untouched:

```text
deploy/wave1-hostinger
current Wave 1 API
existing Wave 1 responses table
production database
```

No production deploy is authorized.
