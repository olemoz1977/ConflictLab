# ConflictLab — Result Calculation Architecture v0.1 — Critical Review & v0.2 Resolution Package

**Date:** 2026-08-13
**Review by:** Claude (critical audit) + Oleg (resolution verdicts)
**Status:** REVIEW COMPLETE — resolutions carried into v0.2

---

## Review summary

Claude's audit identified 5 BLOCKER-level issues and 4 IMPORTANT issues in v0.1. The resolution package below constitutes the first v0.2 decision baseline.

The subsequent adversarial Grok audit is recorded separately in:

`docs/architecture/RESULT_CALCULATION_ARCH_v0.2_REDTEAM.md`

Integrated architecture:

`docs/architecture/RESULT_CALCULATION_ARCH_v0.2.md`

---

## C1 — no_clear_choice + shared timer contradiction

**Verdict:** Tikras blocker. **RESOLVED.**

`no_clear_choice` does NOT exist in the rapid block. The rapid stage accepts only:

```text
A / B / timeout
```

`unsure / hard to say` appears only in the Reflection stage.

This eliminates the strategic use of `no_clear_choice` to save shared block time, and keeps timeout as a clean procedural fact:

> a directional selection was not recorded within the specified shared-time condition.

---

## C2 — primary_choice vs final_choice — which feeds Directional Balance?

**Verdict:** Tikras blocker. **RESOLVED.**

```text
Directional evidence = first-attempt primary_choice ONLY.
```

Example:

```text
Attempt 1:  P1 +   P2 -   P3 timeout
Retry:      P1 -   P2 -   P3 +

CS/CR primary evidence uses only: + -
P3 primary_direction = MISSING_DUE_TO_TIMEOUT
```

Retry information is stored (`final_choice`, `choice_changed`, retry latency) but never fills the primary evidence gap.

---

## C3 — Directional Balance formula undefined when n=0; coverage integration

**Verdict:** Pusiau teisinga. **RESOLVED.**

Coverage must NOT be integrated into the Directional Balance formula — keeping them separate is the correct design. The formula correctly describes direction among recorded eligible choices.

However, the missing edge case is real:

```python
if n_pos + n_neg == 0:
    direction_balance = NOT_ESTIMABLE
    evidence_status = INSUFFICIENT
```

This must be explicit in v0.2.

---

## C4 — Reflection classification has no defined classifier

**Verdict:** Tikras blocker. **RESOLVED.**

Structured reason variants must have pre-defined `reason_id` and `interpretability_class`:

```json
{
  "reason_id": "CS_PR_R03",
  "text_lt": "Norėjosi aiškiau matyti visą objektą",
  "interpretability_class": "SUPPORTED",
  "coding_version": "reason-map-v1"
}
```

```json
{
  "reason_id": "GEN_AESTHETIC",
  "text_lt": "Šis vaizdas tiesiog gražiau atrodė",
  "interpretability_class": "OTHER",
  "coding_version": "reason-map-v1"
}
```

`Another reason` → `OTHER_UNCODED`. Free text stored raw, never auto-classified.

If post-hoc AI/researcher classification occurs, it is a separate versioned layer:

```text
raw_free_text
↓
coding_model_version
↓
posthoc_classification
```

This never overwrites the original reason.

**Post-Grok refinement:** v0.2 uses less causal terminology:

```text
DOMAIN_CONSISTENT_REASON
CROSS_DOMAIN_REASON
OTHER_REASON
UNRESOLVED
```

These labels describe the selected reason option, not the hidden true cause of the visual choice.

---

## C5 — Self-report and visual channels use same [-1,+1] range implying commensurability

**Verdict:** Lengvai išsprendžiama. **RESOLVED.**

Alignment in the initial v0.2 decision was direction-level only:

```text
Visual direction:      POSITIVE / NEGATIVE / MIXED / INSUFFICIENT
Self-report direction: POSITIVE / NEGATIVE / MIXED / INSUFFICIENT
```

Forbidden:

```text
difference = visual 0.7 - self-report 0.3 = 0.4
```

Magnitude subtraction is not permitted because scale equivalence has not been established.

**Post-Grok refinement:** avoid `CONVERGENT / DIVERGENT` terminology until channel comparability is supported. Use:

```text
SAME_DIRECTION_ACROSS_CHANNELS
OPPOSITE_DIRECTION_ACROSS_CHANNELS
MIXED
INSUFFICIENT
```

---

## I1 — Block budget storage

**ACCEPTED.** Store:

```text
block_start_timestamp
pair_ready_timestamp
choice_timestamp
remaining_budget_at_pair_start
```

---

## I2 — Training pairs storage

**ACCEPTED.** Training telemetry is stored with:

```text
is_training = true
```

Never allowed into research/scoring pipeline. May help understand timeout patterns.

---

## I3 — mapping_version field placement

**ACCEPTED with refinement.**

Raw event stores: `protocol_version`, `stimulus_set_version`, `pair_id`, `asset`.

Derived result stores: `mapping_version` + `scoring_version`.

