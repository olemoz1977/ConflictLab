# ConflictLab — Validation Protocol v0.1

**Status:** DRAFT / pre-data methodological baseline  
**Purpose:** define a falsifiable validation sequence that separates mechanical timing, pair-level mapping, cross-exemplar aggregation, and reflection usefulness.  
**Inputs:** four-model independent review synthesis, `THEORY_TO_VALIDATION_MATRIX_v0.1.md`, `CONFOUND_REGISTER_v0.1.md`, current Gate D/E architecture, current timing-calibration specification.

> Core rule: no stage may borrow evidence from a later stage, and no failed hypothesis may be rescued by changing criteria after target data are inspected.

---

## 1. What this protocol is for

ConflictLab currently has a technically functioning product-shaped pilot but does not have validated CS/CR directional mappings or validated cross-exemplar aggregation.

This protocol therefore separates four different questions that must not be collapsed into one word such as "validation" or "calibration":

```text
A. TIMING CALIBRATION
   Can participants mechanically complete the rapid 3-pair protocol under the candidate 6000 ms shared budget?

B. GATE D VALIDATION
   Does one exact visual pair support a defensible pair-level directional mapping after independent semantic evidence and confound challenge?

C. GATE E VALIDATION
   Do multiple independently surviving exemplars support aggregation into a common candidate domain without a simpler shared-confound explanation?

D. REFLECTION UTILITY
   Does the experience help participants notice or articulate something about their own reaction process without requiring a trait claim?
```

These are four different research programs.

Passing one does not imply passing another.

---

## 2. Non-negotiable epistemic boundary

```text
SCENE PROPERTY
≠ PARTICIPANT RESPONSE
≠ DERIVED SIGNAL
≠ PERSON CHARACTERISTIC
```

Additional implications:

- a designed scene contrast is a manipulation hypothesis, not a validated construct;
- an A/B choice is a raw comparative response, not a domain score;
- a structured reason is a self-report about a possible explanation, not proof of causal motive;
- repeated choices may show reproducibility without proving construct meaning;
- a mathematically coherent aggregate may still reflect aesthetics, salience, position, form, training or another nuisance factor;
- no participant-facing directional interpretation is authorized while the relevant evidence gates are not valid.

Current safe state remains:

```text
Gate D = NONE
Gate E = NONE
participant directional result = NOT AUTHORIZED
```

---

## 3. Three evidence libraries

This protocol keeps three knowledge sources separate.

### 3.1 Human / Behavioural Lens Library

Historical 14-theory package plus other already used foundations such as Cognitive Appraisal, Predictive Processing, Epistemology, Reflective Practice and related lenses.

Allowed use:
- generate pre-data hypotheses;
- identify alternative explanations;
- define semantic/context boundaries;
- challenge interpretation.

Forbidden use:
- automatically prove a stimulus-to-domain mapping;
- diagnose the participant;
- rescue a failed empirical mapping post-hoc.

### 3.2 Validation / Measurement Method Library

Includes:
- construct-validity / psychometric reasoning;
- experimental design and counterbalancing;
- visual psychophysics / perceptual-confound measurement;
- blind qualitative coding and inter-rater agreement;
- paired-comparison methods;
- variance/generalizability thinking;
- convergent/discriminant multi-method validation;
- preregistration/version locking.

This library decides whether an empirical claim survives challenge.

### 3.3 Reference Instruments / Products

GERT and AgileBrain are practical precedents only.

GERT lesson:
- candidate stimuli are expendable items;
- attractive items may fail and be removed.

AgileBrain lesson:
- rapid image-based protocols are researchable;
- internal consistency is not enough;
- external and repeated validation matter.

Neither is evidence that ConflictLab's CS/CR mappings are valid.

---

## 4. Global preregistration rule

Before any dataset is used as confirmatory evidence for a specific claim, freeze the following:

```text
research_question
protocol_version
stimulus_set_version
inclusion_rules
exclusion_rules
blinding_roles
primary_outcomes
secondary_outcomes
confounds_to_test
decision_rule
PASS conditions
FAIL conditions
SUSPEND / REDESIGN conditions
stopping / data-floor rule
allowed analyses
forbidden post-hoc reinterpretations
```

