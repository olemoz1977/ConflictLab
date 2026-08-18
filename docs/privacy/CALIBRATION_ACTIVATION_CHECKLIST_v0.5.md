# ConflictLab — Calibration Activation Checklist v0.5

**Date:** 2026-08-15  
**Status:** FINAL TECHNICAL CANDIDATE / NOT YET AUTHORIZED FOR EXTERNAL CALIBRATION  
**Target:** `calibration-v0.1` / `future-rapid-v1` / 6000 ms mechanical timing only

## 1. Non-negotiable boundary

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

## 2. Current authoritative deployment candidate

```text
code head: c72bde02c9358ff15d2ebb5e6c9f8eea2455c3a4
workflow: Future Session Baseline
run: 31856033244 (#503)
CI: SUCCESS
artifact id: 9239045582
artifact digest: sha256:5be68e7347f1a8bd340954f0ea5656c446f86cceba668fa08704829443d2f8df
```

This candidate adds explicit pre-consent disclosure that, if the participant opts in, the browser creates a deletion code and may retain that plaintext code only in local browser storage as a withdrawal convenience. The plaintext code is not sent to the research server.

## 3. Live controls already proven on the immediately preceding candidate

```text
PASS collection_mode TECHNICAL
PASS DB consent + deletion-token migrations
PASS consent_version configured
PASS retention_days = 90
PASS explicit 18+ + voluntary research opt-in
PASS local-only alternative present
PASS pre-upload deletion code
PASS server stores deletion-token hash only
PASS same-browser local code retention
PASS public self-service deletion end-to-end
PASS local code cleanup after deletion
PASS admin TECHNICAL/CALIBRATION separation; N/20 remains 0/20
PASS timing CSV with real TECHNICAL rows
PASS prohibited/private fields excluded from timing CSV
PASS daily retention cron configured: 0 0 * * *
PASS Hostinger primary = Lithuania
PASS Hostinger backup location = France
PASS weekly backup configuration observed
```

The c72bde02 code change only alters pre-consent disclosure text in the delivery adapter. It does not expand server payload, research purpose, retention, DB schema, Gate D/E, or participant result behavior. Nevertheless the final candidate must be deployed and the final participant-facing smoke checks below must be run against it.

## 4. Privacy/consent release candidate

```text
consent evidence version: timing-research-consent-v0.1
consent documentation: TIMING_RESEARCH_CONSENT_v0.1.md
privacy release candidate: PRIVACY_NOTICE_TIMING_RESEARCH_v0.3.md
```

Privacy Notice v0.3 now reflects:

```text
pre-upload deletion code
localStorage plaintext code only on participant device/browser profile
up to 12 recent local deletion codes
no plaintext code in server research DB
server SHA-256 hash only
local code excluded from export/analysis
self-service + email deletion
active DB max 90 days
backup residual-copy qualification
Hostinger logs separated from research dataset
local-only/no-upload path
```

The public `/privacy.html` remains PREPARATION while the server remains TECHNICAL. It must be synchronized to this active processing profile immediately before external collection is authorized.

## 5. Remaining activation checks

### R1 — deploy exact c72bde02 artifact

**PENDING LIVE DEPLOY.** Preserve `server/config.php`. Do not repeat DB migrations. Keep `collection_mode = TECHNICAL`.

### R2 — final EN consented smoke

**PENDING.** Verify on c72bde02:

```text
EN consent disclosure includes local browser storage
pre-upload deletion-code screen works
main block uploads as TECHNICAL
result remains NOT_ESTIMABLE
same-browser delete page can recover the code
```

Delete the disposable EN run afterward.

### R3 — final local-only no-DB proof

**PENDING.** Record TECHNICAL count before and after a complete local-only flow. Count must not change.

### R4 — authenticated data-admin deletion smoke

**PENDING.** Prove lookup + transactional deletion through `data_admin.php` using a disposable TECHNICAL run/deletion code.

### R5 — first scheduled retention execution

**PENDING FIRST RUN.** Cron exists and schedule/path are correct. Capture the first Hostinger result. Normal current result should be:

```text
retention_cleanup deleted_runs=0
```

This may be treated as a monitored operational follow-up only if the owner explicitly accepts that residual risk before activation; otherwise wait for first run.

### R6 — live public privacy alignment

**BLOCKER.** Immediately before activation, replace the Calibration PREPARATION wording in `/privacy.html` with the active v0.3 processing profile. Do not publish active wording while the study is still intentionally TECHNICAL unless clearly labelled as upcoming/not active.

### R7 — activation record

**PENDING.** After R1-R6 close, create `CALIBRATION_ACTIVATION_RECORD_v0.1.md` recording exact artifact, digest, live privacy version, consent version, cron state, Hostinger mode, activation date/time and owner authorization.

### R8 — explicit owner authorization

**PENDING.** No automatic switch.

Only after explicit authorization may the live secret change from:

```text
'collection_mode' => 'TECHNICAL'
```

to:

```text
'collection_mode' => 'CALIBRATION'
```

That switch does not authorize Gate D/E, psychological interpretation, public product deployment, `/wave1/` changes, or merge to `main`.

## 6. Verdict

```text
ENGINEERING / PRIVACY-BY-DESIGN CONTROLS      READY AS FINAL CANDIDATE
CURRENT LIVE MODE                             TECHNICAL
FINAL ARTIFACT DEPLOY                         PENDING
FINAL EN SMOKE                                PENDING
LOCAL-ONLY NO-DB PROOF                        PENDING
ADMIN FALLBACK DELETION                       PENDING
RETENTION FIRST SCHEDULED RUN                 PENDING
PUBLIC PRIVACY ACTIVE WORDING                 BLOCKER
ACTIVATION RECORD                             PENDING
OWNER AUTHORIZATION                           PENDING

OVERALL: DO NOT SWITCH TO CALIBRATION YET
```
