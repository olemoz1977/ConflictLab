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

Created initially:

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

## EU data-protection baseline and DPIA gate

After reviewing current European Commission, EDPB and Lithuanian VDAI guidance, the project adopted a conservative privacy-by-design baseline:

`docs/architecture/EU_DATA_PROTECTION_BASELINE_v0.1.md`

and a DPIA screening gate:

`docs/architecture/DPIA_SCREENING_v0.1.md`

Key decisions:

- event-level research records are treated as pseudonymous personal data, not automatically anonymous data;
- no direct identifiers are needed for the current method-validation program;
- server-side open free text is prohibited by default for the next beta;
- no special-category data are intentionally collected;
- no third-party non-essential analytics/marketing tracking is authorized;
- external research beta is 18+ only;
- Hostinger processor/DPA, actual hosting region, subprocessors/transfers and security boundary must be documented before real participant upload;
- participant/controller identity and contact must be real and transparent in the privacy notice;
- a DPIA-style assessment is an internal gate before Gate D/E behavioural research even if a later qualified legal opinion concludes that a statutory Article 35 DPIA is not mandatory at current scale;
- behavioural research consent is not a blanket permission to collect future-use data.

## Conservative next-study privacy decision

A stricter scope was created for the next external participant cycle:

`docs/architecture/RESEARCH_DATA_AND_CONSENT_SCOPE_v0.2.md`

Decision:

```text
NEXT EXTERNAL SERVER STUDY = TIMING / UX MECHANICS ONLY
```

The server may collect only the minimum pseudonymous timing/completion payload needed by `timing-calibration-v1` plus purpose/version/consent provenance.

For that next study the server must not collect:

```text
names / emails / employer
open reflection text
reason_id
intensity
reason or intensity response latency
persistent participant identifier
participant psychological/directional result
```

The product-shaped reflection flow may still operate locally, but reflection content must not enter the research database or routine telemetry.

Gate D, Gate E and reflection-content research are now explicitly separate future studies requiring their own preregistration, privacy notice/purpose, DPIA update, payload and retention decision.

This supersedes the earlier operational possibility of combining timing plus behavioural-validation server collection in the first external participant cycle.

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

## Methodology and compliance sequence status

Completed:

1. `VALIDATION_PROTOCOL_v0.1`
2. `GATE_D_VALIDATION_CONTRACT_v0.1`
3. `GATE_E_VALIDATION_CONTRACT_v0.1`
4. `RESEARCH_DATA_AND_CONSENT_SCOPE_v0.1`
5. `EU_DATA_PROTECTION_BASELINE_v0.1`
6. `DPIA_SCREENING_v0.1`
7. `RESEARCH_DATA_AND_CONSENT_SCOPE_v0.2`

Before first real external timing participant:

1. freeze actual data-controller identity/contact;
2. freeze participant privacy notice and timing-research consent copy;
3. document lawful basis for technical/security processing and timing research;
4. freeze concrete retention/deletion rule;
5. review Hostinger DPA, actual hosting region and subprocessor/transfer route;
6. implement/verify withdrawal/deletion mechanism without unnecessary direct identifiers;
7. confirm non-essential trackers are OFF;
8. harden/document admin/export security;
9. finish timing-study DPIA screening/mitigations;
10. only then authorize switch from `TECHNICAL` to timing `CALIBRATION`.

The next fresh-participant study must remain mechanically scoped and must not later be repurposed as Gate D/E evidence.