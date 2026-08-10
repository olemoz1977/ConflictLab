# ConflictLab v0.8 — Stimulus Experience Card V1

**Status:** Active working template / candidate design tool  
**Date:** 2026-08-10  
**Scope:** Pair P0 / v0.8 stimulus-library development  
**Depends on:** `STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md`, ADR-011, `METHODOLOGY_DELTA_2026-08-10.md`

---

## Purpose

This card is the working unit for designing candidate stimulus pairs before asset generation.

A candidate must satisfy three independent requirements:

> **CONTROL + EXPERIENCE + INTERPRETABILITY**

- **CONTROL** — the X/Y difference is observable, documented, and sufficiently isolated.
- **EXPERIENCE** — both alternatives are legitimately engaging; the pair creates real choice tension and is worth experiencing.
- **INTERPRETABILITY** — the participant's reaction can later provide useful context for Gate D, including a defensible `NONE` outcome.

Methodological cleanliness alone is not sufficient. Neutral does not mean meaningless.

This document does **not** validate any stimulus, assign AW/CS/CR polarity, or freeze Gate D mathematics.

---

## Constitutional boundary

Per ADR-011:

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
```

At design stage a candidate may use:

```text
target_signal_hypothesis: AW | CS | CR | exploratory
hypothesized_direction: unconfirmed
signal_mapping_status: NONE
vector_assignment: NONE
```

A raw X/Y choice has no inherent psychological polarity.

---

# Card template

## 1. Identity

```text
pair_candidate_id:
scene_family:
target_signal_hypothesis:
hypothesized_direction: unconfirmed
status: DRAFT
```

## 2. Scene

Describe what the participant sees in ordinary visual language. This is not yet an image-generation prompt.

## 3. Manipulation

```text
manipulated_property:
constant_elements:
known_secondary_changes:
```

The dominant X/Y difference should be expressible in one clear sentence.

## 4. Experience gate

Document:

```text
why_X_can_legitimately_attract:
why_Y_can_legitimately_attract:
```

Check qualitatively:

- visual interest
- genuine choice tension
- equal legitimacy
- reaction richness
- willingness to continue to another pair

Do not invent numeric pass thresholds.

## 5. Reaction space

Before writing cues, list plausible participant reasons:

```text
plausible_X_reactions:
plausible_Y_reactions:
aesthetic_or_surface_reactions:
possible_crossloads:
```

Cue language must come from plausible reaction space, not from AW/CS/CR labels.

## 6. Response UX candidate

After the image choice:

1. `reaction_intensity` — ordinal 1–5, midpoint 3
2. `Kas labiausiai nulėmė tavo pasirinkimą?` / equivalent localized wording
3. approximately three scene-relevant reaction options, plus:
   - `Kita`
   - `Sunku įvardyti`

`no_clear_choice` and `hard_to_identify` remain distinct states.

Cue = reaction context, not automatic vector generation.

## 7. Gate D paths — preformal examples only

Before human-response work, document examples of what could later be:

```text
supported_candidate
NONE
cross_load
unresolved
```

These examples are safeguards against post-hoc interpretation. They are **not** frozen mapping rules and do not constitute a Gate D contract.

## 8. Control / confound audit

Document at minimum:

- visual salience / composition
- aesthetics
- information availability
- structure / organization
- affordance / agency
- threat / reward / damage
- social meaning / status / privacy when applicable
- technical X/Y differences introduced by asset generation

## 9. Failure conditions

Return to `REVISE`, `HOLD`, or `REJECT` when, for example:

- one alternative becomes obviously better, safer, more correct, more professional, or more attractive
- reaction space collapses to one banal reason
- aesthetics dominate the intended scene-property manipulation
- a competing interpretation structurally dominates
- X/Y technical differences exceed the documented manipulation
- the pair is visually sterile or encourages mechanical clicking
- later responses provide little evidence relevant to the target hypothesis

A cue must never rescue a weak stimulus.

---

# Pilot candidate pool

The following are **PILOT CANDIDATES**, not accepted stimuli and not validated mappings. No final assets are approved by this document.

---

## AW-C01 — Relational social scene

```text
pair_candidate_id: AW-C01
scene_family: public-space / two-agent relation
target_signal_hypothesis: AW
hypothesized_direction: unconfirmed
status: PILOT CANDIDATE
signal_mapping_status: NONE
vector_assignment: NONE
```

### Scene

Two visually neutral, stylized, faceless human figures in an attractive but calm contemporary public/gallery space. No dominant artwork, doorway, status cue, facial expression, or explicit social story.

### Manipulation

**Manipulated property:** relative whole-body orientation of the two agents.

**Constants:** feet positions, inter-agent distance, camera, lighting, architecture, body form, posture and all non-orientation scene elements.

X/Y must not simultaneously change distance, gaze, gesture, or expression.

### Choice tension

One realization may legitimately attract because the relationship feels more connected, active, or mutually oriented.

The other may legitimately attract because it feels more spacious, calm, autonomous, or less direct.

Neither realization should imply friendship, conflict, rejection, romance, threat, or departure.

### Reaction space examples

Possible reactions include:

- `Čia jaučiasi daugiau ryšio.`
- `Čia daugiau erdvės.`
- `Kitas variantas per daug tiesioginis.`
- `Šita scena atrodo natūralesnė.`
- `Man tiesiog gražesnė kompozicija.`
- `Sunku įvardyti.`

### Gate D path examples — not mappings

- relation / engagement / desired distance language may later support an AW candidate
- composition-only or aesthetic reasons may support `NONE`
- vague social discomfort may remain `unresolved` unless evidence is sufficient

### Main risks

Social-story projection, symmetry preference, intimacy, rejection semantics, gender/status leakage, aesthetic dominance.

---

## CS-C01 — Partial reveal

```text
pair_candidate_id: CS-C01
scene_family: architectural / controlled reveal
target_signal_hypothesis: CS
hypothesized_direction: unconfirmed
status: PILOT CANDIDATE
signal_mapping_status: NONE
vector_assignment: NONE
```

### Scene

An aesthetically engaging, calm architectural/interior scene. A neutral sculptural or environmental element is partly visible behind a separate foreground screen or partition. No obvious path, door, destination, threat, valuable object, or narrative reveal.

### Manipulation

**Manipulated property:** degree of direct visual reveal of the same neutral element.

**Constants:** camera, architecture, object, lighting, color, scale, scene content and all non-occlusion geometry.

The foreground screen remains present in both X and Y; only its documented position/reveal relation changes.

### Choice tension

More reveal may legitimately attract because more can be seen or understood.

Less reveal may legitimately attract because it preserves intrigue, ambiguity, imagination, or a calmer composition.

Both realizations must remain complete, intentional compositions.

### Reaction space examples

Possible reactions include:

- `Norėjosi matyti daugiau.`
- `Taip lengviau suprasti vaizdą.`
- `Įdomiau, kai ne viskas parodyta.`
- `Smalsu, kas ten.`
- `Šita kompozicija ramesnė.`
- `Šitas tiesiog gražiau atrodo.`
- `Sunku įvardyti.`

### Gate D path examples — not mappings

- explicit easier-understanding / information-availability language may later support a CS candidate
- explicit comfort with partial information may later support a CS candidate in the other direction
- curiosity may be a possible CS/AW cross-load rather than a clean signal
- aesthetic-only reasons may support `NONE`

### Main risks

Curiosity dominating the choice, path/access semantics, dramatic concealment, aesthetic imbalance, salience changes caused by occlusion.

---

## CR-C01 — Structured vs continuous creative workspace

```text
pair_candidate_id: CR-C01
scene_family: creative-workspace / spatial organization
target_signal_hypothesis: CR
hypothesized_direction: unconfirmed
status: PILOT CANDIDATE
signal_mapping_status: NONE
vector_assignment: NONE
```

### Scene

An attractive contemporary creative/work surface with several neutral, non-branded objects already arranged neatly. No text, screens, status markers, people, or obvious performance cue.

### Manipulation

**Manipulated property:** degree to which the physical surface pre-defines spatial zones or positions.

**Constants:** every object's position and orientation, camera, lighting, cleanliness, materials, scene content and overall visual quality.

One realization uses subtle physical zoning; the other uses a continuous open surface. Actual object order remains equally neat in both.

### Choice tension

Zoning may legitimately attract because boundaries and locations are explicit and easy to navigate.

A continuous surface may legitimately attract because it preserves flexibility, openness, and self-directed arrangement.

Neither may look more expensive, efficient, professional, clean, or correct.

### Reaction space examples

Possible reactions include:

- `Patinka, kai aišku, kur kas priklauso.`
- `Taip lengviau susiorientuoti.`
- `Patinka, kad galiu pats nuspręsti.`
- `Čia daugiau laisvės.`
- `Atrodo profesionaliau.`
- `Atrodo erdviau ir gražiau.`
- `Sunku įvardyti.`

### Gate D path examples — not mappings

- explicit predefined-place / flexibility language may later support a CR candidate
- orientation/easier-navigation language may be a possible CR/CS cross-load
- professional/beautiful/expensive preference may support `NONE`

### Main risks

Professionalism and efficiency bias, visual complexity, premium-design preference, zoning interpreted mainly as clarity rather than configurational constraint.

---

# Pilot purpose

The first pilot is not intended to infer a person profile from three pairs.

It tests whether the v0.8 pipeline can support:

```text
controlled + engaging stimulus
        -> spontaneous choice
        -> reaction context
        -> later defensible SIGNAL / CROSS-LOAD / NONE / UNRESOLVED handling
```

Only after the candidate assets survive visual-control and experience review should the project expand the library pool or formalize Gate D mappings.
