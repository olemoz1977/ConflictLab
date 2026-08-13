# ConflictLab — Future Result Calculation Architecture v0.1

**Status:** ARCHIVED — superseded by v0.2
**Purpose:** future post-Wave-1 / post-Gate-D architecture
**Archived:** 2026-08-13

**Not implemented**
**Not validated**
**Not a personality scoring model**

See review and resolution package:
`docs/architecture/RESULT_CALCULATION_ARCH_v0.1_REVIEW.md`

---

## 1. Core epistemic rule

```text
SCENE PROPERTY
≠
PARTICIPANT RESPONSE
≠
DERIVED SIGNAL
≠
PERSON CHARACTERISTIC
```

ConflictLab should describe patterns appearing in observed reactions, not infer stable characteristics of the person from individual responses.

The architecture keeps separate:

```text
VISUAL CHOICE
REFLECTION / REACTION CONTEXT
REACTION INTENSITY
REACTION LATENCY
EXPLICIT SELF-DESCRIPTION
RETRY / TIMEOUT BEHAVIOR
```

No channel automatically increases or decreases another channel.

## 2. Candidate domains

Current active candidates:

```text
CS: Clarity ↔ Ambiguity
CR: Structure ↔ Flexibility
```

These labels may only become measurable response directions after the relevant stimulus families pass empirical validation.

Static:

```text
AW: Approach ↔ Withdrawal
```

is NOT part of this scoring architecture.

Possible future domain-specific response trajectory remains a separate hypothesis.

## 3. Future session architecture

### Stage 0 — Training

Participant receives several dummy pairs not used in analysis.

Purpose:
- learn the interaction;
- understand that choices should be rapid;
- understand automatic transitions;
- experience the shared block time constraint.

Training must not reveal CS/CR or what the experiment is attempting to measure.

Exact number of training pairs remains empirical.

### Stage 1 — Rapid Visual Choice Block

One block contains:

```text
3 sequential image pairs
```

For each pair:

```text
2 images shown simultaneously
→ participant selects one
→ next pair appears
```

There is one shared time budget for the entire 3-pair block.

Working hypothesis:

```text
~6 seconds total
```

This is NOT yet a frozen constant. It must be calibrated empirically.

Important:

```text
NOT 6 seconds per pair
NOT fixed 2 seconds per pair
```

Participant naturally allocates available time among the three decisions.

The system silently records the latency of every individual choice.

Example:

```text
Pair 1 = 1.2 s
Pair 2 = 2.6 s
Pair 3 = 1.4 s

Block total = 5.2 s
```

No reflection, explanation or intensity question is shown during this stage.

## 4. Timeout / retry

If all three choices are not completed before the shared time budget expires:

```text
block_attempt = timeout
```

The entire block is repeated.

Current preferred hypothesis:

```text
same pair order on retry
```

because changing order simultaneously introduces both re-exposure and order-change contamination.

Every attempt remains stored.

Critical distinction:

```text
block_attempt_number
≠
pair_exposure_number
```

Retry data never overwrite first-attempt data.

## 5. Primary vs retry evidence

### PRIMARY RAPID EVIDENCE

Responses obtained during:

```text
block_attempt_number = 1
```

are the primary rapid-choice evidence.

If the participant makes two selections and then the block times out:

```text
Pair 1 → primary response
Pair 2 → primary response
Pair 3 → no primary directional response
```

The first two observations are NOT deleted simply because the complete block timed out.

### RETRY EVIDENCE

Anything from:

```text
block_attempt_number > 1
```

is retained as secondary process evidence.

It may tell us about:
- re-exposure;
- changed choice;
- adaptation to pace;
- difficulty completing the block;
- UI effects.

It is not automatically pooled with first-attempt rapid evidence.

## 6. Final completed choice

For UX purposes, the process eventually needs one final selected image from each pair.

Therefore we distinguish:

```text
primary_choice
final_choice
```

They can be identical or different.

If:

```text
primary_choice != final_choice
```

record:

```text
choice_changed_on_retry = true
```

This is potentially interesting process evidence but does not itself have psychological meaning.

## 7. Stage 2 — Reflection

After the rapid block has been completed, each final selected image is processed individually.

Possible response classes might include:

```text
domain-relevant reason
alternative-domain reason
unsure / hard to say
another reason / different view
```

There is no visible timer. But the system records:

```text
reflection_latency_ms
```

Timing begins only after:
- selected image is fully rendered;
- every response option is visible;
- interface is interactive.

## 8. Stage 3 — Reaction Intensity

After selecting the reaction/reason, the participant sees that reaction again and rates its intensity:

```text
1–5
```

Example anchors:

```text
1 = very slight
5 = very strong
```

Store:

```text
reaction_intensity
intensity_latency_ms
```

## 9. One complete event

```text
VISUAL
│
├─ primary_choice
├─ final_choice
├─ rapid_latency
├─ block_position
├─ block_attempt
├─ timeout context
└─ exposure history

REFLECTION
│
├─ selected_reason
├─ reflection_class
└─ reflection_latency

INTENSITY
│
├─ intensity 1–5
└─ intensity_latency
```

These remain separate evidence fields.

## 10. Gate D — prerequisite for CS/CR calculation

A visual choice cannot contribute to CS/CR merely because designers intended it to.

Before scoring, a validated mapping must exist.

```text
pair_id: CS-PR-02

asset_A → clarity direction (+1)
asset_B → ambiguity direction (-1)

mapping_status: VALIDATED
mapping_version: gate-d-v1
```

Position has no meaning:

