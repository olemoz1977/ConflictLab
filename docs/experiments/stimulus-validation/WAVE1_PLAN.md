# ConflictLab v0.8 — Stimulus Validation Wave 1

**Status:** PILOT READY — `wave1-v0.3` FROZEN; first real participant cycle not yet started  
**Date:** 2026-08-13  
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

**Begin the first real Human Wave 1 blind multi-pair participant cycle using only `wave1-v0.3`.**

Do not generate additional stimulus before Wave 1 human evidence exists.

## Asset and presentation rules

- every stimulus asset: **1:1**
- X and Y are separate files
- no labels, percentages, axis names, cues, or explanatory text inside assets
- the two variants should be as visually identical as practical
- only the intended manipulated property should change
- pair assets are presented **vertically** in the participant UI
- preserve the full 1:1 image as far as practical; avoid cropping (`object-fit: contain` rather than crop-to-fill)
- the assignment of X/Y to first/second vertical position must be randomized by the validation UI
- X/Y position has no psychological meaning

## Internal curation gate (completed)

`docs/experiments/stimulus-validation/pair-review.html` was used for internal curation.
It sends X/Y images to Gemini for constrained multimodal audit of CONTROL / EXPERIENCE / INTERPRETABILITY.
AI recommendation is curation support only — it does not validate CS/CR, assign signal direction, or replace human-response evidence.
Final curation verdict was human.

## Blind participant flow — v0.3 frozen

For every candidate pair:

1. show the two 1:1 assets vertically, with randomized first/second position
2. ask neutrally: **Kurį renkiesi?** / **Which do you choose?**
3. allow `no_clear_choice` (`Neturiu aiškaus pasirinkimo`)
4. allow optional free-text reason
5. allow optional reaction intensity 1–5 for a left/right choice
6. allow independent `hard_to_identify` when the participant cannot clearly name the reason
7. save the response successfully before moving to the next pair

Important distinction:

```text
no_clear_choice != hard_to_identify != empty free text
```

Do not show CS/CR, family names, hypotheses, signal directions, radar, or reflection output.

`reaction_intensity` is an optional ordinal 1–5 self-report. It is not confidence, latency, valence, or signal-vector magnitude.

## Minimum raw event schema

Implementation field names preserve the following raw information:

```json
{
  "participant_id": "anonymous-session-id",
  "candidate_id": "CS-PR-01",
  "protocol_version": "wave1-v0.3",
  "presentation_index": 1,
  "left_asset": "...",
  "right_asset": "...",
  "choice": "left | right | no_clear_choice",
  "free_text": "... | null",
  "intensity": "1..5 | null",
  "hard_to_identify": "0 | 1",
  "latency_ms": 0
}
```

`left_asset` / `right_asset` are retained implementation field names for continuity with the existing database. In the current mobile UI they correspond to randomized **first/second vertical presentation**, not literal screen-left/screen-right positions.

Latency starts only after both pair images have loaded successfully and the pair is available for choice.

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

## Freeze rule

`wave1-v0.3` is the real-pilot baseline. Once real participant collection starts, do not change participant-facing wording, presentation, capture semantics, or stimulus assets under this protocol version.

Any such change requires a new protocol version and an explicit documented delta before further research data are collected.
