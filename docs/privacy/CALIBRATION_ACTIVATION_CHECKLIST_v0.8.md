# ConflictLab — Calibration Activation Checklist v0.8

**Date:** 2026-08-15  
**Status:** FINAL TECHNICAL CANDIDATE / ACTIVATION MATERIALS PREPARED / EXTERNAL CALIBRATION NOT YET AUTHORIZED

## Frozen boundary

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
PASS final artifact deployed with secret config preserved
PASS server remains TECHNICAL
PASS LT consented TECHNICAL flow
PASS EN consented TECHNICAL flow
PASS pre-upload deletion code
PASS browser-local deletion-code retention
PASS result remains NOT_ESTIMABLE
PASS no CS/CR participant interpretation
PASS consented runs persist only as TECHNICAL
PASS CALIBRATION N/20 remains 0/20
PASS local-only complete flow creates no DB run
PASS public self-service deletion
PASS authenticated data_admin deletion lookup
PASS authenticated transactional admin deletion
PASS timing CSV real-row export
PASS prohibited/private fields excluded from timing CSV
PASS daily retention cron configured at 0 0 * * *
PASS Hostinger primary = Lithuania
PASS Hostinger backup location = France
PASS weekly backup configuration previously observed
```

## Activation materials prepared

```text
PASS PRIVACY_NOTICE_TIMING_RESEARCH_v0.3 documented
PASS current single public Privacy Centre recovered as source baseline
PASS ACTIVE public privacy candidate prepared offline from that baseline
PASS ACTIVE candidate preserves general OMESG360 + Wave 1 sections
PASS ACTIVE candidate updates only Calibration processing profile + retention entry
PASS ACTIVE candidate includes 18+, consent, local-only, exact timing payload boundaries
PASS ACTIVE candidate includes pre-upload deletion code + localStorage boundary
PASS ACTIVE candidate includes self-service/email erasure routes
PASS ACTIVE candidate includes max 90-day active DB retention + backup residual-copy qualification
PASS ACTIVE candidate LT/EN stale PREPARATION phrases removed
PASS ACTIVE candidate HTML parser smoke passed
PASS controlled public privacy activation plan documented
PASS activation-record template documented
```

Prepared files / docs:

```text
docs/privacy/PRIVACY_NOTICE_TIMING_RESEARCH_v0.3.md
docs/privacy/PUBLIC_PRIVACY_ACTIVE_DEPLOY_PLAN_v0.1.md
docs/privacy/CALIBRATION_ACTIVATION_RECORD_TEMPLATE_v0.1.md
```

The ACTIVE HTML candidate is intentionally **not published live yet** because public ACTIVE wording with a TECHNICAL server would be inconsistent.

## Remaining activation items

### R5 — first scheduled retention execution evidence

**PENDING FIRST RUN.** Cron configuration is live. Preferred evidence:

```text
retention_cleanup deleted_runs=0
```

Because the cron was configured after the current day's midnight run window, the first normal scheduled evidence is expected at the next `0 0 * * *` execution.

If owner intentionally activates before that evidence exists, the activation record must explicitly record temporary residual-risk acceptance and require follow-up after the first run.

### R6 — publish ACTIVE public privacy wording during controlled activation window

**PREPARED / NOT EXECUTED.** Candidate is ready offline. During activation:

```text
back up current /privacy.html
upload ACTIVE candidate
verify LT + EN render and Calibration says ACTIVE
keep interval short before collection_mode switch
if activation aborts, restore PREPARATION privacy wording
```

### R7 — final activation record

**TEMPLATE READY / FINAL RECORD PENDING.** Fill only during the real activation switch with live timestamp/evidence.

### R8 — explicit owner authorization

**PENDING.** Do not infer authorization from testing activity.

Only after explicit owner authorization may live secret config change:

```text
'collection_mode' => 'TECHNICAL'
```

to:

```text
'collection_mode' => 'CALIBRATION'
```

## Current verdict

```text
FINAL LT/EN TECHNICAL PARTICIPANT FLOW         PASS
LOCAL-ONLY NO-DB PROOF                        PASS
SELF-SERVICE WITHDRAWAL                       PASS
AUTHENTICATED ADMIN FALLBACK DELETION         PASS
TIMING CSV                                    PASS
RETENTION CONFIGURATION                       PASS
RETENTION FIRST SCHEDULED EXECUTION            PENDING
ACTIVE PRIVACY CANDIDATE                      READY OFFLINE
PUBLIC PRIVACY LIVE ACTIVE WORDING            PENDING CONTROLLED SWITCH
ACTIVATION RECORD TEMPLATE                    READY
FINAL ACTIVATION RECORD                       PENDING
OWNER AUTHORIZATION                           PENDING

OVERALL: TECHNICAL READINESS COMPLETE; DO NOT SWITCH TO CALIBRATION YET
```
