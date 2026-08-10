# ConflictLab — Project State

**Last updated:** 2026-08-10
**Purpose:** AI context document. Read this first in every new conversation.

---

## CURRENT STATE SYNC — 2026-08-10

**Current methodology decision commit:** `6219eef3e98aa67d72f10135b2cf4fac4c9b2bc3`
**Canonical stimulus operationalization spec:** `STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md`
**Current AW status decision:** `AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md`
**Active stable tag:** `pair-p0-prototype-nine-v1-radar-ux-stable`

**Methodology status:**
- V1.3 introduces Stimulus–Signal Separation architecture
- Scene property ≠ participant response ≠ derived signal (ADR-011)
- Cue = reaction context, not automatic vector generation
- Result UX describes tendencies in reactions, not properties of the person
- Radar/bipolar map is secondary visual explanation, not the primary result
- Working stimulus quality rule: **CONTROL + EXPERIENCE + INTERPRETABILITY**

**AW status — CURRENT:**
- AW as a third active static-stimulus axis is **SUSPENDED** for v0.8 development
- Do not create new AW-specific static-image assets
- Previous AW epistemic candidates E1/E2/E3 remain historical exploratory evidence, not production candidates
- `prototype-nine-v1` AW behavior remains frozen as technical/UX reference only
- Current hypothesis: response-orientation evidence may become meaningful only as a **domain-specific response trajectory** anchored to CS or CR
- Domain-specific trajectory is **NOT VALIDATED** and must remain separate from product/session engagement

**Active stimulus work:**
- CS candidate pool — ACTIVE
- CR candidate pool — ACTIVE
- AW-specific stimulus pool — STOP / SUSPENDED
- No accepted new v0.8 stimulus assets as of 2026-08-10

---

## Strategic Direction

> **ConflictLab v0.7 — Frozen Product Baseline.**
> **Pair P0 — Active Candidate Architecture for v0.8.**
> **prototype-nine-v1 — technical/UX stable reference, not a methodologically final stimulus set.**

The previous `3 AW + 3 CS + 3 CR` and 18-pair planning model is no longer treated as current methodological truth.

- `3+3+3` = historical/prototype block-construction assumption under review
- `18 unique pairs` = possible technical planning target for two non-repeating 9-pair prototype blocks, **not a validated scientific minimum**
- Current v0.8 methodology work prioritizes high-quality CS/CR stimulus candidates and tests whether domain-specific response trajectories add value

| Product | Status | Live |
|---|---|---|
| **v0.7** (`docs/index.html`) | Frozen baseline. Deployment architecture uses direct Claude API calls from browser — not resolved for public use. Source of reusable methodological components. | `olemoz1977.github.io/ConflictLab/` |
| **Pair P0** (`docs/experiments/pair-p0/index.html`) | **Active development.** Current live P9 behavior is a frozen technical/UX reference while v0.8 methodology changes are evaluated separately. | `olemoz1977.github.io/ConflictLab/experiments/pair-p0/?set=prototype-nine-v1` |

---

## Core Philosophy

An **Epistemic Reflection Framework** — a transparent signal interpretation system for self-reflection.

> *"We don't help people understand themselves faster. We help them learn to better observe themselves."*

**NOT:** personality assessment, psychological diagnosis, human scoring, behavioral prediction.

**Observation principle:** Never infer causes, never explain personality traits, never predict behavior, never create facts beyond provided data.

**Result-language principle:** Describe the tendency in the reactions, not a property of the person.

---

## Pair P0 — Current Active State

**Stable tag:** `pair-p0-prototype-nine-v1-radar-ux-stable`
**URL:** `?set=prototype-nine-v1`
**Phone QA:** sessions 1–6 = PASS (2026-08-08)

### What is verified technically

- 3-session blocks × 3 pairs = 9 choices per radar in the frozen P9 prototype
- Radar shown only after a complete 3-session block (sessions 3, 6, 9...)
- Progress-only screens between blocks (no partial radar)
- Block 1 vs Block 2 overlay comparison (bipolar map)
- P9/M0 isolation by `set_id`
- Full provenance export (SESSION, choices, reflections)
- Display calibration `p9-display-v1`, `BOUND=0.65`
- LT + EN parity

### What is historical/prototype methodology

The following remain useful as prototype evidence but are not current v0.8 truth:

- AW / CS / CR as three equivalent stimulus axes
- `3 AW + 3 CS + 3 CR` block balance
- `axis: aw` in prototype pair metadata
- choice → cue → predefined vector logic
- repeated sessions 4–6 stimulus architecture
- 18 unique pairs as if it were a scientific minimum

### What is not yet done

- Active v0.8 CS/CR stimulus pool is not yet complete
- No formal domain-specific response trajectory contract exists
- Gate D remains to be minimally formalized under the newer reaction-context architecture
- Current result architecture (pattern description first, radar secondary) is not yet implemented in Pair P0
- Existing P9 vectors remain prototype-only/reviewed historical mappings, not validated v0.8 mappings

---

## v0.7 — Frozen Baseline

**Do not actively develop.** Use as reference for:
- Methodology documents (`docs/methodology/`)
- Language standards (R1–R8, S1–S5, F1–F7)
- Architecture concepts (Observation Engine ADR-010, DSM, Reflection Engine)
- Python engine (`src/`) — validated, not live-integrated

**Known issue:** `docs/index.html` calls Anthropic API directly from browser. CORS/authentication not resolved for public deployment. Treat as architecture problem, not confirmed broken product.

