# ConflictLab — Result Calculation Architecture v0.1 — Critical Review & v0.2 Resolution Package

**Date:** 2026-08-13
**Review by:** Claude (critical audit) + Oleg (resolution verdicts)
**Status:** Resolution package for v0.2 — not yet implemented

---

## Review summary

Claude's audit identified 5 BLOCKER-level issues and 4 IMPORTANT issues in v0.1. The resolution package below constitutes the v0.2 decision baseline.

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
  "interpretability_class": "OTHER"
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

---

## C5 — Self-report and visual channels use same [-1,+1] range implying commensurability

**Verdict:** Lengvai išsprendžiama. **RESOLVED.**

Alignment in v0.2 is direction-level only:

```text
Visual direction:      POSITIVE / NEGATIVE / MIXED / INSUFFICIENT
Self-report direction: POSITIVE / NEGATIVE / MIXED / INSUFFICIENT

Alignment:
  same direction
  opposite direction
  mixed
  insufficient
```

Forbidden:

```text
difference = visual 0.7 - self-report 0.3 = 0.4
```

Magnitude subtraction is not permitted because scale equivalence has not been established.

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

`mapping_version` lives in the derived-results table, not in raw responses rows.

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

Criteria for transitions between these states are deferred to Gate D / later validation. No numeric threshold (e.g. coverage > 0.8) is invented as a methodological constant.

---

## New issue identified — reflection_anchor_choice (not in Claude's original audit)

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

---

## v0.2 rule summary

| Rule | Decision |
|---|---|
| Rapid block choices | A / B / timeout only — no `no_clear_choice` |
| Directional evidence source | `primary_choice` (first attempt) ONLY |
| Retry evidence | Secondary — never fills primary CS/CR gap |
| Direction formula edge case | `n=0` → `NOT_ESTIMABLE`, not 0 |
| Coverage | Separate dimension, never merged into formula |
| Reflection classification | Pre-defined `reason_id` + `interpretability_class`; free text raw |
| Reflection anchor | `primary_choice` if exists; else `FIRST_COMPLETED_RETRY` |
| Intensity / latency | Independent channels — unchanged |
| Self-report vs visual alignment | Direction-level only (POSITIVE/NEGATIVE/MIXED/INSUFFICIENT) |
| Raw DB | Append-only — never overwrite |
| Derived data | Versioned `mapping_version` + `scoring_version` in derived table |
| Evidence status | `INSUFFICIENT / DESCRIPTIVE_ONLY / DOMAIN_INTERPRETABLE / REPLICATED` |

---

## Next step

Adversarial Grok audit — not opinion-based review, but concrete counterexample datasets that would produce misleading outputs under v0.2 architecture.
