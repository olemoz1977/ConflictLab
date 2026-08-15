# ConflictLab — Calibration Activation Checklist v0.6

**Date:** 2026-08-15  
**Status:** FINAL TECHNICAL CANDIDATE / NOT YET AUTHORIZED FOR EXTERNAL CALIBRATION

## Frozen boundary

```text
collection_mode = TECHNICAL
Gate D = NONE
Gate E = NONE
CS/CR mappings = NOT VALIDATED
participant directional result = NOT AUTHORIZED
/wave1/ = UNCHANGED
main branch = UNCHANGED
```

## Authoritative deployment candidate

```text
code head: c72bde02c9358ff15d2ebb5e6c9f8eea2455c3a4
workflow run: 31856033244 (#503)
CI: SUCCESS
artifact id: 9239045582
artifact digest: sha256:5be68e7347f1a8bd340954f0ea5656c446f86cceba668fa08704829443d2f8df
```

## Live checks now closed

```text
PASS final c72bde02 artifact deployed with secret config preserved
PASS server remains TECHNICAL
PASS LT consented TECHNICAL flow
PASS final EN consented TECHNICAL flow
PASS EN pre-upload deletion code renders before measured block
PASS browser-local deletion-code retention works on final artifact
PASS final result remains NOT_ESTIMABLE; no CS/CR interpretation shown
PASS consented EN run persisted as TECHNICAL
PASS CALIBRATION N/20 remained 0/20
PASS local-only complete flow created no DB run
PASS public self-service deletion removed disposable EN run
PASS TECHNICAL count moved 5 -> 6 -> 5 during consented run + deletion
PASS timing CSV export
PASS daily retention cron configured: 0 0 * * *
```

## Remaining activation items

### R4 — authenticated data-admin deletion smoke

**PENDING.** Public `delete_my_data.php` deletion is proven. The separate authenticated fallback in `server/data_admin.php` still needs one live disposable TECHNICAL run.

Required proof:

```text
create consented disposable TECHNICAL run
TECHNICAL count N -> N+1
open authenticated data_admin.php
paste participant deletion code into deletion lookup
lookup resolves exactly one matching TECHNICAL run
confirm transactional deletion
TECHNICAL count N+1 -> N
```

### R5 — first scheduled retention execution

**PENDING FIRST RUN.** Cron path/schedule are configured correctly. Capture first Hostinger output after scheduled execution. Expected with no expired runs:

```text
retention_cleanup deleted_runs=0
```

### R6 — live public privacy alignment

**BLOCKER BEFORE EXTERNAL COLLECTION.** `/privacy.html` must be synchronized from PREPARATION wording to the active `PRIVACY_NOTICE_TIMING_RESEARCH_v0.3` processing profile immediately before activation.

### R7 — activation record

**PENDING.** Create `CALIBRATION_ACTIVATION_RECORD_v0.1.md` only after R4-R6 are closed or an explicitly documented operational residual-risk decision is made for R5.

### R8 — explicit owner authorization

**PENDING.** No automatic switch. Only after explicit owner authorization may secret config change:

```text
'collection_mode' => 'TECHNICAL'
```

to:

```text
'collection_mode' => 'CALIBRATION'
```

This does not authorize Gate D/E, psychological interpretation, `/wave1/` changes, participant directional results, or merge to `main`.

## Current verdict

```text
FINAL LT/EN TECHNICAL PARTICIPANT FLOW         PASS
LOCAL-ONLY NO-DB PROOF                        PASS
SELF-SERVICE WITHDRAWAL                       PASS
TIMING CSV                                    PASS
ADMIN FALLBACK DELETION                       PENDING
RETENTION FIRST SCHEDULED EXECUTION            PENDING
PUBLIC PRIVACY ACTIVE WORDING                 BLOCKER
ACTIVATION RECORD                             PENDING
OWNER AUTHORIZATION                           PENDING

OVERALL: DO NOT SWITCH TO CALIBRATION YET
```
