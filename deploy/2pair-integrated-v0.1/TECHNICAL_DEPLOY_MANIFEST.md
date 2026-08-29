# 2Pair Integrated v0.1 — TECHNICAL deploy manifest

**Status:** CANDIDATE / DO NOT DEPLOY UNTIL OWNER APPROVAL

Target package:

```text
deploy/2pair-integrated-v0.1/
```

Required Hostinger state for the first deployment:

```text
collection_mode = TECHNICAL
protocol_version = 2pair-integrated-v0.1
release_id = 2pair-integrated-v0.1
stimulus_set_version = stimulus-set-v1
training_set_version = training-set-v1
consent_version = 2pair-integrated-research-consent-v0.1
block_budget_ms = 6000
retention_days = 90
```

The first deployment must use new integrated tables from `server/schema.sql`. Do not point this build at historical Wave 1 or Calibration tables and do not overwrite their application directories.

Do not publish the integrated privacy DRAFT as active and do not switch to `RESEARCH` during the TECHNICAL deployment/smoke stage.

Required post-deploy evidence is defined in `DEPLOY_CHECKLIST.md` and includes LT/EN flow, rapid/retry/NCC behavior, local-only no-write, two exports, deletion, admin metrics, and retention cleanup.
