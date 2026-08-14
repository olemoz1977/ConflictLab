# ConflictLab — Future Session F1 Asset Freeze Runbook v0.1

**Date:** 2026-08-14  
**Status:** OPERATIONAL RUNBOOK — DOES NOT AUTHORIZE RELEASE

## Purpose

Convert the six factual Wave 1 F0 candidate pairs into a reproducible **DRAFT F1 asset set** once the exact twelve canonical source image files are available.

This runbook performs stimulus identity/provenance only. It does not:

- validate CS/CR meaning;
- write Gate D mappings;
- pass Gate E;
- create reflection reason text;
- mark the stimulus set `RELEASED`;
- deploy anything.

## Expected source filenames

Place the exact source files in one local directory:

```text
more-reveal.webp
less-reveal.webp
sharp-photo.webp
compressed-photo.webp
object-clear.webp
object-occluded.webp
puzzle-complete.webp
puzzle-piece-missing.webp
symmetry-perfect.webp
symmetry-disturbed.webp
objects-aligned.webp
objects-one-shifted.webp
```

The factual mapping from source filenames to stable neutral IDs is stored in:

```text
config/future-session/wave1-candidate-manifest-v0.1.json
```

## Step 1 — Dry run

From repository root:

```bash
python tools/import_wave1_future_candidates.py \
  --source-dir /path/to/exact-wave1-assets
```

Expected result:

```text
status = DRY_RUN
pair_count = 6
asset_count = 12
```

The dry run does not copy or modify files.

Stop immediately if:

- any expected file is missing;
- any filename differs unexpectedly;
- a file extension is unsupported;
- A/B source bytes are identical;
- the manifest is not the expected F0 inventory.

## Step 2 — Review dry-run mapping

Before writing, inspect every generated pair and confirm only factual identity:

```text
pair_id
source filename -> stable asset ID
source_family
is_training
```

Do not review or assign psychological direction at this stage.

The invariant is:

```text
stable A/B identity != screen position != Gate D direction
```

## Step 3 — Import DRAFT assets

Only after the dry run is correct:

```bash
python tools/import_wave1_future_candidates.py \
  --source-dir /path/to/exact-wave1-assets \
  --write
```

The tool will:

1. copy exact bytes into:

```text
assets/future-session/stimulus-set-v1/
```

2. rename canonical files by stable asset ID;
3. calculate SHA-256 from source bytes;
4. write factual asset paths/hashes/MIME metadata into the DRAFT `stimulus-set-v1.json`;
5. verify the copied bytes again;
6. run the same repository verifier contract in-process.

The importer deliberately leaves:

```text
lifecycle = DRAFT
content_status = PENDING_STIMULUS_FREEZE
released_at = null
```

It cannot release the set.

## Step 4 — Independent verifier

Run again from a fresh process:

```bash
python tools/verify_future_stimulus_assets.py
```

Required result:

```text
status = PASS
verified_pair_count = 6
verified_asset_count = 12
```

A filename alone is never accepted as asset identity. The verifier recomputes SHA-256 from repository bytes.

## Step 5 — Git diff review

Review the diff before commit.

Expected new/changed material:

```text
12 canonical image files
config/future-session/stimulus-set-v1.json
```

The stimulus JSON must contain factual fields only:

```text
pair_id
asset_a_id
asset_b_id
asset_a_path
asset_b_path
asset_a_sha256
asset_b_sha256
asset_a_mime_type
asset_b_mime_type
is_training
source_family
```

The diff must NOT introduce:

```text
signal_mapping_status
mapping_status
asset_a_direction
asset_b_direction
+1/-1 interpretation
trait/personality language
```

Those belong to later independent Gate D work.

## Step 6 — CI

The branch workflow must remain green, including:

```text
test_future_stimulus_asset_verifier.py
test_import_wave1_future_candidates.py
python tools/verify_future_stimulus_assets.py
```

Do not bypass a verifier failure by editing the stored hash. Determine which bytes are canonical first.

## Step 7 — F1 human review

After technical verification, review the exact rendered canonical assets and confirm:

- each A/B image is the intended Wave 1 source;
- no accidental re-encoding/crop/replacement occurred;
- pair membership is correct;
- training status is correct;
- all six pairs or the intended subset should proceed to future-session presentation testing.

Only after this review can the asset set be considered **F1 candidate complete**.

## What comes after F1

F1 still does not authorize interpretation.

Next sequence:

```text
F1 exact asset freeze
-> F2 presentation/protocol review
-> pair+anchor reflection reason authoring
-> independent Gate D validation work
-> independent Gate E aggregation work
```

Wave 1 evidence must not silently be treated as proof that a mapping transports unchanged into the future three-pair shared-budget rapid condition.

## Release boundary

Changing:

```text
lifecycle: DRAFT -> RELEASED
```

is deliberately outside this importer and outside this runbook's automatic actions.

A release requires an explicit reviewed decision after exact assets, protocol composition and version metadata are final. Once `RELEASED`, the version is immutable; later changes require a new stimulus-set version.
