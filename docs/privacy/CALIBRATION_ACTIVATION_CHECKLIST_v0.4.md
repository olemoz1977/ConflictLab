# ConflictLab — Calibration Activation Checklist v0.4

**Date:** 2026-08-15  
**Status:** NOT YET AUTHORIZED — LIVE TECHNICAL VALIDATION SUBSTANTIALLY COMPLETE  
**Target:** `calibration-v0.1` / `future-rapid-v1` / 6000 ms mechanical timing study only

> This checklist records the state after live Hostinger TECHNICAL smoke testing. It does not authorize psychological interpretation, Gate D, Gate E, participant scoring, or a public product switch.

## 1. Frozen boundaries

```text
collection_mode = TECHNICAL
Gate D = NONE
Gate E = NONE
CS/CR mappings = NOT VALIDATED
latency psychological meaning = NOT VALIDATED
participant directional result = NOT AUTHORIZED
/wave1/ = UNCHANGED
main branch = UNCHANGED
```

Mechanical timing calibration is methodologically separate from Gate D/E construct validation.

## 2. Current live code candidate

```text
live code head used for latest package: 94f5b2ef4794fd16d834b9ba4c1232120afd1ca6
workflow: Future Session Baseline
run: 31854625718 (#493)
CI: SUCCESS
artifact id: 9238634000
artifact digest: sha256:ddc78697c49c6cc48e5ea8e911630451dc4d5d5ae2571dad49e5c54fc583fc0c
```

The current repository head may be later because documentation-only commits do not change the deployed bytes.

## 3. Live TECHNICAL checks completed

```text
PASS live server reports SERVER MODE: TECHNICAL
PASS isolated calibration DB exists
PASS migration_002_consent_fields.sql applied successfully
PASS migration_003_deletion_token.sql applied successfully
PASS secret config contains consent_version
PASS secret config contains retention_days = 90
PASS secret config remains collection_mode = TECHNICAL
PASS latest package deployed while preserving secret config.php
PASS LT consented TECHNICAL end-to-end smoke on current privacy-control flow
PASS explicit 18+ declaration
PASS explicit voluntary research opt-in
PASS privacy link at collection point
PASS local-only alternative is present
PASS consent metadata reaches persisted TECHNICAL runs
PASS participant deletion code is generated before research upload
PASS plaintext deletion code is not stored in research DB
PASS server-side deletion-token hash supports lookup/deletion
PASS deletion code is locally retained in same browser as a withdrawal convenience
PASS self-service deletion removed the matching run + attempts + pair events
PASS same-browser deletion page auto-filled the locally retained code
PASS local deletion-code entry was removed after successful deletion
PASS TECHNICAL run deletion changed admin count without affecting N/20
PASS timing CSV export produced real TECHNICAL event rows
PASS timing CSV excludes deletion-token hash, session/message UUID, IP, User-Agent, reason/free text, intensity, and psychological result
PASS admin still reports CALIBRATION N/20 = 0/20
PASS daily retention cron configured to CLI retention_cleanup.php
PASS cron schedule = 0 0 * * *
PASS Hostinger primary server location re-confirmed as Lithuania
PASS Hostinger backup location re-confirmed as France
PASS weekly backup configuration observed
```

## 4. Items not yet closed

### A1 — EN current-artifact smoke

**PENDING.** Earlier EN flow tests existed, but the final pre-upload/localStorage deletion-code path has not yet been re-smoked in English on the current live artifact.

Required result:

```text
EN consent copy renders correctly
pre-upload deletion code renders correctly
localStorage fallback works
research upload succeeds in TECHNICAL mode
result remains NOT_ESTIMABLE
```

The disposable EN run should then be deleted.

### A2 — local-only no-upload proof

**PENDING.** The local-only button is present, but the final live artifact still needs an explicit end-to-end proof that choosing no research upload creates no new research DB run.

Required proof:

```text
admin TECHNICAL count before = N
complete local-only flow
admin TECHNICAL count after = N
```

