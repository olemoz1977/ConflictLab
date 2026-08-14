# ConflictLab — Calibration Activation Checklist v0.1

**Date:** 2026-08-15  
**Status:** BLOCKED / real external CALIBRATION collection not authorized  
**Target:** `calibration-v0.1` / `future-rapid-v1` / 6000 ms candidate budget  
**Purpose:** define the exact operational, privacy and security conditions that must be closed before `collection_mode` may change from `TECHNICAL` to `CALIBRATION`.

> Switching the server flag is the final step, not the authorization mechanism.

---

## 1. Current authorization state

```text
LAB / TECHNICAL owner testing             ALLOWED
EXTERNAL CALIBRATION participant upload   BLOCKED
Gate D                                    NONE
Gate E                                    NONE
participant directional result            NOT AUTHORIZED
collection_mode                           TECHNICAL
```

No item in this checklist authorizes a public `/wave1/` switch.

---

## 2. Evidence reviewed

Implementation reviewed on branch `arch/result-v0.2-implementation-baseline` at pre-check head:

`dce307c1944855847d3351abfc9872f2d9101765`

Primary implementation paths:

```text
deploy/conflictlab-hostinger/releases/calibration-v0.1/index.html
deploy/conflictlab-hostinger/releases/calibration-v0.1/server/calibration_api.php
deploy/conflictlab-hostinger/releases/calibration-v0.1/server/admin.php
deploy/conflictlab-hostinger/releases/calibration-v0.1/server/schema.sql
deploy/conflictlab-hostinger/releases/calibration-v0.1/server/config.example.php
config/future-session/timing-calibration-v1.json
docs/experiments/timing/TIMING_CALIBRATION_PREREGISTRATION_v0.1.md
```

Owner-verified infrastructure facts on 2026-08-15:

```text
Hostinger primary server region: Europe (Lithuania)
Hostinger backup location: France
Hostinger hPanel analytics: server/access-log based
OMESG360 privacy contact: info@omesg360.eu
Data controller: Oleg Mozochin
public privacy.html: owner reports active as the sole current privacy page
```

These owner-verified facts are operational evidence, not repository-derived facts.

---

## 3. Status vocabulary

```text
PASS              implemented and evidenced for the current scope
PARTIAL           useful control exists but release condition is incomplete
NOT_IMPLEMENTED   required mechanism is absent in reviewed implementation
OWNER_VERIFY      implementation may exist outside repo; owner must verify
BLOCKED           unresolved item prevents external CALIBRATION activation
NOT_REQUIRED      not required for this timing-only scope
```

---

## 4. Study-scope and methodology gate

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| M01 | Study scope is mechanical timing only | PASS | preregistration and `timing-calibration-v1.json` explicitly prohibit construct/trait interpretation |
| M02 | 6000 ms is a candidate engineering parameter, not psychological standard | PASS | frozen timing config / preregistration |
| M03 | Gate D remains NONE | PASS | no mapping authorization |
| M04 | Gate E remains NONE | PASS | no aggregation authorization |
| M05 | First confirmatory dataset has frozen inclusion/exclusion and stopping rule | PASS | first 20 eligible clean primary blocks; no outcome-driven extension |
| M06 | Owner/technical runs excluded from N/20 | PASS | server-assigned `run_type`; admin separates TECHNICAL/CALIBRATION |
| M07 | External collection starts only after this activation checklist is closed | BLOCKED | current checklist state is BLOCKED |

---

## 5. Data-minimisation gate

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| D01 | Separate calibration DB/tables from Wave 1 | PASS | `cl_calibration_*` isolated tables |
| D02 | No name/email/phone/employer in timing dataset | PASS | API/schema have no such fields |
| D03 | No open reflection text in timing dataset | PASS | UI keeps reflection local; API does not accept it |
| D04 | No reason/intensity/reason-latency/intensity-latency in timing dataset | PASS | absent from API/schema |
| D05 | No participant directional result in server dataset | PASS | fail-closed local result; absent from API/schema |
| D06 | No persistent cross-study participant identity | PASS | random session UUID only |
| D07 | No full user-agent/device fingerprint in research DB | PASS | only coarse `device_category` |
| D08 | No A/B selected asset identity used for construct inference | PASS | timing payload transmits pair identity and mechanics, not selected A/B identity |
| D09 | Exact timing payload matches frozen preregistration | PARTIAL | mechanical fields match; consent/version fields required by privacy scope are not yet implemented |

---

## 6. Consent and transparency gate

