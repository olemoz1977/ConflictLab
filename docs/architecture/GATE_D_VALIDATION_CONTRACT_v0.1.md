# ConflictLab — Gate D Validation Contract v0.1

**Status:** DRAFT / BLOCKING METHODOLOGY  
**Scope:** exact pair-level directional mapping only  
**Parent:** `VALIDATION_PROTOCOL_v0.1.md`

> Gate D does not ask whether a person "is CS" or "is CR". It asks whether one exact stimulus pair can support one exact directional mapping under a frozen evidence contract.

---

## 1. Gate D question

For an exact versioned pair:

> Is there sufficient independent evidence to assign opposite directions to Asset A and Asset B within one candidate domain, without relying on designer intention, post-hoc reason wording, or a simpler uncontrolled confound?

If not, the runtime mapping remains non-directional.

---

## 2. Gate D is pair-specific

A Gate D decision is bound to:

```text
stimulus_set_version
pair_id
asset_a_id
asset_b_id
exact asset hashes
presentation protocol version
validation study version
```

A redesign, re-render, material wording change, or protocol change may invalidate transfer of the prior Gate D decision.

No Gate D decision automatically transfers to:
- another pair;
- another family;
- another stimulus version;
- another domain;
- Gate E aggregation.

---

## 3. Preconditions before a confirmatory Gate D study may start

All of the following must be frozen before target data are inspected:

```text
pair identity and neutral blind alias
candidate domain hypothesis
candidate direction hypothesis
scene-property hypothesis
confound list relevant to the pair
participant protocol
sampling plan / data floor
blinding roles
coding scheme
primary evidence channels
secondary evidence channels
inclusion / exclusion rules
decision thresholds or qualitative decision rule
PASS condition
FAIL condition
SUSPEND condition
REDESIGN condition
stopping rule
```

If any required field is unset, the study is exploratory only and cannot populate a `VALIDATED` mapping.

---

## 4. Blinding requirement

At least one independent evidence layer must be blind to designer intent.

Blind raters/coders must not see:
- `CS` / `CR` labels;
- intended +1 / -1 direction;
- family name where it leaks the hypothesis;
- designer rationale;
- prior reviewer verdicts;
- Gate D recommendation.

Canonical repository IDs may remain unchanged for provenance, but blind interfaces/datasets use neutral aliases.

Example:

```text
CS-PR-01 -> PAIR-04
CS-PR -> FAM-C
```

Alias resolution happens only after independent coding/rating is locked.

---

## 5. Required evidence stack

A pair can be considered for `VALIDATED` only if all required evidence blocks are satisfied.

### D0 — Technical identity integrity

Required:
- exact assets verified;
- exact version recorded;
- both options rendered before response;
- presentation position known;
- no silent pooling across materially different versions.

Failure:
- affected observations are ineligible.

### D1 — Scene manipulation integrity

Question:
- does the intended visible scene contrast actually exist?

Evidence may include:
- blind scene-property rating;
- manipulation check;
- exact design specification.

Failure:
- `REDESIGN_REQUIRED` or `FAILED` for that pair hypothesis.

### D2 — Confound challenge

Use `CONFOUND_REGISTER_v0.1.md`.

At minimum consider, as relevant:
- luminance / contrast;
- visual complexity;
- symmetry/composition;
- completeness/legibility;
- salience/focal dominance;
- aesthetics;
- utility/affordance;
- familiarity;
- valence/desirability;
- agency/control;
- position;
- device/rendering effects.

Decision principle:

> if a simpler confound explains the observed preference at least as well as the intended domain manipulation and cannot be experimentally separated, Gate D cannot validate the pair.

### D3 — Blind semantic evidence

Preferred hierarchy:
1. spontaneous participant reasons;
2. blind coding of those reasons;
3. blind stimulus-meaning ratings/sorting;
4. structured reason selections only as secondary evidence after demand-characteristic testing.

Current `reason-map-v1` is not Gate D evidence by itself.

### D4 — Response/nuisance challenge

As required by study design, test:
- top/bottom bias;
- form effects;
- repeated exposure;
- training strategy transfer;
- random instability;
- dominant population base preference.

Reproducibility is necessary evidence about the response phenomenon, but is not sufficient evidence about construct meaning.

---

## 6. Evidence channels that cannot independently validate Gate D

The following are insufficient alone:

```text
high A/B consistency
short latency
long latency
strong intensity
structured DOMAIN_CONSISTENT_REASON selection
internal designer KEEP verdict
AI curation verdict
clean UI behavior
passing software tests
mathematically neat directional balance
```

These may be descriptive or supporting evidence only within a larger frozen design.

---

## 7. Required reason-map safeguard

If structured reasons are used as evidence in any Gate D study:

1. `reason-map` content must have a separate validation record;
2. reason categories must be reviewed/coded blind to pair intent where possible;
3. an open/spontaneous comparison condition or equivalent demand-characteristic challenge must be considered;
4. reason class is never treated as causal proof;
5. free-text missingness is reported separately;
6. "hard to identify" / unresolved response does not count as directional confirmation or disconfirmation unless pre-specified.

---

## 8. Decision states

Research decision state for a pair:

```text
NOT_TESTED
INSUFFICIENT_DATA
PENDING
SUPPORTED_FOR_CURRENT_SCOPE
FAILED
SUSPENDED
REDESIGN_REQUIRED
```

Runtime Gate D mapping status remains constrained by current schema:

```text
VALIDATED
PENDING
NONE
```

Mapping rule:

```text
SUPPORTED_FOR_CURRENT_SCOPE -> VALIDATED only if all contract requirements are satisfied
PENDING / INSUFFICIENT_DATA -> PENDING or NONE
FAILED / SUSPENDED / REDESIGN_REQUIRED -> NONE
```

