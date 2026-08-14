# 2026-08-15 — Independent review synthesis and validation-method stack

## Scope

This record captures the methodological state transition after four independent adversarial AI reviews (Claude, Gemini, Grok, Kimi K3) of frozen target `983923243a941b85171f42f0bb973b16a0a55364`.

## Review outcome

The reviews converged on the same high-priority risks:

- circularity / construct-definition loop;
- uncontrolled visual confounds;
- Gate D under-specification;
- Gate E under-specification;
- structured reason-map / post-hoc coherence risk;
- researcher degrees of freedom;
- shared 6000 ms serial-position contamination.

The reviews also converged that the technical fail-closed architecture is defensible while current directional CS/CR interpretation is not validated.

Synthesis:

`docs/review/INDEPENDENT_REVIEW_SYNTHESIS_v0.1.md`

## Theory-package decision

The archived 14-model `ModelRegistry` is **not sufficient as the complete research methodology**.

This does not mean the project needs more interpretive psychology.

The old 14 are now classified primarily as a bounded `Human Lens Library`:

- hypothesis generation;
- alternative explanations;
- semantic/context confound lenses;
- reflection/dialogue boundaries.

They are not allowed to serve as automatic Gate D/E evidence.

The current project already uses additional foundations outside the old 14, including Cognitive Appraisal, Predictive Processing, Epistemology, Reflective Practice, Active Inference, Motivational Interviewing elements and Evidence-Based Reasoning.

The missing layer identified by the audits is measurement/validation methodology:

- construct validity / psychometrics;
- experimental design / counterbalancing / controls;
- visual psychophysics / perceptual-confound measurement;
- qualitative content analysis and inter-rater agreement;
- variance/generalizability analysis;
- paired-comparison / forced-choice measurement;
- preregistration / open-science discipline;
- convergent/discriminant multi-method validation.

Matrix:

`docs/architecture/THEORY_TO_VALIDATION_MATRIX_v0.1.md`

## GERT reference decision

GERT is treated as a **reference instrument**, not a theoretical authority for ConflictLab.

Relevant lesson:

- candidate stimuli are psychometric items;
- attractive candidate items may fail;
- empirical item testing and formal item pruning matter;
- a final item set should be earned by evidence, not design confidence.

ConflictLab must not import GERT correct/incorrect scoring or emotion-recognition semantics.

## AgileBrain reference decision

AgileBrain is treated as a **reference instrument / methods precedent**, not imported evidence for ConflictLab.

Relevant lessons:

- brief rapid image-based capture is an empirically researchable format;
- internal consistency is not enough;
- external convergent/discriminant validation and replication across samples matter;
- image-to-construct mapping still needs its own evidence.

Caution retained: at least one recent peer-reviewed AgileBrain validation publication was authored by the product's developer/employee, so it is useful evidence and precedent but not independent validation of all product claims.

## Confound register

A pre-data confound registry was created:

`docs/architecture/CONFOUND_REGISTER_v0.1.md`

It separates:

- perceptual/visual confounds;
- semantic/contextual confounds;
- procedural confounds;
- reflection/reason confounds;
- individual nuisance factors;
- researcher/analysis confounds.

No arbitrary construct-validity thresholds are frozen in this register.

## Architectural decision

Maintain three separate conceptual registries:

```text
Human / Behavioural Lenses
Validation / Measurement Methods
Reference Instruments / Products
```

Do not collapse them into one ModelRegistry.

This is intended to prevent both:

- theory poverty;
- theory shopping / post-hoc rescue.

## Validation protocol completed

Created:

`docs/architecture/VALIDATION_PROTOCOL_v0.1.md`

It separates four research programs:

```text
TIMING CALIBRATION
GATE D VALIDATION
GATE E VALIDATION
REFLECTION UTILITY
```

It also introduces an explicit evidence ladder:

```text
technical integrity
-> scene manipulation integrity
-> confound challenge
-> blind semantic evidence
-> response/nuisance challenge
-> Gate D
-> Gate E
-> reflection utility / claim boundary
```

The protocol explicitly preserves terminal negative outcomes:

```text
FAILED
SUSPENDED
REDESIGN_REQUIRED
INSUFFICIENT_DATA
```

No stage may be rescued by changing decision rules after target data have been inspected; such a change creates a new protocol/version and a new confirmatory cycle.

## Gate D contract completed

Created:

`docs/architecture/GATE_D_VALIDATION_CONTRACT_v0.1.md`

Key decision:

Gate D is exact-pair / exact-asset / exact-version validation only. It requires independent/blinded evidence, confound challenge and a frozen study registration before participant data may produce a `VALIDATED` mapping.

Current structured `reason-map-v1` is not sufficient Gate D evidence by itself.

Failed pairs remain preserved in provenance and runtime mapping remains `NONE`; they are not silently deleted or returned to indefinite `PENDING`.

## Gate E contract completed

Created:

`docs/architecture/GATE_E_VALIDATION_CONTRACT_v0.1.md`

Key decision:

Gate E may only be asked after multiple independent Gate-D-surviving exemplars exist.

Aggregation must survive:

- shared-confound challenge;
- exemplar/form/version effects;
- participant × exemplar nuisance variance;
- discriminant challenge against a simpler common factor;
- independent confirmation/replication appropriate to the intended claim.

Gate E may legitimately remain `NONE` permanently. If aggregation fails but exemplar-specific reflection remains useful, the product may continue without a domain score.

## Research data / consent scope completed

Created:

`docs/architecture/RESEARCH_DATA_AND_CONSENT_SCOPE_v0.1.md`

Research purposes are separated as:

```text
TECHNICAL
TIMING_CALIBRATION
GATE_D_VALIDATION
GATE_E_VALIDATION
REFLECTION_RESEARCH
```

Core boundary:

consent to mechanical timing research is not automatic consent to construct validation or reflection-text research.

Current local-first safeguards remain:

```text
training server upload = false
free text = local-first by default
reason_id server collection = explicit research consent only
intensity = outside directional balance and current timing payload
reason/intensity response latency = local-only in current pilot
derived participant result = not research upload
```

No database payload expansion is authorized until the relevant research purpose and participant consent/disclosure are frozen.

## Current safety state

Unchanged:

```text
collection_mode              TECHNICAL
Gate D                       NONE
Gate E                       NONE
participant directional result NOT AUTHORIZED
public /wave1                UNCHANGED
```

No public switch or construct claim was authorized by this methodological work.

## Methodology sequence status

Completed:

1. `VALIDATION_PROTOCOL_v0.1`
2. `GATE_D_VALIDATION_CONTRACT_v0.1`
3. `GATE_E_VALIDATION_CONTRACT_v0.1`
4. `RESEARCH_DATA_AND_CONSENT_SCOPE_v0.1`

Next:

1. neutral alias / blind-validation dataset specification;
2. first study-specific preregistration;
3. participant information / consent wording for the chosen study;
4. authenticated admin CSV export implementation/documentation;
5. only then decide whether the next fresh-participant cycle is timing-only or timing + separately consented validation research.

The next fresh-participant study must be able to produce a real negative methodological result that remains negative for that exact protocol/version.