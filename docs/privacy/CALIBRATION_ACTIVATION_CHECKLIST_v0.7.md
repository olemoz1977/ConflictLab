# ConflictLab — Calibration Activation Checklist v0.7

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

## Live checks closed

```text
PASS final c72bde02 artifact deployed with secret config preserved
PASS server remains TECHNICAL
PASS LT consented TECHNICAL flow
PASS final EN consented TECHNICAL flow
PASS EN pre-upload deletion code renders before measured block
PASS browser-local deletion-code retention works on final artifact
PASS final result remains NOT_ESTIMABLE; no CS/CR interpretation shown
PASS consented runs persist only as TECHNICAL
PASS CALIBRATION N/20 remains 0/20
PASS local-only complete flow creates no DB run
PASS public self-service deletion
PASS timing CSV export with prohibited/private fields excluded
PASS authenticated data_admin.php deletion lookup resolves one matching TECHNICAL run
PASS authenticated transactional admin deletion removes the run and its timing dataset
PASS admin deletion smoke count moved 5 -> 6 -> 5
PASS daily retention cron configured: 0 0 * * *
```

## Remaining activation items

### R5 — first scheduled retention execution

**PENDING FIRST RUN.** Cron path/schedule are configured. Capture the first Hostinger cron output after scheduled execution. Expected with no expired runs:

```text
retention_cleanup deleted_runs=0
```

If activation is intentionally performed before the first scheduled execution, that must be recorded as an explicit temporary operational residual-risk acceptance. The cron configuration itself is already in place.

### R6 — live public privacy alignment

**BLOCKER BEFORE EXTERNAL COLLECTION.** `/privacy.html` must be synchronized from PREPARATION wording to the active `PRIVACY_NOTICE_TIMING_RESEARCH_v0.3` processing profile immediately before external calibration starts.

The public active wording must match the actual implementation, including:

```text
18+ voluntary timing-research consent
local-only / no-upload alternative
pre-upload deletion code
plaintext deletion code retained only in participant browser localStorage as a withdrawal convenience
server stores only SHA-256 deletion-token hash
no reason/free-text/intensity/directional result upload
active research DB retention max 90 days
self-service + email deletion routes
Hostinger primary Lithuania / backup France
backup residual-copy qualification
Hostinger access logs as separate technical processing
no OMESG360 marketing/ad trackers for the timing study
```

### R7 — activation record

**PENDING.** After R5/R6 are resolved or R5 is explicitly accepted as temporary residual risk, create `CALIBRATION_ACTIVATION_RECORD_v0.1.md` containing:

```text
exact code artifact + digest
privacy notice version
consent evidence version
deployed Hostinger path
retention cron state
backup state
pre-switch collection_mode = TECHNICAL
activation timestamp
owner authorization statement
post-switch collection_mode = CALIBRATION
```

### R8 — explicit owner authorization

**PENDING.** No automatic switch. Only after explicit owner authorization may the live secret config change from:

```text
'collection_mode' => 'TECHNICAL'
```

to:

```text
'collection_mode' => 'CALIBRATION'
```

This does not authorize Gate D/E, psychological interpretation, participant directional results, `/wave1/` changes, or merge to `main`.

## Current verdict

```text
FINAL LT/EN TECHNICAL PARTICIPANT FLOW         PASS
LOCAL-ONLY NO-DB PROOF                        PASS
SELF-SERVICE WITHDRAWAL                       PASS
AUTHENTICATED ADMIN FALLBACK DELETION         PASS
TIMING CSV                                    PASS
RETENTION CONFIGURATION                       PASS
RETENTION FIRST SCHEDULED EXECUTION            PENDING
PUBLIC PRIVACY ACTIVE WORDING                 BLOCKER
ACTIVATION RECORD                             PENDING
OWNER AUTHORIZATION                           PENDING

OVERALL: DO NOT SWITCH TO CALIBRATION YET
```