Failed state must remain preserved in the evidence reference/history even though runtime status is `NONE`.

---

## 9. PASS logic

A pair may become `SUPPORTED_FOR_CURRENT_SCOPE` only when the pre-registered study rule is satisfied across all required blocks:

```text
D0 technical integrity: PASS
D1 scene manipulation: PASS
D2 confound challenge: PASS / no unresolved dominant alternative
D3 blind semantic evidence: PASS
D4 nuisance-response challenge: PASS as applicable
pre-registered stopping/data requirement: MET
no material unregistered protocol deviation
```

The exact numeric or qualitative thresholds must be justified in the study registration before target data are inspected.

This v0.1 contract deliberately does not invent universal numerical cutoffs.

---

## 10. FAIL logic

A pair must become `FAILED` for the tested hypothesis when a pre-registered failure criterion is reached.

Failure classes include:

### F-D1 — Manipulation failure
The intended scene property cannot be reliably distinguished.

### F-D2 — Dominant confound
A simpler alternative explanation dominates or is inseparable from the intended manipulation under the planned challenge.

### F-D3 — Semantic non-emergence
Blind semantic evidence does not support the candidate domain/direction under the frozen coding rule.

### F-D4 — Procedural dominance
Position, form, training, rendering, or another nuisance factor explains the response pattern sufficiently to invalidate the pair-level inference.

### F-D5 — Non-reproducible response
The pair does not produce a sufficiently stable/interpretable response phenomenon under the pre-registered criterion.

`FAILED` is not converted back to `PENDING` for the same exact version because the result is inconvenient.

A redesigned descendant requires a new identity/version and new confirmatory cycle.

---

## 11. SUSPEND logic

Use `SUSPENDED` when:
- the construct hypothesis is no longer being actively pursued;
- evidence remains fundamentally ambiguous and further work is not justified;
- a family repeatedly fails and the project chooses not to redesign it;
- ethical/privacy/cost constraints make a decisive study impractical.

Suspension is a valid endpoint, not a temporary wording trick.

---

## 12. REDESIGN logic

Use `REDESIGN_REQUIRED` when the candidate hypothesis may remain plausible but the current exact pair cannot test it cleanly.

Examples:
- perceptual confound aligned with intended direction;
- one variant is visually illegible;
- structured reason wording is leading;
- scene manipulation is too weak or too broad;
- both variants are not comparably legitimate.

A redesign must create a new versioned pair/asset identity.

Do not overwrite the failed ancestor.

---

## 13. Study registration template

Every confirmatory Gate D study must create a registration containing at minimum:

```text
study_id:
pair_canonical_id:
pair_blind_alias:
stimulus_set_version:
asset_hashes:
protocol_version:
candidate_domain:
candidate_direction_a:
candidate_direction_b:
scene_property_hypothesis:
primary_confounds:
secondary_confounds:
blinded_roles:
participant_population:
sample_size_rationale:
stopping_rule:
primary_evidence:
secondary_evidence:
coding_scheme_version:
inclusion_rules:
exclusion_rules:
PASS_rule:
FAIL_rule:
SUSPEND_rule:
REDESIGN_rule:
allowed_analyses:
forbidden_posthoc_actions:
registration_commit_sha:
```

No field that materially determines PASS/FAIL may be filled after target data inspection without invalidating confirmatory status.

---

## 14. Forbidden post-hoc rescue actions

For a confirmatory Gate D dataset, the following are forbidden unless they trigger a new version and new confirmatory cycle:

- changing the candidate domain after seeing reasons;
- changing direction labels after seeing choice frequencies;
- removing contradictory participants/pairs outside pre-registered exclusions;
- reclassifying reason categories because the mapping otherwise fails;
- choosing a new threshold because the original threshold fails;
- pooling a new protocol/stimulus version into the old dataset;
- declaring a confound "not important" only after it explains the observed pattern;
- turning `FAILED` into `PENDING` without new evidence/version.

Exploratory analysis may still be performed, but must be labeled exploratory.

---

## 15. External theory role

The Human Lens Library may be used before data to generate alternative explanations.

Examples:
- SCARF -> certainty/autonomy/social confounds;
- Locus of Control -> agency/control alternative;
- SDT -> autonomy/constraint alternative;
- Schema -> familiarity/prior-experience alternative;
- Constructed Emotion -> non-inference guardrail;
- Dual Process -> rapid-choice hypothesis, not mapping proof.

Theories cannot be invoked after a failed study merely to explain away the failure.

---

## 16. GERT / AgileBrain reference role

GERT lesson:
- expect candidate items to fail;
- retain only stimuli that earn survival through empirical testing.

AgileBrain lesson:
- rapid image capture can be tested empirically;
- internal response coherence must not substitute for independent validity evidence.

Neither provides direct Gate D evidence for ConflictLab.

---

## 17. What Gate D authorizes if valid

A `VALIDATED` pair permits only the exact pair-level directional transformation defined in `gate-d-v1`:

```text
selected exact asset
-> exact validated pair mapping
-> +1 or -1 candidate-domain event
```

It does **not** authorize:
- person characteristic language;
- trait labels;
- psychological diagnosis;
- behavioral prediction;
- aggregation with another pair;
- Gate E;
- interpreting intensity or latency as direction strength.

---

## 18. Current status

At creation of this contract:

```text
gate-d-v1 lifecycle: DRAFT
stimulus_set_version: null
mappings: []
current pair-level directional evidence: NONE
```

No existing pair is promoted by creation of this document.

---

## 19. Next artifact dependency

Before any Gate D confirmatory collection begins, create a pair/study-specific preregistration implementing this contract.

In parallel, define:

`GATE_E_VALIDATION_CONTRACT_v0.1.md`

because Gate D validation must never be mistaken for authorization to aggregate across exemplars.