# ConflictLab — Calibration Activation Checklist v0.2

**Date:** 2026-08-15  
**Status:** BLOCKED / repository controls substantially implemented, live activation not authorized  
**Target:** `calibration-v0.1` / `future-rapid-v1` / 6000 ms candidate budget  
**Supersedes operational status in:** `CALIBRATION_ACTIVATION_CHECKLIST_v0.1.md`

> Repository implementation is not the same as live Hostinger readiness. `collection_mode` remains `TECHNICAL` until the live migrations, cron, exact-head deployment, smoke tests, privacy alignment and owner authorization are complete.

---

## 1. Current authorization state

```text
LAB / TECHNICAL owner testing             ALLOWED
EXTERNAL CALIBRATION participant upload   BLOCKED
Gate D                                    NONE
Gate E                                    NONE
participant directional result            NOT AUTHORIZED
live collection_mode                      KEEP TECHNICAL
```

Implementation reviewed through branch head before this checklist:

`8275de99e7f05bd09a5edeb76402be78ce4aeb9b`

---

## 2. What is now implemented in the repository

### Consent / transparency

```text
PASS  dedicated timing-research choice screen
PASS  18+ declaration
PASS  unchecked voluntary research-consent checkbox
PASS  direct /privacy.html link
PASS  local-only continuation without research upload
PASS  refusal is not a psychological signal
PASS  consent version included in consented payload
PASS  server rejects CALIBRATION without exact consent version
PASS  server rejects CALIBRATION without affirmative consent
PASS  server rejects CALIBRATION without 18+ confirmation
PASS  consent evidence fields defined in DB schema
```

Live caveat:

```text
OWNER_VERIFY / BLOCKED
migration_002_consent_fields.sql has not yet been confirmed applied to Hostinger DB
```

### Withdrawal / erasure

```text
PASS  client generates random 128-bit deletion code
PASS  participant sees plaintext code only after successful upload
PASS  client sends only SHA-256 hash to server
PASS  API validates 64-char lowercase SHA-256 hash
PASS  DB schema stores only deletion_token_hash
PASS  unique deletion-token hash index
PASS  authenticated data admin can locate session from participant code
PASS  authenticated data admin deletes events -> attempts -> run in one transaction
PASS  public self-service deletion page exists
PASS  public deletion response avoids exposing whether a supplied code was valid
PASS  no participant email is required merely to support deletion
```

Live caveat:

```text
OWNER_VERIFY / BLOCKED
migration_003_deletion_token.sql has not yet been confirmed applied
end-to-end deletion has not yet been smoke-tested against the live TECHNICAL DB
```

### Retention

```text
PASS  retention_days = 90 defined in config example
PASS  CLI-only retention_cleanup.php exists
PASS  web execution is blocked by PHP_SAPI check
PASS  cleanup deletes events -> attempts -> run transactionally
PASS  cleanup prints aggregate counts only
PASS  batch limited to 500 runs per invocation
```

Live caveat:

```text
BLOCKED
Hostinger cron has not yet been configured/verified
backup lifecycle still requires operational documentation
90-day cleanup has not yet been tested with disposable TECHNICAL records
```

### Admin timing export

```text
PASS  authenticated data_admin.php exists
PASS  CSV streamed directly; no persistent server CSV is intentionally created
PASS  filters: type / form / device / eligible status
PASS  export schema ID = timing-export-v0.1
PASS  schema documented in TIMING_EXPORT_SCHEMA_v0.1.md
PASS  deletion_token_hash excluded
PASS  message_id/session_id excluded
PASS  IP/access-log/user-agent data excluded
PASS  local reflection/reason/intensity fields excluded
```

Live caveat:

```text
BLOCKED
new data_admin.php has not yet been deployed/smoke-tested in Hostinger LAB
```

---

## 3. Data-minimisation boundary after implementation

Server timing research data may contain:

```text
random session/message UUIDs for ingestion integrity
run type
release/protocol/stimulus-set/form versions
coarse device category
mechanical timing/missingness/retry/page-hidden fields
consent version + affirmative consent evidence + 18+ declaration
delection-token SHA-256 hash
```

