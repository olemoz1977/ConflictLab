# ADR-011: Stimulus–Signal Separation

**Status:** Active
**Date:** 2026-08-10
**Context:** ConflictLab v0.8 stimulus library design
**Supersedes:** Implicit assumption in V1.1 that design-stage axis analysis constitutes signal evidence

---

## Decision

Three levels of stimulus work are strictly separated. They cannot be collapsed.

```
LEVEL 1 — SCENE PROPERTY / VISUAL MANIPULATION
What is visible in the image.
Described in visual, observable terms.
Belongs to: designer / AI.

LEVEL 2 — PARTICIPANT RESPONSE
Empirical data: A/B choice, cue, reaction_intensity,
latency, hard_to_identify, no_clear_choice.
Belongs to: participant.

LEVEL 3 — DERIVED SIGNAL (AW / CS / CR)
AW+, AW-, CS+, CS-, CR+, CR-
Reached only after Gate D.
Belongs to: empirical process, not designer.
```

---

## Consequences

### What is permitted at design stage

```
target_signal_hypothesis: AW   (or CS, CR, exploratory)
hypothesized_direction: unconfirmed
```

These are design hypotheses only. They carry no empirical weight.

### What is forbidden before Gate D

- Stating that a scene property "creates" an AW signal
- Writing AW+, AW-, CS+, CS-, CR+, CR- for a stimulus variant
- Using axis separation analysis to conclude signal dominance
- Treating A/B choice as having inherent psychological polarity

### Raw A/B choice

Raw A/B choice has no inherent psychological polarity.
The same choice can be consistent with AW+, AW-, CS, CR, or none,
depending on the participant's reason — which is unknown until Gate C/D.

### prototype-nine-v1 historical note

The choice→cue→vector pipeline used in prototype-nine-v1 is
historical prototype logic. It was methodologically exploratory.
It is not v0.8 truth. prototype-nine-v1 data is labeled
`prototype_only` or `reviewed` accordingly. It is not a
validated stimulus-to-signal mapping.

---

## Rationale

A stimulus pair that reliably elicits a certain reaction profile
is an empirical finding, not a design claim. Claiming signal
direction at design stage introduces confirmation bias into all
subsequent evaluation stages (Gate A–D). Separating the three
levels prevents this.

---

## Relation to other ADRs

ADR-010 (Observation Engine): Engine is cold — never evaluates
psychological meaning. ADR-011 extends this to the design stage:
AI cannot pre-assign signal polarity to a stimulus.

