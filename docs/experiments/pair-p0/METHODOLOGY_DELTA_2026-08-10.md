# ConflictLab v0.8 — Methodology Delta
**Date:** 2026-08-10
**Based on:** STIMULUS_OPERATIONALIZATION_SPEC_V1.3 + ADR-011
**Purpose:** Record decisions made outside Claude sessions 2026-08-08→10.
**Note to AI assistants:** This file records updates that postdate V1.3.
Where this file and V1.3 conflict, this file takes precedence.

---

## 1. PAIR-LEVEL CONTROL + BLOCK-LEVEL EXPERIENCE DIVERSITY

Methodological cleanliness is necessary but not sufficient.

A good stimulus must also have:

- **Visual interest** — the pair must be worth looking at
- **Real choice tension** — both sides must pull meaningfully
- **Equal legitimacy** — neither side obviously correct
- **Reaction richness** — the choice should leave something to reflect on
- **Willingness to continue** — participant should want another session

Neutral does not mean meaningless.
A pair that passes all confound audits but produces no reaction
is a failed stimulus.

---

## 2. CUE = REACTION CONTEXT, NOT VECTOR GENERATOR

Cue captures the participant's reaction framing.
It is not a mechanism for automatic vector generation.

Cue → signal mapping is Gate D work, not cue design work.

---

## 3. REACTION INTENSITY

`reaction_intensity` = ordinal self-report, 1–5, midpoint 3.

It is NOT:
- confidence
- latency proxy
- valence
- vector magnitude

**Never: vector × intensity**

`reaction_intensity` is stored separately.
Its role in aggregation is empirically open — not pre-assigned.

---

## 4. TWO DISTINCT UNKNOWN STATES

`no_clear_choice` ≠ `hard_to_identify`

`no_clear_choice`: participant had no clear A/B preference.
`hard_to_identify`: participant chose A or B, but cannot name the reaction.

These are different data points and must not be collapsed.

---

## 5. RESULT UX PRINCIPLE — "NO LABELS" ≠ "NO INTERPRETATION"

The system describes tendencies in reactions, not properties of the person.

**GOOD:**
"Šiandien tavo pasirinkimuose dažniau pasirodė kryptis į didesnį aiškumą."
"In today's choices, a tendency toward greater clarity appeared more often."

**BAD:**
"Tu vengi neapibrėžtumo."
"You avoid ambiguity."

### Primary result structure

1. What repeated across choices
2. Exceptions and divergences
3. Supporting evidence (which pairs, which sessions)
4. A better reflection question

### Secondary visual

The radar / bipolar map is a **secondary** visual explanation.
It is not the primary result.
Results lead with the pattern description; the map illustrates it.

---

## 6. CURRENT PRIORITY ORDER

1. Engaging, controlled stimulus pairs with real choice tension
2. Reaction capture and reaction context (cue)
3. Minimal Gate D contract — what is the minimum needed to call a signal mapping defensible?
4. Small human-response cycle — real participants, real reactions
5. Aggregation and radar refinement based on empirical data

Design cleanliness without human response data is incomplete.

---

## 7. ACTIVE DOCUMENT CLASSIFICATION

| Document | Classification |
|---|---|
| `STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md` | CURRENT CONSISTENT |
| `ADR-011-stimulus-signal-separation.md` | CURRENT CONSISTENT |
| `RADAR_BLOCK_MODEL_V1.md` | CURRENT CONSISTENT — block model valid |
| `PAIR_P0_STATE.md` | CURRENT CONSISTENT — prototype status correctly labeled |
| `PROGRESS.md` | CURRENT CONSISTENT |
| `STIMULUS_OPERATIONALIZATION_SPEC_V1.1.md` | HISTORICAL-PROTOTYPE — axis separation language predates ADR-011 |
| `N0_SIX_PAIR_CUE_DRAFT.md`, `_v2.md` | HISTORICAL-PROTOTYPE |
| `N0_SIX_PAIR_CUE_DRAFT_v3.md` | HISTORICAL-PROTOTYPE — cue drafts, not v0.8 method |
| `pair-cue-prototype-nine-v1.json` | HISTORICAL-PROTOTYPE — vectors are prototype logic |
| `docs/methodology/stimulus_cue_rules_v1.md` | HISTORICAL-PROTOTYPE — v0.7 era |
| `docs/methodology/behavior_translation_architecture_v1.md` | HISTORICAL-PROTOTYPE — v0.7 era |
| `validation/` | HISTORICAL-PROTOTYPE — v0.4 era |

**Active conflicts fixed by this commit:**
- PROJECT_STATE.md §CURRENT STATE SYNC — removed chair/bench candidate claims
- PROJECT_STATE.md — updated to reflect delta principles and correct SLOT-01 status

**No active conflicts found in:** README.md, REPOSITORY_INVENTORY.md (not contradicted by delta).

