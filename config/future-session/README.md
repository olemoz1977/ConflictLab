# Future-session methodological config

This directory contains versioned methodological artifacts for the post-Wave-1 architecture.

## Source-of-truth rule

The JSON files in this directory are canonical public configuration for:

- stimulus-set pair and stable A/B asset identities;
- training/familiarization stimulus references and exclusion boundaries;
- rapid-presentation protocol mechanics and timing hypothesis;
- Gate D pair-level directional mappings;
- Gate E domain aggregation validity;
- structured reflection reason definitions.

Lifecycle:

- `DRAFT`: may change before release.
- `RELEASED`: immutable. Never edit a released version in place.
- Any methodological change after release creates a new file/version.

Examples:

```text
stimulus-set-v1.json -> RELEASED -> never changed
stimulus-set-v2.json -> changed/extended stimulus composition

gate-d-v1.json -> RELEASED -> never changed
gate-d-v2.json -> new mapping decisions
```

## Asset identity vs screen position

`asset_a_id` and `asset_b_id` are stable identities inside a versioned pair definition. They are not screen sides or psychological signs.

```text
A != left
B != right
A != +1
B != -1
```

Concrete screen position is recorded separately for every presentation. Gate D may later map stable asset identity to a validated direction, but only when `mapping_status = VALIDATED`.

## Current Wave 1 source inventory

The corrected factual inventory of the six pairs currently used by Wave 1 is:

```text
wave1-candidate-manifest-v0.2.json
```

It binds the active Wave 1 pair manifest to the exact repository source assets under:

```text
docs/experiments/stimulus-validation/assets/<pair_id>/
```

using repository-relative paths and Git blob SHAs at the recorded source commit.

The six current Wave 1 pair IDs are:

```text
CS-PR-01
CS-RE-01
CS-CA-01
CR-PZ-01
CR-FS-01
CR-PO-01
```

The older `wave1-candidate-manifest-v0.1.json` is superseded and must not be used as the current Wave 1 inventory.

## Training / familiarization

`training-set-v1.json` defines only the pre-measurement interaction familiarization stage.

It references the existing Pair P0 assets in place:

```text
P0-001
P0-002
P0-003
```

Source paths remain under `docs/experiments/pair-p0/images/`; the P0 files and their historical semantics are not moved, renamed or rewritten.

Training is explicitly fail-closed:

```text
is_training = true
analysis_eligible = false
timing_calibration_eligible = false
Gate D = NOT_APPLICABLE
Gate E = NOT_APPLICABLE
server_upload = false
participant_result = NONE
```

A successful training block is required before the fresh measured pilot block in the isolated owner preview.

## Local-first boundary

These files are public methodological configuration. They contain no participant data.

The server may serve/cache them, but a mutable database table is not the source of truth.

## Current future-session baseline

The future-session implementation remains isolated from production and all methodological artifacts remain pre-release.

Current state:

```text
stimulus-set-v1.json         DRAFT; 6 pairs / 12 exact assets materialized
training-set-v1.json         DRAFT; P0-001/002/003 familiarization references
rapid-presentation-v1.json   DRAFT; rapid mechanics complete for pilot
6000 ms shared budget        hypothesis only; real calibration data pending
reason-map-v1.json           DRAFT; 48 pair+anchor-specific items
exact-asset reason review    COMPLETE
Reflection model/UI          IMPLEMENTED AS DRAFT in isolated preview
Stage 0 training             IMPLEMENTED / LOCAL-ONLY / CALIBRATION-EXCLUDED
owner telemetry export       IMPLEMENTED / schema conflictlab.owner-ux-export.v2
owner UX approval            PENDING — Run 002 next
Gate D                       NONE
Gate E                       NONE
production deploy            NOT AUTHORIZED
```

The exact research stimulus bytes are repository-bound and SHA-256 verified. This factual identity does not authorize directional interpretation.

The current branch status source is:

```text
docs/architecture/FUTURE_SESSION_IMPLEMENTATION_BASELINE_STATUS_v0.9.md
```

Superseded intermediate future-session status/audit/review documents are retained under:

```text
archive/future-session-development-history/
```
