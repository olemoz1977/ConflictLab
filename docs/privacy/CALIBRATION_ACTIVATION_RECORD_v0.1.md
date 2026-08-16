# 2Pair / ConflictLab — Calibration Activation Record v0.1

**Record finalized:** 2026-08-16 10:49 EEST (+03:00)  
**Public participant-facing name:** 2Pair  
**Technical release/repository naming retained:** ConflictLab  
**Study:** first external mechanical timing / UX calibration only

## 1. Exact release identity

```text
release: calibration-v0.1
code head: c72bde02c9358ff15d2ebb5e6c9f8eea2455c3a4
workflow run: 31856033244 (#503)
CI: SUCCESS
artifact id: 9239045582
artifact digest: sha256:5be68e7347f1a8bd340954f0ea5656c446f86cceba668fa08704829443d2f8df
Hostinger path: /public_html/conflictlab/releases/calibration-v0.1/
```

## 2. Methodological boundary at activation

```text
study purpose: MECHANICAL_TIMING_ONLY
6000 ms: experimental engineering candidate
Gate D: NONE
Gate E: NONE
CS/CR mappings: NOT VALIDATED
latency psychological meaning: NOT VALIDATED
participant directional result: NOT AUTHORIZED
```

## 3. Privacy / consent state

```text
privacy source: PRIVACY_NOTICE_TIMING_RESEARCH_v0.3
public privacy page: /privacy.html
public Calibration wording: ACTIVE
public naming: 2Pair · Calibration
LT live verification: PASS, 2026-08-16 10:48 EEST
EN live verification: PASS, 2026-08-16 10:47 EEST
consent evidence version: timing-research-consent-v0.1
18+ declaration: REQUIRED
local-only/no-upload path: ENABLED
participant deletion code: PRE-UPLOAD, 32 hex chars
server deletion-token storage: SHA-256 hash only
browser localStorage deletion-code convenience: ENABLED
active DB retention: max 90 days
```

## 4. Infrastructure state

```text
pre-switch SERVER MODE: TECHNICAL
pre-switch CALIBRATION N/20: 0/20
technical/owner run count: 5
Hostinger primary server: Lithuania / re-confirmed: YES
Hostinger backup location: France / re-confirmed: YES
weekly backup setting re-confirmed: YES
retention cron path present: YES
live retention schedule: 0 1 * * *
first scheduled cron execution evidence: PASS
cron output: retention_cleanup deleted_runs=0
```

Operational security note: DB password and admin password were rotated during activation troubleshooting. No secrets are recorded here.

## 5. Owner authorization

```text
Owner explicitly authorizes the first external 2Pair Calibration mechanical timing / UX study: YES
Authorization wording: “Autorizuoju 2Pair Calibration išorinį mechaninio timing / UX tyrimą.”
Authorization date: 2026-08-16
Authorization exact minute: not independently captured in the activation record; authorization occurred before the live mode switch.
```

## 6. TECHNICAL -> CALIBRATION switch

The only intended live mode change was:

```php
'collection_mode' => 'TECHNICAL'
```

to:

```php
'collection_mode' => 'CALIBRATION'
```

Evidence:

```text
switch performed: 2026-08-16, before 10:40 EEST; exact switch minute not independently captured
post-switch SERVER MODE: CALIBRATION
post-switch admin evidence: PASS by 2026-08-16 10:40 EEST
post-switch CALIBRATION N/20 before owner smoke: 0/20
technical/owner runs: 5
```

No application/research byte change was made as part of the mode switch.

## 7. Post-switch owner smoke

```text
one consented owner smoke completed: YES
run stored as CALIBRATION: YES
N/20 during smoke: 1/20
consent_version correct: YES — current artifact/config previously verified; activation changed only collection_mode
18+ / affirmative consent path: YES
deletion-code path: YES
server deletion-token hash / plaintext boundary: YES — same verified artifact; successful self-service deletion exercised
participant result remains NOT_ESTIMABLE: YES — unchanged verified artifact
Gate D/E remain NONE: YES — visible in live admin
smoke run deleted via participant self-service deletion: YES
N/20 after smoke deletion: 0/20
```

## 8. External collection authorization state

```text
external participants may be invited: YES
starting clean CALIBRATION N/20: 0/20
first external invitation: NOT YET ISSUED at record finalization
```

The public entry point may now link to the existing Hostinger Calibration release. The research DB and privacy/control layer remain on OMESG360 infrastructure.

## 9. Explicit non-authorization

This activation does **not** authorize:

```text
Gate D or Gate E
CS/CR construct-validity claims
psychological interpretation of latency
psychological/personality diagnosis or profiling
participant directional result
employment or health use
changes to /wave1/
merge to main
broader claims beyond the mechanical timing / UX calibration study
```
