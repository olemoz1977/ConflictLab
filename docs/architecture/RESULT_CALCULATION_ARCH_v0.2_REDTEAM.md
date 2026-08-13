# ConflictLab — Result Calculation Architecture v0.2 — Adversarial Red-Team Record

**Date:** 2026-08-13  
**Source:** Grok adversarial counterexample audit + owner/ChatGPT resolution  
**Status:** REVIEW RECORD — informs `RESULT_CALCULATION_ARCH_v0.2.md`

---

## Overall adversarial verdict

**KEEP WITH MAJOR SAFEGUARDS**

The red-team audit found that mathematically correct Directional Balance + Coverage can still produce misleading interpretations when missingness is systematic, time pressure depends on serial position, exemplars are heterogeneous, reflection anchors are not comparable, or pair base rates are ignored.

The audit therefore attacked the **meaning of valid calculations**, not only implementation correctness.

---

## Strongest counterexample

### Cross-exemplar false domain pattern

Example:

```text
Exemplar A — simplicity confound → +CS
Exemplar B — simplicity confound → +CS
Exemplar C — controlled clarity contrast → -CS

aggregate = (+1 +1 -1) / 3 = +0.33
```

A positive aggregate can appear even when no coherent domain-level CS process generated the choices.

### Resolution

Introduce two separate validation gates:

```text
Gate D — PAIR MAPPING VALIDITY
Can this specific exemplar contrast defensibly receive a directional mapping?

Gate E — DOMAIN AGGREGATION VALIDITY
Can multiple Gate-D-valid exemplars defensibly be aggregated into a broader CS/CR domain?
```

Gate D does not imply Gate E.

Before Gate E, results remain pair/exemplar-specific.

---

## Finding 1 — low coverage can create strong-looking Directional Balance

Example:

```text
+ / timeout / timeout

Directional Balance = +1.0
Coverage = 1/3
```

### Resolution

Do not modify the balance formula with a coverage multiplier.

Instead:

- zero directional observations → `NOT_ESTIMABLE / INSUFFICIENT`;
- one directional observation → single observation only, never repeated-pattern language;
- stronger evidence-state transitions remain empirically gated.

No arbitrary `coverage <= 1/3` universal cutoff is frozen.

---

## Finding 2 — shared timer can convert serial position into apparent direction

The same exemplar may produce a primary choice in position 1 and timeout in position 3 because earlier choices consume the shared budget.

### Resolution

Keep primary-only scoring, but make observability context first-class:

```text
position_in_block
remaining_budget_at_pair_start
pair_ready_timestamp
choice_timestamp
block_attempt_number
pair_exposure_number
```

Analyze timeout/missingness by pair, family, position, asset, device, and remaining budget.

Coverage does not correct systematic missingness.

---

## Finding 3 — primary vs retry divergence

Example:

```text
Attempt 1: + - timeout
Retry:     - - +
```

Retry may produce a cleaner pattern than first exposure, but it represents a different condition.

### Resolution

Keep:

```text
Directional evidence = first-attempt primary choice ONLY
```

Retry remains secondary process evidence.

However, materially different retry choices must be available as result context. The primary directional summary must not be narrated as though later divergence did not occur.

---

## Finding 4 — reflection-anchor non-comparability

A reflection anchored to a first-exposure choice is not methodologically equivalent to a reflection anchored to a retry choice.

### Resolution

Store:

```text
reflection_anchor_choice
reflection_anchor_source = PRIMARY | FIRST_COMPLETED_RETRY
```

Never silently pool anchor sources for trajectory or cross-participant claims.

The provenance must always be available to research analysis; it need not always be shown to the participant unless it changes the interpretation.

---

## Finding 5 — structured reflection can create false confidence

A participant can select a domain-looking reason while another unobserved motive generated the visual choice. Conversely, a domain-relevant motive may be present even if the selected reason is `OTHER`.

### Resolution

Rename the interpretation classes to avoid implying causal validation:

```text
DOMAIN_CONSISTENT_REASON
CROSS_DOMAIN_REASON
OTHER_REASON
UNRESOLVED
```

