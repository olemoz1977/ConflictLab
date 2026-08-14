# ConflictLab — Theory-to-Validation Matrix v0.1

**Status:** methodological working baseline  
**Purpose:** clarify which theoretical lenses can legitimately inform ConflictLab, which validation disciplines are still missing, and what can be learned from GERT and AgileBrain without importing their claims as proof.  
**Context:** created after the four-model independent review synthesis.

> Core decision: the historical 14-theory package is useful but **not sufficient as the complete methodological foundation**. It was primarily an interpretive/human-behaviour lens library. The current research risks require a separate measurement/validation stack.

---

## 1. Three distinct libraries — do not merge them

ConflictLab should maintain three conceptually separate registries:

```text
A. HUMAN / BEHAVIOURAL LENSES
   -> generate hypotheses, alternative explanations, boundaries

B. VALIDATION / MEASUREMENT METHODS
   -> determine whether an observation or mapping survives empirical challenge

C. REFERENCE INSTRUMENTS / PRODUCTS
   -> show practical design and validation precedents
```

A theory or product may inspire a hypothesis. It does not validate a ConflictLab mapping by analogy.

---

## 2. Historical 14-theory package — current role

Source: archived `Model Transparency Principle v0.4`.

| Framework | Current useful role | Current validation status / caution |
|---|---|---|
| Transactional Analysis | later interpersonal/context interpretation | CONTEXT ONLY; not a stimulus-mapping method |
| Karpman Drama Triangle | later conflict-role dynamics / possible contextual confound | CONTEXT ONLY; not Gate D evidence |
| Polyvagal Theory | possible autonomic-state hypothesis generator | HOLD / CONTESTED; do not use as core validation foundation |
| SCARF | strong confound lens for status, certainty, autonomy, relatedness, fairness | USEFUL CONFOUND LENS |
| Attachment Theory | relational/social stimulus confound lens | USEFUL FOR SOCIAL-STIMULUS AUDIT |
| Cognitive Distortions | language/interpretation confound lens; reflection wording | SECONDARY; not visual-domain proof |
| Locus of Control | agency/control alternative explanation | USEFUL CONFOUND LENS |
| Schema Theory | individual-history / prior-experience alternative explanation | USEFUL BOUNDARY LENS |
| Dual Process Theory | rationale for minimizing deliberative self-presentation | CORE CAPTURE HYPOTHESIS, but exact timing must be empirically tested |
| Nonviolent Communication | dialogue/reflection language discipline | PRODUCT/DIALOGUE ONLY |
| Thomas-Kilmann Conflict Model | later conflict-context lens | CONTEXT ONLY |
| Self-Determination Theory | candidate autonomy/structure rationale; CR alternative explanations | CANDIDATE CONSTRUCT RATIONALE, not mapping proof |
| Gross Emotion Regulation Model | response-strategy / post-choice explanation lens | USEFUL ALTERNATIVE EXPLANATION |
| Constructed Emotion Theory | guardrail against treating visible/selected emotion as fixed universal meaning | CORE NON-INFERENCE GUARDRAIL |

### 2.1 Conclusion about the 14

The package is not weak because it has only 14 entries. It is incomplete because most entries answer:

> "What human process could explain this reaction?"

while the four independent reviews exposed a different class of questions:

> "How do we know the stimulus manipulation is what we think it is?"  
> "How do we separate intended construct from visual salience/confounds?"  
> "What evidence is allowed to validate Gate D/E?"  
> "What observation forces the hypothesis to fail?"

Those are measurement and experimental-design questions, not additional personality theories.

---

## 3. Foundations already used by current ConflictLab but outside the old 14

`WHY_CONFLICTLAB.md` already relies on frameworks that were not part of the archived 14-model registry.

| Foundation | Present role | Needed caution |
|---|---|---|
| Cognitive Appraisal (Lazarus) | candidate response-orientation rationale | broad explanatory lens; can become circular if used to label its own stimuli |
| Predictive Processing | uncertainty/ambiguity rationale; rapid interpretation | theoretical plausibility only; does not prove CS mapping |
| Epistemology | observation ≠ knowledge; fail-closed inference boundary | governance principle rather than empirical construct validation |
| Reflective Practice (Schön) | reflection ends in a question, not diagnosis | validates reflection design rationale, not stimulus meaning |
| Active Inference | repeated-hypothesis / longitudinal rationale | broad; avoid using as post-hoc explanation for any pattern |
| Motivational Interviewing elements | micro-dialogue style, autonomy-preserving language | dialogue method only |
| Evidence-Based Reasoning | evidence/provenance discipline | methodological governance; needs operational contracts |

**Implication:** the real methodological ecosystem was already larger than 14 before the independent audits.

---

## 4. Missing validation disciplines — the important expansion

Do **not** respond to audit risk by adding more interpretive psychology. Add the disciplines that can make the hypotheses fail.

### V1. Modern construct-validity / psychometrics