### A3 — authenticated data-admin deletion smoke

**PENDING.** Public self-service deletion is proven. The authenticated `data_admin.php` lookup + transactional deletion path has not yet been live-smoked.

This is operational fallback capability, not a participant requirement, but it should be tested before external collection.

### A4 — first scheduled retention execution evidence

**PENDING FIRST RUN.** Script, configuration, path and cron schedule are in place. Hostinger had no output yet because the cron had not executed after creation.

Expected normal output with no expired runs:

```text
retention_cleanup deleted_runs=0
```

This is not evidence of construct validity; it is only an operational retention control.

### A5 — active public privacy wording

**BLOCKER BEFORE EXTERNAL COLLECTION.** `/privacy.html` must remain PREPARATION while `collection_mode = TECHNICAL`, but immediately before activation its Calibration section must be synchronized with the actual live processing.

The current repository `PRIVACY_NOTICE_TIMING_RESEARCH_v0.2.md` is now stale on one material UX detail: it says the deletion code is shown after successful upload. The live implementation intentionally creates/displays it before the measured block and stores it locally in the browser as a withdrawal convenience.

Before activation, public privacy information must disclose at least:

```text
controller + contact
18+ voluntary consent-based timing purpose
local-only/no-upload alternative
exact minimal server-side data classes
no reflection reason/free-text/intensity/result upload
pre-upload random deletion code
server stores only SHA-256 deletion-token hash
browser localStorage stores plaintext deletion code locally as a withdrawal convenience
localStorage value is not uploaded/exported/analyzed
self-service + email deletion routes
active DB maximum 90-day retention
Hostinger backup residual-copy qualification
Hostinger Lithuania primary / France backup
Hostinger access logs as separate technical layer
no OMESG360 marketing/ad trackers
```

Because browser storage is used, the pre-consent transparency copy must make that local storage purpose clear before the code is written.

### A6 — activation record + exact release freeze

**PENDING.** Create `CALIBRATION_ACTIVATION_RECORD_v0.1.md` only after A1-A5 close. It must record the exact live code artifact/digest, privacy notice version, consent version, retention state, Hostinger mode immediately before switch, and the activation timestamp.

### A7 — explicit owner authorization

**PENDING.** No automatic activation. Only the owner can explicitly authorize the first external mechanical timing study.

After authorization, change only:

```text
'collection_mode' => 'CALIBRATION'
```

Do not merge to `main`, change `/wave1/`, promote Gate D/E, or enable participant directional results as part of that switch.

## 5. Historical checklist corrections

`CALIBRATION_ACTIVATION_CHECKLIST_v0.3.md` is preserved as history. Its L11 expected the deletion code only after successful upload. That requirement is superseded.

Current requirement:

```text
consent
-> create + display deletion code locally
-> retain code locally as withdrawal convenience
-> participant confirms awareness/saving
-> measured block
-> if completed, upload timing data with deletion-token hash only
```

If the block is abandoned before upload, no research run exists. If upload succeeds and the browser closes later, the participant already possesses the deletion handle.

## 6. Readiness verdict

```text
ENGINEERING / DATA-MINIMIZATION CONTROLS      READY
LIVE CONSENTED TECHNICAL PATH                 PASS
SELF-SERVICE WITHDRAWAL                      PASS
TIMING CSV EXPORT                            PASS
RETENTION CONFIGURATION                      PASS
RETENTION FIRST SCHEDULED EXECUTION           PENDING
FINAL EN SMOKE                               PENDING
LOCAL-ONLY NO-DB PROOF                       PENDING
ADMIN FALLBACK DELETION SMOKE                PENDING
ACTIVE PUBLIC PRIVACY ALIGNMENT               BLOCKER
ACTIVATION RECORD                             PENDING
OWNER AUTHORIZATION                           PENDING

OVERALL: DO NOT SWITCH TO CALIBRATION YET
```

The remaining work is activation hygiene, not a methodological claim that CS/CR or participant interpretation is valid.
