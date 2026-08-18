# ConflictLab — Calibration Activation Record Template v0.1

**Status:** TEMPLATE ONLY / NOT AN ACTIVATION RECORD  
**Purpose:** complete only during the controlled TECHNICAL -> CALIBRATION switch

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

## 3. Privacy / consent identity

```text
privacy source: PRIVACY_NOTICE_TIMING_RESEARCH_v0.3
public privacy page: /privacy.html
public Calibration wording status before switch: ACTIVE / VERIFIED LT+EN
consent evidence version: timing-research-consent-v0.1
18+ declaration: REQUIRED
local-only/no-upload path: ENABLED
participant deletion code: PRE-UPLOAD, 32 hex chars
server deletion-token storage: SHA-256 hash only
browser localStorage deletion-code convenience: ENABLED
active DB retention: max 90 days
```

## 4. Infrastructure state immediately before switch

Fill with live evidence:

```text
activation date/time + timezone: ____________________
owner: Oleg Mozochin
pre-switch SERVER MODE: TECHNICAL
pre-switch CALIBRATION N/20: ____ / 20
technical/owner run count: ____
Hostinger primary server: Lithuania / re-confirmed: YES | NO
Hostinger backup location: France / re-confirmed: YES | NO
weekly backup setting re-confirmed: YES | NO
retention cron path present: YES | NO
retention schedule: 0 0 * * *
first scheduled cron execution evidence: PASS | PENDING ACCEPTED RESIDUAL RISK
cron output/evidence: ____________________
```

## 5. Owner authorization

Do not infer or auto-fill this section.

```text
Owner explicitly authorizes the first external ConflictLab mechanical timing / UX calibration study: YES | NO
Authorization wording / reference: ____________________
Authorization timestamp: ____________________
```

If `NO`, stop. Do not change collection mode.

## 6. Switch

The only intended live secret-config mode change is:

```text
'collection_mode' => 'TECHNICAL'
```

to:

```text
'collection_mode' => 'CALIBRATION'
```

Record:

```text
switch performed at: ____________________
post-switch SERVER MODE: CALIBRATION | OTHER: __________
post-switch admin screenshot/evidence: ____________________
```

## 7. Post-switch owner smoke

Before inviting external participants:

```text
one consented owner smoke completed: YES | NO
run stored as CALIBRATION: YES | NO
consent_version correct: YES | NO
18+ / consent evidence correct: YES | NO
delection hash present / plaintext absent server-side: YES | NO
N/20 behavior matches preregistered eligibility rules: YES | NO
participant result remains NOT_ESTIMABLE: YES | NO
Gate D/E remain NONE: YES | NO
smoke run deleted/excluded according to research rules: ____________________
```

If any critical item is `NO`, revert collection mode to TECHNICAL and restore public privacy wording to PREPARATION until resolved.

## 8. External collection authorization state

```text
external participants may be invited: YES | NO
external collection start timestamp: ____________________
```

## 9. Explicit non-authorization

This activation record does not authorize:

```text
Gate D or Gate E
psychological or personality conclusions
employment/health use
participant directional result
changes to /wave1/
merge to main
construct-validity claims from timing calibration
```