Purpose:
- distinguish reliability from validity;
- specify convergent, discriminant, criterion and structural evidence;
- prevent "internally coherent = valid" reasoning.

Use for:
- Gate D evidence architecture;
- Gate E aggregation evidence;
- deciding what claims the data support.

### V2. Experimental design: randomization, counterbalancing, controls

Purpose:
- isolate position, order, form, training and repeated-exposure effects;
- define null/control conditions;
- distinguish manipulation from procedural artifact.

Use for:
- 6000 ms protocol;
- top/bottom effects;
- F2-A/F2-B equivalence;
- training-transfer experiments.

### V3. Visual psychophysics / perceptual-confound measurement

Purpose:
- quantify or experimentally control luminance, contrast, edge density, spatial frequency, complexity, salience, symmetry, size and visual load;
- test whether a low-level visual model predicts choice better than intended semantic manipulation.

Use for:
- Confound Register;
- stimulus exclusion/redesign;
- blind perceptual-rating studies.

### V4. Qualitative content analysis + inter-rater agreement

Purpose:
- code spontaneous reason language without designer-domain leakage;
- separate domain-relevant language from aesthetics, utility, salience, familiarity and other alternatives;
- quantify coder agreement.

Use for:
- Gate D candidate evidence;
- reason-map validation;
- blind coding.

### V5. Generalizability / variance-component thinking

Purpose:
- separate variance attributable to participant, pair, family, form, position, device, session and their interactions;
- prevent pair- or form-specific effects from being misnamed as person signal.

Use for:
- deciding whether cross-exemplar aggregation is even plausible;
- identifying dominant nuisance variance before Gate E.

### V6. Paired-comparison / forced-choice measurement

Purpose:
- treat A/B response first as comparative choice data rather than an immediate latent-trait score;
- estimate base preferences and item effects before psychological interpretation.

Use for:
- pair-level descriptive modeling;
- testing whether one variant dominates population choice independent of participant differences.

### V7. Open-science / preregistration discipline

Purpose:
- freeze hypotheses, exclusion rules, Gate D/E evidence criteria and terminal FAIL/SUSPEND conditions before target data are inspected;
- convert researcher degrees of freedom into versioned decisions.

Use for:
- every confirmatory Gate D / Gate E cycle.

### V8. Convergent / discriminant multi-method validation

Purpose:
- test whether candidate domains relate to independent measures in theoretically expected ways while remaining distinguishable from neighboring constructs and simple visual preferences.

Important:
- external instruments must not redefine ConflictLab as a personality test;
- external correlations are evidence about construct relations, not identity claims.

---

## 5. Conditional methods — useful later, not automatically applicable now

### Item Response Theory / Rasch

Potential value:
- item difficulty/discrimination analysis;
- principled stimulus pruning;
- information/precision assessment.

But:
- GERT has an externally defined correct target emotion for each portrayal;
- ConflictLab currently has no correct/incorrect response and Gate D is empty;
- applying Rasch/IRT before a defensible latent-variable model would merely formalize an unvalidated construct.

Decision: **METHOD CANDIDATE AFTER Gate D/Gate E assumptions become empirically defensible, not a current Gate D shortcut.**

---

## 6. Practical reference instrument: GERT

**Geneva Emotion Recognition Test (GERT)** is not a theoretical basis for ConflictLab. It is a useful methodological contrast/reference.

Relevant design lessons:

1. GERT treats stimulus development as a psychometric item-development problem, not merely a content-design problem.
2. Candidate items were empirically screened and a subset retained using a formal measurement model.
3. Stimulus identity and target category are explicit; item quality can therefore be tested against a known task definition.
4. Dynamic multimodal portrayals improve ecological coverage for an emotion-recognition task.

ConflictLab-specific lesson:

```text
GERT shows:
large candidate pool
-> empirical item testing
-> model-based item pruning
-> retained validated item set
```

This is highly relevant to how ConflictLab should think about stimulus families: **do not fall in love with six designed pairs; expect candidates to fail and be removed.**

Do **not** import:
- GERT correct/incorrect scoring;
- emotion-recognition semantics;
- assumption that a participant response has a known target label.

In fact, current ConflictLab intentionally avoids explicit human emotional expressions because that would risk turning the task into emotion recognition rather than observing reaction to scene properties.

---

## 7. Practical reference instrument: AgileBrain

AgileBrain is a closer practical analogue to the capture idea:

- image-based rather than purely verbal;
- rapid-exposure / rapid-response;
- brief, gamified participant experience;
- defined image-to-need model;
- published validation work compares its outputs with established wellbeing/clinical/self-report indicators across multiple large samples.

Useful methodological lessons:

### 7.1 Rapid image selection is empirically testable

The practical precedent supports the *researchability* of a brief image-selection protocol. It does not validate ConflictLab's specific domains or timing.

### 7.2 External validation matters

AgileBrain's published work does not stop at internal choice consistency; it evaluates relations with external measures across multiple datasets. ConflictLab therefore should not treat Gate E internal coherence as the final validity argument.

