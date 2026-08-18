# ConflictLab — EU Data Protection Baseline v0.1

**Date:** 2026-08-15  
**Status:** DRAFT / compliance design baseline  
**Scope:** EU/EEA personal-data processing for ConflictLab technical, timing-calibration and future validation studies.  
**Important:** this is an engineering/compliance baseline, not a legal opinion. A final public privacy notice and controller identity must be reviewed before real participant collection.

---

## 1. Conservative compliance position

ConflictLab will not use consent as permission to collect every potentially useful variable.

Primary design rule:

```text
DEFINED PURPOSE
-> MINIMUM NECESSARY DATA
-> SHORTEST JUSTIFIED RETENTION
-> RESTRICTED ACCESS
-> VERSIONED PROCESSING RULES
```

This follows GDPR principles of lawfulness/fairness/transparency, purpose limitation, data minimisation, storage limitation, integrity/confidentiality and privacy by design/default.

Where anonymous data can answer the question, prefer anonymous data. Where event-level data must remain linkable to a session for QC or analysis, treat it as **personal data / pseudonymous data**, not as anonymous merely because no name or email is stored.

---

## 2. Controller identity is a blocking public-launch field

Before any real participant data collection beyond owner/technical testing, the participant information notice must identify the actual data controller and provide contact details.

The controller must be one real accountable entity:

```text
OPTION A: named natural person operating the project
OPTION B: named legal entity operating the project
```

Do not publish a placeholder, brand name alone, or invented entity as controller.

Until controller identity is frozen, real participant research collection remains blocked.

---

## 3. Treat current event-level telemetry as personal data

A random run/session UUID can enable singling out and linking multiple events within a session. Server requests may also involve IP addresses, user-agent information and security/access logs outside the application database.

Therefore:

- do not label event-level ConflictLab research records as anonymous by default;
- use `pseudonymous` or `minimised` where appropriate;
- do not store IP address in the ConflictLab research database;
- do not intentionally store full user-agent strings or device fingerprints in the research database;
- use only coarse device category when it is needed for the registered timing question;
- keep hosting/security logs logically separate from research data and do not join them for research analysis.

True anonymous aggregate datasets may be created only after a documented anonymisation step removes reasonably linkable individual/session-level information.

---

## 4. Current lawful-basis strategy

### 4.1 Strictly necessary technical/security processing

For server operation, security, abuse prevention, integrity checks and narrowly necessary technical diagnostics, the project should document the applicable legal basis before launch. A likely candidate for non-contractual public beta operation is **legitimate interests (GDPR Art. 6(1)(f))**, supported by a documented balancing/LIA assessment.

Do not use legitimate interests as a blanket basis for optional behavioural research.

### 4.2 Optional research / validation processing

For current small-scale voluntary beta research, the conservative default is **purpose-specific opt-in consent (GDPR Art. 6(1)(a))** for optional research telemetry that is not required to operate the site.

Consent must be:

- freely given;
- specific;
- informed;
- unambiguous;
- recorded by affirmative action;
- as easy to withdraw as to give.

Participation refusal must not block access to a non-research experience where technically feasible.

### 4.3 Special-category data

ConflictLab does not need health, political, religious, biometric, sexual-orientation or other GDPR Article 9 special-category data for the current protocol.

Therefore current policy is:

```text
DO NOT INTENTIONALLY COLLECT SPECIAL-CATEGORY DATA
```

Open free text is the highest risk because participants may disclose such information unexpectedly. For the current real-participant beta, **server-side open free-text storage is prohibited by default**. A later qualitative study that truly needs raw text requires a separate protocol, legal-basis review, explicit participant notice/consent appropriate to the actual data, access controls and DPIA update before collection.

---

## 5. Scientific-research caution

ConflictLab may conduct methodical validation work, but the project must not rely on GDPR scientific-research derogations merely because the work is called “research”.

EDPB 2026 research guidance identifies factors such as systematic method, ethical standards, verifiability/transparency, autonomy/independence, research objectives and contribution to knowledge when assessing scientific-research context.

Current compliance decision:

```text
DO NOT USE ARTICLE 89 / SCIENTIFIC-RESEARCH FLEXIBILITIES
AS A SHORTCUT FOR THE BETA
```

Use ordinary GDPR purpose, legal-basis, minimisation, transparency and rights rules unless a later qualified legal review establishes otherwise.

---

## 6. Collection profile for the next beta

### 6.1 Allowed without behavioural-research expansion

Under the current TECHNICAL / future timing-only design, retain only what is necessary for mechanics:

```text
random run UUID
purpose/run type
protocol/config version
form
neutral/canonical pair key where mechanically necessary
presentation index / position where necessary
choice latency
block elapsed / remaining budget
timeout / never-presented
page-hidden / retry diagnostics
coarse device category
technical error code
```

Do not add:

```text
name
email
phone
employer
precise location
full IP in research DB
full user-agent
advertising ID
browser fingerprint
persistent cross-study participant ID
free-text reason
special-category questions
participant psychological profile
```

### 6.2 Separate behavioural-validation opt-in

If a later frozen Gate D/E study needs additional fields, collect them only under a separately disclosed opt-in purpose. Candidate fields may include A/B response identity, structured reason ID, confound rating or intensity **only when the preregistered study question needs them**.

A field that is merely “potentially useful later” is not sufficient justification.

---

## 7. Open text decision

Current beta decision:

```text
UI MAY ALLOW LOCAL REFLECTION TEXT
SERVER UPLOAD OF OPEN TEXT = OFF
ADMIN EXPORT OF OPEN TEXT = OFF
```

If local reflection text is used, it should remain on-device and should not silently enter analytics, logs, error reports or support tools.

Participant-facing copy should discourage entering names or sensitive information even for local-only fields where practical.

