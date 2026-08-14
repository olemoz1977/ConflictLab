# ConflictLab — Future Session Implementation Baseline Status v1.0

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**PR:** Draft PR #2  
**Revision:** Hostinger release routing + isolated `calibration-v0.1` LAB package  
**Status:** LAB PACKAGE PREPARED IN REPOSITORY; NOT DEPLOYED; PUBLIC SWITCH NOT AUTHORIZED

## Current state

```text
M1-M7 architecture decisions       CLOSED
F1 exact stimulus identity          COMPLETE AS DRAFT
F2 rapid mechanics                  COMPLETE FOR PILOT
Stage 0 training                    IMPLEMENTED
training source                     P0-001 / P0-002 / P0-003 BYTE-IDENTICAL DEPLOY COPIES
training calibration eligibility    EXCLUDED
mobile rapid viewport fit           IMPLEMENTED / OWNER VISIBILITY PASS
6000 ms timing gate                 READY / clean real data pending
calibration Hostinger release       calibration-v0.1 / LAB PACKAGE READY
calibration server storage          ISOLATED / NOT WAVE1 RESPONSES
calibration admin                   IMPLEMENTED / N-OF-20 + TIMING DIAGNOSTICS
release routing                     LAB -> OWNER APPROVAL -> PUBLIC -> ROLLBACK
owner public approval               NOT GRANTED
public /wave1 switch                NOT AUTHORIZED
omesg360.eu root                    UNCHANGED
live /wave1                         UNCHANGED
Gate D                              NONE
Gate E                              NONE
production deploy                   NOT AUTHORIZED
```

## Release routing boundary

Architecture:

`docs/architecture/HOSTINGER_RELEASE_ROUTING_v0.1.md`

The already-published URL remains a stable entrypoint:

```text
https://omesg360.eu/wave1/
```

Candidate releases are versioned separately under the intended Hostinger path:

```text
/conflictlab/releases/<release-id>/
```

Promotion is explicit and staged:

```text
LAB
-> OWNER APPROVAL of exact deployed release bytes
-> separate PUBLIC switch authorization
-> optional ROLLBACK by restoring previous /wave1/index.html
```

`OWNER_APPROVED` never implies `PUBLIC`. CI success, a Git merge, owner UX testing, or a timing-calibration result cannot authorize the public switch.

## calibration-v0.1 package

Repository package:

`deploy/conflictlab-hostinger/releases/calibration-v0.1/`

It contains:

- participant `index.html` derived from the canonical future-session flow;
- exact byte copies of required future-session configs and JS modules;
- exact byte copies of P0-001/P0-002/P0-003 training assets;
- exact byte copies of all 12 F2 research assets;
- isolated calibration API;
- isolated SQL schema;
- password-protected calibration admin dashboard;
- release manifest and canonical blob inventory.

The canonical source files and frozen P0/Wave1 paths remain untouched. Deployment copies are for release packaging only.

## Participant calibration flow

```text
Stage 0 familiarization
  -> local only / excluded from calibration
fresh selected F2 form
  -> three sequential pairs
  -> one shared 6000 ms candidate budget
  -> all selected assets fetched + decoded before timing starts
measured timing upload
  -> after rapid block terminates
Reflection
  -> local only for calibration-v0.1 dataset
finish
```

Network saving occurs only after the timed rapid block has ended, so upload latency cannot consume the shared 6000 ms budget.

## Calibration storage boundary

The release does **not** reuse the frozen Wave 1 response store.

New tables:

```text
cl_calibration_runs
cl_calibration_attempts
cl_calibration_pair_events
```

The timing dataset stores only data required for the mechanical timing decision. It deliberately excludes:

```text
training choices / training telemetry
selected A/B identity
Reflection reasons / free text
participant psychological result
Gate D mapping
Gate E aggregation
persistent participant ID
exact viewport / user-agent fingerprint
```

A random session UUID is used for one calibration run. Device context is reduced to the coarse diagnostic category `mobile | tablet | desktop | unknown`.

A/B choice identity is converted client-side to `response_status = choice`; timeout remains `response_status = timeout`. Pair identity and timing position remain available because they are required for pair-specific and P1/P2/P3 timing diagnostics.

## Clean-primary classification

A stored primary block is calibration-eligible when the calibration payload is structurally valid, the measured assets were successfully preloaded, and the page was not hidden during the primary block.

Primary timeout/incompletion is **not** an exclusion. It is an observed outcome required to evaluate whether 6000 ms is viable.

Current explicit exclusion:

```text
PAGE_HIDDEN_DURING_PRIMARY
```

Retries are stored for diagnostics but only the primary attempt contributes to the calibration decision metrics.

## Timing admin

`server/admin.php` reports:

- clean primary `N / 20`;
- excluded runs and reasons;
- primary completion rate;
- P3 missing rate;
- P3 never-presented rate;
- P3 minus P1 missingness gradient;
- pair-specific missingness with the configured per-pair N floor;
- retry-rate diagnostic;
- median choice latency by P1/P2/P3;
- median remaining budget at pair start by P1/P2/P3;
- form and coarse device-category counts.

The admin applies the thresholds in `timing-calibration-v1` only after the configured clean-primary data floor. Before then the decision is `INSUFFICIENT_DATA`.

Possible timing decisions remain:

```text
KEEP_6000
ADJUST_AND_RETEST
REJECT_6000
```

No timing decision assigns psychological meaning to any response.

## Gate and interpretation boundary

Still unchanged:

```text
Gate D pair mapping          NONE
Gate E aggregation           NONE
stimulus lifecycle           DRAFT
reason-map lifecycle         DRAFT
participant result claims    NOT AUTHORIZED
```

The generic future-session `api_v2.php` remains untouched and continues to fail closed for unreleased methodology. `calibration-v0.1` therefore uses a separate timing-only ingest rather than weakening the generic release gate.

## Current deployment state

```text
repository LAB package                 READY
CI contract                            PASS required before use
Hostinger versioned LAB path           NOT DEPLOYED
Hostinger calibration DB/schema        NOT CREATED
Hostinger calibration config.php       NOT CONFIGURED
owner review of deployed LAB bytes     NOT STARTED
owner approval                         NOT GRANTED
stable /wave1 public switch            NOT AUTHORIZED
production deployment                  NONE
```

## Next operational step

The next step is **not** to change `/wave1/`.

When a Hostinger deployment action is explicitly authorized, deploy `calibration-v0.1` only to its versioned LAB path, create/configure its isolated calibration storage, and smoke-test that exact release. The owner then reviews the exact deployed release. Only after that can a separate PUBLIC-switch decision be considered.

## Production safety

Still untouched:

```text
omesg360.eu root
deployed /wave1/ entrypoint
frozen deploy/wave1-hostinger source mirror
current Wave 1 API
existing Wave 1 responses storage
Pair P0 source files and paths
```

No merge or public/production deploy is authorized.