```text
Top != +
Bottom != -
A != +
B != -
```

If:

```text
signal_mapping_status = NONE
```

the event contributes `0 directional evidence` — not a numeric zero. It is simply not eligible for directional aggregation.

## 11. Primary visual directional balance

```text
n_pos = primary eligible choices mapped +1
n_neg = primary eligible choices mapped -1

Directional Balance(D) = (n_pos - n_neg) / (n_pos + n_neg)

Range: -1.00 ... 0 ... +1.00
```

This should initially be called **Descriptive Directional Balance** — NOT CS score, CR score, or personality score — until construct validation supports stronger terminology.

## 12. Coverage must remain separate

```text
Coverage = n_primary_directional_choices / n_eligible_presentations
```

`CS Directional Balance = +0.50` and `Coverage = 0.80` are two separate quantities. A result with coverage 1.00 must not be treated as equivalent to the same direction with coverage 0.40.

## 13. Timeout is NOT neutral

A timeout must never be encoded as `0` on the CS/CR axis.

```text
timeout ≠ neutral preference
```

Store separately:

```text
primary_timeout_count
retry_count
block_completion_attempts
```

## 14. no_clear_choice

If a future rapid protocol includes an explicit `no_clear_choice`, it remains a separate state:

```text
no_clear_choice ≠ timeout
no_clear_choice ≠ midpoint
no_clear_choice ≠ missing
```

Whether `no_clear_choice` should exist in the speeded future protocol itself remains an open design decision.

## 15. Reflection evidence

Reflection DOES NOT multiply visual direction.

A reflection response may later be classified as:

```text
SUPPORTED
CROSS_LOAD
OTHER / NONE
UNRESOLVED
```

## 16. Reflection must not secretly rewrite the score

```text
visual direction = +1
reflection = OTHER / aesthetics
```

We should NOT automatically do `visual event = 0` or `visual event = excluded` unless future empirical work explicitly justifies such filtering.

The reflection constrains what we are allowed to claim about the choice, not necessarily the raw observed choice itself.

## 17–22. Latency and intensity separation

Three distinct latency measures exist: `rapid_visual_latency`, `reflection_latency`, `intensity_latency`. They must NEVER be merged into one general reaction-speed score. Intensity is a separate ordinal self-report channel and never multiplies CS/CR vectors.

## 23–26. Self-description layer

A later ConflictLab stage may include conventional self-description statements with 1–5 Likert agreement. This is a different construct channel from reaction intensity.

Visual and self-report channels stay separate. No combined final score without empirical justification.

## 27. Response trajectory / epistemic openness

No numeric openness score exists in v0.1. This must remain domain-anchored rather than resurrecting AW as a generic third axis.

## 28. Proposed internal result object

```json
{
  "scoring_version": "future-result-v0.1",
  "mapping_version": "gate-d-v1",
  "protocol_version": "future-session-v0.x",
  "CS": {
    "visual": {
      "direction_balance": 0.50,
      "primary_choice_count": 4,
      "eligible_count": 5,
      "coverage": 0.80
    },
    "reflection": {
      "supported": 2,
      "cross_load": 1,
      "other": 1,
      "unresolved": 0
    },
    "intensity": { "values": [4, 3, 5, 2] },
    "latency": {
      "rapid_ms": [1200, 2100, 900, 1800],
      "reflection_ms": [3400, 5100, 2200, 4100],
      "intensity_ms": [900, 1300, 800, 1500]
    },
    "self_report": { "balance": 0.25, "valid_items": 4 }
  }
}
```

No automatic `final_CS_score` field exists.

## 29–30. Separation examples

See full PDF for detailed examples of primary vs retry evidence separation and reflection evidence separation.

## 31. User-facing result architecture

The primary result should NOT be a number or radar. Recommended order: what repeated → evidence coverage → exceptions → interpretation evidence → self-description comparison → reflection question.

## 32. Secondary visualization

Do NOT restore the old three-axis AW/CS/CR radar as the primary result.

```text
CS
Ambiguity  ←────────●────────→  Clarity

CR
Flexibility ←────●────────────→ Structure
```

Coverage shown separately: `Evidence: 4/5`

## 33. Versioning requirements

Every derived result must retain: `protocol_version`, `stimulus_set_version`, `mapping_version`, `scoring_version`. Raw responses are immutable.

## 34. What must never enter CS/CR vector magnitude in v0.1

```text
❌ reaction intensity
❌ visual latency
❌ reflection latency
❌ intensity latency
❌ retry speed
❌ number of retries
❌ self-report Likert
❌ free-text length
❌ product continuation
❌ "engagement"
```

## 35. What remains deliberately unresolved

1. Gate D criteria
2. Cross-exemplar aggregation
3. Minimum number of independent exemplars
4. Shared block time calibration
5. Retry architecture
6. Reflection anchor after changed retry choice
7. Self-report statement validation
8. Criteria for convergence/divergence language
9. Interpretability evidence threshold
10. Whether response trajectory deserves a formal derived layer

## 36. Proposed hierarchy of claims

- Level 0: Raw observation
- Level 1: Repeated observation
- Level 2: Domain-supported pattern (after cross-exemplar and interpretability evidence)
- Level 3: Recurring response tendency (requires replication)

NOT currently permitted: "You are a clarity-seeking person." / "Your openness score is 72%."

## 37. Central design principle

The model should add evidence without collapsing evidence. The goal is not to calculate the strongest possible score. The goal is to preserve enough independent evidence to show what repeated, what did not, and where the participant's own interpretation agrees or diverges from observed choices.
