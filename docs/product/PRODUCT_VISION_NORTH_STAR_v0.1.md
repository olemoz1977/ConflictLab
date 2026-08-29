# ConflictLab — Product Vision North Star v0.1

**Date:** 2026-08-15  
**Status:** PRODUCT DIRECTION BASELINE  
**Scope:** product purpose and invariants only. This document does **not** freeze the current research protocol, stimulus set, domains, scoring architecture, backend, hosting provider, or UI implementation.

---

## 1. North Star

> **Mes nepadedame žmogui greičiau suprasti save. Mes padedame jam išmokti geriau stebėti save.**

ConflictLab exists to help a person notice recurring patterns in their own reactions without turning those observations into a personality label, diagnosis, verdict, or predetermined identity claim.

The desired participant reaction is not:

> „Dabar žinau, koks esu.“

It is closer to:

> „Keista... nepastebėdavau, kad taip reaguoju.“

This distinction is the product core.

---

## 2. Product proposition

ConflictLab is an **experimental self-observation / epistemic reflection product**.

Its intended experience is:

```text
CONTROLLED EXPERIENCE
        ↓
SPONTANEOUS RESPONSE
        ↓
OBSERVATION / EVIDENCE
        ↓
CAREFULLY BOUNDED REFLECTION
        ↓
REPEATED SELF-OBSERVATION
        ↓
"Do I notice something that repeats?"
```

The product should create an opportunity to notice a pattern. It must not manufacture certainty where the evidence does not support it.

---

## 3. The user problem

Traditional self-report tools often begin by asking the person to describe themselves directly.

ConflictLab explores a different route:

> first create an experience in which the person reacts, then help them inspect that reaction.

The product hypothesis is not that images reveal a hidden personality. The product hypothesis is that carefully designed experiences may create useful observations that are harder to obtain by asking a person only to describe themselves abstractly.

Whether any specific stimulus, domain, timing protocol, or derived signal works remains an empirical question.

---

## 4. What is essential to the product

The following are **product invariants** unless the product vision itself is intentionally reopened.

### 4.1 Observation before interpretation

```text
SCENE PROPERTY
!= PARTICIPANT RESPONSE
!= DERIVED SIGNAL
!= PERSON CHARACTERISTIC
```

A participant response is an observation, not a diagnosis.

### 4.2 Reflection, not classification

The system may show what was observed and ask a bounded reflective question.

It must not tell the participant who they are merely because a mathematically neat pattern exists.

### 4.3 Evidence provenance

Any participant-facing statement must be traceable to the observations that support it and to the validated rules that produced it.

When evidence is insufficient, the correct product result is uncertainty or no result.

### 4.4 Repeated observation matters more than a single score

The long-term product value is expected to come from noticing whether something recurs across experiences, contexts, or time — not from maximizing information extracted from one click.

### 4.5 Autonomy

The participant remains the final interpreter of their experience.

ConflictLab may offer a mirror. It must not claim ownership of the person's meaning.

### 4.6 Privacy is architectural

Participant data collection must be proportional to the active product/research purpose.

The product should remain compatible with a local-first architecture wherever server-side processing is not necessary.

---

## 5. What is **not** a product invariant

The following are current or candidate implementation/research choices and may change or disappear without violating the North Star:

```text
6000 ms shared budget
3-pair block
CS domain
CR domain
AW hypothesis
Gate D implementation format
Gate E implementation format
reason-map options
intensity scale
specific stimulus families
specific calculation formula
Hostinger
MySQL
admin.php
current Wave 1
Calibration v0.1
current result UI
Claude / other LLM use
```

These serve the product vision. The product vision does not exist to preserve them.

If empirical evidence rejects CS/CR, a stimulus family, the 6000 ms mechanic, or the current reflection flow, those components may be removed while ConflictLab remains ConflictLab.

---

## 6. Product vs research infrastructure

ConflictLab currently requires research infrastructure to learn whether candidate mechanisms work.

That infrastructure is not automatically part of the final product.

```text
RESEARCH INFRASTRUCTURE
Wave 1 / calibration / telemetry / validation DB / admin
        ↓
answers methodological questions
        ↓
may later be archived or removed

PRODUCT CORE
experience -> response -> evidence -> reflection -> repeated observation
        ↓
should survive even if the research infrastructure disappears
```

This explicitly allows Hostinger and the current server/database architecture to be temporary validation infrastructure.

---

## 7. Backend decision principle

The final product **does not currently require a backend by definition**.

Backend services are justified only by a real product capability that cannot reasonably be delivered local-first.

