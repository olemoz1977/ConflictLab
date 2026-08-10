# ConflictLab — External AI Handoff
**Current as of 2026-08-10; newer repository decisions supersede this handoff.**
**Canonical source: PROJECT_STATE.md**

---

## What ConflictLab is

An Epistemic Reflection Framework. It helps people observe their own
spontaneous reaction patterns — not diagnose them.

NOT: personality test, psychological diagnosis, scoring system.
IS: stimulus-pair-based reaction capture with neutral signal orientation.

---

## Current product split

| | v0.7 | Pair P0 |
|---|---|---|
| Status | Frozen baseline | Active v0.8 candidate |
| Live | Yes (limited — browser API issue) | Yes, fully |
| AI dependency at runtime | Yes (Claude API) | None |
| URL | `olemoz1977.github.io/ConflictLab/` | `…/experiments/pair-p0/?set=prototype-nine-v1` |

---

## Active stable reference

`pair-p0-prototype-nine-v1-radar-ux-stable` → commit `463b09755fe6`

Verified: 3-session block model, bipolar map, block comparison,
sessions 1–6 phone QA PASS, provenance export, LT+EN.

---

## Canonical methodology spec

`docs/experiments/pair-p0/STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md`

Core rule (ADR-011):

```
SCENE PROPERTY  ≠  PARTICIPANT RESPONSE  ≠  DERIVED SIGNAL
```

- AW/CS/CR signal assignment: only after Gate D
- Design stage allows only: `target_signal_hypothesis: AW`, `hypothesized_direction: unconfirmed`
- Raw A/B choice has no inherent psychological polarity
- prototype-nine-v1 choice→cue→vector = historical prototype logic, not v0.8 truth

---

## Current methodology principles (2026-08-10 delta)

1. Methodological cleanliness necessary but not sufficient.
   Stimulus must also have: visual interest, real choice tension,
   equal legitimacy, reaction richness, willingness to continue.

2. Cue = reaction context. Not automatic vector generation.

3. `reaction_intensity` = ordinal 1–5, midpoint 3.
   Not confidence, not latency, not valence, not vector magnitude.
   Never: vector × intensity.

4. `no_clear_choice` ≠ `hard_to_identify` — different data points.

5. Result UX: describe tendencies in reactions, not properties of person.
   GOOD: "A tendency toward greater clarity appeared more often."
   BAD: "You avoid ambiguity."
   Radar/bipolar map = secondary visual, not primary result.

6. Priority: engaging stimuli → reaction capture → minimal Gate D
   contract → small human-response cycle → aggregation refinement.

---

## What is not yet done

- 18 unique pairs needed (currently 9; sessions 4–6 repeat stimuli)
- N0-010–018 pairs not yet created
- N0-004–009 vectors are `prototype_only`, not validated
- SLOT-01 design in progress — no committed stimulus assets yet
- Gate D contract not yet formally defined

---

## Do not do

- Do not assign AW+/AW- to stimulus variants at design stage
- Do not treat prototype-nine-v1 cue vectors as validated mappings
- Do not actively develop v0.7 code
- Do not use `localStorage.clear()` — namespace-scoped clearing only
- Do not modify M0 flow or stable tags without Oleg approval

