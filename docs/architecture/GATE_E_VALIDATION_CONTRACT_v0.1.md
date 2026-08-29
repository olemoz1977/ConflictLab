# ConflictLab — Gate E Validation Contract v0.1

**Status:** DRAFT / BLOCKING METHODOLOGY  
**Scope:** cross-exemplar aggregation within a candidate domain only  
**Parent:** `VALIDATION_PROTOCOL_v0.1.md`  
**Dependency:** multiple independently surviving Gate D exemplars

> Gate E does not ask whether multiple pairs look conceptually similar to the designers. It asks whether independently surviving exemplars share enough response structure to justify aggregation without a simpler shared-confound explanation.

---

## 1. Gate E question

For a candidate domain such as CS or CR:

> After multiple exact pairs have independently survived Gate D, is there sufficient evidence that their directional events may be aggregated as observations of a common candidate response domain?

If not, results remain exemplar-specific.

Gate E may remain `NONE` permanently.

---

## 2. Preconditions

A confirmatory Gate E study cannot begin unless:

```text
at least multiple exemplars have Gate D VALIDATED status
all exemplar identities and versions are frozen
candidate domain is pre-specified
aggregation hypothesis is pre-specified
shared confounds are pre-registered
form/protocol/version treatment is frozen
participant sampling plan is frozen
analysis method is frozen
PASS / FAIL / SUSPEND rules are frozen
stopping / data-floor logic is frozen
```

The exact minimum number/diversity of exemplars must be justified in the study registration; this contract does not invent a universal number.

---

## 3. What Gate E is not

Gate E is not:
- a reliability shortcut;
- a personality-trait validation step;
- permission to average every Gate-D-valid event;
- proof from internal consistency alone;
- proof from shared designer labels;
- proof from similar-looking response distributions;
- permission to use latency or intensity as directional weight.

A high internal correlation can itself be caused by a shared nuisance factor.

---

## 4. Candidate aggregation unit

Every Gate E registration must define exactly what is being aggregated.

Example:

```text
domain: CS
included Gate D pairs: [exact IDs + versions]
directional event coding: {-1, +1}
missingness treatment: separate coverage channel
retry treatment: excluded from primary directional evidence
intensity treatment: separate channel
latency treatment: separate channel
reason treatment: separate validation/context channel
```

No new pair may be added after target data inspection without a new Gate E version/cycle.

---

## 5. Required evidence blocks

### E0 — Gate D integrity

Every included pair must have a valid evidence reference showing it survived the Gate D contract.

If a pair loses Gate D validity because of a material asset/protocol change, it cannot remain in the Gate E set without revalidation.

### E1 — Exemplar diversity

The surviving pairs must not all be trivial visual variants of one manipulation.

Reason:
- apparent cross-exemplar agreement among near-duplicates may only demonstrate one local visual preference.

Registration must describe:
- how exemplars differ;
- which scene properties are shared;
- which nuisance properties are intentionally varied.

### E2 — Shared-confound challenge

Use `CONFOUND_REGISTER_v0.1.md`.

High-priority Gate E alternatives include:
- stable aesthetic preference;
- preference for visual simplicity/complexity;
- brightness/contrast preference;
- openness/completeness preference;
- utility/affordance preference;
- familiarity/schema;
- position bias;
- form composition;
- repeated exposure;
- cultural convention.

Core question:

> Do exemplars agree because they share the intended candidate domain, or because they share a simpler nuisance property?

### E3 — Participant × exemplar variance

The study must evaluate whether apparent domain structure is dominated by:
- participant main effects;
- pair main effects;
- family effects;
- position effects;
- form effects;
- device/protocol effects;
- participant × pair interactions.

The exact statistical framework may vary with sample/design, but the analysis must be chosen before confirmatory data are inspected.

### E4 — Cross-exemplar coherence

Aggregation requires evidence that independently surviving exemplars show compatible response structure under the pre-frozen model.

Important:
- compatibility does not mean identical choice proportions;
- a population-level base preference may coexist with individual variation;
- internal consistency alone is not sufficient.

### E5 — Discriminant challenge

For CS and CR to remain separate candidate domains, evidence must address whether:
- CS exemplars relate more strongly to each other than to CR exemplars under the planned model;
- observed cross-domain association is explainable by shared confounds;
- one general preference dimension fits the data more parsimoniously than two candidate domains.

If a simpler one-factor/confound explanation is superior under the pre-specified comparison, the two-domain aggregation hypothesis fails for that dataset/version.

