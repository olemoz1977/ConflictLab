# ConflictLab — Research Data and Consent Scope v0.2

**Date:** 2026-08-15  
**Status:** DRAFT TO FREEZE BEFORE FIRST EXTERNAL PARTICIPANT  
**Supersedes for next-cycle planning:** `RESEARCH_DATA_AND_CONSENT_SCOPE_v0.1.md`  
**Compliance parent:** `EU_DATA_PROTECTION_BASELINE_v0.1.md`  
**DPIA parent:** `DPIA_SCREENING_v0.1.md`

> Privacy decision: the next real participant cycle will be **mechanical timing / UX calibration only** at server level. Behavioural/construct-validation content remains local or uncollected until a separate privacy package and study registration are approved.

---

## 1. Why v0.2 is stricter than v0.1

v0.1 allowed the possibility of combining timing collection with a separately consented Gate D/reflection component in one session.

For the next external participant cycle, that option is intentionally rejected.

Reason:

- EU GDPR purpose limitation and data minimisation;
- event-level research records are treated as pseudonymous personal data, not anonymous data;
- open reflection content can unexpectedly contain highly personal or special-category information;
- the current Gate D/E method is not yet empirically validated;
- a simple timing study can answer its question without collecting behavioural interpretation content.

---

## 2. Exact next-study purpose

Only this research question is authorized for the first external participant cycle:

> Does the current three-pair rapid protocol with a shared 6000 ms budget produce acceptable completion and missingness mechanics on supported devices?

It does **not** ask:

- what the participant is like;
- whether the participant prefers clarity/ambiguity or structure/flexibility;
- why the participant chose an image;
- whether CS or CR are valid constructs;
- whether Gate D or Gate E should pass.

---

## 3. Server payload for next study

Allowed research fields:

```text
random run/session UUID
research purpose = TIMING_CALIBRATION
consent version / consent state
protocol version
stimulus-set version
form
pair key where required for missingness diagnostics
presentation index
presentation position where required
visual-choice latency
block elapsed time
remaining budget at pair start
timeout / never-presented state
page-hidden diagnostic
retry diagnostic
coarse device category
technical error/status code
collection timestamp
```

No direct identifiers.

---

## 4. Explicitly prohibited server fields in next study

```text
name
email
phone
employer
exact age / date of birth
precise location
IP address in research DB
full user-agent / browser fingerprint
persistent cross-study participant ID
A/B choice identity for construct use
reason_id
open free text
reaction intensity
reason-response latency
intensity-response latency
hard-to-identify as behavioural evidence
derived directional event
Directional Balance
CS / CR participant result
psychological label / diagnosis
```

If the web server/hosting layer necessarily processes IP/security logs, those logs remain under a separate security/operations purpose and may not be joined to the research dataset.

---

## 5. Participant-facing local experience

The product-shaped flow may still show local reflection/reason/intensity UI for UX testing provided that:

```text
reflection content remains local
reason selection remains local
intensity remains local
reason latency remains local
intensity latency remains local
no derived psychological result is shown
```

The server must receive timing data before/independently of reflection, as already designed.

Local reflection data must not leak into analytics, error logs, URLs or support telemetry.

---

## 6. Legal-basis split

### Necessary operations/security

Document separately under the controller's selected Article 6 basis. For a public non-contractual beta, legitimate interests may be considered for narrowly necessary security/technical processing only after a documented LIA/balancing assessment.

### Optional timing research

Conservative beta default:

```text
GDPR Art. 6(1)(a) consent
```

Consent must be affirmative, informed, purpose-specific and withdrawable.

The participant must understand that the collected data are used to evaluate the interaction mechanics, not to evaluate the participant.

---

## 7. Consent interaction rule

Before timing upload:

```text
[ ] I am 18 or older

Timing research information
What is collected
Why it is collected
How long it is kept
Who controls/processes it
How to withdraw/delete where applicable

[Participate in timing research]
[Continue without research upload]  <- where implementation supports local-only use
```

No pre-ticked boxes.

Research refusal must not be disguised as failure or produce a dark-pattern disadvantage.

Exact participant copy must be frozen before collection.

---

## 8. Adult-only rule

```text
EXTERNAL RESEARCH PARTICIPANTS = 18+
```

Collect only the self-declaration, not date of birth or ID documents.

---

## 9. Tracking technologies

For the external beta:

```text
third-party analytics = OFF
marketing trackers = OFF
advertising pixels = OFF
cross-site tracking = OFF
```

No non-essential terminal-device tracking is authorized.

Any necessary local/session storage must be documented and limited to the requested functionality.

---

## 10. Retention

Before the first participant, choose and publish a concrete retention period for pseudonymous timing-event data.

The period must cover only:

- study collection;
- quality control;
- declared timing analysis;
- withdrawal/deletion window where applicable.

After that period:

```text
delete event-level personal/pseudonymous data
OR
irreversibly anonymise/aggregate it under a documented process
```

Do not keep raw timing events indefinitely “for future research”.

---

## 11. Withdrawal/deletion without email collection

Do not collect email merely to support GDPR rights.

Preferred design:

```text
random deletion/withdrawal token
-> shown to participant after consent
-> stored only in a form necessary to locate/delete that study record
```

The privacy notice must explain that once data are irreversibly anonymised, individual deletion may no longer be technically possible because the data are no longer linked to an identifiable participant.

---

## 12. Gate D/E collection is a separate future study

The following remain blocked:

```text
GATE_D_VALIDATION server collection
GATE_E_VALIDATION server collection
REFLECTION_RESEARCH server collection
```

Before any of them can start, require all of:

1. frozen study preregistration;
2. frozen Gate D/E evidence contract as applicable;
3. updated DPIA;
4. updated privacy notice;
5. separate research purpose/legal basis;
6. exact server payload;
7. retention/deletion rule;
8. security/export review;
9. if raw free text is proposed, a separate special-category/highly-personal-data risk review.

Timing data collected under v0.2 may **not** later be re-labelled as Gate D/E evidence merely because pair IDs were present.

---

## 13. Controller/processor blocking items

Before real participant upload:

```text
actual controller identity = REQUIRED
controller contact = REQUIRED
Hostinger processor/DPA review = REQUIRED
actual hosting/data region = VERIFIED
subprocessor / transfer route = REVIEWED
privacy notice = FROZEN
```

Brand name alone is not sufficient as controller identity.

---

## 14. DPIA gate

`DPIA_SCREENING_v0.1.md` applies.

For the timing-only study, complete at least the documented screening and mitigations before participant collection.

For future Gate D/E behavioural validation, complete a full DPIA-style risk table before collection.

---

## 15. Complaint-ready rationale

If challenged, the next-study data design should be explainable in one paragraph:

> ConflictLab collected a pseudonymous minimum dataset only to test the mechanical completion and missingness of a three-pair timed interface. It did not collect names, contact data, open reflections, behavioural reason labels, psychological scores or special-category data for this study. The research purpose, consent, retention, processor and rights process were documented before collection, and the data were not reused to validate psychological constructs.

---

## 16. Current authorization state

```text
TECHNICAL owner/developer mode       ACTIVE
external timing research             BLOCKED UNTIL privacy package freeze
Gate D server research               BLOCKED
Gate E server research               BLOCKED
reflection-content server research   BLOCKED
open-text server storage              OFF
third-party non-essential trackers   OFF
minors                                OUT OF SCOPE
participant directional result       NOT AUTHORIZED
```

This v0.2 is the authoritative privacy-scope decision for planning the next participant cycle.