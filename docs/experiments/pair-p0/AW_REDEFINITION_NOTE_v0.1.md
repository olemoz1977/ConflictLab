# ConflictLab v0.8 — AW Redefinition Note v0.1

**Status:** Active working note  
**Date:** 2026-08-10  
**Scope:** Pair P0 / v0.8 methodology  
**Depends on:** ADR-011, `STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md`, `METHODOLOGY_DELTA_2026-08-10.md`

---

## Why this note exists

The current AW label (`Approach / Step Back`) risks being interpreted as one latent psychological mechanism. That is too strong.

Recent red-team work showed that reactions that look directionally similar may arise from very different processes, including:

- epistemic / exploratory interest
- affective overload regulation
- instrumental effort allocation
- relational trust / social positioning

These are not assumed to be one causal construct.

This note therefore narrows what AW is allowed to mean in v0.8.

---

## Working definition

> **AW is a response-orientation layer, not a latent cause, personality trait, or single motivational system.**

AW describes the direction of a participant's response in a specific situation when the response context supports movement toward greater engagement/contact/investment or toward reduced engagement/contact/investment.

AW does **not** explain why that direction occurred.

---

## Constitutional separation

Per ADR-011:

```text
SCENE PROPERTY
!= PARTICIPANT RESPONSE
!= DERIVED SIGNAL
```

Therefore:

- no image is inherently `AW+` or `AW-`
- raw A/B choice has no inherent AW polarity
- the stimulus may only carry `target_signal_hypothesis: AW`
- any derived AW direction requires participant response context at Gate D
- the same visual choice may yield AW-relevant, cross-loaded, unresolved, or `NONE` outcomes

---

## What AW is NOT

AW must not be reduced to any single one of the following:

- curiosity
- liking
- fear / threat response
- social trust
- effort / utility calculation
- physical distance
- willingness to act
- openness to experience

Any of these may provide reaction context in a specific case, but none is synonymous with AW.

---

## Reaction-context families

The following families are exploratory context labels only. They are **not new axes**, not validated subscales, and not stable person categories.

### 1. Epistemic

Examples of reaction context:

- `noriu suprasti kaip tai veikia`
- `noriu išsiaiškinti kodėl sugedo`
- `noriu rasti dėsningumą`
- `įdomu, kas čia vyksta`

Possible directional form: more vs less willingness to invest attention in understanding.

### 2. Affective

Examples:

- `per daug emocijų, nenoriu veltis`
- `noriu sumažinti kontaktą su tuo, kas mane perkrauna`

Possible directional form: more vs less willingness to remain engaged under affective load.

### 3. Instrumental

Examples:

- `neįdomu, bet padarysiu dėl rezultato`
- `nebematau naudos investuoti daugiau laiko`

Possible directional form: continue vs reduce investment for goal/value reasons.

### 4. Relational

Examples:

- `jei nėra pasitikėjimo, neįsitrauksiu`
- `noriu atsitraukti ten, kur manęs nereikia`

Possible directional form: approach/maintain vs reduce relational engagement.

### 5. Other / unresolved

Used when the reaction does not fit cleanly or evidence is insufficient.

---

## Important consequence for stimulus design

A single AW-targeting stimulus family does not need to represent all possible AW contexts.

Instead, candidate stimulus families may deliberately target one narrow context family while keeping the derived signal open until Gate D.

For the next design step, ConflictLab will explore **epistemic AW** first because it is the clearest currently observed reaction-context family and is comparatively feasible for static visual stimuli.

This is a working choice, not a claim that epistemic AW is the "true" or primary form of AW for all people.

---

## Why Gemini's proposed full split is not adopted yet

The red-team critique that AW mixes distinct psychological mechanisms is accepted.

The stronger recommendation to replace AW with a new construct such as `Spatial & Epistemic Orientation` is **not** adopted at this stage because it risks collapsing AW into CS/CR territory through visual complexity, ambiguity, and boundary structure.

Current decision:

```text
KEEP the AW top-level directional layer
REDEFINE it as response orientation
DO NOT treat it as one causal psychological construct
EXPLORE narrow reaction-context families underneath it
```

---

## Falsification mindset

The next stimulus work should be able to fail.

If epistemic-AW candidate scenes repeatedly produce reactions better explained by CS, CR, aesthetics, or generic curiosity without a defensible engagement-direction component, then the working AW definition must be reviewed again.

No stimulus should be rescued by cue wording or post-hoc interpretation.