### E6 — Replication / new-sample challenge

Before a strong domain-level participant claim is considered, Gate E evidence should survive a new sample or other genuinely independent confirmation cycle.

An exploratory pattern found and confirmed on the same data is not sufficient.

---

## 6. Convergent and discriminant external evidence

Gate E should eventually include independent external evidence where justified.

Purpose:
- test theoretically expected relations to neighboring constructs/processes;
- demonstrate that CS/CR are not simply renamed versions of an existing construct;
- test discriminant separation from simple visual/aesthetic preference.

Important:
- external instruments do not redefine ConflictLab as a personality test;
- correlation with a questionnaire is not identity;
- failure to correlate with one external measure does not automatically invalidate the domain unless that prediction was pre-registered as critical;
- theory must specify expected relation before data are inspected.

Reference lesson:
- AgileBrain demonstrates the importance of external validation across multiple datasets, but its measures and thresholds are not imported into ConflictLab.

---

## 7. Form and protocol treatment

Current future-session forms contain different exemplars and different domain composition.

Therefore:

```text
F2-A != assumed equivalent to F2-B
```

Gate E registration must specify whether form is:
- a blocking factor;
- modeled explicitly;
- tested for equivalence;
- kept separate.

Pooling forms without a frozen justification is forbidden.

Materially different protocol versions must remain separate unless equivalence is explicitly justified.

---

## 8. Missingness and coverage

Coverage remains separate from directional balance.

Gate E must preserve:

```text
observed directional events
missing / timeout events
never-presented events
retry events
```

Rules:
- missingness cannot be silently coded as zero direction;
- retry events cannot repair primary evidence;
- systematic exemplar/form/position missingness can invalidate aggregation even when observed choices look coherent;
- timing-calibration success does not eliminate construct-level missingness concerns.

---

## 9. Intensity, latency and reflection channels

Current invariants remain:

```text
intensity never enters directional balance
latency never enters directional balance
retry events never enter directional balance
reflection class never changes direction
```

These channels may be studied separately.

Gate E cannot be rescued by:
- weighting "strong" intensity more heavily;
- weighting fast decisions more heavily;
- removing slow decisions post-hoc;
- using domain-consistent structured reasons to force exemplar coherence.

---

## 10. Required decision states

Research state for each candidate domain:

```text
NOT_TESTED
INSUFFICIENT_DATA
PENDING
SUPPORTED_FOR_CURRENT_SCOPE
FAILED
SUSPENDED
REDESIGN_REQUIRED
```

Runtime Gate E schema currently supports:

```text
VALID
PENDING
NONE
```

Mapping:

```text
SUPPORTED_FOR_CURRENT_SCOPE -> VALID only when all contract requirements are satisfied
PENDING / INSUFFICIENT_DATA -> PENDING or NONE
FAILED / SUSPENDED / REDESIGN_REQUIRED -> NONE
```

Failure/suspension evidence must remain visible in the evidence record.

---

## 11. PASS logic

A candidate domain may become `SUPPORTED_FOR_CURRENT_SCOPE` only when the pre-registered Gate E study shows:

```text
all included exemplars retain Gate D validity
exemplar set satisfies pre-defined diversity requirement
shared-confound challenge does not provide a sufficient simpler explanation
cross-exemplar structure meets the frozen analysis criterion
form/version effects are addressed under the frozen plan
missingness/coverage does not invalidate inference under the frozen rule
discriminant challenge is satisfied for the intended claim scope
pre-registered stopping/data requirement is met
no material unregistered protocol deviation occurred
```

Exact thresholds/sample requirements are study-specific and must be justified before target data are inspected.

---

## 12. FAIL logic

A candidate-domain aggregation must fail for the tested stimulus set/version when a pre-registered failure criterion is reached.

Failure classes:

### F-E1 — Shared-confound dominance
Cross-exemplar agreement is better explained by a nuisance factor than by the intended candidate domain under the frozen comparison.

### F-E2 — Exemplar incoherence
Independently Gate-D-valid exemplars do not show compatible response structure under the pre-registered aggregation model.

### F-E3 — Form/version dependence
The apparent aggregate depends materially on one form/version in a way that violates the frozen equivalence/analysis rule.

### F-E4 — Domain non-separability
The planned discriminant test does not support treating CS and CR as separate candidate domains, and a simpler common explanation is favored under the frozen rule.

