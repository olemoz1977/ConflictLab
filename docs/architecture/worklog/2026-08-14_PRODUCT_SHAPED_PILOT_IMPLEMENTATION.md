# ConflictLab — Product-Shaped Pilot Implementation Log

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Release path:** `/conflictlab/releases/calibration-v0.1/`  
**Status:** IMPLEMENTED IN REPOSITORY / HOSTINGER OVERWRITE PATCH PENDING  
**Collection mode:** `TECHNICAL`  
**Public `/wave1/`:** UNCHANGED / PUBLIC SWITCH NOT AUTHORIZED

## Why this change was made

Fresh testers are scarce. A narrow timing-only page would use a participant mainly to answer the 6000 ms question and would postpone testing the future product flow.

Decision: evolve the isolated LAB into a **product-shaped pilot** before starting real N/20 collection. One fresh participant should experience the same structural sequence intended for the future product while each evidence layer remains methodologically separate.

This does not validate Gate D, Gate E, stimulus direction, or a participant characteristic.

## Implemented participant flow

```text
LT / EN language selection
-> Stage 0 training
-> rapid A/B block / shared 6000 ms candidate budget
-> timing-only server save
-> reason reflection
-> reaction intensity 1-5
-> local Calculation Engine
-> local Evidence Engine
-> fail-closed result screen
```

Language is chosen before training and remains fixed during the session.

## Response-time channels

Three timings are deliberately separate:

```text
1. visual_choice_latency_ms
   pair fully ready -> A/B choice

2. reason_response_latency_ms
   selected image + all reason controls ready -> final reason selection

3. intensity_response_latency_ms
   selected image + 1-5 controls ready -> intensity selection
```

Additional local UX diagnostic:

```text
reflection_total_elapsed_ms
```

Reason and intensity have no deadline. Their timing values are process observations only and must not be interpreted as confidence, depth, decisiveness, impulsivity or psychological strength without separate validation.

## Visual-readiness invariant

A timing race was identified during implementation: reason/intensity controls could theoretically be clicked before the selected image had completed decode/render readiness.

Resolution:

- reason controls start disabled;
- intensity controls start disabled;
- selected image is decoded;
- next animation frame marks the stage ready;
- only then are the response controls enabled and the stage timer considered active.

This preserves the meaning of the response-time origin.

## Reflection semantics

Reason and intensity are sequential rather than shown together so the two response latencies remain separable.

Current local statuses:

```text
reason_status     = ANSWERED | SKIPPED | NOT_REACHED
intensity_status  = ANSWERED | SKIPPED | NOT_REACHED
```

If a participant completes the rapid block and later skips or abandons reflection, the already-recorded rapid timing evidence is not automatically invalidated.

## Intensity boundary

Intensity is retained because it is useful as an independent self-report channel and mirrors a meaningful part of the earlier Wave1/v0.4 experience.

Hard calculation rule remains:

```text
intensity never enters Directional Balance
latency never enters Directional Balance
retry events never enter Directional Balance
reflection class never changes direction
```

## Local-first boundary

The product-shaped flow captures the following locally:

```text
reason_id
optional free text
reason_response_latency_ms
intensity 1-5
intensity_response_latency_ms
reflection_total_elapsed_ms
derived result state
```

The calibration API/schema remain timing-only and do not receive those fields in this build.

The server continues to receive the mechanical timing dataset required for the 6000 ms calibration decision, with the existing TECHNICAL/CALIBRATION run classification.

## Result-pipeline implementation

The LAB now wires the actual future-session Calculation Engine and Evidence Engine into the participant flow.

Current Gate D source remains fail-closed:

```text
lifecycle = DRAFT
stimulus_set_version = null
mappings = []
```

Current Gate E source remains fail-closed:

```text
CS = NONE
CR = NONE
```

Therefore real participant execution currently produces:

```text
resultStatus = NOT_ESTIMABLE
```

The result UI explains that directional interpretation is intentionally unavailable. It does not substitute a generic psychological result.

Synthetic/fixture inputs remain the allowed route for developing future result-processing and presentation behavior before Gate D/E validation.

## Hostinger compatibility

Hostinger previously served `.mjs` as `text/plain`. The release therefore continues to carry:

- canonical `.mjs` copies for source/integrity;
- Hostinger `.js` compatibility copies;
- `index.php` bootstrap that maps module references from `.mjs` to `.js` at delivery time.

New product-shaped modules have both canonical `.mjs` and Hostinger-compatible `.js` versions.

## Tests added / updated

New CI gates include:

```text
Product reflection timing flow
Product result fail-closed gate
Product-shaped release contract
```

They check:

- separate reason/intensity latency semantics;
- intensity range 1-5;
- local-only reflection/intensity boundary;
- LT/EN presence;
- canonical source-byte identity for packaged `.mjs` modules/configs;
- Hostinger `.js` modules do not import `.mjs`;
- current Gate D/E remain NONE;
- real result remains NOT_ESTIMABLE;
- reflection controls wait for visual readiness;
- timing API/schema do not gain reflection/intensity fields.

## Deployment state after implementation

Repository implementation is complete for this gate, but the currently deployed Hostinger LAB still contains the previous build until the owner uploads the next validated overwrite patch.

No DB migration is required for this product-shaped update.

Do not change:

```text
collection_mode = TECHNICAL
https://omesg360.eu/wave1/
omesg360.eu root
Wave1 API/storage
```

## Next gate

```text
CI green on final implementation head
-> generate validated Hostinger overwrite patch
-> owner uploads to versioned LAB path only
-> owner smoke test LT
-> owner smoke test EN
-> verify resulting runs remain TECHNICAL and N/20 stays 0
-> record UX/data-boundary findings
-> decide whether research-consent/data-collection scope is sufficient for the hypotheses
-> only then consider switching collection_mode to CALIBRATION
```
