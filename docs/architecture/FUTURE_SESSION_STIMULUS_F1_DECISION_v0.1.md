# ConflictLab — Future Session Stimulus F1 Decision v0.1

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Status:** F1 ASSET IDENTITY COMPLETE — DRAFT, NOT RELEASED

## Decision

All six pairs currently used by `wave1-v0.3` are retained as the initial DRAFT candidate composition for `stimulus-set-v1`:

```text
CS-PR-01
CS-RE-01
CS-CA-01
CR-PZ-01
CR-FS-01
CR-PO-01
```

No pair is removed based on the current very small Wave 1 sample. The current Wave 1 observations remain descriptive stimulus diagnostics only.

## Exact identity binding

`config/future-session/stimulus-set-v1.json` now binds all six pairs to the exact repository assets already used by Wave 1.

Each pair records:

```text
pair_id
stable neutral asset_a_id / asset_b_id
repository-relative asset paths
SHA-256 of exact bytes
MIME type
is_training = false
source_family provenance
```

The source inventory is independently recorded in:

```text
config/future-session/wave1-candidate-manifest-v0.2.json
```

which also records the Wave 1 source commit and Git blob SHA provenance.

## Verification

The repository verifier must pass:

```text
python tools/verify_future_stimulus_assets.py
```

Expected DRAFT result:

```text
verified_pair_count = 6
verified_asset_count = 12
```

The verifier checks exact SHA-256 against repository bytes, path safety, MIME/extension agreement, stable identity uniqueness and non-identical A/B bytes.

## Boundary

This decision establishes **stimulus identity only**.

It does not authorize:

```text
Gate D directional mapping
Gate E domain aggregation
+1/-1 scoring
trait/personality inference
Reflection reason-map content
stimulus-set RELEASED status
production deployment
```

A/B remain neutral stable identities:

```text
A != left
B != right
A != +1
B != -1
```

## Remaining gate

The next stimulus decision is **F2 presentation/protocol review** for the future rapid block:

- exact three-pair block composition rules;
- use of six candidates across blocks/sessions;
- pair order randomization/counterbalancing;
- A/B screen-position counterbalancing;
- loading/rendering readiness before the monotonic experimental clock;
- whether Wave 1 choice concentration, no-clear-choice rate or position diagnostics justify excluding a pair once a larger sample exists.

Until F2 is reviewed, `stimulus-set-v1` remains:

```text
lifecycle = DRAFT
content_status = PENDING_STIMULUS_FREEZE
f1_asset_identity_status = COMPLETE
```

Gate D and Gate E remain independent and non-interpretive.
