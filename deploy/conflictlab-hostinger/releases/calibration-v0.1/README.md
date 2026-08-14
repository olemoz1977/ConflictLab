# ConflictLab calibration-v0.1

**Lifecycle:** LAB  
**Deploy status:** NOT DEPLOYED  
**Public switch:** NOT AUTHORIZED

This is a Hostinger deployment candidate for validating the shared 6000 ms rapid-block timing hypothesis. It is not a psychological scoring release.

## Participant flow

```text
Stage 0 familiarization (local only)
→ fresh 3-pair measured block / shared 6000 ms
→ timing-only server save
→ Reflection (local only for this calibration release)
→ finish
```

The measured server payload deliberately excludes:

- training selections/telemetry;
- A/B choice identity (stored only as `choice` vs `timeout`);
- reflection reasons and free text;
- participant result;
- Gate D/E interpretation;
- persistent participant ID;
- exact viewport, user agent or device fingerprint.

Only coarse `device_category` (`mobile`, `tablet`, `desktop`, `unknown`) is stored for the timing diagnostic defined by `timing-calibration-v1`.

## Canonical byte copies

The subtree `canonical/` is a deployment copy of the current repository source/config/assets required by the app. Configs, JS modules and images are copied byte-for-byte using their existing Git blob identities. The methodology source of truth remains outside this deployment directory.

The release app uses:

```text
./canonical/config/future-session/*
./canonical/src/future_session/*
./canonical/docs/experiments/stimulus-validation/assets/*
./canonical/docs/experiments/pair-p0/images/*
```

This preserves the repository-relative paths embedded in the canonical stimulus/training configs without rewriting methodology JSON.

## Isolated server storage

Run `server/schema.sql` against a dedicated calibration database/schema or database user. Do not point this package at the frozen Wave 1 `responses` storage.

Copy:

```text
server/config.example.php → server/config.php
```

and set the real DB credentials plus an admin password hash on Hostinger. `config.php` must never be committed.

Admin:

```text
/conflictlab/releases/calibration-v0.1/server/admin.php
```

The admin dashboard reports clean N/20, exclusions, primary completion, P3 missingness/never-presented rate, P3-P1 gradient, pair missingness, retry diagnostic and positional latency/budget medians. It applies the current `timing-calibration-v1` KEEP / ADJUST / REJECT thresholds only after the configured N floor.

## Promotion boundary

LAB deployment does not modify:

```text
omesg360.eu/
omesg360.eu/wave1/
deploy/wave1-hostinger/
```

After LAB deployment, the owner must test the exact versioned release URL. `OWNER_APPROVED` still does not authorize the stable `/wave1/` public switch. That is a separate explicit action under `docs/architecture/HOSTINGER_RELEASE_ROUTING_v0.1.md`.