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

## Next methodology sequence

1. `VALIDATION_PROTOCOL_v0.1`
2. `GATE_D_VALIDATION_CONTRACT_v0.1`
3. `GATE_E_VALIDATION_CONTRACT_v0.1`
4. research data / consent scope decision

The next protocol must define a real route to `FAIL` / `SUSPEND`, not only `PENDING` / `VALIDATED`.
