# ConflictLab — Project State

**Last updated:** 2026-08-08
**Purpose:** AI context document. Read this first in every new conversation.

---

---

## CURRENT STATE SYNC — 2026-08-10

**HEAD commit:** `07fce0cbb0ff893fca0cf0e179acc35b37ac0096`
**Canonical methodology spec:** `STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md`
**Active stable tag:** `pair-p0-prototype-nine-v1-radar-ux-stable`

**Methodology status:**
- V1.3 introduces Stimulus–Signal Separation architecture
- AW/CS/CR signals may only be assigned after Gate D (participant response)
- Design-stage language: `target_signal_hypothesis: AW`, `hypothesized_direction: unconfirmed`
- V1.1 remains in repo as historical reference; V1.3 is canonical
- `METHODOLOGY_DELTA_2026-08-10.md` records post-V1.3 decisions (pair-level control, result UX, intensity, cue role)

**SLOT-01 status:**
- Concept exploration in progress (no committed candidates)
- No accepted candidates as of 2026-08-10
- Chair/bench concepts from earlier session were uncommitted exploratory text — not accepted
- Current methodology per STIMULUS_OPERATIONALIZATION_SPEC_V1.3 + ADR-011 applies
- Next step: Gate 0A blind concept review when ready


## Strategic Direction (decided 2026-08-08)

> **ConflictLab v0.7 — Frozen Product Baseline.**
> **Pair P0 — Active Candidate Architecture for v0.8.**
> **prototype-nine-v1 — technical/UX stable reference, not a methodologically final stimulus set.**
> **A clean multi-block comparison requires 18 unique methodologically acceptable pairs.**

| Product | Status | Live |
|---|---|---|
| **v0.7** (`docs/index.html`) | Frozen baseline. Deployment architecture uses direct Claude API calls from browser — not resolved for public use. Source of reusable methodological components. | `olemoz1977.github.io/ConflictLab/` |
| **Pair P0** (`docs/experiments/pair-p0/index.html`) | **Active development.** No runtime AI dependency. Works fully as static GitHub Pages. | `olemoz1977.github.io/ConflictLab/experiments/pair-p0/?set=prototype-nine-v1` |

---

## Core Philosophy

An **Epistemic Reflection Framework** — a transparent signal interpretation system for self-reflection.

> *"We don't help people understand themselves faster. We help them learn to better observe themselves."*

**NOT:** personality assessment, psychological diagnosis, human scoring, behavioral prediction.

**Observation principle:** Never infer causes, never explain personality traits, never predict behavior, never create facts beyond provided data.

---

## Pair P0 — Current Active State

**Stable tag:** `pair-p0-prototype-nine-v1-radar-ux-stable`
**URL:** `?set=prototype-nine-v1`
**Phone QA:** sessions 1–6 = PASS (2026-08-08)

### What is verified

- 3-session blocks × 3 pairs = 9 choices per radar
- Radar shown only after a complete 3-session block (sessions 3, 6, 9...)
- Progress-only screens between blocks (no partial radar)
- Block 1 vs Block 2 overlay comparison (bipolar map)
- P9/M0 isolation by `set_id`
- Full provenance export (SESSION, choices, reflections)
- Display calibration `p9-display-v1`, `BOUND=0.65`
- LT + EN parity

### What is not yet done

- **18 unique pairs** needed for clean Block 1 vs Block 2 (currently 9, sessions 4–6 repeat stimuli)
- N0-004–009: 6 pairs are `prototype_only`, not methodologically validated
- N0-005 axis assignment unresolved
- N0-010–018: not yet created (3 AW + 3 CS + 3 CR)
- Second radar block uses `comparison_status: "prototype_repeated_stimuli"` — not a clean measurement

### Milestone path to v0.8

| Milestone | Requirement |
|---|---|
| `prototype-nine-v1-radar-ux-stable` ✅ | 3×3 flow, bipolar map, block comparison, QA pass |
| Intermediate (9 reviewed pairs) | ≥9 methodologically acceptable pairs, all `reviewed` vectors |
| **v0.8 candidate** | 18 unique pairs, clean Block 1 vs Block 2 without repeated stimuli |

---

## v0.7 — Frozen Baseline