If any material rule changes after target data have been inspected:

```text
old dataset = exploratory / historical evidence only
new rule = new protocol version
new confirmatory claim = requires a new confirmatory cycle
```

This is the primary control against researcher degrees of freedom.

---

## 5. Allowed terminal states

Every hypothesis must have more than `PENDING` and `VALIDATED`.

Conceptual research states:

```text
NOT_TESTED
PENDING
SUPPORTED_FOR_CURRENT_SCOPE
FAILED
SUSPENDED
REDESIGN_REQUIRED
INSUFFICIENT_DATA
```

Important:

- `FAILED` is a legitimate scientific result;
- `SUSPENDED` means the question is not being pursued under the current architecture;
- `REDESIGN_REQUIRED` means a new stimulus/protocol version is needed;
- `INSUFFICIENT_DATA` must not be used indefinitely to avoid a negative conclusion after a pre-specified stopping rule is reached.

Existing runtime Gate D/E JSON schemas remain unchanged until separate implementation decisions are made. These research states first live in validation records/contracts.

---

## 6. Validation Level 0 — Technical integrity

### Question

Did the participant actually receive and interact with the intended exact stimulus/protocol?

### Required evidence

- exact versioned asset identity;
- both options successfully decoded/rendered before interaction;
- known presentation order/position;
- valid event provenance;
- protocol version captured;
- page visibility/device diagnostics captured where relevant;
- no silent version pooling.

### Fail conditions

Any event with uncertain asset identity, incomplete render readiness, corrupted protocol provenance, or other material technical ambiguity cannot support later validation stages.

### Output

```text
TECHNICALLY_ELIGIBLE
or
TECHNICALLY_INELIGIBLE
```

No construct inference exists at this level.

---

## 7. Validation Level 1 — Scene manipulation integrity

### Question

Is the intended visible contrast actually present as a scene property, before asking what it means psychologically?

Example form:

```text
Hypothesis:
Asset A visibly contains more of property X than Asset B.
```

This is a scene claim only.

### Evidence sources

- design specification;
- independent blind scene-property ratings where needed;
- manipulation checks that do not expose CS/CR labels;
- exact asset audit.

### Blinding

External raters should receive neutral aliases and should not see designer-intended domain labels/directions.

Canonical IDs may remain in repository provenance, but blinded validation interfaces/datasets must use neutral aliases.

### Fail / redesign logic

If independent raters cannot reliably distinguish the intended scene contrast, or identify a materially different dominant contrast, the pair cannot proceed to Gate D under the same hypothesis.

Possible result:

```text
SCENE_MANIPULATION_SUPPORTED
SCENE_MANIPULATION_AMBIGUOUS
SCENE_MANIPULATION_FAILED
```

---

## 8. Validation Level 2 — Perceptual and semantic confound challenge

Source of required alternatives:

`docs/architecture/CONFOUND_REGISTER_v0.1.md`

### Question

Can a simpler non-domain explanation account for the choice or apparent pair meaning at least as well as the intended candidate manipulation?

### Mandatory challenge families as relevant

Perceptual:
- luminance / brightness;
- contrast;
- complexity / edge density / spatial frequency;
- symmetry / composition;
- focal dominance / size / centrality;
- completeness / legibility;
- colour;
- visible rendering/compression artifacts.

Semantic/contextual:
- aesthetics;
- utility / affordance;
- familiarity;
- desirability / valence;
- safety / threat;
- agency / control;
- social-status/autonomy/fairness cues;
- attachment/relational cues;
- cultural convention.

### Evidence sources

Possible methods include:
- objective image metrics where meaningful;
- blind human ratings;
- matched/control stimuli;
- neutral semantic classification;
- null/control contrasts;
- model comparison where justified.

### Decision principle

Do not require that every alternative explanation be literally zero.

Instead ask:

> Does the intended domain hypothesis add explanatory value beyond plausible simpler alternatives?

### Fail / suspend logic

If a dominant confound explains the response pattern at least as well as the intended manipulation and cannot be experimentally separated, the pair cannot advance to Gate D.

