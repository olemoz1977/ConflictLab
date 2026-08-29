# ConflictLab — Confound Register v0.1

**Status:** DRAFT / pre-data risk register  
**Purpose:** pre-specify alternative explanations that could account for participant responses before Gate D/E validation.  
**Rule:** a listed confound is a hypothesis to challenge, not a finding that the current stimulus is invalid.

> A simpler alternative explanation must be tested before a psychological/domain explanation is promoted.

---

## 1. Use of this register

For every candidate pair / family, reviewers must record:

```text
confound_id
relevance: NONE | LOW | MEDIUM | HIGH | UNKNOWN
why_relevant
measurement_or_control
result
impact_on_gate: NONE | BLOCK | REDESIGN | SUSPEND
reviewer_blinded_to_domain: yes/no
```

No post-data invention of a new confound may be used to rescue a failed mapping without creating a new protocol/version and retest.

---

## 2. Perceptual / visual confounds

### P01 — Luminance / brightness
Alternative explanation: participant selects the brighter/darker image independently of intended semantic manipulation.

Test/control candidates:
- image-level luminance statistics;
- blind human brightness ratings;
- controlled variants if needed.

Gate relevance: Gate D.

### P02 — Contrast / local contrast
Alternative explanation: higher visual contrast or sharper local boundaries create salience/ease-of-parse preference.

Test/control candidates:
- contrast metrics;
- blind perceptual ratings;
- matched contrast variants.

Gate relevance: Gate D.

### P03 — Visual complexity / edge density / spatial frequency
Alternative explanation: choice follows perceptual simplicity or complexity rather than candidate domain.

Test/control candidates:
- objective complexity proxies;
- blind complexity ratings;
- compare whether complexity predicts choice across families.

Gate relevance: Gate D and Gate E.

### P04 — Symmetry / balance / composition
Alternative explanation: image composition or visual balance drives aesthetic preference.

Test/control candidates:
- symmetry/composition audit;
- blind aesthetic/composition ratings.

Gate relevance: Gate D.

### P05 — Size / focal dominance / center-of-mass
Alternative explanation: larger, nearer, more central or more dominant object is selected because it attracts attention.

Test/control candidates:
- bounding-box/focal-area comparison;
- center-of-mass / salience analysis;
- controlled focal variants.

Gate relevance: Gate D.

### P06 — Completeness / reveal / legibility
Alternative explanation: more complete or more legible visual information is preferred because it is easier to parse, not because of CS-related response.

This is especially important for candidate reveal/visibility families because perceptual ease can be structurally aligned with designer intent.

Test/control candidates:
- independent legibility/ease ratings;
- control contrasts where completeness changes without the intended domain interpretation.

Gate relevance: Gate D / high priority.

### P07 — Colour / colour temperature
Alternative explanation: warmer/cooler or more saturated image is preferred independently of intended manipulation.

Test/control candidates:
- colour statistics;
- matched-colour variants where feasible.

Gate relevance: Gate D.

### P08 — Rendering / compression / file-format artifact
Alternative explanation: visible compression, scaling or rendering differences affect perceived quality.

Important: different file extensions alone are **not evidence** of a confound. Only visible/rendered differences matter.

Test/control candidates:
- exact rendered comparison at target viewport;
- asset quality audit;
- standardized deployment rendering where needed.

Gate relevance: technical integrity / Gate D if visible.

---

## 3. Semantic / contextual confounds

### S01 — Aesthetic preference
Alternative explanation: participant simply likes one visual style more.

Test/control candidates:
- separate aesthetic-preference rating;
- compare aesthetic rating with choice.

### S02 — Utility / functional affordance
Alternative explanation: one scene appears more practical, efficient, usable or sensible.

Relevant lenses:
- Self-Determination Theory (autonomy/constraint as alternative, not proof);
- Locus of Control / agency.

### S03 — Familiarity / prior exposure
Alternative explanation: participant chooses what is more familiar or culturally typical.

Relevant lenses:
- Schema Theory;
- prior-experience metadata only if ethically/operationally justified.