This section is BLOCKING.

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| C01 | Clear participant-facing timing-study purpose before upload | PARTIAL | current intro says technical telemetry is stored, but no dedicated research-consent step |
| C02 | Direct link to current privacy information at collection point | NOT_IMPLEMENTED | reviewed calibration UI contains no privacy link |
| C03 | Explicit voluntary research opt-in before timing upload | NOT_IMPLEMENTED | no consent control/state exists in reviewed UI |
| C04 | Refusal possible without being treated as psychological signal | NOT_IMPLEMENTED | no refusal/local-only branch exists |
| C05 | 18+ declaration for external research phase | NOT_IMPLEMENTED | no age declaration in reviewed UI |
| C06 | Consent version/state included in upload | NOT_IMPLEMENTED | current payload has no consent fields |
| C07 | Server rejects CALIBRATION upload without valid affirmative consent metadata | NOT_IMPLEMENTED | API validates mechanics but not consent |
| C08 | Consent evidence stored with run | NOT_IMPLEMENTED | schema has no consent version/state fields |
| C09 | Final participant copy matches implemented payload exactly | BLOCKED | cannot freeze until C02-C08 are implemented |

Activation rule:

```text
C02-C08 must be PASS before external CALIBRATION collection.
```

---

## 7. Withdrawal / erasure gate

This section is BLOCKING because consent is the planned research legal basis.

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| W01 | Participant receives random withdrawal/deletion code | NOT_IMPLEMENTED | no code generation/display exists |
| W02 | Server stores only a one-way token representation sufficient to locate the run | NOT_IMPLEMENTED | schema has no token field |
| W03 | Controller can locate run from participant-provided code | NOT_IMPLEMENTED | no admin lookup exists |
| W04 | Controller can delete eligible pseudonymous run data end-to-end | NOT_IMPLEMENTED | no deletion workflow exists; current foreign keys use `ON DELETE RESTRICT` |
| W05 | Deletion removes run, attempts and pair events transactionally | NOT_IMPLEMENTED | must be explicit transaction or migration to safe cascade semantics |
| W06 | Withdrawal/deletion process tested before activation | BLOCKED | dependent on W01-W05 |
| W07 | Contact channel exists | PASS | `info@omesg360.eu` |

Design preference:

```text
plaintext deletion code -> shown once to participant
server -> stores only cryptographic hash
email -> participant sends code to controller if they request deletion
admin -> authenticated lookup + explicit delete confirmation
```

Do not collect participant email merely to support deletion.

---

## 8. Retention gate

This section is BLOCKING for the proposed 90-day timing-study rule.

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| R01 | Retention period defined for timing study | PASS | planned maximum 90 days |
| R02 | Automatic or controlled deletion mechanism exists | NOT_IMPLEMENTED | no retention cleanup script/job in reviewed release |
| R03 | Retention deletion covers child records | NOT_IMPLEMENTED | schema currently uses RESTRICT foreign keys |
| R04 | Hostinger cron / scheduled execution configured | OWNER_VERIFY | cannot be established from repo |
| R05 | Backup retention/deletion behavior documented | OWNER_VERIFY | Hostinger backup location verified, lifecycle not yet recorded |
| R06 | 90-day process tested with disposable TECHNICAL records | BLOCKED | dependent on implementation/configuration |

No external CALIBRATION collection until R02-R06 are closed or the participant notice is changed to an actually implemented retention rule.

---

## 9. Server/API integrity gate

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| S01 | Server assigns run type; client cannot self-label CALIBRATION | PASS | `collection_mode` read from server config |
| S02 | Default/example mode is TECHNICAL | PASS | `config.example.php` |
| S03 | Exact release/protocol/stimulus-set/budget checked server-side | PASS | API rejects mismatch |
| S04 | Preload must succeed before ingestion | PASS | API requires `technicalPreloadOk` |
| S05 | Duplicate message/session handling | PASS | idempotency and unique session checks |
| S06 | Body size/content type/input validation | PASS | bounded JSON + field validation |
| S07 | Training excluded from server calibration attempt | PASS | API rejects `isTraining=true` |
| S08 | Page-hidden primary exclusion is server-derived | PASS | `clean_primary` derived by API |
| S09 | Config/SQL denied from web access | PASS | server `.htaccess` protects `config*.php` and SQL |
| S10 | HTTPS verified for live Hostinger path | OWNER_VERIFY | owner browser/HHostinger SSL evidence indicates SSL active; perform final live check before activation |

---

## 10. Admin/security gate

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| A01 | Admin is authenticated | PASS | password hash + PHP session + session ID regeneration |
| A02 | Admin distinguishes TECHNICAL/CALIBRATION | PASS | UI/filtering/decision N/20 separation |
| A03 | Admin export exists | NOT_IMPLEMENTED | no CSV/export path found in reviewed `admin.php` |
| A04 | Export limited to timing-study fields | NOT_IMPLEMENTED | dependent on A03 |
| A05 | Export is generated on demand, not left in public directory | NOT_IMPLEMENTED | dependent on A03 |
| A06 | Admin session cookie flags explicitly hardened | PARTIAL | code calls `session_start()` without explicit cookie security parameters; host PHP defaults unknown |
| A07 | Privileged external access has additional hardening | PARTIAL | password exists; no MFA/rate-limit/second access layer evidenced in repo |
| A08 | Admin access/security reviewed after new deletion/export controls | BLOCKED | must be re-reviewed after implementation |

