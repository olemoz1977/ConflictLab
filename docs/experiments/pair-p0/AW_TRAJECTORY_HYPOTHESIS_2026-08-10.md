# ConflictLab v0.8 — AW Status Decision / Trajectory Hypothesis

**Date:** 2026-08-10  
**Status:** Active methodological decision for current v0.8 exploration  
**Scope:** Pair P0  
**Supersedes as active direction:** `AW_REDEFINITION_NOTE_v0.1.md` and `AW_EPISTEMIC_CANDIDATES_v0.1.md`  
**Does NOT rewrite:** prototype-nine-v1 historical/technical behavior

---

## Decision

The current AW (`Approach / Step Back`) stimulus-axis program is **SUSPENDED** for active v0.8 stimulus development.

AW is no longer treated as a third stimulus-target domain equivalent to CS and CR.

Current working architecture:

```text
SCENE PROPERTY
    ↓
PARTICIPANT RESPONSE
    ↓
DOMAIN INTERPRETATION
CS / CR / OTHER / NONE
    ↓
RESPONSE-ORIENTATION EVIDENCE
further-investment / reduce-investment / unresolved
    ↓
REPEATED EVENTS
    ↓
DOMAIN-SPECIFIC RESPONSE TRAJECTORY
```

The trajectory layer is an **active methodological hypothesis**, not a validated construct.

---

## Why AW stimulus development is suspended

Independent red-team reviews converged on the same problem:

- static AW-targeting concepts repeatedly collapse into CS, CR, novelty, salience, puzzle-solving, social narrative, or generic preference;
- a raw image choice does not uniquely encode approach/withdrawal orientation;
- the same observable choice can arise from incompatible motives;
- `continue` behavior can reflect duty, anxiety, reward, compliance, or product curiosity rather than a domain-specific response;
- `stop` behavior can coexist with high interest or reflective processing.

Therefore, continuing to manufacture AW-specific static-image pairs would currently create more construct contamination than information.

---

## What remains active

### CS

Clarity / Ambiguity remains an active stimulus-response domain candidate.

### CR

Structure / Flexibility remains an active stimulus-response domain candidate.

### Response trajectory

ConflictLab may later describe how reactions evolve within CS or CR contexts, for example:

- whether further-investment language repeatedly appears;
- whether reduce-investment language repeatedly appears;
- whether the direction changes across scene families;
- whether the pattern is inconsistent or unresolved.

This must always remain domain-anchored.

Allowed working labels:

```text
CS Response Trajectory
CR Response Trajectory
```

Avoid treating `AW = +0.7` or a general engagement score as meaningful.

---

## Product engagement is NOT domain trajectory

These must remain separate:

```text
PRODUCT ENGAGEMENT
Did the participant continue or return to ConflictLab?

SESSION BEHAVIOR
Did the participant complete the current flow?

DOMAIN-SPECIFIC RESPONSE TRAJECTORY
Did reaction-context evidence within CS or CR repeatedly indicate further or reduced investment?
```

Product continuation may be stored as telemetry, but it must not automatically create a psychological or domain-level signal.

---

## Single response vs trajectory

A single response may be informative evidence, but it is **not a trajectory**.

One trial can contribute:

```text
choice
reaction_context
reaction_intensity
latency
no_clear_choice / hard_to_identify
possible orientation evidence
```

Only repeated, sufficiently interpretable events may support a trajectory description.

No numeric threshold is frozen here.

---

## Response-orientation evidence

At this stage, orientation is not inferred from raw A/B choice alone.

Potential evidence may include reaction-context language such as:

- `noriu suprasti daugiau`
- `norėčiau pažiūrėti toliau`
- `man jau pakanka`
- `nenoriu tam skirti daugiau dėmesio`

But these are examples, not validated mappings.

Aesthetic, compositional, or unrelated reasons may yield `NONE` or `unresolved`.

Cue remains reaction context, not an automatic vector generator.

---

## Consequences for stimulus work

Active v0.8 stimulus-library work now prioritizes **CS and CR** candidate pools.

Do not create new AW-specific static-image assets until this suspension is explicitly reversed.

The previously drafted epistemic-AW candidates E1/E2/E3 are retained as historical exploratory evidence. They are not active production candidates.

The working stimulus quality triad remains:

> **CONTROL + EXPERIENCE + INTERPRETABILITY**

---

## Consequences for prototype-nine-v1

`prototype-nine-v1` remains frozen as a technical/UX stable reference.

Its AW/CS/CR radar, `axis: aw` metadata, cue-vector logic, and 3+3+3 arrangement are **historical prototype behavior**, not current v0.8 methodological truth.

Do not rewrite the frozen prototype solely to reflect this hypothesis.

---

## Consequences for current architecture documents

The following assumptions are now **under review / historical-prototype where they describe AW as a peer stimulus axis**:

- 3 AW + 3 CS + 3 CR as a required active v0.8 block composition;
- AW-targeting SPMC stimulus slots;
- AW as a peer bipolar radar dimension;
- 18 unique pairs as a scientific minimum.

The number 18 remains useful only as a technical planning target for two non-repeating 9-pair prototype blocks if that architecture is retained. It is not a validated scientific minimum.

Do not rewrite historical specifications in-place yet. A future integrated methodology revision may supersede them after the trajectory hypothesis is tested.

---

## Smallest next methodological step

Do not build more AW stimuli.

1. Continue designing controlled, engaging CS and CR stimulus candidates.
2. For candidate reactions, explicitly model plausible response-context paths including:
   - domain-relevant evidence;
   - possible further-investment evidence;
   - possible reduce-investment evidence;
   - cross-load;
   - `NONE`;
   - unresolved.
3. Check whether orientation-like evidence can repeat within the same domain without relying on product continuation.
4. Only then decide whether a formal domain-specific trajectory layer deserves implementation.

---

## Current status summary

```text
AW stimulus axis: SUSPENDED / historical prototype for active v0.8 work
AW-specific asset generation: STOP
CS stimulus domain: ACTIVE
CR stimulus domain: ACTIVE
Domain-specific response trajectory: ACTIVE HYPOTHESIS / NOT VALIDATED
prototype-nine-v1: FROZEN TECHNICAL/UX REFERENCE
```