### S04 — Positive/negative valence or desirability
Alternative explanation: one variant appears safer, better, healthier, more professional or socially desirable.

Control:
- Equal Legitimacy audit;
- blind valence/desirability ratings.

### S05 — Threat / safety
Alternative explanation: perceived threat or security drives the choice.

Relevant lenses:
- Cognitive Appraisal;
- SCARF where social;
- do not infer autonomic state from choice.

### S06 — Agency / control
Alternative explanation: participant prefers greater personal control/agency rather than candidate CS/CR semantics.

Relevant lenses:
- Locus of Control;
- Self-Determination Theory.

### S07 — Social status / relatedness / fairness / autonomy cue
Alternative explanation: social cue activates SCARF-like response dimensions.

Relevant lens:
- SCARF as confound generator, never Gate D proof.

### S08 — Attachment / relational cue
Alternative explanation: interpersonal distance/availability activates relational history rather than intended domain.

Relevant lens:
- Attachment Theory.

### S09 — Cultural convention
Alternative explanation: scene meaning depends on learned cultural convention.

Test/control candidates:
- independent semantic ratings across relevant language/cultural groups when required;
- avoid assuming cross-cultural invariance from image-only presentation.

---

## 4. Procedural confounds

### R01 — Top / bottom position bias
Alternative explanation: participant systematically selects the first/top or second/bottom option.

Control:
- randomize/counterbalance positions;
- retain exact position telemetry;
- analyze same asset across both positions.

Gate relevance: timing + Gate D.

### R02 — Serial position / shared-budget depletion
Alternative explanation: P2/P3 response opportunity depends on time spent on earlier pairs.

Control:
- preserve pair position and remaining-budget telemetry;
- timing decision rule remains mechanical only;
- consider explicit counterbalanced/per-pair-budget experiment if shared-budget contamination cannot be separated.

Gate relevance: timing calibration / high priority.

### R03 — Training strategy transfer
Alternative explanation: training teaches pacing, rushing, or "save time for P3" strategy rather than only interaction familiarity.

Control candidates:
- compare training and measured latency patterns;
- experimentally compare training timing variants if required.

### R04 — Form composition (F2-A / F2-B)
Alternative explanation: observed domain difference is actually exemplar/form difference.

Control:
- preserve form identity;
- do not assume form equivalence;
- Gate E requires explicit treatment of form/exemplar variance.

### R05 — Device / input modality
Alternative explanation: touch vs mouse/trackpad changes response latency or accidental-choice rate.

Control:
- retain coarse device category;
- timing comparisons are mechanical, not psychological.

### R06 — Rendering / preload readiness
Alternative explanation: participant saw one option later or interacted before full visual readiness.

Control:
- exact preload/decode requirement;
- response activation only after both options are ready.

### R07 — Repeated exposure / memory
Alternative explanation: second exposure reflects recognition/memory rather than the same spontaneous process.

Control:
- primary attempt only for directional/timing evidence;
- retries remain diagnostic;
- longitudinal design must distinguish novel vs repeated assets.

### R08 — Fatigue / attention drift
Alternative explanation: later responses differ because of fatigue or reduced attention.

Control candidates:
- short sessions;
- position diagnostics;
- page visibility rules;
- do not infer psychological meaning from slowing alone.

---

## 5. Reflection / reason-stage confounds

### Q01 — Prompt-induced convergence / demand characteristic
Alternative explanation: structured reason options tell participants how to explain a choice.

Control candidates:
- blind reason-content audit;
- spontaneous/open reason condition;
- structured-vs-open experimental comparison.

Gate relevance: Gate D / high priority.

### Q02 — Post-hoc rationalization
Alternative explanation: participant constructs a plausible explanation after an intuitive/random/aesthetic choice.

Relevant lenses:
- Dual Process as hypothesis generator;
- Cognitive Distortions / Constructed Emotion as non-inference guards.

Rule:
- selected reason class is never causal proof.

### Q03 — Option-set coverage / wording bias
Alternative explanation: participant chooses the least-bad available phrase rather than a true reason.

Control:
- "another reason" path;
- blind content review;
- coverage analysis before reason class is used as evidence.