---

## 8. Cookies, local storage and tracking

Current beta should avoid all non-essential third-party analytics/marketing trackers.

```text
Google Analytics / Meta Pixel / ad trackers / cross-site tracking = OFF
```

If future non-essential cookies, pixels or similar terminal-device tracking are added, they require compliant prior consent under Lithuanian ePrivacy/electronic-communications rules and GDPR. VDAI guidance states legitimate interest is not a valid substitute for consent for non-essential tracking technologies.

Necessary local/session storage used solely for the requested functionality should be documented in the privacy/cookie information and kept to the minimum scope and duration.

---

## 9. Hosting / processor boundary

Current hosting provider: Hostinger.

Hostinger publishes a Data Processing Addendum (DPA). Before real participant collection:

1. retain/reference the current DPA version applicable to the account;
2. document Hostinger as a processor where it processes ConflictLab participant data on the controller's behalf;
3. verify the actual hosting/data-region configuration rather than assuming an EU location from the brand/company address;
4. inspect subprocessors and any international-transfer mechanism applicable to the chosen service;
5. ensure HTTPS remains mandatory.

Research and security data should remain separated where feasible.

---

## 10. Retention model

A retention period must be justified by purpose, not by storage availability.

Conservative starting rule for future pseudonymous participant research:

```text
active-study raw event data:
retain only through the defined QC / analysis / withdrawal window

post-study:
anonymise/aggregate where feasible and delete event-level personal data
unless a longer retention period is explicitly justified and disclosed
```

No universal number is declared in this baseline because the period must match the registered study. The study-specific privacy notice must give a concrete period or objectively determinable criterion before collection begins.

Security/access logs may have a separate shorter/necessary retention under the security purpose and must not be repurposed as research telemetry.

---

## 11. Data-subject rights and withdrawal

Before consent-based research begins, the implementation must support:

- withdrawal of future research processing as easily as opt-in;
- access/information requests where data remain identifiable/pseudonymous;
- deletion where legally applicable and technically possible;
- clear explanation of when truly anonymised aggregate data can no longer be traced back for deletion;
- response workflow capable of meeting GDPR deadlines.

Avoid collecting email solely to manage deletion. Prefer a random participant/session deletion token or equivalent privacy-preserving mechanism if individual deletion must remain possible.

---

## 12. Adult-only beta

Current research beta should be restricted to adults:

```text
18+ ONLY
```

Use a simple self-declaration, not collection of date of birth or identity documents.

This avoids unnecessary child-consent and vulnerability complexity during method validation.

---

## 13. Automated decision / profiling boundary

Current system must continue to state and implement:

```text
NO automated decision with legal or similarly significant effect
NO validated personality diagnosis
NO employment/eligibility recommendation
NO participant ranking
Gate D = NONE
Gate E = NONE
participant directional result = NOT AUTHORIZED
```

Event analysis for method validation must not be repurposed into employment, insurance, credit, health or other consequential decisions.

---

## 14. DPIA decision

Even if a later lawyer concludes that a formal DPIA is not strictly mandatory at current small scale, ConflictLab will perform a DPIA-style assessment **before behavioural Gate D/E participant collection**.

Reason: the project combines at least plausible EDPB high-risk indicators:

- evaluation/scoring of behavioural responses;
- innovative/new methodological technology;
- potentially highly personal reaction data.

Small scale, no legal effects, no direct identifiers and fail-closed interpretation reduce risk, but do not remove the value of documented risk assessment.

Internal gate:

```text
NO BEHAVIOURAL VALIDATION COLLECTION
UNTIL DPIA SCREENING / MITIGATION IS DOCUMENTED
```

If the assessment identifies high residual risk that cannot be mitigated, obtain qualified legal/DPO advice and, where legally required, consult the competent supervisory authority before processing.

---

## 15. Security minimum

Before real participant collection:

- separate research DB from legacy/public Wave1 data stores;
- least-privilege DB account;
- secrets outside web-readable paths;
- strong admin authentication;
- HTTPS only;
- authenticated admin export;
- no persistent generated CSV files in a public web directory;
- no raw personal data in URLs/query strings;
- access logging and export access limited to need-to-know;
- backup/restore and deletion behavior documented;
- dependency/runtime patching maintained;
- incident response contact/process documented.

VDAI enforcement in 2026 continues to include access-control and security failures, so security evidence is part of compliance, not only application quality.

---

## 16. Complaint-ready evidence pack

The project should be able to produce, without reconstructing history after a complaint:

```text
controller identity + contact
privacy notice version
purpose/legal-basis register
consent copy/version and withdrawal mechanism
record of processing activities (lightweight ROPA)
DPIA screening / DPIA if applicable
Hostinger DPA + processor/subprocessor review
retention/deletion schedule
security measures record
study preregistration / frozen schema
exact data dictionary
admin-access/export controls
incident-response procedure
```

The goal is not to prove that “no risk exists”. The goal is to prove that the controller knew what was processed, why, for how long, under which basis, with which safeguards and with which rights process.

---

## 17. Current authorization state

```text
TECHNICAL owner/developer testing      ALLOWED UNDER CURRENT INTERNAL BASELINE
REAL TIMING CALIBRATION PARTICIPANTS   NOT YET AUTHORIZED
GATE D/E BEHAVIOURAL COLLECTION        NOT AUTHORIZED
SERVER OPEN FREE TEXT                  PROHIBITED BY DEFAULT
NON-ESSENTIAL TRACKERS                 PROHIBITED BY DEFAULT
MINORS                                  OUT OF SCOPE
Gate D                                  NONE
Gate E                                  NONE
```

Real participant collection can move forward only after controller identity, privacy notice, lawful-basis record, exact payload, retention rule, processor review and DPIA screening are frozen for the study.