---

## Current Methodological Model

### Active stimulus-response domains

| Code | Working domain | Status |
|---|---|---|
| CS | Aiškumas / neapibrėžtumas — Clarity / Ambiguity | ACTIVE candidate domain |
| CR | Struktūra / lankstumas — Structure / Flexibility | ACTIVE candidate domain |

### AW

| Item | Status |
|---|---|
| AW as peer static-stimulus axis | **SUSPENDED** |
| AW-specific asset generation | **STOP** |
| AW in `prototype-nine-v1` | HISTORICAL/TECHNICAL PROTOTYPE |
| Domain-specific response trajectory | ACTIVE HYPOTHESIS / NOT VALIDATED |

A single response may be informative evidence, but a trajectory requires repeated, interpretable events within a domain.

Product continuation, session completion, and domain-specific response trajectory must not be collapsed.

---

## Source of Truth Hierarchy

| Document | Purpose |
|---|---|
| `PROJECT_STATE.md` | **This file.** Short current state. Read first. |
| `docs/experiments/pair-p0/AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md` | Current AW suspension / trajectory decision |
| `docs/adr/ADR-011-stimulus-signal-separation.md` | Scene property ≠ response ≠ signal boundary |
| `docs/experiments/pair-p0/METHODOLOGY_DELTA_2026-08-10.md` | Post-V1.3 methodology decisions |
| `docs/experiments/pair-p0/STIMULUS_EXPERIENCE_CARD_V1.md` | Active stimulus design working unit |
| `REPOSITORY_INVENTORY.md` | Full file/module categorization |
| `docs/experiments/pair-p0/PAIR_P0_STATE.md` | Pair P0 milestone history and OQ log |
| `docs/experiments/pair-p0/RADAR_BLOCK_MODEL_V1.md` | Historical/current prototype architecture reference; AW peer-axis assumptions now under review |
| `docs/experiments/pair-p0/PROGRESS.md` | Chronological log |
| `docs/methodology/METHODOLOGY_FREEZE_v1.md` | v0.7 methodology (frozen) |
| `README.md` | Public-facing description |

---

## What Has Been Tried and Rejected / Suspended (Do NOT repeat blindly)

- ❌ Cumulative 1–6 radar (mixed block sizes)
- ❌ Partial block radar display (radar after 1/3 or 2/3 of block)
- ❌ `hasUnlockedRadar()` triggering radar display (it means "exists", not "show now")
- ❌ Per-axis display scaling (distorts cross-axis geometry)
- ❌ `MIN_VISIBLE_PX` / `pow(0.7)` amplification in P9 (removed, linear only)
- ❌ Raw axis numbers shown directly to users
- ❌ Personality labels in reflections (S1)
- ❌ `localStorage.clear()` (use namespace-scoped clearing only)
- ⏸ AW-specific static-image stimulus development — suspended pending trajectory hypothesis evaluation
- ⏸ Epistemic-AW E1/E2/E3 asset generation — suspended after red-team convergence toward CS/novelty/puzzle contamination

---

## Repository Structure

```
ConflictLab/
├── PROJECT_STATE.md          ← current state / read first
├── REPOSITORY_INVENTORY.md
├── README.md
├── WHY_CONFLICTLAB.md
├── docs/
│   ├── index.html            ← v0.7 FROZEN baseline
│   ├── generator.html
│   ├── media/
│   ├── methodology/          ← frozen methodology docs
│   ├── adr/
│   │   └── ADR-011-stimulus-signal-separation.md
│   └── experiments/
│       └── pair-p0/          ← ACTIVE DEVELOPMENT
│           ├── index.html    ← frozen P9 technical/UX behavior remains live
│           ├── STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md
│           ├── METHODOLOGY_DELTA_2026-08-10.md
│           ├── STIMULUS_EXPERIENCE_CARD_V1.md
│           ├── AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md
│           ├── AW_REDEFINITION_NOTE_v0.1.md          ← superseded working note
│           ├── AW_EPISTEMIC_CANDIDATES_v0.1.md      ← suspended exploratory pool
│           ├── pair-set-prototype-nine-v1.json
│           ├── pair-cue-prototype-nine-v1.json
│           ├── PAIR_P0_STATE.md
│           ├── RADAR_BLOCK_MODEL_V1.md
│           └── PROGRESS.md
├── src/engine/               ← v0.7 Python engine (frozen, not live)
├── stimuli/ST-001–010        ← v0.7 provisional/frozen
├── tests/
├── validation/               ← LEGACY v0.4 era
└── archive/
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

1. **Active work = Pair P0 v0.8 methodology/stimulus development.** Do not treat the live P9 radar geometry as current methodology truth.
2. Read `PROJECT_STATE.md`, ADR-011, `METHODOLOGY_DELTA_2026-08-10.md`, and `AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md` before methodology work.
3. Do not create AW-specific static-image assets unless the AW suspension is explicitly reversed.
4. Current stimulus work prioritizes CS and CR candidate pools using **CONTROL + EXPERIENCE + INTERPRETABILITY**.
5. Product engagement must not be used as automatic evidence of domain-specific response trajectory.
6. Before any code change: read the plan and confirm with Oleg.
7. Never use `localStorage.clear()`.
8. Never modify M0 flow or stable tags without explicit approval.
9. All methodological decisions belong to Oleg. If uncertain — ask, do not invent.
