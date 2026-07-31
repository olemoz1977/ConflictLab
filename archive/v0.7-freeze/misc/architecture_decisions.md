# ConflictLab — Architecture Decision Records
**Version:** v0.4.0-RC1
**Status:** Active
**Language:** English (technical reference)

> This document records binding architectural decisions for ConflictLab v0.4.
> Each ADR must be reviewed before any new feature is implemented.
> Decisions here override implementation convenience.

---

## ADR-001: Epistemic Position of the System

**Status:** ACCEPTED
**Date:** 2026-07-29

### Context

ConflictLab processes human behavioral signals and produces reflections.
There is a persistent risk that the system drifts from reflection toward
diagnosis — especially as the model grows more sophisticated.

### Decision

ConflictLab occupies a strictly defined epistemic position:

**The system models:**
- observed signals (latency, choice vectors, context markers)
- possible interpretations (weighted, sourced, bounded)
- uncertainty across five dimensions
- reflection opportunities for the person

**The system does NOT:**
- identify personality traits
- diagnose psychological conditions
- predict future behavior
- determine who is right in a conflict
- produce verdicts about a person's character

### The Forbidden Transformation

The system must never execute this transformation:

```
observation → personality judgement
```

The permitted transformation is:

```
observation → signal → interpretation candidate → uncertainty-weighted reflection
```

### Enforcement

Every `ReflectionContract` output must include:
- `reflection_scope`: explicit statement of where this reflection is valid
- `uncertainty_note`: what the system cannot know
- `model_context`: which theoretical framework was applied and why

Violation of this principle is an architectural defect, not a feature gap.

---

## ADR-002: ConflictLab Is Not a Diagnostic System

**Status:** ACCEPTED
**Date:** 2026-07-29

### Context

Many behavioral platforms begin as reflection tools and gradually
accumulate diagnostic language. Phrases like "you tend to..." or
"your profile shows..." transform a mirror into a label.

### Decision

ConflictLab is an **Epistemic Reflection Framework**, not:
- a personality assessment system
- a psychological diagnostic tool
- a behavioral prediction engine
- a human scoring system

### Language Rules

| Forbidden | Permitted |
|---|---|
| "You are an avoidant type" | "A withdrawal signal was observed in this context" |
| "Your score is 0.8" | "Signal orientation: approach_withdrawal = -0.65 in this session" |
| "This means you fear rejection" | "One possible interpretation under Attachment Theory: rejection sensitivity" |
| "You always react this way" | "This pattern has appeared in 3 of 4 observed contexts" |

### Theoretical Frameworks as Lenses

Psychological theories (Karpman, Berne, Polyvagal, SCARF, etc.) are
**interpretive lenses**, not truth engines. Each theory:
- explains some signals well
- has explicit blind spots
- carries assumptions that may not apply
- must be declared when used

---

## ADR-003: Uncertainty Is a First-Class Object

**Status:** ACCEPTED
**Date:** 2026-07-29

### Context

Behavioral systems tend to hide uncertainty behind single confidence scores.
A score of 0.72 looks precise. It conceals whether the uncertainty comes
from insufficient data, contradictory signals, or model limitations.

### Decision

Uncertainty is never collapsed into a single number.

The `UncertaintyEngine` always decomposes uncertainty into five dimensions:

| Dimension | Description |
|---|---|
| `data_insufficiency` | Not enough observations to form a reliable signal |
| `signal_conflict` | Observed signals point in contradictory directions |
| `source_diversity_gap` | All signals come from the same modality or context |
| `temporal_instability` | Signal pattern changes significantly over time |
| `model_assumption_gap` | The theoretical framework's assumptions may not apply here |

Each dimension is reported independently.
No single aggregate uncertainty score is produced.

### Rationale

A reflection offered with visible uncertainty components is epistemically
honest. The person can assess: "I gave only one example" (data_insufficiency)
versus "my own signals contradicted each other" (signal_conflict).
These are meaningfully different experiences.

---

## ADR-004: SignalOrientation — Neutral Directional Vectors

**Status:** ACCEPTED
**Date:** 2026-07-29

### Context

Behavioral signals must be represented without importing moral or
psychological judgement into the data structure itself.

### Decision

`SignalOrientation` represents position on a neutral axis, not a quality.

**v0.4 Core Axes:**

| Axis | Negative pole (-1.0) | Positive pole (+1.0) |
|---|---|---|
| `approach_withdrawal` | Withdrawal / distancing | Approach / engagement |
| `control_release` | Release / surrender | Control / structuring |
| `certainty_seeking` | Tolerance of ambiguity | Drive to reduce uncertainty |

**Range:** `[-1.0, +1.0]` per axis.
**Neutral:** `0.0` = no directional signal observed.

