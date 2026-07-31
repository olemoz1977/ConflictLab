# ConflictLab — Project State
**Last updated:** 2026-07-31
**Purpose:** AI context document. Read this first in every new conversation.

---

## Current Version

**v0.7 — Feature Freeze / Beta Ready**

Live at: `https://olemoz1977.github.io/ConflictLab/`

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

### Observation Engine (ADR-010) — IMPLEMENTED in index.html
Translates raw axis signals → semantic observations before Claude API.
Constitutional rule: NEVER infer causes, NEVER explain personality traits, NEVER predict behavior, NEVER create facts beyond provided data.

### Dialogue State Machine (micro_dialogue_dsm_v1.md) — SPECIFIED, partially implemented
```
Reflection → STATE 0 (Agreement) → STATE 2A/2B/2C → STATE 3 (Mirror) → STATE 4 (Bridge)
```
User responses: TAIP / NE / NEŽINAU

---

## Methodology Freeze v1.0 (DO NOT CHANGE without beta data)

**Frozen documents:**
- `conflictlab_voice_v1.md` — how system speaks
- `behavior_translation_architecture_v1.md` — Reflection Engine
- `stimulus_validation_protocol.md` — stimulus evaluation
- `stimulus_matrix_v1.md` — library planning
- `stimulus_cue_rules_v1.md` (F1–F7) — cue creation rules
- `stimulus_lifecycle_v1.md` — production process
- `beta_research_protocol_v1.md` — H1–H4 research hypotheses

**Freeze commitment:**
> Methodology changes accepted ONLY when beta data clearly shows SC1–SC5 criteria are not met. Ideas, intuition, or individual opinions are NO LONGER sufficient grounds to change the system.

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
- F1–F6: Stimulus and cue construction rules
- F7: Semantic Independence — cues created fresh per stimulus, NOT standardized across library

---

## Stimulus Library

**10 active stimuli:** ST-001 through ST-010
- Located in `stimuli/ST-XXX/` with `stimulus.yaml`, `status.yaml`, `review.md`
- Known gap: cs axis underrepresented (22% vs optimal 33%)
- Known issue: ST-001 and ST-006 both aw- with single figure — may cause monotony

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

## Current Blockers

### 1. Stimulus Generator CORS problem
`docs/generator.html` calls Anthropic API directly from browser.
GitHub Pages blocks this (CORS). Generator.html exists and is functional UI — but API calls fail.

**Options not yet decided:**
- Local Python server (`python -m http.server`)
- Proxy solution
- Accept manual YAML creation for now

### 2. Beta not started yet
10–15 participants needed. Protocol ready. UI ready. Waiting to start.

---

## What Has Been Tried (Do NOT repeat)

- ❌ 12-stimulus session (reduced to 4 — users fatigued)
- ❌ Showing raw axis numbers (aw=-0.09) to users — removed, replaced with dot on line
- ❌ alert() dialogs — removed, replaced with UI screens
- ❌ Attention Anchors / FC-004 — rejected (assigning axis weights to visual elements = speculation)
- ❌ Standardized cues across library (violates F7 — Semantic Independence)
- ❌ Single session pattern detection (needs ≥3 sessions)
- ❌ Personality labels in reflections (forbidden by S1)
- ❌ "Evidence Engine" naming (changed to "Observation Engine" — observation ≠ evidence about personality)

---

## Archived Modules (exist in archive/, not active)

These Python modules exist and are well-written but NOT integrated into active `src/`:
- `signal_orientation.py` — SignalOrientation dataclass with [-1.0, +1.0] axes
- `evidence_graph.py` — EvidenceNode + EvidenceGraph + provenance chain
- `event_log.py` — Immutable append-only EventLog
- `uncertainty_engine.py` — 5-dimensional UncertaintyProfile (decomposed, never collapsed)
- `model_registry.py` — 14 registered frameworks with assumptions + blind spots
- `reflection_contract.py` — ReflectionContract with 7 required fields + validation

**These are v0.4 architecture.** Integration into active UI requires decision on whether v0.4 Python layer is needed before beta, or after.

---

## Repository Structure (Clean State)

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

### For AI assistants — read this first:
1. The methodology is FROZEN. Do not propose methodology changes.
2. The architecture is FROZEN. Do not propose architectural redesigns.
3. Current priority is BETA — getting 10–15 people to test.
4. If you are unsure about methodology, ASK — do not invent.
5. Changes to `docs/index.html` require understanding ConflictLab Voice (see `conflictlab_voice_v1.md`).
6. Stimulus creation follows F1–F7 rules. Read `stimulus_cue_rules_v1.md` before proposing stimuli.

### Role of the human (Oleg):
- Product architect and methodologist
- Holds final authority on all architectural and methodological decisions
- Operates primarily from mobile (GitHub is difficult — prefer direct commits)

### Current immediate tasks (in priority order):
1. Start beta with 10–15 participants using current `docs/index.html`
2. Solve generator.html CORS problem (or workaround)
3. Monitor H1–H4 hypothesis results

---

*"Not architecture. Evidence."*
