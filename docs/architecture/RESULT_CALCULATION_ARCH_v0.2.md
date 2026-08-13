# ConflictLab — Future Result Calculation Architecture v0.2

**Date:** 2026-08-13  
**Status:** DRAFT FOR IMPLEMENTATION REVIEW  
**Purpose:** future post-Wave-1 / post-Gate-D result architecture  
**Supersedes:** `RESULT_CALCULATION_ARCH_v0.1.md`  
**Inputs:** Claude critical review + Grok adversarial counterexample audit + owner resolution decisions

**Not implemented**  
**Not validated**  
**Not a personality scoring model**

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

ConflictLab describes patterns appearing in observed reactions. It does not infer stable person characteristics from single choices or from a mathematically neat aggregate alone.

The architecture keeps these evidence channels separate:

```text
VISUAL CHOICE
COVERAGE / MISSINGNESS
RETRY BEHAVIOR
REFLECTION / REACTION CONTEXT
REACTION INTENSITY
REACTION LATENCY
EXPLICIT SELF-DESCRIPTION
BASE-RATE / POSITION CONTEXT
```

No channel automatically increases, decreases, validates, or cancels another channel.

---

## 2. Active candidate domains

```text
CS: Clarity ↔ Ambiguity
CR: Structure ↔ Flexibility
```

These are candidate response domains, not established traits.

Static:

```text
AW: Approach ↔ Withdrawal
```

is not part of this scoring architecture.

A possible future domain-specific response trajectory remains a separate hypothesis and must not be recreated as a generic third score.

---

## 3. Future session architecture

### Stage 0 — Training

Participant receives dummy pairs used only to learn the interaction and pacing.

Training telemetry may be stored, but every training event must carry:

```text
is_training = true
```

Training events are excluded from all research and scoring pipelines.

Exact number of training pairs remains empirical.

### Stage 1 — Rapid Visual Choice Block

One block contains:

```text
3 sequential image pairs
```

Each pair shows two images simultaneously.

Allowed rapid responses:

```text
A / B / timeout
```

There is **no `no_clear_choice` in the rapid block**.

The participant selects one image and the next pair appears. There is one shared time budget for the whole block.

Working hypothesis:

```text
~6 seconds total
```

This is not frozen and must be calibrated empirically.

The shared budget is explicitly a time-pressure condition. It may create serial depletion and must therefore be treated as experimental context, not as a neutral measurement environment.

No reflection, explanation, Likert scale, or intensity question is shown during Stage 1.

---

## 4. Required rapid-block telemetry

At block level, store at minimum:

```text
block_id
block_attempt_number
block_budget_ms
block_start_timestamp
block_end_timestamp
block_timed_out
```

At pair-event level, store at minimum:

```text
pair_id
stimulus_set_version
asset_A
asset_B
asset_position_A
asset_position_B
position_in_block
pair_exposure_number
pair_ready_timestamp
choice_timestamp
visual_choice_latency_ms
remaining_budget_at_pair_start
choice = A | B | timeout
is_training
```

Device / interaction context should remain available for later diagnostics:

```text
device_type
input_method
viewport_width
viewport_height
browser / rendering context as technically feasible
```

A choice clock starts only after both assets are ready and the pair is interactive.

---

## 5. Timeout / retry

If all three choices are not completed before the shared budget expires, the full block may be repeated.

Current preferred rule:

```text
same pair order on retry
```

Changing pair order on retry would mix re-exposure with an additional order manipulation.

All retry events are append-only.

Critical distinction:

```text
block_attempt_number
≠
pair_exposure_number
```

Retry data never overwrite first-attempt events.

---

## 6. Primary vs retry evidence

### Primary rapid evidence

Only first-attempt selections are eligible for primary directional evidence:

```text
block_attempt_number = 1
```

Example:

```text
Attempt 1: P1 +   P2 -   P3 timeout
Retry:     P1 -   P2 -   P3 +
```

Primary directional evidence uses only:

```text
P1 +
P2 -
```

P3 has:

```text
primary_direction = MISSING_DUE_TO_TIMEOUT
```

### Retry evidence

Retry responses are secondary process evidence only.

They may describe:

- re-exposure;
- choice change;
- changed pacing;
- block adaptation;
- UI or timing difficulty.

Retry choices never fill a missing primary CS/CR directional event.

---

## 7. Reflection anchor provenance

The reflection stage must be tied to a known selection event.

Rule:

```text
If primary_choice exists:
    reflection_anchor_choice = primary_choice
    reflection_anchor_source = PRIMARY

Else if a later completed retry choice exists:
    reflection_anchor_choice = first completed retry choice
    reflection_anchor_source = FIRST_COMPLETED_RETRY
```

Do not use an ambiguous generic `final_choice` as the only provenance field.

`PRIMARY`-anchored and `FIRST_COMPLETED_RETRY`-anchored reflections are different observation conditions and must not be silently pooled for trajectory or cross-participant claims.

---

## 8. Gate D — pair-level directional mapping

A visual pair does not contribute to CS/CR because designers intended it to.

Before any directional scoring, the specific pair contrast must pass a mapping gate.

Example only:

```text
pair_id: CS-PR-02
asset_A → clarity direction (+1)
asset_B → ambiguity direction (-1)
mapping_status: VALIDATED
mapping_version: gate-d-v1
```

Position has no psychological meaning:

```text
Top != +
Bottom != -
A != +
B != -
```

Direction belongs to the validated reaction contrast.

If:

```text
signal_mapping_status = NONE
```

then the event contributes **no directional evidence**. This is not numeric zero.

Gate D validates a **pair-level mapping only**. It does not authorize aggregation across different exemplars.

---

## 9. Gate E — domain aggregation validity

Gate E is separate from Gate D.

Question:

> Even if several exemplars have defensible pair-level mappings, is it empirically defensible to aggregate them into one broader CS or CR domain?

Until Gate E is passed:

```text
NO domain-level CS/CR score
NO domain-level Directional Balance
NO claim that different exemplars are interchangeable indicators
```

Allowed language before Gate E:

> directional pattern among these specific validated exemplars

Gate E must examine whether apparent cross-exemplar agreement can be explained by shared confounds, such as visual simplicity, salience, aesthetics, utility, position strategy, or another non-domain process.

No fixed Gate E numeric threshold is frozen in v0.2.

---

## 10. Pair-level directional evidence

For every Gate-D-eligible primary event:

```text
mapped direction = +1 or -1
```

This remains an event-level observation.

Base rates, latency, intensity, reflection, and retry behavior do not multiply or shrink this event value.

---

## 11. Descriptive Directional Balance

Only after the relevant aggregation level is allowed:

```text
n_pos = eligible primary choices mapped +1
n_neg = eligible primary choices mapped -1

Directional Balance = (n_pos - n_neg) / (n_pos + n_neg)
```

Range:

```text
-1.00 ... 0 ... +1.00
```

This is called:

> **Descriptive Directional Balance**

It is not a personality score.

### Edge case

```text
if n_pos + n_neg == 0:
    direction_balance = NOT_ESTIMABLE
    evidence_status = INSUFFICIENT
```

If only one eligible directional event exists, the event may be reported as a single observation but must not be described as a repeated pattern.

---

## 12. Coverage remains separate

```text
Coverage = n_primary_directional_choices / n_eligible_presentations
```

Coverage answers:

> how much eligible primary evidence was observed?

Directional Balance answers:

> among observed eligible directional choices, which direction appeared more often?

They must remain separate.

Do not multiply Directional Balance by Coverage.

A result such as:

```text
direction = +0.60
coverage = 1.00
```

is not equivalent in evidential support to:

```text
direction = +0.60
coverage = 0.40
```

although the directional component is numerically the same.

---

## 13. Missingness is a first-class diagnostic

Timeout-based missingness must not be assumed to be Missing At Random.

A timeout can systematically depend on:

- pair complexity;
- domain/family;
- block position;
- remaining time;
- device or input method;
- participant strategy;
- the specific decision difficulty.

Therefore research analysis must preserve diagnostics such as:

```text
timeout_by_pair
timeout_by_family
timeout_by_block_position
timeout_by_asset_variant
timeout_by_device
timeout_by_remaining_budget
```

Coverage alone does not correct selection bias among the observed responses.

Missingness diagnostics are used to constrain interpretation, not to create an automatic weighting correction in v0.2.

---

## 14. Position / laterality diagnostics

Asset placement must be randomized or counterbalanced according to the protocol.

Store the concrete presented positions for every event.

Research analysis should test whether the same asset is selected differently depending on its presentation position.

Do not infer position bias merely because Top or Bottom is chosen more than 50% overall; the relevant diagnostic is whether **the same asset** changes selection probability by position.

Strong participant-level positional strategies may force a result to remain descriptive-only, but no universal numeric detector threshold is frozen in v0.2.

---

## 15. Base-rate context

Population choice rates are contextual evidence, not automatic scoring weights.

Example:

```text
Pair P1:
participant direction = +1
population chose + variant = 94%
```

The raw directional event remains `+1`.

However, the event may have lower individual discriminative value than a rare choice.

v0.2 does **not** introduce inverse-frequency weighting or rarity bonuses.

Store / calculate item base rates separately and use them to constrain claims.

---

## 16. Reflection stage

After the rapid block, each reflection anchor is shown separately.

Structured reason options have stable IDs and versioned interpretation metadata.

Preferred v0.2 terminology:

```text
DOMAIN_CONSISTENT_REASON
CROSS_DOMAIN_REASON
OTHER_REASON
UNRESOLVED
```

These labels describe the **selected reason option**, not the participant's hidden true motive.

Example:

```json
{
  "reason_id": "CS_PR_R03",
  "text_lt": "Norėjosi aiškiau matyti visą objektą",
  "interpretability_class": "DOMAIN_CONSISTENT_REASON",
  "coding_version": "reason-map-v2"
}
```

`Another reason` keeps the free text raw and does not receive automatic domain classification.

If AI or researcher post-hoc coding is later used:

```text
raw_free_text
↓
coding_model_version
↓
posthoc_classification
```

The post-hoc layer never overwrites the original participant response.

---

## 17. Reflection does not rewrite visual direction

Example:

```text
visual direction = +1
selected reason class = OTHER_REASON
```

Do not automatically change the visual event to 0 or exclude it.

Store both observations:

```text
Visual choice: +1
Selected reason class: OTHER_REASON
```

Reflection constrains interpretation of the visual event. It is not a numeric multiplier.

---

## 18. Reflection summary metrics

Research layer may summarize:

```text
domain_consistent_reason_ratio
cross_domain_reason_ratio
other_reason_ratio
unresolved_ratio
```

No fixed validity threshold is frozen.

Structured reason agreement must never be described as proof of the participant's true motive.

---

## 19. Reaction intensity

`reaction_intensity` is an ordinal self-report channel.

Strong rule:

```text
NEVER: CS/CR direction × intensity
```

A `+1` visual directional event remains `+1` whether intensity is 2/5 or 5/5.

Possible research summaries include medians and distributions, but intensity does not modify Directional Balance.

---

## 20. Latency

Keep distinct:

```text
rapid_visual_latency
reflection_latency
intensity_latency
```

They must not be merged into one reaction-speed score.

Forbidden:

```text
slow = stronger domain signal
fast = stronger domain signal
slow = deeper reflection
fast = impulsive
```

Latency remains process evidence.

Rapid latency must always be interpreted with block position, remaining budget, exposure number, and device context.

---

## 21. Explicit self-description

A later layer may contain validated self-description statements.

This channel stays separate from visual evidence.

Even if both internal metrics are represented on mathematically similar ranges, their magnitudes are not assumed commensurable.

Forbidden:

```text
visual 0.7 - self_report 0.3 = divergence 0.4
```

### Allowed v0.2 comparison

