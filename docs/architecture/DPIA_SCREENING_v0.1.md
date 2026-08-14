# ConflictLab — DPIA Screening v0.1

**Date:** 2026-08-15  
**Status:** DRAFT / mandatory internal gate before behavioural validation  
**Scope:** GDPR Article 35 screening for ConflictLab participant research.  
**Related:** `EU_DATA_PROTECTION_BASELINE_v0.1.md`, `RESEARCH_DATA_AND_CONSENT_SCOPE_v0.1.md`

> This screening is intentionally conservative. It does not state that a statutory DPIA is definitely required; it records why ConflictLab will perform a DPIA-style assessment before Gate D/E participant collection.

---

## 1. Processing under assessment

Candidate future operation:

```text
voluntary adult participant
-> rapid image choices
-> pseudonymous event-level research telemetry
-> possible structured reason/confound/intensity responses
-> method-validation analysis
```

Current excluded scope:

```text
no direct identifiers
no employment decision
no clinical/health decision
no legal/similarly significant automated decision
no minors
no public-area monitoring
no large-scale special-category processing
no open-text server storage by default
```

---

## 2. EDPB high-risk indicator screen

### A. Evaluation or scoring

**Present / plausible.**

ConflictLab records behavioural choices and may derive research variables from them. Even though current participant-facing directional interpretation is blocked, this is sufficiently close to evaluation/scoring that it should be treated as a DPIA indicator.

### B. Automated decision-making with legal or similarly significant effect

**Absent under current architecture.**

Explicitly prohibited.

### C. Systematic monitoring

**Limited / not public-area monitoring.**

The research protocol observes interactions within a voluntary session. It is not continuous monitoring across services or public spaces.

### D. Sensitive or highly personal data

**Potentially present at behavioural level; Article 9 data not intentionally collected.**

Reaction/choice data can be highly personal in context even if they are not automatically GDPR special-category data. Open text could accidentally contain special-category data, which is why server-side open text is prohibited by default.

### E. Large scale

**Absent in current beta.**

Current planned participant cycle is small-scale.

### F. Matching or combining datasets

**Absent by default.**

No data-broker, employer, health, social-media or external profile matching is authorized.

### G. Vulnerable data subjects

**Reduced by adult-only scope.**

Minors excluded. No patient/employee dependency relationship should be used for recruitment where refusal could carry consequences.

### H. Innovative technological or organisational solution

**Present / plausible.**

The project uses a novel image-choice/reflection methodology with timing and evidence gates.

### I. Processing prevents exercise of a right/use of service or contract

**Absent under intended beta.**

Research refusal must not create a legal or contractual disadvantage.

---

## 3. Screening conclusion

ConflictLab plausibly meets at least two EDPB DPIA indicators:

```text
EVALUATION / SCORING
+
INNOVATIVE TECHNOLOGY / METHOD
```

There is also a possible `highly personal data` element depending on the final research payload.

Therefore project policy is:

```text
DPIA-STYLE ASSESSMENT REQUIRED INTERNALLY
BEFORE GATE D/E PARTICIPANT COLLECTION
```

This remains true even if external counsel later determines that Article 35 does not strictly compel a formal DPIA at current scale.

---

## 4. Risk-reduction measures already present

Current safeguards:

- no names/emails/employer identifiers in method-validation payload;
- random session/run UUID only;
- local-first reflection;
- server open free text disabled by default;
- no persistent cross-study participant ID;
- no psychological/directional result while Gate D/E are invalid;
- no latency/intensity psychological interpretation;
- no consequential automated decisions;
- technical and research purpose separation;
- versioned schemas/configs;
- isolated calibration database;
- adult-only proposed beta;
- no non-essential trackers proposed;
- Hostinger processor DPA available for review.

---

## 5. Risks still requiring explicit assessment

Before behavioural research:

1. **Re-identification / singling-out** from session UUID + hosting logs.
2. **Purpose creep** from timing telemetry into construct validation.
3. **Profiling perception risk** even when the project claims not to infer traits.
4. **Unauthorized admin/export access** to event-level data.
5. **Retention creep** because research data are easy to keep indefinitely.
6. **Consent validity** if research is bundled with use of the tool.
7. **Special-category disclosure** if any open text reaches the server.
8. **International transfer/subprocessor risk** from hosting configuration.
9. **Security breach risk** in DB, backups, admin interface or exported CSV.
10. **Withdrawal/deletion feasibility** without collecting direct identifiers.
11. **Dataset combination risk** across Wave1, calibration and later studies.
12. **Function creep** into employee selection, ranking or assessment.

---

## 6. Required mitigations before real participant collection

Must be completed:

```text
controller identity frozen
privacy notice frozen
lawful-basis/LIA or consent basis documented per purpose
exact server payload frozen
retention/deletion period frozen
Hostinger DPA + subprocessor/transfer review documented
non-essential trackers confirmed OFF
adult-only participant condition implemented
withdrawal/deletion mechanism defined
admin/export hardening confirmed
incident-response workflow documented
```

For Gate D/E behavioural research additionally:

```text
study preregistration frozen
separate behavioural-validation consent frozen
open text server upload remains OFF unless separately approved
DPIA risk table completed with likelihood/severity/mitigation/residual risk
```

---

## 7. Residual-risk decision rule

Before the study begins, each material risk must have:

```text
risk description
likelihood
severity
mitigation
residual likelihood
residual severity
owner
review date
```

If residual high risk remains after feasible safeguards:

```text
DO NOT START COLLECTION
-> obtain qualified privacy/legal/DPO review
-> consult supervisory authority if legally required
```

---

## 8. Reassessment triggers

Repeat/reopen the DPIA when any of these occur:

- server-side open text enabled;
- special-category questions added;
- persistent participant identity introduced;
- cross-session/cross-study linking introduced;
- participant result/score becomes user-facing;
- data used for employment or other consequential decisions;
- external datasets matched;
- major new analytics/AI processing added;
- scale increases materially;
- new processor/subprocessor or non-EEA transfer route introduced;
- security incident exposes participant data.

---

## 9. Current gate

```text
TECHNICAL owner runs               PASS FOR INTERNAL DEVELOPMENT
TIMING PARTICIPANT STUDY           BLOCKED pending privacy study package
GATE D/E BEHAVIOURAL STUDY         BLOCKED pending completed DPIA-style assessment
PUBLIC PSYCHOLOGICAL RESULT        BLOCKED
```