### 7.3 Multiple samples / replication matter

A single attractive pilot pattern is not enough. Confirmation should survive new samples and, ideally, independent replication.

### 7.4 Image semantics still require proof

AgileBrain explicitly maps images to a defined needs framework. ConflictLab must not infer that because another system successfully uses image mapping, ConflictLab's CS/CR image mappings are therefore valid.

### 7.5 Independence caution

At least one recent AgileBrain validation paper was authored by the tool's developer/employee. It is useful peer-reviewed evidence and a methodological precedent, but it should not be treated as independent validation of all AgileBrain claims.

Decision: **REFERENCE INSTRUMENT / METHODS PRECEDENT, not imported evidence.**

---

## 8. What the two practical inspirations add to ConflictLab

GERT and AgileBrain point in complementary directions:

```text
GERT
-> rigorous item/stimulus development
-> candidate items may fail
-> formal psychometric pruning

AgileBrain
-> rapid image-based capture is practical
-> validate against independent external criteria
-> use repeated large samples / cross-validation
```

ConflictLab's distinctive contribution should not be "images can measure hidden psychology".

A safer research proposition is:

> A controlled image contrast can elicit a reproducible response. Whether that response supports a specific candidate domain must be established through independent semantic evidence, confound challenge, repeated observations and explicit evidence gates.

---

## 9. Theory-to-audit-risk map

| Four-review consensus risk | Existing useful lenses | Missing methodological control |
|---|---|---|
| Circularity / construct-definition loop | Epistemology, Constructed Emotion, Cognitive Appraisal | blind validation, construct-validity framework, preregistration |
| Visual confounds | SCARF, Attachment, Locus of Control, SDT as semantic alternatives | visual psychophysics, controlled/null conditions |
| Gate D under-specified | Evidence-Based Reasoning | Gate D validation contract, blind qualitative coding |
| Gate E under-specified | none of the 14 is sufficient | generalizability/variance analysis, convergent-discriminant validation |
| Structured reason post-hoc coherence | Cognitive Distortions, Reflective Practice, Gross ER | spontaneous-language condition, blind content analysis, experimental reason-map test |
| Researcher degrees of freedom | Epistemology / model transparency | preregistration, immutable versions, terminal FAIL/SUSPEND states |
| Shared timing-budget contamination | Dual Process gives rationale only | counterbalancing, experimental timing design, HCI telemetry |
| Training strategy transfer | Dual Process / Gross ER can generate hypotheses | randomized training conditions, variance analysis |
| F2-A/F2-B equivalence | none | form-equivalence / variance-component analysis |
| Position bias | none | paired-comparison / randomized counterbalancing |

---

## 10. Proposed evidence stack

The project should no longer have one vague concept called "validation".

```text
LEVEL 0 — TECHNICAL INTEGRITY
assets, timing, event provenance, reproducibility

LEVEL 1 — SCENE MANIPULATION INTEGRITY
is the intended visible contrast actually present?

LEVEL 2 — PERCEPTUAL CONFOUND CHALLENGE
can luminance/salience/complexity/aesthetics/position explain choice more simply?

LEVEL 3 — BLIND SEMANTIC EVIDENCE
without domain labels, what do independent raters / spontaneous participant reasons say the contrast is about?

LEVEL 4 — RESPONSE REPRODUCIBILITY
is response structure distinguishable from random, position, form, device and training effects?

LEVEL 5 — GATE D
is a pair-level directional mapping defensible under a pre-frozen contract?

LEVEL 6 — GATE E
can multiple independently surviving exemplars be aggregated without a shared-confound explanation?

LEVEL 7 — REFLECTION UTILITY
regardless of trait validity, does the experience actually improve self-observation compared with an appropriate control?

LEVEL 8 — CLAIM BOUNDARY
what participant-facing statement is supported, and what remains forbidden?
```

---

## 11. Decision about "do 14 theories suffice?"

**No.**

But the correct response is **not** to build a 30-theory interpretation engine.

The historical 14 should become a bounded **Human Lens Library**. Only the lenses that generate a specific pre-data hypothesis or alternative explanation should be activated for a given experiment.

Create a separate **Validation Method Library** for measurement science and experimental controls.

Treat **GERT and AgileBrain as Reference Instruments**, not theoretical authorities.

This prevents two opposite failures:

1. **theory poverty** — weak assumptions with no scientific anchors;
2. **theory shopping** — enough frameworks to explain any result after the fact.

---

## 12. Immediate next artifacts

Use this matrix to create, in order:

1. `CONFOUND_REGISTER_v0.1`
2. `VALIDATION_PROTOCOL_v0.1`
3. `GATE_D_VALIDATION_CONTRACT_v0.1`
4. `GATE_E_VALIDATION_CONTRACT_v0.1`
5. research collection / consent scope

Do not add new participant scoring during this phase.
Do not promote Gate D/E.
Do not change public `/wave1/`.
Keep current server mode `TECHNICAL` until the next fresh-participant protocol is frozen.