Only direction-level comparison:

```text
Visual channel:
POSITIVE / NEGATIVE / MIXED / INSUFFICIENT

Self-report channel:
POSITIVE / NEGATIVE / MIXED / INSUFFICIENT
```

Relationship language:

```text
SAME_DIRECTION_ACROSS_CHANNELS
OPPOSITE_DIRECTION_ACROSS_CHANNELS
MIXED
INSUFFICIENT
```

Avoid `CONVERGENT` / `DIVERGENT` until the two channels are shown to measure sufficiently comparable constructs.

Neither channel represents the participant's “true self”.

---

## 22. Evidence status and claim hierarchy

Working evidence states:

```text
INSUFFICIENT
DESCRIPTIVE_ONLY
DOMAIN_INTERPRETABLE
REPLICATED
```

No arbitrary coverage threshold is frozen for transitions.

Logical constraints:

- zero eligible primary events → `INSUFFICIENT`;
- one eligible primary event → single observation only, not repeated-pattern language;
- `DOMAIN_INTERPRETABLE` requires Gate E support;
- `REPLICATED` requires independent repetition across item sets and/or sessions according to a later validation rule.

### Claim levels

**Level 0 — Raw observation**  
“You selected this image.”

**Level 1 — Specific repeated observation**  
“A similar direction appeared across these specific eligible pairs.”

**Level 2 — Domain-supported pattern**  
Allowed only after Gate E.  
“Across different validated situations, a direction toward greater clarity appeared more often.”

**Level 3 — Recurring response tendency**  
Requires independent replication.  
“A similar reaction direction has appeared repeatedly across different sessions.”

Not permitted:

> “You are a clarity-seeking person.”  
> “You dislike ambiguity.”  
> “You need control.”  
> “Your openness score is 72%.”

---

## 23. Retry divergence context

Primary-only scoring remains the rule.

However, when retry choices differ materially from first-attempt choices, the system must not narrate the primary pattern as though no later divergence occurred.

Possible process statement:

> First-pass choices leaned in one direction, while later repeated choices under a different condition were different.

Retry divergence is context, not a replacement score.

---

## 24. Three separate histories

Mapping changes create a provenance problem that versioning alone does not solve unless result history is separated.

ConflictLab therefore keeps three conceptual layers:

### RAW EVENTS — immutable

What the participant actually selected and when.

### DERIVED RESEARCH VIEW — recalculable and versioned

What historical raw events produce under a specified current `mapping_version` and `scoring_version`.

### PUBLISHED RESULT SNAPSHOT — immutable

What was actually shown to the participant at that time under the then-valid mapping and scoring rules.

A later mapping reversal must never silently rewrite historical participant-facing result history.

---

## 25. Versioning requirements

Every derived result must retain:

```text
protocol_version
stimulus_set_version
mapping_version
aggregation_gate_version
reason_map_version
scoring_version
```

Raw response events store the protocol/stimulus/pair/asset facts, not future interpretation.

Derived results carry mapping and scoring provenance.

Published result snapshots carry the exact derivation versions used at publication time.

---

## 26. Proposed internal result object

```json
{
  "protocol_version": "future-session-v0.x",
  "stimulus_set_version": "stimulus-set-vX",
  "mapping_version": "gate-d-v1",
  "aggregation_gate_version": "gate-e-v1",
  "reason_map_version": "reason-map-v2",
  "scoring_version": "future-result-v0.2",

  "CS": {
    "aggregation_status": "DOMAIN_INTERPRETABLE",

    "visual": {
      "direction_balance": 0.50,
      "primary_directional_count": 4,
      "eligible_presentations": 5,
      "coverage": 0.80
    },

    "missingness": {
      "timeouts": 1,
      "by_position": {"1": 0, "2": 0, "3": 1}
    },

    "reflection": {
      "domain_consistent_reason": 2,
      "cross_domain_reason": 1,
      "other_reason": 1,
      "unresolved": 0,
      "anchor_sources": {
        "PRIMARY": 3,
        "FIRST_COMPLETED_RETRY": 1
      }
    },

    "intensity": {
      "values": [4, 3, 5, 2]
    },

    "latency": {
      "rapid_ms": [1200, 2100, 900, 1800],
      "reflection_ms": [3400, 5100, 2200, 4100],
      "intensity_ms": [900, 1300, 800, 1500]
    },

    "self_report": {
      "direction_class": "POSITIVE",
      "valid_items": 4
    },

    "channel_relationship": "SAME_DIRECTION_ACROSS_CHANNELS"
  }
}
```