Possible result:

```text
CONFOUND_CHALLENGE_SURVIVED
CONFOUND_DOMINANT
CONFOUND_UNRESOLVED
REDESIGN_REQUIRED
```

---

## 9. Validation Level 3 — Blind semantic evidence

### Question

Without being shown CS/CR labels or designer intention, what meaning do independent people assign to the contrast and to spontaneous participant explanations?

This level exists specifically to break the design-definition loop.

### Preferred evidence hierarchy

Strongest candidate evidence:
1. spontaneous participant reason language;
2. blind independent coding of that language using neutral pair aliases;
3. blind independent sorting/rating of stimulus meaning;
4. structured reason selections only as secondary/supporting data after the reason map itself has been evaluated for demand characteristics.

### Structured reason rule

Current `reason-map-v1` remains DRAFT and explicitly does not validate Gate D.

`DOMAIN_CONSISTENT_REASON` must never be treated as proof of true motive.

If structured reasons are used in validation research, separately test whether they induce apparent coherence compared with an open/spontaneous condition.

### Coding requirements

Before coding target data, freeze:
- coding categories;
- domain-neutral confound categories;
- coder instructions;
- blinding procedure;
- disagreement-resolution procedure;
- reliability/agreement reporting method.

### Fail logic

A pair cannot proceed to Gate D when blind semantic evidence is dominated by unrelated/confound explanations, when intended-domain meaning does not emerge, or when coding is too unstable to support the claimed distinction.

Do not invent universal numeric thresholds in this protocol. The Gate D contract must justify and freeze the exact decision rule for the specific study design.

---

## 10. Validation Level 4 — Response reproducibility and nuisance-variance challenge

### Question

Is the observed response structure distinguishable from random choice and from procedural/individual nuisance effects?

### Required nuisance factors as relevant

- top/bottom position;
- serial position;
- shared-budget depletion;
- training strategy transfer;
- form composition;
- device/input modality;
- repeated exposure;
- fatigue/attention drift;
- stable aesthetic preference;
- prior experience/schema.

### Important distinction

Reproducibility alone does **not** prove CS/CR meaning.

A person may reproducibly prefer:
- brighter images;
- simpler images;
- open spaces;
- first/top options;
- familiar objects.

Therefore this stage asks whether there is a stable response phenomenon worth explaining, not whether the explanation is already known.

### Possible methods

- counterbalanced position repetitions;
- delayed retest on selected stimuli;
- form comparison;
- participant × pair × position variance decomposition;
- control/null pairs;
- repeated-sample replication.

### Fail logic

If the apparent pattern is dominated by position, form, training, random instability, or another nuisance source, the intended mapping cannot advance.

---

## 11. Research Program A — Mechanical timing calibration

Current authoritative spec:

`config/future-session/timing-calibration-v1.json`

Current scope is explicitly:

```text
MECHANICAL_TIMING_ONLY
```

### Question

Does the shared 6000 ms budget for 3 sequential pairs produce acceptable completion and missingness mechanics?

### Existing pre-specified decision rule

The current config already defines:
- clean-primary data floor;
- position-3 missingness/never-presented thresholds;
- block completion thresholds;
- pair-specific missingness thresholds;
- `INSUFFICIENT_DATA`;
- `REJECT_6000`;
- `ADJUST_AND_RETEST`;
- `KEEP_6000`.

These thresholds apply only to the mechanical timing question.

### Forbidden inference

A `KEEP_6000` result does **not** imply:

```text
CS valid
CR valid
Gate D valid
Gate E valid
latency psychologically meaningful
rapid choices are trait-like
the reflection is useful
```

### Operational decision before fresh participants

Because fresh participants are scarce, the research data/consent scope should be frozen before real `CALIBRATION` collection so that ethically justified non-timing validation channels are not accidentally omitted.

However, non-timing channels must remain analytically separate from the mechanical timing decision.

---

## 12. Research Program B — Gate D pair-level validation

Gate D answers only:

> For this exact pair and exact asset identities, is a directional mapping to one candidate domain defensible under a pre-frozen evidence contract?