Possible future capability classes:

```text
LOCAL-FIRST CORE
- stimulus experience
- local observations
- local evidence calculation
- local reflection/history where feasible

OPTIONAL SERVICES
- research telemetry
- cross-device continuity
- user-authorized backup/sync
- aggregate research
- remote model/API capabilities
- account-based history, if the product vision later requires it
```

Decision rule:

> Do not introduce persistent server identity, storage, or profiling merely because a backend is technically convenient.

---

## 8. GERT and AgileBrain — inspiration boundary

GERT and AgileBrain influenced the early project vision by demonstrating that structured non-traditional stimuli can be used in serious measurement/research workflows.

Their value to ConflictLab is inspirational and methodological, not identity-defining.

ConflictLab does **not** need to become:

- an emotion-recognition test like GERT;
- an image-based latent-needs scoring instrument like AgileBrain;
- a conventional psychometric test with a more attractive visual interface.

The distinctive direction worth preserving is:

```text
not:
stimulus -> hidden trait score

but:
stimulus -> observed response -> bounded evidence -> reflection
```

---

## 9. What ConflictLab must never become by accident

Without an explicit product-vision reopening, ConflictLab must not drift into:

- personality typing;
- clinical or psychological diagnosis;
- employee selection/ranking;
- suitability or eligibility scoring;
- a black-box AI telling a person what their reaction "really means";
- a system where every response can be post-hoc explained as confirming the model;
- a surveillance product collecting behavioural data because it may become useful later;
- a research platform whose laboratory instrumentation becomes the user value proposition.

---

## 10. Product success

Methodological validity and product usefulness are related but distinct.

A valid measurement mechanism can still produce a useless product. A pleasant reflection experience can still be methodologically misleading.

ConflictLab requires both boundaries to hold.

Product success should eventually be evaluated by questions such as:

1. Did the person react naturally rather than search for a "correct" answer?
2. Did the reflection remain grounded in actual observations?
3. Did it help the person notice something they had not consciously noticed before?
4. Did the person feel observed rather than judged or diagnosed?
5. Is there value in returning to observe themselves again?
6. Does repeated use create better self-observation rather than dependence on a score?

These are product questions. Exact metrics require separate validated research protocols.

---

## 11. Future feature test

Before adding a major feature, ask:

```text
A. Does this help create a better observation?
B. Does this improve evidence quality/provenance?
C. Does this help the person reflect without overclaiming?
D. Does this support meaningful repeated self-observation?
E. Is it necessary for validation, safety, privacy or operation?
```

If the answer to all five is `no`, the feature is probably not core ConflictLab work.

If a feature increases interpretation while weakening evidence, it moves the product away from the North Star.

---

## 12. Current research phase in relation to the vision

Current work on:

- stimulus validation;
- confound control;
- Gate D;
- Gate E;
- timing calibration;
- privacy/data minimisation;
- independent methodological review;

exists to determine **which mechanisms are safe and useful enough to support the product core**.

It is not the final product roadmap.

The correct outcome of validation may be to remove a mechanism entirely.

---

## 13. Change control

This document is intentionally more stable than individual methodology or implementation documents.

A change to:

- number of pairs;
- timing;
- stimuli;
- domains;
- scoring;
- research database;
- hosting provider;
- LLM provider;
- participant-flow details

**does not require a North Star version change** unless it changes the product purpose or the observation-before-interpretation philosophy.

A new North Star version is required if the project intentionally changes from self-observation/reflection into a different primary product category, such as assessment, diagnosis, employee selection, or predictive profiling.

---

## 14. One-sentence product definition

> **ConflictLab is a self-observation tool that uses controlled experiences to create evidence for reflection, helping people notice how they react without reducing those reactions to a label.**

---

## 15. Current decision

```text
PRODUCT NORTH STAR        STABLE
RESEARCH METHODS          EVOLVABLE / MUST BE VALIDATED
CS / CR                   CANDIDATE / NOT PRODUCT IDENTITY
HOSTINGER BACKEND         CURRENT RESEARCH INFRASTRUCTURE / NOT FINAL-PRODUCT REQUIREMENT
LOCAL-FIRST               PREFERRED DEFAULT WHERE CAPABILITY ALLOWS
PARTICIPANT LABELING      FORBIDDEN BY DEFAULT
PRODUCTIVE UNCERTAINTY    ALLOWED / REQUIRED WHEN EVIDENCE IS INSUFFICIENT
```

**ConflictLab is the mirror. The current laboratory apparatus is replaceable.**