**Do not actively develop.** Use as reference for:
- Methodology documents (`docs/methodology/`)
- Language standards (R1–R8, S1–S5, F1–F7)
- Architecture concepts (Observation Engine ADR-010, DSM, Reflection Engine)
- Python engine (`src/`) — validated, not live-integrated

**Known issue:** `docs/index.html` calls Anthropic API directly from browser. CORS/authentication not resolved for public deployment. Treat as architecture problem, not confirmed broken product.

---

## Signal Axes (shared by v0.7 and Pair P0)

| Code | Positive | Negative |
|---|---|---|
| AW | Artėti / Approach | Atsitraukti / Step back |
| CS | Aiškumas / Clarity | Neapibrėžtumas / Ambiguity |
| CR | Struktūra / Structure | Laisvumas / Flexibility |

Scale: [-1.0, +1.0]. No moral valence. Directional, not evaluative.

---

## Source of Truth Hierarchy

| Document | Purpose |
|---|---|
| `PROJECT_STATE.md` | **This file.** Short current state. Read first. |
| `REPOSITORY_INVENTORY.md` | Full file/module categorization |
| `docs/experiments/pair-p0/PAIR_P0_STATE.md` | Pair P0 milestone history and OQ log |
| `docs/experiments/pair-p0/RADAR_BLOCK_MODEL_V1.md` | Pair P0 architecture specification |
| `docs/experiments/pair-p0/PROGRESS.md` | Chronological log |
| `docs/methodology/METHODOLOGY_FREEZE_v1.md` | v0.7 methodology (frozen) |
| `README.md` | Public-facing description |

---

## What Has Been Tried and Rejected (Do NOT repeat)

- ❌ Cumulative 1–6 radar (mixed block sizes)
- ❌ Partial block radar display (radar after 1/3 or 2/3 of block)
- ❌ `hasUnlockedRadar()` triggering radar display (it means "exists", not "show now")
- ❌ Per-axis display scaling (distorts cross-axis geometry)
- ❌ `MIN_VISIBLE_PX` / `pow(0.7)` amplification in P9 (removed, linear only)
- ❌ Raw axis numbers shown directly to users
- ❌ Personality labels in reflections (S1)
- ❌ `localStorage.clear()` (use namespace-scoped clearing only)

---

## Repository Structure

```
ConflictLab/
├── PROJECT_STATE.md          ← this file
├── REPOSITORY_INVENTORY.md   ← full file inventory
├── README.md                 ← public description
├── WHY_CONFLICTLAB.md        ← philosophy
├── docs/
│   ├── index.html            ← v0.7 FROZEN baseline
│   ├── generator.html        ← stimulus generator (CORS issue)
│   ├── media/                ← v0.7 stimulus images + video
│   ├── methodology/          ← frozen methodology docs
│   ├── adr/                  ← Architecture Decision Records
│   └── experiments/
│       └── pair-p0/          ← ACTIVE DEVELOPMENT
│           ├── index.html    ← main app (4500+ lines)
│           ├── pair-set-prototype-nine-v1.json
│           ├── pair-cue-prototype-nine-v1.json
│           ├── PAIR_P0_STATE.md
│           ├── RADAR_BLOCK_MODEL_V1.md
│           └── PROGRESS.md
├── src/engine/               ← v0.7 Python engine (frozen, not live)
├── stimuli/ST-001–010        ← v0.7 stimuli (PROVISIONAL, frozen)
├── tests/                    ← v0.7 Python tests + P0 audit script
├── validation/               ← LEGACY v0.4 era
└── archive/                  ← historical content
```

---

## Git Tags (Pair P0 milestones)

| Tag | Meaning |
|---|---|
| `pair-p0-m0-remote-beta-stable` | M0 remote beta |
| `pair-p0-prototype-nine-v1-flow-stable` | 3×3 flow, provenance, radar unlocked |
| `pair-p0-prototype-nine-v1-radar-ux-stable` | Bipolar map, calibration v1, routing fix, QA pass |

---

## For AI Assistants

1. **Active work = Pair P0** (`docs/experiments/pair-p0/`). Do not touch v0.7 code.
2. Before any code change: read the plan, confirm with Oleg.
3. Never use `localStorage.clear()`.
4. Never modify M0 flow or stable tags.
5. All methodological decisions belong to Oleg. If uncertain — ask, do not invent.
6. Pair P0 works from phone. Edge mobile is the primary test browser (Chrome mobile has viewport issues with P0).