Gate D does **not** answer:
- whether the domain is a stable trait;
- whether other exemplars measure the same thing;
- whether domain aggregation is valid;
- whether the participant can be described by a characteristic label.

### Minimum evidence stack before `VALIDATED` can be considered

```text
Level 0 technical integrity
+
Level 1 scene manipulation integrity
+
Level 2 confound challenge
+
Level 3 blind semantic evidence
+
Level 4 response/nuisance challenge as required by the design
+
pre-frozen Gate D contract
```

### Required negative path

A pair must be able to end as:

```text
FAILED
SUSPENDED
REDESIGN_REQUIRED
```

It is not acceptable to retain every contradictory pair indefinitely as `PENDING`.

### Pair provenance

Failed pairs remain in history. Do not silently delete/relabel them to manufacture a clean surviving set.

---

## 13. Research Program C — Gate E cross-exemplar/domain validation

Gate E may only be asked after multiple exemplars independently survive Gate D.

### Question

Do the surviving exemplars share enough response structure to justify a common candidate-domain aggregate, and does that commonality survive simpler shared-confound explanations?

### Core threats

- stable aesthetic preference;
- shared complexity/simplicity;
- openness/completeness preference;
- form composition;
- stimulus-family idiosyncrasy;
- device/protocol differences;
- cultural conventions;
- single nuisance factor creating apparent cross-exemplar coherence.

### Evidence requirements

The Gate E contract must specify, before confirmatory data:
- minimum number/diversity of Gate-D-surviving exemplars;
- participant sampling design;
- cross-exemplar analysis method;
- confound comparison method;
- form/version treatment;
- convergent/discriminant evidence plan;
- explicit failure/suspension logic.

### Critical rule

Gate E may legitimately remain `NONE` permanently.

If exemplars work only as exemplar-specific observations, ConflictLab must remain exemplar-specific rather than forcing a domain score.

---

## 14. Research Program D — Reflection usefulness

This question is intentionally independent of personality/trait validity.

### Primary product question

> Does the ConflictLab experience help a participant notice, articulate, or reconsider something about their own reaction process better than an appropriate comparison condition?

### Possible operational outcomes

Examples to be developed in a dedicated protocol:
- participant can state a previously unnoticed reaction preference;
- reflection question prompts specific self-observation rather than generic agreement;
- participant reports useful discrepancy or curiosity;
- later session recalls/revises previous observation;
- comparison condition produces less specific self-observation.

### Important caution

"Interesting", "resonant", "sounds like me", or "wow" are not sufficient construct-validation evidence.

Reflection usefulness may exist even if Gate E never validates a domain score.

This is strategically important because ConflictLab's product value proposition may be epistemic reflection rather than latent-trait measurement.

---

## 15. Null and adversarial control logic

At least some validation cycles should include conditions designed to make the system fail if the supposed signal is generic.

Candidate controls:

### 15.1 Position swap

Same exact A/B assets, reversed top/bottom presentation.

Purpose:
- detect positional preference without changing image content.

### 15.2 Non-domain / null contrast

A visually comparable pair deliberately not hypothesized to represent CS/CR.

Purpose:
- test whether the same apparent "consistency" emerges from arbitrary or generic visual preference.

### 15.3 Confound-matched contrast

Manipulate a known confound while minimizing the intended candidate-domain contrast.

Purpose:
- estimate how strongly the nuisance feature itself drives response.

### 15.4 Open-reason vs structured-reason condition

Purpose:
- test whether structured reason options create post-hoc domain-consistent coherence.

### 15.5 Training variant

Compare current shared-budget training with a condition that teaches interaction without the same pacing structure.

Purpose:
- test strategy transfer.

These are candidate designs. Their exact implementation and decision rules must be versioned before confirmatory use.

---

## 16. Sample-size and threshold discipline

The four external AI reviews proposed many numeric thresholds and sample sizes.

This protocol intentionally does **not** adopt them automatically.

Rules:

1. use the existing timing-calibration thresholds only for the already defined mechanical timing question;
2. justify Gate D/Gate E sample size from the planned analysis, expected uncertainty and practical design;
3. do not choose a threshold because it makes the observed dataset pass;
4. if an exploratory pilot is used to estimate variability, freeze a new confirmatory rule before the next sample;
5. report uncertainty, not only binary PASS/FAIL;
6. distinguish absence of evidence from evidence against a hypothesis.

---

## 17. Data separation and privacy

Current architecture is local-first and intentionally limits server collection.

Validation may require aggregate data that the timing-only payload does not currently contain.

Before collection, define an explicit research/consent scope for each channel:

```text
A/B response identity
position
pair identity
visual-choice latency
reason_id
open free text
reaction intensity
reason-response latency
intensity-response latency
derived local outputs
```

Rules:

- timing calibration must not silently expand into construct research;
- construct research must not silently upload local-only reflection data;
- free text remains local-first unless a separately justified explicit-consent protocol authorizes collection;
- consented research data must preserve TECHNICAL vs CALIBRATION vs future validation-study provenance;
- participant IDs must remain privacy-minimized and purpose-limited.

---

## 18. Blinding architecture

To reduce circularity, validation tooling should support neutral aliases.

Example:

```text
canonical repo identity: CS-PR-01
blind validation alias: PAIR-04
canonical family: CS-PR
blind family alias: FAM-C
```

Blinded raters/coders must not see:
- CS/CR labels;
- intended +/− direction;
- designer rationale;
- prior Gate D recommendation;
- other coder verdicts before independent coding.

After coding is locked, aliases can be resolved for analysis.

Do not rename or destroy frozen historical canonical assets solely to create blinding.

---

## 19. Claim ladder

Participant-facing claims must follow the strongest validated evidence level and no higher.

```text
LEVEL 0 only
-> "the interaction was captured successfully"

LEVEL 1–2
-> internal stimulus-development evidence only

LEVEL 3–4
-> "this pair elicited a reproducible response pattern in this study"
   only if justified; no person characteristic claim

Gate D VALIDATED
-> exemplar-specific directional language may become technically possible,
   subject to final claim contract and uncertainty boundary

Gate E VALID
-> candidate-domain aggregate language may become technically possible,
   subject to separate claim review

Reflection utility supported
-> may claim evidence that the process supports self-observation,
   without converting that into a personality claim
```

No stage authorizes diagnosis, personality classification or behavioral prediction.

---

## 20. Failure is preserved as data

Following the GERT-style item-development lesson, candidate stimuli are expendable.

When a pair/family fails:

- preserve the exact failed version;
- preserve the reason for failure;
- do not overwrite the historical verdict;
- any redesign receives a new version/identity;
- a redesigned descendant does not retroactively validate the failed ancestor.

A surviving library should represent items that earned survival, not items protected by design attachment.

---

## 21. Immediate implementation sequence

This protocol now becomes the parent methodology document for the next artifacts:

```text
1. GATE_D_VALIDATION_CONTRACT_v0.1
2. GATE_E_VALIDATION_CONTRACT_v0.1
3. RESEARCH_DATA_AND_CONSENT_SCOPE_v0.1
4. blind-alias / validation dataset specification
5. experiment-specific preregistration records
```

Do not modify participant scoring while these are being specified.

Do not promote Gate D or Gate E.

Do not switch public `/wave1/`.

Keep current server collection mode `TECHNICAL` until the next fresh-participant collection protocol and data scope are explicitly frozen.

---

## 22. Bottom-line methodological position

ConflictLab should not try to prove that its designers were right about CS/CR.

It should create a sequence in which:

```text
a candidate theory proposes a contrast
↓
a stimulus attempts to instantiate it
↓
confounds try to defeat it
↓
blind human evidence challenges the designer interpretation
↓
response reproducibility is tested against nuisance variance
↓
Gate D may validate or kill the pair
↓
multiple surviving pairs face Gate E
↓
reflection usefulness is tested independently
↓
only the surviving evidence determines what may be said to a participant
```

The methodological success criterion is therefore not "every candidate domain survives".

It is:

> the system can tell the difference between an attractive hypothesis and one that survives independent empirical challenge.