These labels describe the participant's selected reason option only.

They do not prove the hidden cause of the visual choice.

Free text remains raw. Any later coding is versioned and post-hoc.

---

## Finding 6 — base-rate blindness

A choice made by 94% of participants and a rare opposite choice both currently contribute ±1.

### Resolution

Keep raw event symmetry:

```text
Gate-D mapped event = +1 or -1
```

Do not introduce inverse-frequency weighting or rarity bonuses without evidence.

Instead store/report pair-level population base rates as separate interpretive context.

Base rate may constrain individual-level claims but does not automatically change vector magnitude.

---

## Finding 7 — self-report and visual channels can point the same way while measuring different things

Example:

```text
visual items → perceptual clarity
self-report items → preference for clear work instructions
```

Both may yield positive direction without demonstrating construct convergence.

### Resolution

Do not use `CONVERGENT / DIVERGENT` terminology in v0.2.

Use only:

```text
SAME_DIRECTION_ACROSS_CHANNELS
OPPOSITE_DIRECTION_ACROSS_CHANNELS
MIXED
INSUFFICIENT
```

Meaning:

> the measured channels pointed in the same/opposite direction on the items used here.

No magnitude comparison and no claim of trait-level agreement.

---

## Finding 8 — participant position strategies can mimic domain patterns

Examples:

- always choose Top;
- choose first visually acceptable item;
- alternate positions;
- sacrifice later pairs to finish the block.

### Resolution

Store concrete asset placement and participant selections.

Position diagnostics must examine whether the **same asset** changes selection probability by presentation position.

Do not use raw Top/Bottom 50/50 balance as the sole position-bias test.

No universal positional-strategy cutoff is frozen.

---

## Finding 9 — latency can remain outside the formula but still contaminate narrative

Two participants can have identical Directional Balance but radically different speed profiles.

### Resolution

Latency remains independent process evidence.

Never translate speed into:

```text
strength
impulsivity
depth
confidence
openness
```

Any future narrative that uses latency must explicitly define the supported observable process claim.

---

## Finding 10 — mapping reversals can rewrite apparent history

A later Gate-D mapping may reverse the sign of an old exemplar.

Versioning alone records the difference but does not decide which history the participant should see.

### Resolution — three histories

```text
RAW EVENTS
immutable factual record

DERIVED RESEARCH VIEW
recalculable under explicit mapping/scoring versions

PUBLISHED RESULT SNAPSHOT
immutable record of what the participant was shown at that time
```

A later mapping must never silently rewrite historical participant-facing results.

---

## Safeguards retained unchanged

The red-team explicitly did **not** justify weakening these rules:

```text
reaction intensity does not weight CS/CR
latency does not weight CS/CR
self-report magnitude is not blended with visual evidence
retry choices do not replace first-exposure primary evidence
raw events are append-only
n=0 Directional Balance is NOT_ESTIMABLE
coverage remains separate
no single final personality-style CS/CR score
AW is not restored as a static third axis
```

---

## v0.2 architectural consequences

```text
SCENE
↓
RAW FIRST-EXPOSURE CHOICE
↓
Gate D — pair-level mapping validity
↓
PAIR-LEVEL DIRECTIONAL EVIDENCE
↓
Gate E — cross-exemplar aggregation validity
↓
DOMAIN-LEVEL DESCRIPTIVE PATTERN
```

Parallel context remains separate:

```text
COVERAGE
MISSINGNESS
POSITION / ORDER
BASE-RATE CONTEXT
RETRY BEHAVIOR
REFLECTION REASON
INTENSITY
LATENCY
SELF-DESCRIPTION
```

No parallel channel becomes an automatic weight.

---

## Remaining blockers

Before domain-level implementation, v0.2 still requires explicit contracts for:

1. Gate D pair-mapping validity.
2. Gate E cross-exemplar aggregation validity.
3. Shared rapid-block time calibration.
4. Structured reason-map design and versioning.
5. Exact event / timing telemetry schema.

These are methodological/implementation gates, not reasons to collapse evidence into a cleaner score.
