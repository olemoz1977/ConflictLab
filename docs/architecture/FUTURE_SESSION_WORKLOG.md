# ConflictLab — Future Session Worklog / Decision Log

**Purpose:** living engineering/research worklog for the future-session branch.  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Started:** 2026-08-14  
**Status:** ACTIVE / continuously updated while this branch is under development.

> This file records what was done, why it was done, what was observed, what remains unvalidated, and the next gate. It does **not** override ADRs, versioned methodology configs, or released specifications. When this log conflicts with a versioned architecture/methodology source, the versioned source wins and the conflict must be resolved explicitly.

## 1. Permanent project boundaries

- ConflictLab remains an epistemic reflection framework, not a personality test, diagnosis, prediction, or psychological scoring instrument.
- Observation → Evidence → Reflection remains the governing sequence.
- Scene property ≠ participant response ≠ derived signal ≠ person characteristic.
- Current active future-session domains are CS and CR. AW is not an active future-session scoring domain.
- Gate D = NONE and Gate E = NONE until separately validated/released.
- No participant-level directional/psychological result is authorized while Gate D/E are NONE.
- Existing Wave1 data, API, storage, public entrypoint and frozen mirrors remain separate from future-session development.
- Public `https://omesg360.eu/wave1/` is a stable entrypoint and must not be changed without a separate explicit PUBLIC authorization.

## 2. Release routing decision

Deployment model:

```text
LAB
-> OWNER APPROVAL of exact deployed release
-> separate PUBLIC switch authorization
-> ROLLBACK path retained
```

Versioned LAB releases live under:

```text
/conflictlab/releases/<release-id>/
```

Current LAB path:

```text
/conflictlab/releases/calibration-v0.1/
```

The OMESG360 root and live `/wave1/` remain unchanged.

## 3. Mobile rapid-presentation finding

Owner testing on a mobile viewport revealed that the original square-card presentation made the second rapid image partially inaccessible without scrolling.

Resolution:

- preserve exact research asset bytes;
- do not resample or change source image resolution for research presentation;
- use responsive CSS presentation scaling;
- rapid stage uses dynamic viewport (`100dvh`), no vertical scroll, two flexible top/bottom rows and `object-fit: contain`;
- training and measured blocks use the same geometry.

Owner retest confirmed both images were simultaneously visible. Mobile visibility is therefore a passed UX condition for the corrected rapid layout, not a validation of the 6000 ms timing hypothesis.

## 4. Stage 0 familiarization

A training stage was added after OWNER_UX_RUN_001 showed that the first measured-looking block could be contaminated by learning the interaction itself.

Training uses P0-001/P0-002/P0-003 as read-only familiarization assets and is explicitly excluded from calibration/evidence.

```text
is_training = true
analysis_eligible = false
timing_calibration_eligible = false
Gate D = NOT_APPLICABLE
Gate E = NOT_APPLICABLE
server_upload = false
participant_result = NONE
```

The training interaction mirrors the three-pair vertical rapid mechanic and shared 6000 ms budget.

## 5. 6000 ms timing calibration

The 6000 ms shared block budget remains an **unvalidated pilot hypothesis**.

Current timing-calibration decision floor:

- at least 20 clean primary blocks;
- primary timeout/incompletion is an observed outcome, not automatically an exclusion;
- page-hidden primary is excluded;
- retries are diagnostic only;
- Gate decision remains `INSUFFICIENT_DATA` below the configured data floor.

Possible future decisions:

```text
KEEP_6000
ADJUST_AND_RETEST
REJECT_6000
```

No timing metric is allowed to imply personality, confidence, impulsivity, depth, or any other psychological characteristic.

## 6. Hostinger LAB deployment — owner-operated

The owner manually deployed the isolated LAB release to Hostinger at:

```text
https://omesg360.eu/conflictlab/releases/calibration-v0.1/
```

The live OMESG360 root and `/wave1/` were not changed.

### 6.1 Hostinger `.mjs` compatibility finding

