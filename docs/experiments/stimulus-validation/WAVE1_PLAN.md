# ConflictLab v0.8 — Stimulus Validation Wave 1

**Status:** ACTIVE — internal curation complete, awaiting human session
**Date:** 2026-08-12
**Scope:** pre-product blind stimulus validation

## Purpose

Validate manipulation families before building a full stimulus library.

This wave does **not** validate personality traits, stable person characteristics, or a final scoring model.

Core rule:

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
```

## Wave 1 composition — 6/6 KEEP, all assets committed

Six family exemplars. Internal curation complete.

### CS

1. `CS-PR-01` — Partial Reveal — `KEEP` — assets: `more-reveal.webp` / `less-reveal.jpg`
2. `CS-RE-01` — Relation Evidence — `KEEP` — assets: `more-evidence.png` / `less-evidence.png`
3. `CS-CA-01` — Context / Reference Availability — `KEEP` — assets: `more-reference.png` / `less-reference.png`

### CR

4. `CR-PZ-01` — Predefined Zones — `KEEP` — assets: `no-predefined-zones.png` / `predefined-zones.png`
5. `CR-FS-01` — Fixed Slots vs Continuous Capacity — `KEEP` — assets: `continuous-capacity.png` / `fixed-slots.png`
6. `CR-PO-01` — Partitioned vs Open Functional Space — `KEEP` — assets: `open-space.png` / `partitioned-space.png`

All six remain unvalidated hypotheses with `signal_mapping_status: NONE`.
X/Y choice has no inherent CS/CR polarity until Gate D.
AW static-stimulus axis: **SUSPENDED**.

The purpose is to test families, not to fill a predetermined 3+3+3 or 18-pair architecture.

## Next action

**Human Wave 1 blind multi-pair session.**

Do not generate additional stimulus before Wave 1 human evidence exists.

## Asset rules

- every stimulus asset: **1:1**
- X and Y are separate files
- no labels, percentages, axis names, cues, or explanatory text inside assets
- the two variants should be as visually identical as practical
- only the intended manipulated property should change
- left/right position must be randomized by the validation UI

## Internal curation gate (completed)

`docs/experiments/stimulus-validation/pair-review.html` was used for internal curation.
It sends X/Y images to Gemini for constrained multimodal audit of CONTROL / EXPERIENCE / INTERPRETABILITY.
AI recommendation is curation support only — it does not validate CS/CR, assign signal direction, or replace human-response evidence.
Final curation verdict was human.

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

Also record dominant confounds: aesthetics, composition, utility, familiarity, social desirability, salience / novelty.

A family is promising only if reactions in its intended domain appear naturally without cue-leading and both variants remain legitimate choices.

## Decision path

```text
6 family exemplars — internal curation COMPLETE
↓
human Wave 1 blind session
↓
KEEP / REVISE / REJECT by family
↓
second exemplars only for surviving families
↓
candidate stimulus pool
```