There is no `final_CS_score` field.

---

## 27. User-facing result architecture

Primary result order:

1. **What was observed** — specific pair-level repetition first.
2. **Coverage** — how much eligible primary evidence was actually observed.
3. **Missingness / exceptions** — timeouts, opposite-direction events, relevant retry divergence.
4. **Interpretation context** — selected reflection reasons, stated cautiously.
5. **Cross-channel relation** — only direction-level and only if both channels are eligible.
6. **Reflection question** — turns evidence into self-observation rather than label assignment.

Before Gate E, user-facing language must remain exemplar-specific.

After Gate E, cautious domain-level language may be allowed.

Numbers and visualizations are secondary explanations, not the primary result.

---

## 28. Secondary visualization

Do not restore the old three-axis AW/CS/CR radar as the primary result.

Potential future display after relevant gates:

```text
CS
Ambiguity  ←────────●────────→ Clarity

CR
Flexibility ←────●────────────→ Structure
```

If explicit self-description is displayed, it must use a visually distinct marker and must not imply metric equivalence.

Coverage and evidence status are displayed separately.

Avoid presentation such as:

```text
CS = 73%
```

---

## 29. What must never enter CS/CR vector magnitude in v0.2

```text
❌ reaction intensity
❌ visual latency
❌ reflection latency
❌ intensity latency
❌ retry speed
❌ number of retries
❌ self-report Likert magnitude
❌ free-text length
❌ product continuation
❌ product engagement
❌ item rarity / base-rate bonus
❌ coverage multiplier
```

Directional evidence comes only from a Gate-D-eligible primary visual choice.

Domain aggregation additionally requires Gate E.

---

## 30. What remains deliberately unresolved

### BLOCKING before domain-level implementation

1. **Gate D contract** — what evidence is sufficient for a pair-level directional mapping?
2. **Gate E contract** — what evidence is sufficient for cross-exemplar domain aggregation?
3. **Rapid-block time calibration** — whether ~6 seconds is appropriate.
4. **Reason-map design** — structured reason options and versioning rules.
5. **Telemetry contract** — exact event schema and readiness/timing implementation.

### IMPORTANT but deferrable

6. Minimum evidence required for `REPLICATED` status.
7. Base-rate presentation policy.
8. Participant-level position-strategy diagnostics.
9. Self-report statement validation and direction-class rules.
10. Research policy for recalculating historical raw events under new mappings.

### HYPOTHESIS only

11. Whether domain-specific response trajectory deserves a formal derived layer.

No arbitrary numeric threshold should be frozen merely because it simplifies implementation.

---

## 31. Central design principle

> **Add evidence without collapsing evidence.**

```text
PAIR-LEVEL VISUAL DIRECTION
        │
        ├── COVERAGE
        ├── MISSINGNESS
        ├── POSITION / ORDER
        ├── BASE-RATE CONTEXT
        ├── RETRY BEHAVIOR
        ├── REFLECTION CONTEXT
        ├── INTENSITY
        ├── LATENCY
        └── SELF-DESCRIPTION

        Gate E
           ↓
DOMAIN-LEVEL DESCRIPTIVE PATTERN
```

The goal is not to calculate the strongest possible score.

The goal is to preserve enough independent evidence to show:

- what repeated;
- what did not;
- what was not observable under the rapid condition;
- which interpretations were participant-endorsed;
- where other evidence channels agreed or differed;
- and which claims the available evidence does **not** justify.