### F-E5 — Instability / replication failure
A confirmatory/new-sample cycle does not reproduce the pre-registered aggregate pattern sufficiently for the intended claim.

On failure:

```text
Gate E runtime status = NONE
participant output remains exemplar-specific or NOT_ESTIMABLE
```

Do not change the aggregation rule on the same target dataset and call the revised result confirmatory.

---

## 13. SUSPEND logic

Use `SUSPENDED` when:
- too few distinct Gate-D-surviving exemplars remain to justify an aggregation program;
- repeated aggregation attempts fail;
- the candidate domain is no longer a productive research direction;
- resources/privacy constraints make adequate validation infeasible;
- exemplar-specific reflection remains useful enough that aggregation is unnecessary.

Suspension is an acceptable project outcome.

---

## 14. REDESIGN logic

Use `REDESIGN_REQUIRED` when:
- current exemplar set is too homogeneous;
- form structure prevents clean comparison;
- shared confounds are baked into all surviving pairs;
- domain distinction is plausible but current item pool cannot test it;
- additional contrasting exemplar families are needed.

New exemplars require their own Gate D cycle before entering a new Gate E study.

---

## 15. Study registration template

Every confirmatory Gate E study must include:

```text
study_id:
domain:
included_pair_ids:
included_pair_versions:
Gate_D_evidence_refs:
protocol_versions:
forms_included:
form_treatment:
participant_population:
sample_size_rationale:
stopping_rule:
exemplar_diversity_rule:
primary_shared_confounds:
secondary_confounds:
primary_aggregation_model:
variance_components_or_equivalent_plan:
missingness_rule:
discriminant_test_plan:
external_validation_plan:
replication_plan:
PASS_rule:
FAIL_rule:
SUSPEND_rule:
REDESIGN_rule:
allowed_analyses:
forbidden_posthoc_actions:
registration_commit_sha:
```

No material PASS/FAIL field may be completed after target data inspection without converting the study to exploratory status.

---

## 16. Forbidden post-hoc rescue actions

Forbidden for a confirmatory Gate E dataset unless a new version/new sample is created:

- dropping a contradictory Gate-D-valid exemplar because it weakens the aggregate;
- adding a supportive exemplar after seeing the result;
- changing domain boundaries after seeing cross-loads;
- merging CS/CR only because the two-domain model fails, then calling the merged result confirmatory on the same data;
- changing form pooling rules post-hoc;
- changing missingness treatment post-hoc;
- weighting intensity/latency to improve coherence;
- selecting a correlation/factor threshold after seeing the observed value;
- invoking a new theory after failure solely to rescue the same hypothesis.

Exploratory re-analysis remains allowed if clearly labeled exploratory.

---

## 17. GERT / AgileBrain methodological lessons

### GERT

Useful principle:
- item pools are empirically earned;
- weak items are pruned rather than protected.

Gate E implication:
- aggregation should be built only from independently surviving exemplars, not from a predetermined quota.

### AgileBrain

Useful principle:
- internal image-response structure should ultimately face external convergent/discriminant and replication evidence.

Gate E implication:
- internal coherence is a necessary candidate signal, not final construct proof.

Neither instrument supplies ConflictLab's Gate E thresholds.

---

## 18. What Gate E authorizes if valid

A Gate E `VALID` status may authorize candidate-domain aggregation only within the exact validated scope.

It does not automatically authorize:
- stable personality labels;
- diagnosis;
- behavioral prediction;
- causal claims about why a participant chose an image;
- interpreting latency as confidence/decisiveness;
- interpreting intensity as directional strength;
- generalization across cultures/protocol versions/populations not covered by evidence.

A separate participant-claim contract must still determine allowed wording.

---

## 19. Current status

At creation of this contract:

```text
Gate D mappings: none validated in current gate-d-v1
Gate E CS status: NONE
Gate E CR status: NONE
current domain aggregation evidence: NONE
participant directional result: NOT AUTHORIZED
```

No domain is promoted by creation of this document.

---

## 20. Strategic fallback if Gate E fails

Failure of Gate E does not necessarily mean the entire ConflictLab product fails.

A valid fallback product architecture may remain:

```text
exact stimulus
-> observed response
-> exemplar-specific reflection
-> uncertainty / alternative explanations
-> no domain score
```

This is consistent with ConflictLab's core philosophy of helping a participant observe reactions rather than forcing a personality classification.

Therefore Gate E is a hypothesis about useful aggregation, not a condition that the project must force to succeed.