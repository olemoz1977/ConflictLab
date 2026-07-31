# ConflictLab — Project State
**Last updated:** 2026-07-31
**Purpose:** AI context document. Read this first in every new conversation.

> *"Not architecture. Evidence."*
> We are no longer building theories. We are collecting evidence from real people.

---

## Current Version

**v0.7 — Feature Freeze / Beta Ready**

Live at: `https://olemoz1977.github.io/ConflictLab/`

**This document MUST be updated before every beta milestone or release.**

---

## What ConflictLab IS

An **Epistemic Reflection Framework** — a transparent signal interpretation system for self-reflection.

Core philosophy:
> "We don't help people understand themselves faster. We help them learn to better observe themselves."

**NOT:**
- Personality assessment
- Psychological diagnosis
- Human scoring system
- Behavioral prediction engine

---

## Current Blocker (Technical)

### Stimulus Generator CORS problem — unresolved
`docs/generator.html` calls Anthropic API directly from browser.
GitHub Pages blocks this (CORS). Generator UI is functional — API calls fail.

**Options not yet decided:**
- Local Python server (`python -m http.server`)
- Proxy solution
- Accept manual YAML creation for now

This is the only current technical blocker before beta can begin.

---

## Architecture (Current — Do NOT redesign)

### Session structure: 3×4
- 3 sessions minimum per user
- 4 stimuli per session (image-based)
- Pattern detection activates after session 3

### Signal Axes (3 axes, scale −1.0 to +1.0)
| Internal | Semantic signal | Description |
|---|---|---|
| `aw+` | `approach_impulse` | Engagement toward situation |
| `aw-` | `withdrawal_impulse` | Distancing from situation |
| `cs+` | `clarity_seeking` | Drive to reduce uncertainty |
| `cs-` | `ambiguity_tolerance` | Openness to uncertainty |
| `cr+` | `structure_seeking` | Control / structuring |
| `cr-` | `release_impulse` | Surrender of structure |

**No positive/negative moral labels. Values are directional, not evaluative.**

### Pipeline
```
Stimuli → Signal Engine (aw/cs/cr) → Observation Engine → Claude API → Reflection
```

### Active Python Engine (`src/engine/behavior_translation/`)
- **Pattern Detection:** P1–P9 (P9=trajectory is highest priority)
- **AHA Detection:** K1–K4 filters
- **Reflection Engine:** generates CandidateInsight
- All 13 tests passing

### Observation Engine (ADR-010) — implemented in index.html
Translates raw axis signals → semantic observations before Claude API.
Constitutional rule: NEVER infer causes, NEVER explain personality traits, NEVER predict behavior, NEVER create facts beyond provided data.

### Dialogue State Machine (micro_dialogue_dsm_v1.md) — specified, partially implemented
```
Reflection → STATE 0 (Agreement) → STATE 2A/2B/2C → STATE 3 (Mirror) → STATE 4 (Bridge)
```
User responses: TAIP / NE / NEŽINAU

---

## Methodology Status

**The methodology is frozen for implementation, not for critique.**
Do not propose changes unless they are supported by beta evidence or explicitly requested.

If you find a logical flaw — name it clearly. Do not implement it without Oleg's decision.

**Frozen documents:**
- `conflictlab_voice_v1.md` — how system speaks
- `behavior_translation_architecture_v1.md` — Reflection Engine
- `stimulus_validation_protocol.md` — stimulus evaluation
- `stimulus_matrix_v1.md` — library planning
- `stimulus_cue_rules_v1.md` (F1–F7) — cue creation rules
- `stimulus_lifecycle_v1.md` — production process
- `beta_research_protocol_v1.md` — H1–H4 research hypotheses

---

## Language Standards

### Reflection Language (R1–R8)
- R1: Describe only what was observed
- R2: Never explain WHY
- R3: End with a question, not a conclusion
- R4: Acknowledge what the system cannot know
- R5: Subject = person's attention, not the system
- R6: Calm, curious, humble tone
- R7: No diagnostic language
- R8: Scope declaration required

### Reflection Safety (S1–S5)
- S1: Never create a personality label
- S2: Never predict future behavior
- S3: Never explain the cause of a reaction
- S4: Never claim the observation applies beyond this session
- S5: Never compare the person to others

### Stimulus Language (F1–F7)
- F7 key rule: Semantic Independence — cues created fresh per stimulus, NOT standardized across library

---

## Stimulus Library

**10 active stimuli:** ST-001 through ST-010
- Located in `stimuli/ST-XXX/` with `stimulus.yaml`, `status.yaml`, `review.md`
- Known gap: cs axis underrepresented (22% vs optimal 33%)
- Known issue: ST-001 and ST-006 both aw− with single figure — may cause monotony