**Required metadata per orientation reading:**

```json
{
  "axes": {
    "approach_withdrawal": -0.65,
    "control_release": 0.40,
    "certainty_seeking": 0.75
  },
  "confidence": 0.55,
  "context": "session:sess_001, stimulus:STIM_AUD_001",
  "source": "observed"
}
```

### The Critical Distinction

```
certainty_seeking = +0.80
```

Does NOT mean: "this person is controlling"

MEANS: "in this observed context, a signal toward uncertainty reduction
was recorded with this magnitude"

### Extensibility

The three core axes are locked for v0.4.
Additional axes may be proposed via a new ADR.
Axes must always be defined as bidirectional and label-neutral.

---

## ADR-005: EvidenceGraph — Provenance Chain

**Status:** ACCEPTED
**Date:** 2026-07-29

### Context

Reflections must be traceable. The person must be able to understand
what observations led to what interpretation.

### Decision

Every interpretation is backed by an `EvidenceGraph` — an internal
directed structure linking:

```
Stimulus → Response → SignalWeight → FrameworkContext → ReflectionCandidate
```

**Internal name:** `EvidenceGraph`
**User-facing name:** `Signal Trace`

The user sees a Signal Trace, not raw graph data.
The graph is never described as "evidence about the person."

**EvidenceNode minimum fields:**
- `node_id`
- `stimulus_ref`
- `response_observed`
- `signal_weight`
- `timestamp`
- `source_modality` (text / visual / audio / scenario)

**Provenance principle:**
No reflection is generated without a traceable `EvidenceGraph`.
A reflection without provenance is an architectural violation.

---

## ADR-006: Immutable Event Log

**Status:** ACCEPTED
**Date:** 2026-07-29

### Context

Mutable hidden state makes the system's reasoning invisible and
untraceable. It also makes debugging and audit impossible.

### Decision

All state changes are recorded as append-only events.
System state is always reconstructable from the event log.

**EventLog entry minimum fields:**
- `event_id`
- `event_type`
- `timestamp`
- `payload`
- `session_ref`

No event is ever modified or deleted after writing.
New understanding creates a new corrective event, not a mutation.

---

## ADR-007: ModelRegistry — Theory Declaration

**Status:** ACCEPTED
**Date:** 2026-07-29

### Context

When a theoretical framework is applied, the person deserves to know
which framework, what it assumes, and where it fails.

### Decision

Every theoretical framework used by the system must be registered
in `ModelRegistry` with these required fields:

```python
{
  "model_id": str,
  "name": str,
  "assumptions": [str],
  "blind_spots": [str],
  "applicable_context": [str],
  "non_applicable": [str],
  "confidence_level": str   # "high" | "medium" | "low" | "contested"
}
```

No framework is applied without a registry entry.
Unregistered frameworks are an architectural violation.

---

## ADR-008: ReflectionContract — Required Output Structure

**Status:** ACCEPTED
**Date:** 2026-07-29

### Context

Without a binding output contract, reflections risk becoming vague,
overreaching, or epistemically dishonest.

### Decision

Every system-generated reflection must satisfy `ReflectionContract`:

| Field | Description |
|---|---|
| `observation` | What was objectively observed (no interpretation) |
| `context` | The session/stimulus context of the observation |
| `uncertainty_note` | What the system cannot know or claim |
| `reflection_question` | An open question returned to the person |
| `model_context` | Which framework was applied and its confidence level |
| `reflection_scope` | Where this reflection is valid / where it is not |
| `signal_trace` | Reference to the backing EvidenceGraph |

A reflection missing any field is invalid and must not be delivered.

---

## Architectural Invariants (Never Violate)

1. **No diagnosis.** The word "diagnose" must not appear in any user-facing output.
2. **No verdicts.** Reflections end with questions, not conclusions about the person.
3. **No hidden uncertainty.** Every reflection exposes its uncertainty components.
4. **No unregistered theory.** Every applied framework is declared.
5. **No orphan reflection.** Every reflection has a Signal Trace.
6. **No mutable history.** State is reconstructed from events, never overwritten.
7. **No label from a single signal.** Triangulation across contexts is required.

---

## What Comes Next

| Step | Module | Status |
|---|---|---|
| 1 | `src/core/signal_orientation.py` | TODO |
| 2 | `src/core/evidence_graph.py` | TODO |
| 3 | `src/engine/uncertainty_engine.py` | TODO |
| 4 | `src/frameworks/model_registry.py` | TODO |
| 5 | `src/mirror/reflection_contract.py` | TODO |
| 6 | `src/core/event_log.py` | TODO |
| 7 | `validation/scenarios/` | TODO |