Security decision for this small pilot:

- do not claim current password-only admin is a completed privacy/security gate merely because it works;
- before real participant collection, at minimum freeze strong unique admin password practice, secure session-cookie settings, login throttling or an equivalent access-control layer, and an authenticated non-persistent export path;
- if Hostinger provides an additional protected-directory or access-control mechanism, document it as defence in depth, not as proof of MFA unless it is genuinely multi-factor.

---

## 11. Hostinger / processor gate

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| H01 | Primary hosting location known | PASS | owner verified Lithuania |
| H02 | Backup location known | PASS | owner verified France |
| H03 | Hostinger server analytics understood as access-log analytics | PASS | owner verified hPanel analytics view |
| H04 | Hostinger DPA applicable to account retained/referenced | OWNER_VERIFY | obtain/store current applicable DPA reference |
| H05 | Subprocessor/transfer route reviewed | OWNER_VERIFY | review current Hostinger terms/subprocessor information before activation |
| H06 | Research DB remains separate from Wave 1 | PASS | separate calibration schema/tables/database design |

---

## 12. Privacy-document gate

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| P01 | Controller identity/contact fixed | PASS | Oleg Mozochin / info@omesg360.eu |
| P02 | Public OMESG360 privacy page exists | OWNER_VERIFY | owner reports current sole `privacy.html` is uploaded |
| P03 | Calibration section states external research is not active | OWNER_VERIFY | owner-uploaded current privacy file should be checked again at activation |
| P04 | Privacy copy updated from PREPARATION to ACTIVE only at activation | BLOCKED | future activation task |
| P05 | Public copy matches exact implemented fields/legal basis/retention | BLOCKED | depends on consent + deletion + retention implementation |
| P06 | Historical previous notice retained before material change | PARTIAL | establish archive practice before next material privacy change |

---

## 13. Operational analysis gate

| ID | Requirement | Status | Evidence / action |
|---|---|---:|---|
| O01 | Admin computes preregistered N/20 decision metrics | PASS | current admin implements thresholds from timing calibration config |
| O02 | Pair/form/device diagnostics available | PASS | current admin implementation |
| O03 | Authenticated CSV export for reproducible analysis | NOT_IMPLEMENTED | previously required operational feature |
| O04 | Export schema/version documented | NOT_IMPLEMENTED | dependent on O03 |
| O05 | Export never includes local reflection/reason/intensity data | PASS BY ARCHITECTURE | those fields are absent from server DB; preserve this boundary |

O03-O04 should be completed before or at activation so the confirmatory dataset can be exported reproducibly without ad-hoc database access.

---

## 14. Activation blocker summary

Current hard blockers:

```text
B1  consent UI / affirmative opt-in
B2  18+ declaration
B3  privacy link at collection point
B4  consent metadata in payload + schema + server validation
B5  refusal / local-only path
B6  withdrawal/deletion token and admin deletion workflow
B7  implemented/tested 90-day retention cleanup
B8  Hostinger DPA/subprocessor operational record
B9  admin hardening review
B10 authenticated versioned CSV export
B11 final privacy copy aligned to exact implementation
B12 final TECHNICAL smoke test after all code changes
```

No Gate D or Gate E work is required to clear these timing-only activation blockers.

---

## 15. Implementation order

Recommended dependency order:

```text
1. consent + 18+ + privacy-link UX
2. consent/deletion fields + DB migration
3. API validation of consent metadata
4. refusal/local-only branch
5. deletion-token + admin lookup/delete
6. retention cleanup script + Hostinger cron design
7. admin CSV export + export schema
8. admin session/access hardening
9. tests / CI
10. exact-head Hostinger LAB artifact
11. owner TECHNICAL smoke test
12. public privacy copy final alignment
13. Hostinger DPA/subprocessor record final check
14. explicit activation record
15. only then change local Hostinger config `collection_mode` to `CALIBRATION`
```

The repository default/example config should continue to default to `TECHNICAL` even after an authorized live study exists.

---

## 16. Final activation record

When every hard blocker is closed, create a separate immutable record:

`CALIBRATION_ACTIVATION_RECORD_v0.1.md`

It must include:

```text
activated_release_commit_sha
successful_CI_run
artifact_digest
live_release_path
privacy_notice_version
consent_version
retention_version
export_schema_version
admin_security_review_version
Hostinger processor-review date
TECHNICAL smoke-test result
activation timestamp
owner authorization
```

Only that record plus the final owner authorization may permit the live server config to change:

```php
'collection_mode' => 'CALIBRATION',
```

No merge to `main`, no `/wave1/` replacement and no participant directional interpretation are implied by calibration activation.
