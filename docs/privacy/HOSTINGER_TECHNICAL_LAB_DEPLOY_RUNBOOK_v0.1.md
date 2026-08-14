# ConflictLab — Hostinger TECHNICAL LAB Deploy Runbook v0.1

**Scope:** deploy the privacy-control update to the existing versioned LAB only.  
**Target path:** `/public_html/conflictlab/releases/calibration-v0.1/`  
**Safety state:** `collection_mode = TECHNICAL` throughout.  
**Public `/wave1/`:** do not modify.

## 0. Preconditions

Artifact source:

```text
workflow run: 31851659459 (#465)
workflow head_sha: 8eaf2dcea7a9863e2a11fd9e67ef97cfaaf5a5e9
artifact id: 9237707344
artifact digest: sha256:05e868794eee2d45ec1b7c989aed48005224f2e5a2d34cd4817237c8fd6139e9
CI: SUCCESS
```

Before beginning, verify in the live secret `server/config.php`:

```php
'collection_mode' => 'TECHNICAL',
```

Do not paste DB credentials or admin-password hashes into chat/screenshots.

---

## 1. Back up current LAB

Back up only the versioned LAB and its isolated calibration DB before changing them.

Do not change:

```text
/public_html/wave1/
/public_html/privacy.html
OMESG360 root index
```

The current public privacy page stays in PREPARATION state during TECHNICAL testing.

---

## 2. Apply DB migration 002

Use Hostinger phpMyAdmin / SQL against the isolated calibration database.

Run the exact contents of:

```text
server/migration_002_consent_fields.sql
```

Expected new nullable columns in `cl_calibration_runs`:

```text
consent_version
research_consent
age_18_confirmed
```

Existing TECHNICAL runs should remain valid with NULL values in these fields.

---

## 3. Apply DB migration 003

Run the exact contents of:

```text
server/migration_003_deletion_token.sql
```

Expected new field/index:

```text
deletion_token_hash CHAR(64) NULL
UNIQUE index uq_cl_calibration_runs_deletion_token
```

Plaintext deletion codes must never be stored in the DB.

---

## 4. Update the existing secret config.php

Keep all existing real credentials and the existing admin password hash.

Add only these keys if absent:

```php
'consent_version' => 'timing-research-consent-v0.1',
'retention_days' => 90,
```

Confirm again:

```php
'collection_mode' => 'TECHNICAL',
```

Do not replace the live `config.php` with `config.example.php`.

---

## 5. Overwrite the versioned LAB application bytes

Extract the successful-CI artifact directly into:

```text
/public_html/conflictlab/releases/calibration-v0.1/
```

Overwrite existing release files.

Critical:

```text
preserve server/config.php
no extra nested calibration-v0.1 directory
no /wave1/ changes
no root privacy/index changes
```

After extraction, verify these files exist:

```text
server/data_admin.php
server/delete_my_data.php
server/retention_cleanup.php
server/migration_002_consent_fields.sql
server/migration_003_deletion_token.sql
```

---

## 6. TECHNICAL smoke test — participant UI

Use the LAB URL, not `/wave1/`.

### Test A — local-only path

1. choose LT;
2. complete Stage 0 training;
3. verify consent screen appears;
4. verify both boxes are unchecked initially;
5. confirm 18+ only;
6. choose `Tęsti be tyrimo duomenų įkėlimo`;
7. complete the measured block and reflection;
8. verify result says research upload was not selected;
9. verify no new `cl_calibration_runs` row was created for this session.

### Test B — consented TECHNICAL path

1. choose EN or LT;
2. complete training;
3. open the privacy link and verify it points to `/privacy.html` in the correct language;
4. confirm 18+ and research consent;
5. complete measured block;
6. verify timing upload succeeds;
7. verify final screen shows a 32-character deletion code;
8. copy/save the code temporarily for deletion testing;
9. verify admin shows the run as `TECHNICAL`;
10. verify N/20 remains `0/20`.

---

## 7. Verify stored fields

For the consented disposable TECHNICAL run, confirm `cl_calibration_runs` contains:

```text
run_type = TECHNICAL
consent_version = timing-research-consent-v0.1
research_consent = 1
age_18_confirmed = 1
deletion_token_hash = 64 lowercase hex characters
```

Do not attempt to reverse or display the hash as a participant code.

Verify timing tables still do not contain local reason/free-text/intensity fields.

---

## 8. Test authenticated admin deletion

Open:

```text
/conflictlab/releases/calibration-v0.1/server/data_admin.php
```

Log in using the existing admin password.

Enter the disposable participant deletion code from Test B.

Verify the tool locates the run, then explicitly confirm deletion.

After deletion verify:

```text
run row = gone
attempt rows = gone
pair event rows = gone
```

Do not use a non-disposable run for this test.

---

## 9. Test self-service deletion

Create a new consented disposable TECHNICAL run and save its deletion code.

Open:

```text
/conflictlab/releases/calibration-v0.1/server/delete_my_data.php?lang=lt
```

Enter the code and confirm deletion.

Verify the run/attempt/events disappear from DB/admin.

The public page should not reveal whether an arbitrary invalid code exists.

---

## 10. Test CSV export

Open `data_admin.php` and export CSV.

Expected export schema:

```text
timing-export-v0.1
```

Verify the CSV does not contain:

```text
deletion_token_hash
message_id
session_id
IP
user-agent
reason_id
free text
intensity
psychological result
```

Verify it does contain the timing/mechanical fields documented in `TIMING_EXPORT_SCHEMA_v0.1.md`.

---

## 11. Configure retention cron

Create a Hostinger cron that runs the PHP CLI script:

```text
/public_html/conflictlab/releases/calibration-v0.1/server/retention_cleanup.php
```

Recommended operational cadence for a 90-day maximum retention rule:

```text
DAILY
```

The exact PHP executable/path must be taken from the Hostinger cron UI/environment; do not guess it from local development paths.

Cron output must contain only aggregate status such as:

```text
retention_cleanup deleted_runs=0
```

Before relying on the 90-day rule for real participants, test cleanup with disposable TECHNICAL data or a controlled temporary retention configuration in an isolated test context. Do not alter the live declared retention merely to force-delete genuine participant data during testing.

---

## 12. Post-deploy verification

After all TECHNICAL tests:

```text
collection_mode = TECHNICAL
Calibration N/20 = 0/20
Gate D = NONE
Gate E = NONE
/wave1/ unchanged
privacy.html still describes Calibration as not yet active for external research
```

Record:

```text
deployment date/time
artifact digest
migration 002 result
migration 003 result
config update result
LT smoke result
EN smoke result
local-only DB check
consented upload result
admin deletion result
self-service deletion result
CSV result
cron result
```

---

## 13. What this deployment does NOT authorize

Even after every TECHNICAL smoke test passes:

```text
DO NOT switch collection_mode to CALIBRATION
DO NOT invite fresh external calibration participants yet
DO NOT change /wave1/
DO NOT merge to main solely because LAB works
DO NOT enable Gate D/E
DO NOT show participant directional results
```

The next gate is `CALIBRATION_ACTIVATION_CHECKLIST_v0.2.md` plus Hostinger processor/backup/security closure and explicit owner authorization.
