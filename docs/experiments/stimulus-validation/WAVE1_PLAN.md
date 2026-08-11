# ConflictLab v0.8 — Stimulus Validation Wave 1

**Status:** ACTIVE PLAN  
**Date:** 2026-08-11  
**Scope:** pre-product blind stimulus validation  

## Purpose

Validate manipulation families before building a full stimulus library.

This wave does **not** validate personality traits, stable person characteristics, or a final scoring model.

Core rule:

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
```

## Wave 1 composition

Six family exemplars:

### CS
1. `CS-PR-01` — Partial Reveal
2. `CS-RE-01` — Relation Evidence
3. `CS-CA-01` — Context / Reference Availability

### CR
4. `CR-PZ-01` — Predefined Zones
5. `CR-FS-01` — Fixed Slots vs Continuous Capacity
6. `CR-PO-01` — Partitioned vs Open Functional Space

The purpose is to test families, not to fill a predetermined 3+3+3 or 18-pair architecture.

## Asset rules

- every stimulus asset: **1:1**
- X and Y are separate files
- no labels, percentages, axis names, cues, or explanatory text inside assets
- the two variants should be as visually identical as practical
- only the intended manipulated property should change
- left/right position must be randomized by the validation UI

## Internal curation gate

Use:

`docs/experiments/stimulus-validation/pair-review.html`

This is an **internal Pair Candidate Review tool**, not the human validation UI.

It accepts local X/Y image files in the browser and sends both images to Gemini for a constrained multimodal audit of:

- CONTROL
- EXPERIENCE
- INTERPRETABILITY
- unintended visual differences
- plausible confounds
- triggered failure conditions
- what should be inspected later in blind human responses

The AI recommendation is curation support only. It does not validate CS/CR, assign signal direction, or replace human-response evidence.

The final internal curation verdict remains human:

```text
KEEP for Wave 1
REVISE
ARCHIVE
```

## Current first candidate

### `CS-PR-01` — Partial Reveal

Working status:

```text
family: partial_reveal
target_domain: CS
asset_status: exploratory_pilot
calibration_status: approximate
signal_mapping_status: NONE
```

Current variants should be described neutrally as:

- `more_reveal`
- `less_reveal`

Do **not** claim exact 75% / 50% calibration in repository metadata unless later measured and confirmed.

Pilot question:

> Does changing visual access to the same object spontaneously produce reaction language about wanting to see/know more, completeness, or uncertainty — or is the choice mainly aesthetic/compositional?

## Blind participant flow

For every candidate pair:

1. show X/Y assets with randomized left/right order
2. ask: **Which do you choose?**
3. allow `no_clear_choice`
4. ask free text first: **What most influenced your choice?**
5. optionally capture reaction intensity 1–5
6. continue to next pair

Do not show CS/CR, family names, hypotheses, signal directions, radar, or reflection output.

## Minimum raw event schema

```json
{
  "participant_id": "anonymous-session-id",
  "candidate_id": "CS-PR-01",
  "candidate_version": "v0.1",
  "left_asset": "...",
  "right_asset": "...",
  "choice": "left | right | no_clear_choice",
  "free_text_reason": "...",
  "reaction_intensity": 1,
  "choice_latency_ms": 0
}
```

## Analysis target

For each family, classify raw reasons post-hoc as one of:

```text
supported
cross-load
insufficient
NONE
```

Also record dominant confounds such as:

- aesthetics
- composition
- utility
- familiarity
- social desirability
- salience / novelty

A family is promising only if reactions in its intended domain appear naturally without cue-leading and both variants remain legitimate choices.

## Decision path

```text
6 family exemplars
↓
internal pair curation gate
↓
human response data
↓
KEEP / REVISE / REJECT by family
↓
second exemplars only for surviving families
↓
candidate stimulus pool
```

Do not scale the library before Wave 1 evidence exists.
