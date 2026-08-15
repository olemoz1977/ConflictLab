# ConflictLab — Public Privacy ACTIVE Deploy Plan v0.1

**Date:** 2026-08-15  
**Status:** PREPARED / DO NOT EXECUTE YET  
**Scope:** `/privacy.html` transition for the first external mechanical timing / UX Calibration study only

## 1. Current live state

```text
server collection_mode = TECHNICAL
public /privacy.html Calibration status = PREPARATION
external CALIBRATION = NOT AUTHORIZED
```

This is internally consistent and must remain so until the activation sequence is deliberately executed.

## 2. Prepared ACTIVE privacy candidate

The active candidate is derived from the current single OMESG360 Privacy Centre rather than replacing the Wave 1/general privacy structure.

Only the Calibration processing profile is promoted from PREPARATION to ACTIVE, together with the corresponding retention entry.

The ACTIVE candidate must disclose at minimum:

```text
controller: Oleg Mozochin
contact: info@omesg360.eu
mechanical timing / UX purpose only
6000 ms = experimental engineering parameter, not psychological standard
18+ only
voluntary affirmative consent
local-only / no-upload alternative
exact minimal pseudonymous timing payload
no reason/free-text/intensity/directional-result upload
pre-upload 32-hex deletion code
browser localStorage plaintext code only as participant-rights convenience
server receives/stores deletion-token SHA-256 hash only
local deletion code excluded from CSV and research analysis
self-service deletion + email route
no partial-stream upload before completed block upload
GDPR 6(1)(a) consent basis for timing research
active research DB retention max 90 days
daily retention process
backup residual-copy qualification
Hostinger primary Lithuania / backup France
Hostinger access logs as separate technical/security processing
GitHub boundary
no OMESG360 advertising/marketing trackers for this timing study
no automated significant decisions / employment / health / personality conclusions
```

Authoritative detailed source: `PRIVACY_NOTICE_TIMING_RESEARCH_v0.3.md`.

## 3. Activation order

Do not publish ACTIVE wording days/hours before the study is actually enabled. Use a short controlled activation window.

Recommended order:

```text
A. Re-confirm current live admin = SERVER MODE: TECHNICAL and N/20 = 0/20.
B. Re-confirm Hostinger backup setting and retention cron still exist.
C. Back up current public /privacy.html.
D. Upload the prepared ACTIVE /privacy.html candidate.
E. Immediately verify LT and EN /privacy.html render and Calibration says ACTIVE.
F. Owner explicitly authorizes external mechanical timing study.
G. Change only secret config.php collection_mode: TECHNICAL -> CALIBRATION.
H. Open admin and verify SERVER MODE: CALIBRATION.
I. Run one owner smoke only; confirm it enters CALIBRATION rules as intended.
J. Create/finalize CALIBRATION_ACTIVATION_RECORD_v0.1 with exact timestamp and evidence.
K. Only then invite external participants.
```

The interval between D and G should be kept short. If activation is aborted after D, restore PREPARATION privacy wording rather than leaving public ACTIVE wording with a TECHNICAL server.

## 4. Explicit non-scope

Activation does **not** authorize:

```text
Gate D
Gate E
CS/CR construct validation claims
latency psychological meaning
participant directional result
personality diagnosis/profile
employment or health use
/wave1/ changes
merge to main
public product promotion beyond the timing study
```

## 5. Retention first-run dependency

The daily retention cron is already configured at `0 0 * * *`, but its first scheduled execution evidence is still pending.

Preferred path: capture the first successful output before activation:

```text
retention_cleanup deleted_runs=0
```

If the owner intentionally activates before that first scheduled execution, the activation record must explicitly state that:

```text
cron configuration/path were live and previously reviewed;
first scheduled execution evidence was pending;
this was accepted as a temporary operational residual risk;
follow-up evidence must be captured after the first run.
```

No methodological or construct-validity claim follows from the cron state.
