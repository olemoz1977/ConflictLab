# ConflictLab v0.8 — Stimulus Validation Checkpoint

**Date:** 2026-08-12  
**Scope:** Wave 1 candidate development  
**Status:** ACTIVE CHECKPOINT

## Constitutional boundary

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
```

All current candidates remain design/test hypotheses. No X/Y choice has inherent CS/CR polarity and `signal_mapping_status` remains `NONE` until human evidence supports later interpretation.

## Current Wave 1 progress

### CS — 3/3 candidate families ready for Wave 1

#### CS-PR-01 — Partial Reveal

- internal pair review: completed
- status: `KEEP for Wave 1`
- variants: `more_reveal` / `less_reveal`
- calibration: approximate; do not claim exact percentages
- main human-test question: informational completeness / partial information vs aesthetics/composition
- committed image assets already exist in repo; do not regenerate without evidence-based reason

#### CS-RE-01 — Relation Evidence

- MASTER approved
- X/Y pair approved by internal review
- status: `KEEP for Wave 1`
- X: `more_evidence`
- Y: `less_evidence`
- intended controlled delta: visibility of the central connector section between the same two modules
- main confounds to watch: composition, connector aesthetics, possible structural/CR cross-load
- final image assets are **not committed in this checkpoint**; image upload is deferred to Claude/direct GitHub workflow

#### CS-CA-01 — Context / Reference Availability v2

- initial horizontal-reference concept: `REVISE` because it was too easily read as composition/structure
- v2 spatial-reference concept approved
- MASTER approved
- X/Y pair approved by internal review
- status: `KEEP for Wave 1`
- X: `more_reference` — subtle vertical wall edge provides spatial orientation
- Y: `less_reference` — same scene with that edge removed
- main confounds to watch: composition / visual anchoring / CR cross-load
- final image assets are **not committed in this checkpoint**; image upload is deferred to Claude/direct GitHub workflow

## Pair Review status

`docs/experiments/stimulus-validation/pair-review.html` has already been used with real candidate pairs. It is not merely QA-pending.

Important limitation: Gemini/AI pair-review output can be overly positive. Treat it as a technical/confound curation aid only. Final internal `KEEP / REVISE / ARCHIVE` remains human, and actual family support can come only from blind participant responses.

## Image-generation workflow rule

For future protocol-critical assets:

- new candidate / new MASTER -> start a fresh image-generation conversation to avoid style/context carryover
- once MASTER is approved -> derive X/Y from that exact MASTER in the same edit context
- ChatGPT does not generate protocol-critical images unless explicitly asked
- Claude/direct GitHub workflow is preferred for binary image upload
- all final stimulus assets must be 1:1
- remove model/provider logos/watermarks consistently before human testing

## Next action

Begin CR Wave 1 with:

`CR-PZ-01 — Predefined Zones`

Do not build the human Wave 1 session until all six family exemplars have passed internal curation.

---

## Update — 2026-08-12 (asset batch upload)

All 10 final Wave 1 assets committed to repo in one batch:

### CR families — 3/3 assets committed

#### CR-PZ-01 — Predefined Zones
- X: `predefined-zones.png`
- Y: `no-predefined-zones.png`
- status: `KEEP for Wave 1`
- signal_mapping_status: NONE

#### CR-FS-01 — Fixed Slots vs Continuous Capacity
- X: `fixed-slots.png`
- Y: `continuous-capacity.png`
- status: `KEEP for Wave 1`
- signal_mapping_status: NONE

#### CR-PO-01 — Partitioned vs Open Functional Space
- X: `partitioned-space.png`
- Y: `open-space.png`
- status: `KEEP for Wave 1`
- signal_mapping_status: NONE

### CS assets now complete
- CS-RE-01: `more-evidence.png` / `less-evidence.png` — committed
- CS-CA-01: `more-reference.png` / `less-reference.png` — committed

## Wave 1 internal curation — COMPLETE

```text
6/6 families KEEP for Wave 1
12 assets committed (including CS-PR-01 from prior commit)
signal_mapping_status: NONE for all pairs
AW static-stimulus axis: SUSPENDED
```

## Constraints for next phase

- do not generate additional stimulus before Wave 1 human evidence
- human Wave 1 = blind multi-pair session, all 6 exemplars together
- left/right position must be randomized by UI
- do not expose CS/CR/family labels to participants
- free text reason required per choice