---

## Beta Research Protocol

**Target:** 10–15 participants, ≥3 sessions each

**Hypotheses:**
| ID | Hypothesis | Success criterion |
|---|---|---|
| H1 | ≥70% participants rate ≥1 insight as "hadn't noticed this" | ≥7/10 participants |
| H2 | Fallback rate ≤20% of sessions | ≤1 fallback per 5 sessions |
| H3 | P9 insights cause more AHA moments than P5 | P9 Q2 ≥ P5 Q2 + 15% |
| H4 | Disagreements include specific reason ≥60% | Q3 field analysis |

**Success Criteria (SC1–SC5):**
- SC1: Natural reaction — user chooses spontaneously
- SC2: Reflection resonance — feels personal, not generic
- SC3: AHA moment — "hadn't thought of this"
- SC4: Trust — user doesn't feel evaluated or diagnosed
- SC5: Return — user wants to come back

---

## Open Design Questions

These questions are NOT yet decided. Do not assume they are resolved.

- **What creates the strongest AHA moment?** P9 is theorized to be highest — not yet confirmed by data.
- **Adaptive stimulus selection:** should it happen before beta or after? Currently random within axis balance rules.
- **Observation Engine branching:** when should the dialogue branch based on signal type (clarity_seeking vs withdrawal_impulse)?
- **Generator CORS:** local server, proxy, or manual YAML — which path?
- **cs axis gap:** 22% representation vs optimal 33% — how many new stimuli are needed before beta?

---

## What Has Been Tried and Rejected (Do NOT repeat)

- ❌ 12-stimulus session → reduced to 4 (users fatigued)
- ❌ Raw axis numbers shown to users (aw=−0.09) → removed, replaced with dot on line
- ❌ alert() dialogs → replaced with UI screens
- ❌ Attention Anchors / FC-004 → rejected (assigning axis weights to visual elements = speculation)
- ❌ Standardized cues across library → violates F7 Semantic Independence
- ❌ Single session pattern detection → needs ≥3 sessions
- ❌ Personality labels in reflections → forbidden by S1
- ❌ "Evidence Engine" naming → changed to "Observation Engine" (observation ≠ evidence about personality)

---

## Archived Modules (exist in archive/, not active)

Well-written Python modules — NOT integrated into active UI. v0.4 architecture.

- `signal_orientation.py` — SignalOrientation dataclass, axes [−1.0, +1.0]
- `evidence_graph.py` — EvidenceNode + EvidenceGraph + provenance chain
- `event_log.py` — immutable append-only EventLog
- `uncertainty_engine.py` — 5-dimensional UncertaintyProfile (never collapsed to single score)
- `model_registry.py` — 14 registered frameworks with assumptions + blind spots
- `reflection_contract.py` — ReflectionContract, 7 required fields + validation

Integration decision: deferred until after beta.

---

## Repository Structure

```
ConflictLab/
├── README.md
├── PROJECT_STATE.md          ← this file
├── REPOSITORY_INVENTORY.md
├── docs/
│   ├── index.html            ← ACTIVE PRODUCT (GitHub Pages)
│   ├── generator.html        ← Stimulus Generator (CORS blocker)
│   ├── media/                ← stimulus images + video
│   ├── methodology/          ← frozen methodology docs
│   ├── adr/                  ← ADR-009, ADR-010
│   ├── beta_research_protocol_v1.md
│   └── tester_instructions.md
├── stimuli/                  ← ST-001 to ST-010 + templates
├── src/engine/behavior_translation/  ← active Python engine
├── tests/                    ← 13/13 passing
├── validation/               ← disagreement log + feedback
└── archive/                  ← everything historical
```

---

## How to Work With This Project

**Role of the human (Oleg):** product architect and methodologist. Final authority on all decisions. Works primarily from mobile.

**For AI assistants:**
1. Methodology is frozen for implementation — critique is welcome, changes require beta evidence or explicit request
2. Architecture is frozen — do not redesign
3. Current priority is BETA — getting real people to test
4. If uncertain about methodology, ask — do not invent
5. Changes to `index.html` require understanding ConflictLab Voice (`conflictlab_voice_v1.md`)
6. Stimulus creation follows F1–F7 rules — read `stimulus_cue_rules_v1.md` first

**Current immediate priorities (in order):**
1. Start beta with 10–15 participants using current `docs/index.html`
2. Solve generator.html CORS problem
3. Monitor H1–H4 results

---

*"Not architecture. Evidence."*