### Q04 — Free-text missingness / self-selection
Alternative explanation: only more articulate/motivated participants provide usable open reasons.

Control:
- report missingness separately;
- do not treat non-response as a domain signal.

### Q05 — Intensity anchoring / scale-use style
Alternative explanation: 1–5 ratings reflect individual scale-use habits more than reaction magnitude.

Rule:
- intensity remains independent self-report;
- never enters Directional Balance.

---

## 6. Individual-difference nuisance factors

These may matter without being targets of measurement.

### I01 — Stable aesthetic preference
A participant may repeatedly choose simpler, more open, more symmetrical or more saturated images.

Risk:
- creates apparent cross-exemplar consistency without candidate-domain mechanism.

Gate E relevance: very high.

### I02 — Visual processing speed
Risk:
- latency differences may reflect perceptual/motor processing speed rather than decision process.

Rule:
- latency has no psychological meaning without separate validation.

### I03 — Prior experience / schema
Risk:
- scene-specific familiarity changes interpretation.

Relevant lens:
- Schema Theory.

### I04 — Accessibility / vision / display conditions
Risk:
- visual impairment, screen quality, scaling or environment affects perceptibility.

Treatment:
- technical/eligibility consideration, not person interpretation.

---

## 7. Researcher / analysis confounds

### X01 — Designer-domain label leakage
Risk:
- IDs such as `CS-*` / `CR-*` prime blind coders or analysts.

Control:
- preserve canonical IDs for provenance;
- use neutral aliases in blinded validation datasets/interfaces.

### X02 — Post-hoc threshold selection
Risk:
- PASS/FAIL rules chosen after seeing data can manufacture apparent validation.

Control:
- freeze Gate D/E contracts before target data.

### X03 — Post-hoc pair exclusion
Risk:
- remove only pairs that contradict intended domain and keep supportive pairs.

Control:
- pre-specified exclusion categories;
- failed pairs remain in provenance with FAILED/SUSPENDED state.

### X04 — Unblinded qualitative coding
Risk:
- coder knows pair family/direction and interprets free text accordingly.

Control:
- neutral aliases;
- blind coding;
- disagreement tracking / inter-rater agreement.

### X05 — Version pooling
Risk:
- combine data from materially different stimulus/protocol versions.

Control:
- version-specific datasets;
- explicit pooling contract only when equivalence is defensible.

### X06 — Flexible stopping / sample expansion
Risk:
- stop or continue collection depending on whether emerging pattern looks favorable.

Control:
- pre-specified data floor/stopping logic appropriate to each study question;
- timing-calibration floor must not be reused as construct-validity floor.

---

## 8. Gate-specific minimum challenge set

### Before Gate D can validate a pair

At minimum address:

```text
P01-P08 perceptual risks as relevant
S01-S09 semantic alternatives as relevant
R01 position
Q01-Q04 reason-stage risks if reasons enter evidence
X01-X04 researcher/coding risks
```

A pair may remain `NONE` or become `SUSPENDED`; validation is not mandatory.

### Before Gate E can validate aggregation

At minimum address:

```text
shared perceptual confounds across exemplars
I01 stable aesthetic preference
R04 form composition
version effects
cross-domain discriminant evidence
participant × pair/family variance
```

Gate E may legitimately remain `NONE` permanently for a stimulus set.

---

## 9. Relation to GERT and AgileBrain

### GERT lesson

Treat candidate stimuli as expendable items. Empirical item development must be able to remove attractive but poorly functioning stimuli.

### AgileBrain lesson

A rapid image-based protocol should ultimately be challenged against independent external criteria and repeated samples rather than validated by internal coherence alone.

Neither reference instrument resolves the confounds above for ConflictLab.

---

## 10. Next use

This register is an input to:

- `VALIDATION_PROTOCOL_v0.1`
- `GATE_D_VALIDATION_CONTRACT_v0.1`
- `GATE_E_VALIDATION_CONTRACT_v0.1`

No numeric construct-validity thresholds are set here. Thresholds must be justified for the specific validation design before confirmatory data are inspected.
