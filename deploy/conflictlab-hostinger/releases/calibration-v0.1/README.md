# ConflictLab calibration-v0.1 — versioned Hostinger LAB

**Lifecycle:** LAB  
**Hostinger LAB:** DEPLOYED / owner-operated  
**Current repository build:** PRODUCT-SHAPED UPDATE READY FOR LAB OVERWRITE  
**Public switch:** NOT AUTHORIZED

Versioned LAB path:

```text
/conflictlab/releases/calibration-v0.1/
```

This directory must not replace or modify the existing public `/wave1/` entrypoint without a separate explicit PUBLIC authorization.

## Current product-shaped flow

```text
LT / EN language selection
-> Stage 0 familiarization
-> rapid 3-pair A/B block / shared 6000 ms candidate budget
-> timing-only calibration upload
-> reason reflection
-> intensity 1-5
-> local Calculation Engine
-> local Evidence Engine
-> fail-closed result screen
```

The release keeps three distinct response-time channels:

```text
visual_choice_latency_ms           server timing telemetry
reason_response_latency_ms         local only
intensity_response_latency_ms      local only
```

`reflection_total_elapsed_ms` is local-only UX/process telemetry.

Reason and intensity controls remain disabled until the selected reflection image is decoded and visually ready.

## Result boundary

Gate D and Gate E remain `NONE`.

Therefore real participant execution remains:

```text
NOT_ESTIMABLE
```

No directional or psychological participant result is authorized by this LAB build.

## Server boundary

The isolated calibration API stores only mechanical timing data needed by the 6000 ms calibration decision. It does not store:

- training selections/telemetry;
- A/B choice identity in the timing calibration dataset;
- reason selections;
- reflection free text;
- reaction intensity;
- reason/intensity response times;
- derived participant result;
- persistent participant ID;
- exact viewport or user-agent fingerprint.

Only coarse device category plus the timing fields required by `timing-calibration-v1` are stored.

Existing Wave1 storage is not reused.

## TECHNICAL vs CALIBRATION

`cl_calibration_runs.run_type` is assigned by server configuration and separates owner engineering runs from real timing calibration.

Keep this in local `server/config.php` during owner testing:

```php
'collection_mode' => 'TECHNICAL',
```

TECHNICAL runs are visible in admin but never enter N/20.

Do not switch to `CALIBRATION` until fresh-participant collection is explicitly authorized.

## Canonical and Hostinger-compatible modules

The subtree `canonical/` carries deployment copies of required source/config/assets.

Research/config `.mjs` copies that are declared canonical are checked against repository source bytes in CI.

Because the deployed Hostinger environment served `.mjs` as `text/plain`, the package also contains Hostinger-compatible `.js` modules. `index.php` rewrites module references from `.mjs` to `.js` at delivery time.

Research image bytes are not resampled or rewritten.

## Updating the existing LAB deployment

A CI artifact may be extracted over the existing versioned LAB directory with overwrite enabled.

Important:

- do not delete the existing local `server/config.php`;
- the repository/artifact does not contain the secret `server/config.php`;
- no DB migration is required for the product-shaped participant-flow update;
- keep `collection_mode = TECHNICAL` during owner smoke testing;
- do not touch `/wave1/` or the OMESG360 root.

## Required owner smoke checks

1. LT flow loads and completes.
2. EN flow loads and completes.
3. reason screen shows the selected image and localized reason options.
4. intensity 1-5 appears only after reason selection.
5. fail-closed result screen reports that directional result is not available yet.
6. timing save succeeds.
7. admin records new runs as `TECHNICAL`.
8. calibration `N/20` remains `0/20` during owner testing.

## Isolated server storage

Tables:

```text
cl_calibration_runs
cl_calibration_attempts
cl_calibration_pair_events
```

Admin:

```text
/conflictlab/releases/calibration-v0.1/server/admin.php
```

Admin v2 separates TECHNICAL and CALIBRATION evidence and reports N/20 plus timing diagnostics.

## Promotion boundary

LAB deployment does not modify:

```text
omesg360.eu/
omesg360.eu/wave1/
deploy/wave1-hostinger/
```

Owner approval of the versioned LAB still does not authorize a stable `/wave1/` public switch.

## Canonical references

- `docs/architecture/FUTURE_SESSION_IMPLEMENTATION_BASELINE_STATUS_v1.0.md`
- `docs/architecture/FUTURE_SESSION_WORKLOG.md`
- `docs/architecture/worklog/2026-08-14_PRODUCT_SHAPED_PILOT_IMPLEMENTATION.md`
- `config/future-session/timing-calibration-v1.json`
- `config/future-session/gate-d-v1.json`
- `config/future-session/gate-e-v1.json`