`mapping_version` lives in the derived-results layer, not in raw response rows.

---

## I4 — Retry storage structure

**ACCEPTED.**

Retry data stored as append-only event rows. Never overwrite first exposure row.

---

## O1 — Coverage threshold for claim levels

**NOT FROZEN.** Instead, v0.2 introduces:

```text
evidence_status:
  INSUFFICIENT
  DESCRIPTIVE_ONLY
  DOMAIN_INTERPRETABLE
  REPLICATED
```

Criteria for transitions between these states are deferred to validation gates. No numeric threshold such as coverage > 0.8 is invented as a methodological constant.

Logical constraint added after adversarial review:

```text
0 eligible primary directional observations → INSUFFICIENT / NOT_ESTIMABLE
1 eligible primary directional observation → single observation only; not repeated-pattern language
```

---

## New issue identified — reflection_anchor_choice

If a 3-pair block times out and is retried, and the participant had already chosen P1 and P2 in the first attempt, those P1/P2 pairs are shown again on retry.

The question: which image does the reflection stage ask about?

**Resolution:**

```text
If pair has primary_choice → reflection anchor = primary_choice
If primary_choice missing due to timeout → reflection anchor = first completed retry choice
```

The abstract `final_choice` field is insufficient. The correct field is:

```text
reflection_anchor_choice
```

with provenance:

```text
reflection_anchor_source:
  PRIMARY
  FIRST_COMPLETED_RETRY
```

This ensures reflection remains tied to a clearly known selection event.

Post-Grok rule: these two anchor sources are different observation conditions and must not be silently pooled for trajectory or cross-participant claims.

---

## Major addition after Grok red-team — Gate E

Gate D alone is insufficient.

A set of individually defensible pair mappings can still create a false domain pattern if different exemplars are driven by shared confounds or different response processes.

Therefore v0.2 separates:

```text
Gate D — PAIR MAPPING VALIDITY
Can this specific exemplar contrast defensibly receive a directional mapping?

Gate E — DOMAIN AGGREGATION VALIDITY
Can multiple Gate-D-valid exemplars defensibly be aggregated into one broader CS/CR domain?
```

Before Gate E, results remain pair/exemplar-specific. Gate D never automatically authorizes a domain-level CS/CR balance.

---

## Major addition after Grok red-team — missingness diagnostics

Timeout-based primary missingness must not be assumed to be random.

Research analysis must preserve diagnostics such as:

```text
timeout_by_pair
timeout_by_family
timeout_by_block_position
timeout_by_asset_variant
timeout_by_device
timeout_by_remaining_budget
```

Coverage tells how much evidence is observed; it does not correct systematic selection bias among observed responses.

---

## Major addition after Grok red-team — base-rate context

A Gate-D mapped event remains `+1` or `-1`. Population rarity does not create an automatic weight.

Pair-level population choice rates are stored/calculated separately as interpretive context.

No inverse-frequency weighting or rarity bonus is introduced in v0.2.

---

## Major addition after Grok red-team — historical result provenance

Mapping changes require three distinct histories:

```text
RAW EVENTS — immutable
DERIVED RESEARCH VIEW — recalculable under explicit mapping/scoring versions
PUBLISHED RESULT SNAPSHOT — immutable record of what participant saw at that time
```

A later mapping reversal must never silently rewrite historical participant-facing results.

---

## v0.2 rule summary

| Rule | Decision |
|---|---|
| Rapid block choices | A / B / timeout only — no `no_clear_choice` |
| Directional evidence source | `primary_choice` first attempt ONLY |
| Retry evidence | Secondary — never fills primary CS/CR gap |
| Direction formula edge case | `n=0` → `NOT_ESTIMABLE`, not 0 |
| One observation | Single observation only; never repeated-pattern language |
| Coverage | Separate dimension, never merged into formula |
| Missingness | First-class diagnostic; not assumed random |
| Gate D | Pair-level mapping validity only |
| Gate E | Required before cross-exemplar domain aggregation |
| Reflection classification | Versioned reason IDs; causal-neutral class labels in v0.2 |
| Reflection anchor | `PRIMARY` if exists; else `FIRST_COMPLETED_RETRY` |
| Intensity / latency | Independent channels — unchanged |
| Self-report vs visual | Direction-level relation only; no magnitude comparison |
| Base rates | Context only; no automatic weight |
| Raw DB | Append-only — never overwrite |
| Derived data | Versioned mapping / aggregation / scoring |
| Published results | Immutable snapshot under then-valid versions |
| Evidence status | `INSUFFICIENT / DESCRIPTIVE_ONLY / DOMAIN_INTERPRETABLE / REPLICATED` |

---

## Review cycle status

Claude blocker review: **COMPLETE**  
Owner resolution: **COMPLETE**  
Grok adversarial counterexample audit: **COMPLETE**  
Integrated architecture: `RESULT_CALCULATION_ARCH_v0.2.md`  
Detailed red-team record: `RESULT_CALCULATION_ARCH_v0.2_REDTEAM.md`