Hostinger served `.mjs` modules as `text/plain`; browsers rejected them under strict module MIME checking.

Attempted `.htaccess` MIME correction did not resolve the live behavior reliably.

Resolution for the Hostinger LAB package:

- retain canonical `.mjs` files as canonical/source copies;
- provide Hostinger-compatible `.js` deployment modules;
- add an `index.php` bootstrap for the compatible Hostinger path;
- do not alter the canonical future-session logic or research asset bytes.

After the compatibility patch the LAB loaded successfully to the training intro.

## 7. Isolated calibration storage

A separate MySQL database was created for future-session calibration. Existing Wave1 storage is not reused.

Tables:

```text
cl_calibration_runs
cl_calibration_attempts
cl_calibration_pair_events
```

DB connection was smoke-tested independently before any end-to-end run. The temporary connection-check file was intended only for one-time diagnostics and must not remain deployed.

Calibration server intentionally does not store:

- training responses;
- selected A/B identity in the timing-only calibration dataset;
- reflection free text;
- reflection reason selections;
- reaction intensity;
- participant psychological result;
- Gate D/E interpretation;
- persistent participant ID;
- exact viewport or user-agent fingerprint.

## 8. First Hostinger end-to-end technical run

One owner-operated end-to-end run was completed after DB/API setup.

Observed chain:

```text
browser
-> preload
-> training
-> measured 3-pair rapid block
-> calibration API
-> MySQL
-> reflection
-> finish
```

The UI confirmed that technical calibration data were saved. The database contained one run, one primary attempt and three pair events.

This run must **never enter N/20** because the owner had prior exposure to the research pairs.

## 9. TECHNICAL vs CALIBRATION run boundary

To preserve useful owner/smoke-test evidence without contaminating real calibration N, `cl_calibration_runs` now has a server-assigned `run_type`:

```text
TECHNICAL
CALIBRATION
```

The deployed owner run was migrated to `TECHNICAL`.

Server configuration controls collection mode. Participant requests cannot assign their own run type.

During development:

```text
collection_mode = TECHNICAL
```

Only immediately before real, fresh-participant collection may the owner intentionally switch to:

```text
collection_mode = CALIBRATION
```

`N/20` is computed only from `CALIBRATION + clean_primary` runs. TECHNICAL runs remain visible for engineering diagnostics but never count toward timing calibration.

## 10. Calibration admin v2

The admin dashboard was expanded to separate technical and calibration evidence.

Current dashboard capabilities:

- server mode indicator (`TECHNICAL` / `CALIBRATION`);
- calibration-eligible clean `N / 20`;
- technical/owner run count;
- excluded calibration run count;
- primary completion;
- P3 missing;
- P3 never presented;
- P3–P1 missingness gradient;
- retry diagnostic;
- filters by type, form, device and status;
- per-run primary elapsed time and retry indicator;
- expandable run details;
- per-attempt elapsed/timeout/page-hidden status;
- per-pair position, pair ID, presented status, ready time, response status, visual-choice latency, elapsed time and remaining budget;
- pair missingness and positional diagnostics calculated only from eligible calibration runs.

The owner verified the first run is displayed as `TECHNICAL`, while calibration remains `0 / 20` and the decision remains `INSUFFICIENT_DATA`.

## 11. Product-shaped pilot decision

Because fresh testers are scarce, the project direction changed from a narrow one-purpose timing page to a **product-shaped pilot**.

Goal: each fresh participant should test the same structural flow intended for the future product while timing calibration remains only one independent evidence layer.

Planned participant flow:

```text
language selection (LT / EN)
-> Stage 0 training
-> rapid A/B choice block
-> reflection reason
-> reaction intensity 1–5
-> local calculation pipeline
-> evidence gate
-> result presentation / fail-closed state
```

While Gate D/E remain NONE, the real-participant result layer must remain fail-closed (`NOT_ESTIMABLE` / no psychological result). Full calculation/evidence/result UX may be developed and tested using fixtures/synthetic cases without pretending real participant direction is validated.

