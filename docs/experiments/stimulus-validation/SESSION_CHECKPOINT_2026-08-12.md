# ConflictLab v0.8 — Stimulus Validation Checkpoint

**Date:** 2026-08-12
**Scope:** Wave 1 candidate development
**Status:** INTERNAL CURATION COMPLETE — awaiting human Wave 1 session

## Constitutional boundary

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
```

All candidates remain design/test hypotheses. No X/Y choice has inherent CS/CR polarity.
`signal_mapping_status: NONE` for all pairs until human evidence supports later interpretation.
AW static-stimulus axis: **SUSPENDED**.

## Wave 1 — 6/6 families KEEP, 12 assets committed

### CS-PR-01 — Partial Reveal

- status: `KEEP for Wave 1`
- X: `more-reveal.webp` (more visual access)
- Y: `less-reveal.jpg` (less visual access)
- calibration: approximate — do not claim exact percentages
- main confound to watch: aesthetics / composition
- signal_mapping_status: NONE

### CS-RE-01 — Relation Evidence

- status: `KEEP for Wave 1`
- X: `more-evidence.png` (central connector section visible)
- Y: `less-evidence.png` (connector section less visible)
- main confounds to watch: composition, connector aesthetics, possible CR cross-load
- signal_mapping_status: NONE

### CS-CA-01 — Context / Reference Availability

- status: `KEEP for Wave 1`
- X: `more-reference.png` (subtle vertical wall edge present)
- Y: `less-reference.png` (same scene, edge removed)
- main confounds to watch: composition / visual anchoring / CR cross-load
- signal_mapping_status: NONE

### CR-PZ-01 — Predefined Zones

- status: `KEEP for Wave 1`
- X: `no-predefined-zones.png`
- Y: `predefined-zones.png`
- signal_mapping_status: NONE

### CR-FS-01 — Fixed Slots vs Continuous Capacity

- status: `KEEP for Wave 1`
- X: `fixed-slots.png`
- Y: `continuous-capacity.png`
- signal_mapping_status: NONE

### CR-PO-01 — Partitioned vs Open Functional Space

- status: `KEEP for Wave 1`
- X: `partitioned-space.png`
- Y: `open-space.png`
- signal_mapping_status: NONE

## Internal curation notes

`pair-review.html` was used with real candidate pairs. Gemini/AI review is curation support only — overly positive outputs possible. Final KEEP verdict was human.

Image-generation workflow rule for future assets:
- new candidate / new MASTER → fresh image-generation conversation
- once MASTER approved → derive X/Y in same edit context
- all final stimulus assets must be 1:1
- remove model/provider logos consistently before human testing

## Next action

**Human Wave 1 blind multi-pair session — all 6 exemplars together.**

- do not generate additional stimulus before Wave 1 human evidence
- left/right position must be randomized by UI
- do not expose CS/CR/family labels to participants
- free text reason required per choice
