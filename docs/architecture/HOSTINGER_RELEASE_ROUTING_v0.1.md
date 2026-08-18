# Hostinger public release routing v0.1

**Status:** DRAFT / REPOSITORY-ONLY / NOT DEPLOYED  
**Date:** 2026-08-14  
**Scope:** OMESG360 / ConflictLab Hostinger release promotion and rollback  

## 1. Goal

Keep already-published public URLs stable while allowing ConflictLab to evolve from experimental validation to calibration, pilot and later product releases.

Stable public URLs are treated as **entrypoints**, not as version identifiers.

Current public surfaces:

```text
https://omesg360.eu/
https://omesg360.eu/wave1/
```

Neither is changed by creating or testing a new release.

## 2. Hard safety constraints

1. `omesg360.eu/` root is not modified as part of ConflictLab calibration work.
2. The live `/wave1/` Human Wave 1 v0.3 flow remains untouched until the owner explicitly authorizes a PUBLIC switch.
3. `deploy/wave1-hostinger/` remains the frozen repository mirror of the current Wave 1 v0.3 deployment.
4. Approved release bytes are immutable. Any post-approval change creates a new release ID and requires a new approval.
5. No public switch is inferred from CI success, owner testing, calibration N, or a Git merge.
6. Public switch and rollback are separate deployment actions and must be recorded.
7. Hostinger credentials, live database credentials and participant data are never committed.

## 3. Target Hostinger layout

```text
public_html/
├── index.html                         # existing OMESG360 root; untouched
├── wave1/
│   ├── index.html                     # current public entrypoint; v0.3 today
│   ├── api.php                        # frozen Wave 1 v0.3 API; untouched
│   ├── admin.php                      # frozen Wave 1 admin; untouched
│   └── assets/                        # frozen Wave 1 assets; untouched
└── conflictlab/
    └── releases/
        ├── calibration-v0.1/
        ├── pilot-v0.1/
        └── product-v1.0/
```

A release is placed under `/conflictlab/releases/<release-id>/` first. It is **not public through the stable `/wave1/` URL** until owner approval and a separate switch action.

An unlinked release URL is not a security boundary. If an owner-only release needs access control, protect that release directory separately; do not rely on obscurity.

## 4. Four-stage promotion model

### LAB

```text
/conflictlab/releases/<release-id>/
```

Purpose:
- integration and technical testing;
- timing/telemetry verification;
- database/API smoke tests;
- no change to `/wave1/`.

### OWNER APPROVAL

The owner reviews the **exact same deployed release bytes** that would later become public.

Approval record must identify at least:

```text
release_id
repo_commit_sha
release_manifest_sha256
owner_approval = YES
approved_at
```

After approval, that release directory becomes immutable.

### PUBLIC

Only after explicit owner authorization:

```text
/wave1/index.html
        ↓
/conflictlab/releases/<approved-release-id>/
```

The preferred first implementation is a tiny static redirect entrypoint. It does not alter the OMESG360 root and does not modify the approved release directory.

The public switch changes only the stable entrypoint artifact. Existing frozen Wave 1 API/admin/assets remain in place for rollback and historical continuity.

### ROLLBACK

Rollback restores the immediately previous `/wave1/index.html` artifact.

No release directory is deleted during rollback.

Target operational property:

```text
PUBLIC SWITCH  = replace one small entrypoint file
ROLLBACK       = restore previous entrypoint file
```

## 5. Release identity

Every candidate release must have a unique release ID, for example:

```text
calibration-v0.1
calibration-v0.2
pilot-v0.1
product-v1.0
```

A release manifest records:

- release ID;
- source commit SHA;
- protocol/config versions;
- deploy target path;
- lifecycle (`LAB`, `OWNER_APPROVED`, `PUBLIC`, `RETIRED`);
- public switch authorization separately from owner UX approval;
- rollback target;
- known exclusions / research boundaries.

`OWNER_APPROVED` does **not** automatically mean `PUBLIC`.

## 6. Public entrypoint semantics

The published LinkedIn URL remains:

```text
https://omesg360.eu/wave1/
```

Its meaning becomes:

> stable entrypoint to the currently owner-authorized ConflictLab public experience.

It must not be treated as the name of a permanent internal protocol version.

The browser may redirect to a versioned release path. The shared/published URL remains stable.

## 7. Approval and switch gates

A release may move from LAB to OWNER_APPROVED only after the owner explicitly approves the participant experience.

A release may move from OWNER_APPROVED to PUBLIC only after a separate explicit authorization such as:

```text
PUBLIKUOJAM
PUBLIC SWITCH APPROVED
```

Ambiguous approval of a screenshot, UX detail, CI result or calibration result is not deployment authorization.

## 8. First calibration release

The first intended release family is:

```text
calibration-v0.1
```

Its purpose is limited to:

- Stage 0 familiarization;
- one 3-pair measured rapid block under the shared timing-budget hypothesis;
- Reflection;
- calibration-quality telemetry;
- isolated calibration storage/admin reporting.

It must not activate Gate D or Gate E and must not produce a participant psychological result.

## 9. Deployment invariants

Before any PUBLIC switch verify:

```text
approved release exists at versioned path
release manifest matches source commit
owner approval is explicit
rollback entrypoint copy exists
root OMESG360 files unchanged
frozen Wave 1 API/admin/assets unchanged
new calibration storage isolated from Wave 1 responses
```

After switch verify:

```text
/wave1/ resolves to approved release
approved release loads on mobile
no response writes hit frozen Wave 1 tables
admin/calibration counters work
rollback procedure still available
```

## 10. Current state

```text
routing architecture        PREPARED AS DRAFT
calibration release         NOT YET PACKAGED FOR HOSTINGER
owner approval              NOT GRANTED FOR PUBLIC RELEASE
public switch               NOT AUTHORIZED
live /wave1/                UNCHANGED
omesg360.eu root            UNCHANGED
```