## 12. Language requirement

The current LAB is LT-only. Before fresh-participant N/20 collection, the product-shaped pilot should support LT and EN across the complete flow:

- language selection before training;
- training copy;
- rapid-stage status text;
- reflection reason text;
- intensity question/labels;
- technical/error messages;
- result/fail-closed presentation.

Language should remain fixed within a started session.

## 13. Three separate response-time channels

The next product-shaped pilot should treat timing as three separate process signals rather than one combined reflection time.

### 13.1 Visual choice latency

```text
pair fully ready/rendered
-> participant selects A/B
= visual_choice_latency_ms
```

This already exists and is used only as timing/process telemetry.

### 13.2 Reason response latency

```text
selected image + all reason options fully ready
-> participant selects a reason
= reason_response_latency_ms
```

No time limit. This must not be interpreted psychologically without separate validation.

### 13.3 Intensity response latency

```text
intensity question becomes active after reason selection
-> participant selects 1–5
= intensity_response_latency_ms
```

No time limit. This must not be interpreted as confidence/strength/decisiveness without validation.

A useful additional UX diagnostic is `reflection_total_elapsed_ms`, again as process telemetry only.

## 14. Reflection/intensity data semantics

`intensity` remains an independent self-report channel. It does **not** enter Directional Balance and does not alter the A/B-derived direction.

Current v0.2 hard calculation constraints remain:

```text
intensity never enters directional balance
latency never enters directional balance
retry events never enter directional balance
reflection class never changes direction
```

Reason and intensity should be sequential rather than displayed simultaneously, so their response latencies remain separable.

Local-first boundary remains the default:

- reason/free text: local by default;
- reaction intensity: local by default;
- derived personal result: local by default;
- timing calibration server receives only justified mechanical telemetry.

## 15. Partial reflection / abandonment semantics

A participant who completes the rapid block but does not finish reflection must not automatically invalidate otherwise eligible timing evidence.

Planned local statuses should distinguish at least:

```text
reason_status = ANSWERED | NO_RESPONSE | ABANDONED | NOT_REACHED
intensity_status = ANSWERED | NO_RESPONSE | ABANDONED | NOT_REACHED
```

Rapid timing eligibility and reflection completeness are separate dimensions.

## 16. Immediate next gate

Do **not** switch the server to `CALIBRATION` yet.

Before fresh-participant collection:

1. extend the LAB into the product-shaped pilot;
2. add full LT/EN support;
3. add sequential reason → intensity 1–5 interaction;
4. measure visual-choice, reason-response and intensity-response latencies independently;
5. retain reason/intensity local-first by default;
6. keep Gate D/E fail-closed;
7. test Calculation Engine / Evidence Engine / result UX with fixtures/synthetic cases;
8. run owner smoke tests as `TECHNICAL` only;
9. only after owner approval intentionally change `collection_mode` to `CALIBRATION` for fresh participants.

## 17. Public safety state

```text
Hostinger versioned LAB path       DEPLOYED / OWNER TESTING
calibration DB                     CREATED / ISOLATED
calibration admin v2               DEPLOYED / OWNER VERIFIED
collection mode                    TECHNICAL
technical runs                     >= 1
calibration N/20                   0 / 20 at last owner check
Gate D                             NONE
Gate E                             NONE
owner public approval              NOT GRANTED
public /wave1 switch               NOT AUTHORIZED
omesg360.eu root                   UNCHANGED
live /wave1                        UNCHANGED
production product deployment      NOT AUTHORIZED
```

## 18. Logging rule going forward

Material changes should be added to this worklog when they affect any of the following:

- architecture or methodology boundary;
- participant flow;
- data model or privacy boundary;
- release/deployment state;
- owner-observed UX finding;
- calibration inclusion/exclusion rule;
- rejected alternative and its reason;
- newly discovered technical incompatibility;
- test evidence and current next gate.

Small mechanical commits do not need prose-by-prose duplication; the log should capture decisions and state transitions, while Git history captures the exact file changes.
