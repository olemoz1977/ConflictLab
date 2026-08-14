# ConflictLab — Hostinger TECHNICAL LAB Deploy Runbook v0.2

**Date:** 2026-08-15  
**Scope:** deploy the privacy-control + hardened-admin update to the existing versioned LAB only.  
**Target path:** `/public_html/conflictlab/releases/calibration-v0.1/`  
**Safety state:** `collection_mode = TECHNICAL` throughout.  
**Public `/wave1/`:** do not modify.

## 0. Authoritative artifact

Use only the artifact tied to this exact code head:

```text
workflow: Future Session Baseline
run: 31852102217 (#477)
head_sha: f082b7bab26e22d41e2ce7b3ddc88a0d8664a4cb
artifact id: 9237833028
artifact digest: sha256:c3a06882be5a258593476f330cff65d9bba30c6e295552d00deaf1f0c6e8f845
CI: SUCCESS
```

The artifact has been inspected after download. It contains:

```text
server/admin.php                  hardened timing dashboard
server/data_admin.php             authenticated deletion + CSV
server/delete_my_data.php         self-service erasure
server/retention_cleanup.php      CLI retention cleanup
server/migration_002_consent_fields.sql
server/migration_003_deletion_token.sql
release-manifest.json             db_migration_required = true
```

Do not use an earlier calibration ZIP.

Before beginning, verify the live secret config still contains:

```php
'collection_mode' => 'TECHNICAL',
```

Never share DB credentials or the admin password hash in screenshots/chat.

---

## 1. Back up current LAB and isolated calibration DB

Back up only:

```text
/public_html/conflictlab/releases/calibration-v0.1/
current isolated calibration DB
```

Do not change:

```text
/public_html/wave1/
/public_html/privacy.html
OMESG360 root index
```

The public privacy page remains Calibration = PREPARATION during all TECHNICAL testing.

---

## 2. Apply migration 002

In phpMyAdmin, against the isolated calibration DB, run the exact SQL from:

```text
server/migration_002_consent_fields.sql
```

Expected new nullable `cl_calibration_runs` fields:

```text
consent_version
research_consent
age_18_confirmed
```

Existing TECHNICAL rows remain valid with NULL values.

---

## 3. Apply migration 003

Run:

```text
server/migration_003_deletion_token.sql
```

Expected:

```text
deletion_token_hash CHAR(64) NULL
UNIQUE uq_cl_calibration_runs_deletion_token
```

Plaintext deletion codes must never be stored in DB.

---

## 4. Update live secret `server/config.php`

Preserve all current credentials and existing `admin_password_hash`.

Add only if absent:

```php
'consent_version' => 'timing-research-consent-v0.1',
'retention_days' => 90,
```

Confirm again:

```php
'collection_mode' => 'TECHNICAL',
```

Do not replace secret `config.php` with `config.example.php`.

---

## 5. Overwrite versioned LAB bytes

Extract the authoritative artifact directly inside:

```text
/public_html/conflictlab/releases/calibration-v0.1/
```

Overwrite release files but preserve the existing secret:

```text
server/config.php
```

Do not create an extra nested `calibration-v0.1` directory.

After extraction confirm these exist:

```text
server/admin.php
server/data_admin.php
server/delete_my_data.php
server/retention_cleanup.php
server/migration_002_consent_fields.sql
server/migration_003_deletion_token.sql
```

---

## 6. TECHNICAL smoke A — local-only path

Use the LAB URL, not `/wave1/`.

```text
choose LT
complete Stage 0
consent screen appears
both checkboxes initially empty
confirm only 18+
choose "Tęsti be tyrimo duomenų įkėlimo"
complete main block + reflection
result confirms no research upload
```

Then confirm no new research run was created for that local-only execution.

---

## 7. TECHNICAL smoke B — consented upload

Use EN or LT.

```text
complete training
open privacy link -> /privacy.html?lang=<selected>
check 18+
check research consent
complete main block
upload succeeds
final screen shows 32-character deletion code
```

Save the disposable deletion code temporarily.

In `admin.php` verify:

```text
run_type = TECHNICAL
Calibration N/20 = 0/20
```

In DB verify the disposable run has:

```text
consent_version = timing-research-consent-v0.1
research_consent = 1
age_18_confirmed = 1
deletion_token_hash = 64 lowercase hex
```

Do not expose or attempt to reverse the hash.

---

## 8. Admin/security smoke

Open:

```text
/conflictlab/releases/calibration-v0.1/server/admin.php
```

Verify login succeeds over HTTPS and the timing dashboard works.

The deployed admin now uses:

```text
strict session mode
Secure cookie
HttpOnly cookie
SameSite=Strict
session ID regeneration
CSRF-protected logout
login failure delay
X-Frame-Options DENY
Referrer-Policy no-referrer
restrictive CSP
```

Then open:

```text
/conflictlab/releases/calibration-v0.1/server/data_admin.php
```

Verify the same admin password grants access to the separate data-admin surface.

---

## 9. Test authenticated deletion

In `data_admin.php`, enter the disposable code from smoke B.

Confirm deletion and verify:

```text
matching run row gone
matching attempt rows gone
matching pair-event rows gone
```

Do not use a non-disposable historical owner run.

---

## 10. Test self-service deletion

Create a second disposable consented TECHNICAL run and save its code.

Open:

```text
/conflictlab/releases/calibration-v0.1/server/delete_my_data.php?lang=lt
```

Enter code + explicit confirmation.

Verify the matching run/attempt/events disappear.

An invalid random code must not reveal whether a record exists.

---

## 11. Test timing CSV

In `data_admin.php`, download CSV.

Expected schema:

```text
timing-export-v0.1
```

Must NOT contain:

```text
deletion_token_hash
message_id
session_id
IP
User-Agent
reason_id
free text
intensity
psychological/directional result
```

It should contain only the documented timing/mechanical/governance columns.

---

## 12. Configure retention cron

Hostinger cron must execute the PHP CLI script:

```text
/public_html/conflictlab/releases/calibration-v0.1/server/retention_cleanup.php
```

Operational cadence:

```text
DAILY
```

Use the PHP command/path offered by the Hostinger cron UI; do not guess it.

Expected non-sensitive output example:

```text
retention_cleanup deleted_runs=0
```

The active DB retention target is 90 days. Hostinger weekly backup copies can remain in provider rotation for up to the separately documented backup lifecycle; they are not research-analysis data.

Before CALIBRATION activation, verify the cron actually runs.

---

## 13. Final TECHNICAL state after deployment

Must still be:

```text
collection_mode = TECHNICAL
Calibration N/20 = 0/20
Gate D = NONE
Gate E = NONE
participant directional result = NOT AUTHORIZED
/wave1/ unchanged
public privacy.html still says Calibration is not active for external research
```

Record the results of migrations, config update, LT/EN smoke, local-only DB check, consented upload, both deletion paths, CSV and cron.

---

## 14. What this deployment does NOT authorize

Even if every smoke test succeeds:

```text
DO NOT switch collection_mode to CALIBRATION yet
DO NOT invite external calibration participants yet
DO NOT modify /wave1/
DO NOT merge to main as part of this deploy
DO NOT enable Gate D/E
DO NOT show participant directional results
```

External collection requires the final activation checklist, exact active privacy wording, activation record and explicit owner authorization.
