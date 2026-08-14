# ConflictLab — Calibration Activation Checklist v0.3

**Date:** 2026-08-15  
**Status:** BLOCKED ONLY BY LIVE/OWNER ACTIVATION STEPS  
**Target:** `calibration-v0.1` / `future-rapid-v1` / 6000 ms mechanical timing study

> Repository implementation is ready for Hostinger TECHNICAL validation. External CALIBRATION collection is still not authorized.

## 1. Repository controls now implemented

```text
PASS explicit voluntary timing-research opt-in
PASS 18+ declaration
PASS privacy link at collection point
PASS local-only / no-upload path
PASS consent metadata in payload, API and DB schema
PASS CALIBRATION server rejection without valid consent/18+
PASS random participant deletion code
PASS only SHA-256 deletion-token hash stored server-side
PASS authenticated admin lookup + transactional deletion
PASS public self-service deletion
PASS 90-day retention configuration + CLI cleanup implementation
PASS timing-only authenticated CSV export
PASS export schema versioning
PASS hardened data_admin session/security boundary
PASS hardened legacy timing admin session/security boundary
PASS Hostinger DPA/subprocessor/SCC review documented
PASS Hostinger primary server / backup locations documented
PASS Hostinger weekly backup lifecycle documented
PASS technical/security legitimate-interests assessment documented
PASS Gate D remains NONE
PASS Gate E remains NONE
```

## 2. Authoritative deployable code artifact

```text
code head: f082b7bab26e22d41e2ce7b3ddc88a0d8664a4cb
workflow: Future Session Baseline
run: 31852102217 (#477)
CI: SUCCESS
artifact id: 9237833028
artifact digest: sha256:c3a06882be5a258593476f330cff65d9bba30c6e295552d00deaf1f0c6e8f845
```

Artifact inspected after download; required privacy-control files and corrected manifest are present.

Docs committed after the code head do not change deploy bytes.

## 3. Remaining blockers are live operational checks

```text
L1  verify live secret config currently says collection_mode = TECHNICAL
L2  back up existing versioned LAB + isolated calibration DB
L3  apply migration_002_consent_fields.sql
L4  apply migration_003_deletion_token.sql
L5  add consent_version + retention_days to secret config.php
L6  deploy exact authoritative artifact while preserving secret config.php
L7  LT TECHNICAL smoke
L8  EN TECHNICAL smoke
L9  local-only path -> confirm no DB run
L10 consented TECHNICAL path -> consent fields/hash stored
L11 verify deletion code shown only after successful upload
L12 authenticated admin deletion smoke
L13 public self-service deletion smoke
L14 timing-export-v0.1 CSV smoke
L15 configure and verify Hostinger daily retention cron
L16 re-confirm live backup setting immediately before activation
L17 align public privacy.html Calibration section from PREPARATION to exact active processing
L18 create CALIBRATION_ACTIVATION_RECORD_v0.1
L19 explicit owner authorization
```

Until L1-L19 close:

```text
collection_mode = TECHNICAL
external CALIBRATION = NOT AUTHORIZED
```

## 4. Privacy wording boundary

Current public `/privacy.html` should stay in PREPARATION mode during TECHNICAL testing.

The future active wording should be derived from:

```text
docs/privacy/PRIVACY_NOTICE_TIMING_RESEARCH_v0.2.md
```

and must disclose at minimum:

```text
controller: Oleg Mozochin
contact: info@omesg360.eu
consent-based timing purpose only
18+
local-only option
exact minimal server data classes
no reason/free-text/intensity/result upload
active DB max 90 days
deletion code + self-service/email paths
Hostinger Lithuania primary / France backup
backup residual-copy qualification
Hostinger access logs separate from research DB
no marketing/ad tracking in OMESG360 code
```

Do not mark Calibration active in public privacy copy before the live TECHNICAL smoke suite passes.

## 5. Activation state after successful TECHNICAL deployment

Even when L1-L16 pass, external collection is still not automatic.

Required final sequence:

```text
public privacy active wording frozen
-> activation record created
-> owner explicitly authorizes external timing study
-> then and only then live secret config may change to CALIBRATION
```

The repository example config remains TECHNICAL.

## 6. Product/methodology boundary unchanged

```text
mechanical timing = the only planned external calibration claim
6000 ms = testable engineering candidate
Gate D = NONE
Gate E = NONE
CS/CR mappings = NOT VALIDATED
latency psychological meaning = NOT VALIDATED
participant directional result = NOT AUTHORIZED
/wave1/ = UNCHANGED
main branch = UNCHANGED
```
