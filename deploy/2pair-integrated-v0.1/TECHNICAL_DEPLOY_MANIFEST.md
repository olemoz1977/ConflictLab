# 2Pair Integrated Pilot v0.1 — TECHNICAL deployment state

**Status:** LIVE / OWNER TECHNICAL deployment

Live participant URL:

```text
https://omesg360.eu/2pair/releases/2pair-integrated-v0.1/
```

Live research/timing admin:

```text
https://omesg360.eu/2pair/releases/2pair-integrated-v0.1/server/admin.php
```

Interest funnel admin after the telemetry patch is deployed:

```text
https://omesg360.eu/2pair/releases/2pair-integrated-v0.1/server/interest_admin.php
```

Hostinger release directory:

```text
public_html/2pair/releases/2pair-integrated-v0.1/
```

Repository source:

```text
repo: olemoz1977/ConflictLab
branch: feature/2pair-integrated-v0.1
package: deploy/2pair-integrated-v0.1/
```

Current server boundary:

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

Integrated research/timing storage remains in the separate `tp_integrated_*` tables. Historical Wave 1 and Calibration tables are not modified.

Minimal public-interest telemetry is intentionally separate from research evidence. It uses only daily aggregate counters in `tp_interest_daily`; no IP, persistent visitor ID, fingerprint, research session UUID, name or email is stored. See `INTEREST_TELEMETRY.md`.

Do not switch the live deployment from `TECHNICAL` to `RESEARCH` until the remaining activation checks and explicit owner authorization are complete.
