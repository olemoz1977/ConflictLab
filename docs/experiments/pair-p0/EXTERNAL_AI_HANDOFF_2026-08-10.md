# ConflictLab — External AI Handoff
**Current as of 2026-08-10; newer repository decisions supersede this handoff.**
**Canonical source: PROJECT_STATE.md**

---

## What ConflictLab is

An Epistemic Reflection Framework. It helps people observe recurring tendencies in their own reactions without converting those observations into personality labels.

NOT: personality test, psychological diagnosis, human scoring, behavioral prediction.

---

## Product split

| | v0.7 | Pair P0 |
|---|---|---|
| Status | Frozen baseline | Active v0.8 candidate methodology + frozen P9 technical reference |
| Runtime AI | Yes in legacy flow | None in Pair P0 |
| Stable reference | — | `pair-p0-prototype-nine-v1-radar-ux-stable` |

`prototype-nine-v1` remains a technical/UX stable reference. Its 3-axis AW/CS/CR radar and cue-vector logic are historical prototype behavior, not current v0.8 methodological truth.

---

## Constitutional rule

ADR-011:

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
```

- Raw A/B choice has no inherent psychological polarity.
- Cue = reaction context, not automatic vector generation.
- `reaction_intensity` = ordinal 1–5; never vector × intensity.
- `no_clear_choice` and `hard_to_identify` are distinct states.
- Results describe tendencies in reactions, not properties of the person.
- Radar/bipolar map is secondary visual explanation, not the primary result.

---

## CURRENT AW decision

Read: `AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md`

Current status:

```text
AW as peer static-stimulus axis: SUSPENDED
AW-specific asset generation: STOP
CS stimulus domain: ACTIVE
CR stimulus domain: ACTIVE
Domain-specific response trajectory: ACTIVE HYPOTHESIS / NOT VALIDATED
```

Reason: AW-targeting static-image concepts repeatedly collapsed into CS/CR, novelty, salience, puzzle-solving, social narrative, or generic preference. Independent red-team reviews converged on the view that single-trial AW is too weak/confounded to justify a peer axis.

A single response can still be informative evidence, but trajectory claims require repeated interpretable events anchored to a domain.

Do not confuse:

- product engagement / return to ConflictLab;
- session completion;
- domain-specific response trajectory.

Product continuation must not automatically create a domain-level signal.

---

## Current stimulus-development model

Use `STIMULUS_EXPERIENCE_CARD_V1.md`.

Working quality triad:

> **CONTROL + EXPERIENCE + INTERPRETABILITY**

Methodological cleanliness alone is insufficient. Neutral does not mean meaningless.

Current active asset/concept work prioritizes CS and CR stimulus pools.

Historical AW notes/candidates are retained as reasoning evidence but are not active production instructions.

---

## Block / pair-count status

The old `3 AW + 3 CS + 3 CR` block composition is a historical/prototype construction assumption under review.

`18 unique pairs` is not a validated scientific minimum. It may remain a technical planning target for two non-repeating 9-pair prototype blocks if that architecture is retained.

Do not force a final 3+3+3 or 18-pair library merely to preserve prototype symmetry.

---

## Current near-term priority

1. Build engaging, controlled CS/CR candidate stimuli.
2. Design plausible reaction spaces, including `NONE`, cross-load and unresolved paths.
3. Minimal Gate D contract for defensible domain interpretation.
4. Examine whether repeated response-context evidence supports domain-specific trajectories without using product continuation as the signal.
5. Only then refine aggregation / result visualization.

---

## Do not do

- Do not generate new AW-specific static-image assets.
- Do not assign AW+/AW-/CS+/CS-/CR+/CR- at stimulus-design stage.
- Do not treat `prototype-nine-v1` vectors as validated mappings.
- Do not treat product continuation as automatic trajectory evidence.
- Do not rewrite frozen prototype files merely to make history look current.
- Do not actively develop v0.7 code.
- Do not use `localStorage.clear()`.
- Do not modify stable tags without explicit approval.
