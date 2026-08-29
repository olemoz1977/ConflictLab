# 2026-08-15 — Calibration privacy controls implementation

## Scope

Implemented the privacy/operational controls required before the versioned `calibration-v0.1` LAB can ever be considered for real external `CALIBRATION` collection.

This work does **not** authorize external participant collection and does not change Gate D/E.

## Starting state

Before this implementation batch:

```text
collection_mode = TECHNICAL
consent UI = absent
18+ declaration = absent
local-only research refusal = absent
consent evidence in DB = absent
withdrawal/deletion handle = absent
retention cleanup = absent
admin CSV export = absent
Gate D = NONE
Gate E = NONE
```

## Implemented

### Participant boundary

- dedicated timing-research choice screen after training;
- explicit 18+ declaration;
- unchecked research-consent checkbox;
- direct `/privacy.html` link;
- local-only path with no research upload;
- refusal is not interpreted as a psychological signal;
- LT/EN copy.

### Consent evidence

- consent version `timing-research-consent-v0.1`;
- browser sends consent version / affirmative consent / 18+ confirmation for consented upload;
- server rejects CALIBRATION uploads without exact affirmative consent evidence;
- consent evidence stored at run level;
- legacy TECHNICAL payloads remain compatible until the new UI/release is deployed.

### Withdrawal / erasure

- client generates 128-bit random plaintext deletion code;
- plaintext code is shown only to the participant after successful upload;
- client sends SHA-256 hash only;
- server stores only `deletion_token_hash`;
- authenticated `data_admin.php` can locate/delete by participant code;
- deletion transaction removes pair events -> attempts -> run;
- public `delete_my_data.php` provides self-service erasure using the same possession token;
- no participant email is collected merely to support deletion.

### Retention

- `retention_days = 90` in config example;
- CLI-only `retention_cleanup.php`;
- transactional child->parent deletion;
- aggregate cleanup count output only;
- live Hostinger cron still required and unverified.

### Admin export

- authenticated `data_admin.php`;
- CSV streamed directly to browser;
- no persistent generated CSV file;
- filters: type / form / device / eligibility;
- export schema `timing-export-v0.1`;
- deletion token hash, message/session UUIDs, IP/user-agent and local reflection channels excluded.

### DB migrations

Required for existing LAB DB:

```text
migration_002_consent_fields.sql
migration_003_deletion_token.sql
```

These have not yet been confirmed applied to Hostinger.

## CI

Final metadata-aligned repository head for this batch:

```text
8eaf2dcea7a9863e2a11fd9e67ef97cfaaf5a5e9
```

GitHub Actions:

```text
workflow: Future Session Baseline
run: 31851659459 / #465
result: SUCCESS
```

Artifact:

```text
artifact id: 9237707344
workflow head_sha: 8eaf2dcea7a9863e2a11fd9e67ef97cfaaf5a5e9
digest: sha256:05e868794eee2d45ec1b7c989aed48005224f2e5a2d34cd4817237c8fd6139e9
```

Artifact filename contains a workflow-generated short token that is not used as provenance. `workflow_run.head_sha` is authoritative.

## Release metadata correction

During artifact inspection, the previous release manifest/README were found stale: they still said DB migration was not required.

Corrected before final artifact:

- `release-manifest.json` now declares migrations 002/003;
- deployment state requires TECHNICAL after overwrite;
- consent / deletion / retention / export controls are listed;
- README now defines the safe migration/deployment/smoke order.

## Current authorization state

```text
repository privacy-control implementation   READY FOR TECHNICAL LAB VALIDATION
live DB migrations                          NOT VERIFIED
live artifact overwrite                     NOT DONE
live retention cron                         NOT DONE
live privacy-control smoke tests             NOT DONE
Hostinger processor/subprocessor record      OPEN
legacy timing dashboard hardening            PARTIAL
collection_mode                              KEEP TECHNICAL
external CALIBRATION                         NOT AUTHORIZED
Gate D                                       NONE
Gate E                                       NONE
participant directional result               NOT AUTHORIZED
/wave1                                       UNCHANGED
```

## Next sequence

1. prepare/use Hostinger deployment runbook;
2. owner applies migrations 002/003 to isolated calibration DB;
3. owner adds consent version + retention days to secret config while keeping TECHNICAL;
4. owner overwrites versioned LAB with exact-head artifact;
5. execute privacy-control TECHNICAL smoke tests;
6. configure/test Hostinger cron;
7. close Hostinger processor/subprocessor/backup record;
8. harden or additionally protect legacy timing dashboard;
9. only after all activation checklist blockers close create `CALIBRATION_ACTIVATION_RECORD_v0.1.md`;
10. explicit owner authorization is required before any switch to CALIBRATION.
