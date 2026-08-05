# 06 — Reviewer Guide

## What we are asking you to evaluate

- Epistemic boundaries: does the documentation or product ever claim more than the evidence supports?
- Stimulus design: are the current image pairs and cues adequate for any intended purpose, and what controls would be needed before drawing conclusions from them?
- Reflection safety: does the system's language ever risk suggesting a conclusion about the person, rather than reflecting their own words back to them?
- User experience clarity: is the task, at each step, understandable without external explanation?
- Potentially misleading statements: are there any claims, labels, or naming choices (in-product or in documentation) that could be misread as scientific or diagnostic claims?
- Minimal validation steps: what would need to happen, methodologically, before any claim in `02_CLAIM_STATUS_MATRIX.md` could move from "hypothesis" to "established"?

## What we are not asking you to evaluate this as

- A diagnostic test
- A psychometric scale
- An analog to the Implicit Association Test (IAT) or Approach-Avoidance Task (AAT)
- A validated neuroscientific instrument

Pair P0 does not claim methodological equivalence to any of the above, and should not be reviewed as if it does.

## Specific questions for the reviewer

1. Where in the documentation do claims sound stronger than the available evidence supports?
2. Where might the system still indirectly interpret the person, even where it does not intend to?
3. Could any of the cue wordings create demand characteristics (leading the person toward a particular response)?
4. What minimal stimulus controls would be needed before running any kind of pilot study?
5. What control measures or established questionnaires, if any, would be appropriate to use for validation purposes only — not for scoring the product itself?
6. Does the Pair P0 reflection flow clearly separate raw data (what the person chose or wrote) from interpretation (any conclusion about what it means)?
7. What ethical risks remain, particularly around self-reflection features that ask a person to introspect repeatedly?
8. What kind of pilot (sample size, design, population) would be methodologically adequate for the next stage of this work?

## Terminology note

The following names describe internal software components, not measurement constructs:

- Signal Engine
- Observation Engine
- Pattern Detection
- Confidence
- Vector Model
- Uncertainty Engine

**These names describe internal software functions. They do not by themselves imply psychometric, statistical, clinical, or neurobiological validity.**

In particular, **"confidence"** as used throughout this codebase refers to an internal weight assigned during content design (e.g., how strongly a given cue phrase was judged to map onto an internal axis when the cue catalog was authored). It is not a statistical confidence interval, and it carries no claim of measurement reliability.

## Status of older and archived material

- **v0.4 architecture documents** — historical / archived; do not reflect current implementation
- **Archived Python modules** — not current implementation
- **Stage F (session comparison)** — implemented as an experimental secondary layer; not validated
- **Stage G (thematic comparison)** — rejected; see `01_CURRENT_STATE.md` and `02_CLAIM_STATUS_MATRIX.md` for why
- **Karpman and other prior theoretical model documents** — historical research material; not current Pair P0 methodology
- **L0 context variation** — planned, not implemented