Still prohibited from the timing research DB:

```text
name
email
phone
employer
precise location
research-use IP address
full user-agent / device fingerprint
A/B selected asset identity for construct interpretation
reason_id
open reflection text
reaction intensity
reason/intensity response latency
derived directional event
CS/CR participant result
persistent cross-study participant ID
```

---

## 4. Remaining hard blockers

The following still prevent external `CALIBRATION` activation:

```text
L1  run migrations 002 + 003 on live Hostinger calibration DB
L2  add consent_version + retention_days to live secret server/config.php
L3  KEEP collection_mode = TECHNICAL during migration/deployment testing
L4  deploy an exact-head successful-CI artifact to LAB
L5  verify consented TECHNICAL upload end-to-end
L6  verify local-only path creates NO research DB run
L7  verify deletion code is shown only after successful upload
L8  verify admin deletion removes run + attempts + events
L9  verify public self-service deletion removes the matching run
L10 verify timing CSV export and exact column schema
L11 configure and test Hostinger cron for retention_cleanup.php
L12 document/verify Hostinger backup retention behavior
L13 final admin/security review, including current legacy timing dashboard session settings
L14 retain/reference applicable Hostinger DPA and review current subprocessor/transfer information
L15 align public privacy.html from PREPARATION to the exact active implementation only at activation
L16 perform final LT + EN + mobile TECHNICAL smoke tests
L17 create exact activation record with commit/CI/artifact/privacy/consent/export/retention versions
L18 explicit owner authorization
```

Only after L1-L18 are closed may the live secret config change to:

```php
'collection_mode' => 'CALIBRATION',
```

The repository `config.example.php` remains `TECHNICAL` by default.

---

## 5. Current security review

### Improved controls

`data_admin.php` now uses:

```text
session.use_strict_mode = 1
Secure cookie
HttpOnly cookie
SameSite=Strict
session ID regeneration after login
CSRF token for state-changing authenticated actions
login failure delay
X-Frame-Options: DENY
Referrer-Policy: no-referrer
no-store
```

The public deletion page:

```text
accepts deletion code only in POST body
never places code in URL
never persists plaintext code
uses a high-entropy possession token
returns a generic completion response
```

### Still open

The pre-existing `admin.php` timing dashboard still uses the older session setup. Its password authentication works, but its session/cookie hardening has not yet been brought to the same standard as `data_admin.php`.

Therefore:

```text
ADMIN SECURITY = PARTIAL / BLOCKING FINAL REVIEW
```

Before activation either:

1. harden the existing dashboard to the same session standard; or
2. place the entire `/server/` admin surface behind an additional Hostinger access-control layer and document the resulting design.

Do not describe a second password layer as MFA unless it actually uses a distinct authentication factor.

---

## 6. Methodology status is unchanged

None of these privacy/security changes validates any psychological claim.

```text
timing calibration         TESTABLE / NOT YET COLLECTING
Gate D                     NONE
Gate E                     NONE
CS/CR mapping              NOT VALIDATED
participant direction      NOT AUTHORIZED
reflection reasons         LOCAL ONLY
intensity                  LOCAL ONLY
```

---

## 7. Next technical sequence

```text
1. run CI on the current complete privacy-control batch
2. fix any regression
3. harden legacy admin.php session boundary
4. produce exact-head release artifact
5. do NOT deploy yet until migration/deploy order is documented
6. prepare Hostinger migration + cron runbook
7. owner deploys to LAB with collection_mode still TECHNICAL
8. execute live TECHNICAL privacy-control smoke tests
9. update public privacy copy to exact active processing
10. close Hostinger DPA/subprocessor/backup records
11. create CALIBRATION_ACTIVATION_RECORD_v0.1
12. explicit owner approval
13. only then switch live secret config to CALIBRATION
```

No merge to `main`, no replacement of `/wave1/`, and no participant directional interpretation are authorized by this checklist.
