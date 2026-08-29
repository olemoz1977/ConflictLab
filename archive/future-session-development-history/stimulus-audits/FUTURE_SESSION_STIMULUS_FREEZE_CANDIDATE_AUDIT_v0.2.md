# ConflictLab — Future Session Stimulus Freeze Candidate Audit v0.2

**Date:** 2026-08-14  
**Status:** DRAFT CANDIDATE AUDIT — NO STIMULUS RELEASE  
**Supersedes:** `FUTURE_SESSION_STIMULUS_FREEZE_CANDIDATE_AUDIT_v0.1.md`  
**Branch:** `arch/result-v0.2-implementation-baseline`

## 1. Correction from v0.1

The stimulus-set artifact stores **factual stimulus identity only**. It does not duplicate Gate D state.

Therefore fields such as:

```text
signal_mapping_status
asset_a_direction
asset_b_direction
```

belong exclusively to the versioned Gate D catalog and must not be copied into `stimulus-set-v1.json`.

This prevents two methodological sources of truth from drifting apart.

---

## 2. Three independent gates

The word “frozen” is insufficiently precise. Future-session stimuli pass three independent questions:

### Identity / presentation

```text
Which exact pair and exact image bytes were presented?
```

Source of truth:

```text
stimulus-set-vN.json
+
canonical repository assets
+
SHA-256
```

### Pair-level interpretation

```text
Does choosing exact asset A or B support a directional interpretation for this exact contrast?
```

Source of truth:

```text
gate-d-vN.json
```

### Domain aggregation

```text
May different validated exemplars be aggregated into CS or CR?
```

Source of truth:

```text
gate-e-vN.json
```

Passing stimulus identity never implies Gate D. Passing Gate D never implies Gate E.

---

## 3. Existing material disposition

### Legacy `stimuli/ST-*`

**Do not migrate directly.**

Reason:

- single visual + textual response protocol;
- incompatible with future simultaneous visual A/B choice;
- historical provisional/unvalidated signal weights;
- AW material is outside active v0.2 result domains.

### `prototype-nine-v1`

**Do not use as the freeze source.**

Reason:

- explicitly marked technical prototype only;
- P0-001 superseded/confounded;
- P0-002 is AW;
- P0-003 superseded by newer controlled CS contrasts;
- N0-004..N0-009 are QA/prototype/unresolved/placeholder/confounded material.

### Current Wave 1 controlled pairs

These are the strongest existing **F0 identity candidates**:

| Pair | Design provenance | Existing X asset filename | Existing Y asset filename | Candidate state |
|---|---|---|---|---|
| `CS-PR-01` | CS / partial reveal | `more-reveal.webp` | `less-reveal.webp` | F0 candidate |
| `CS-CO-01` | CS / compression | `sharp-photo.webp` | `compressed-photo.webp` | F0 candidate |
| `CS-OC-01` | CS / occlusion | `object-clear.webp` | `object-occluded.webp` | F0 candidate |
| `CR-PZ-01` | CR / puzzle | `puzzle-complete.webp` | `puzzle-piece-missing.webp` | F0 candidate |
| `CR-SY-01` | CR / symmetry | `symmetry-perfect.webp` | `symmetry-disturbed.webp` | F0 candidate |
| `CR-OR-01` | CR / order | `objects-aligned.webp` | `objects-one-shifted.webp` | F0 candidate |

`CS` and `CR` in this table are design/provenance labels only. They are not participant signal mappings.

No `+1/-1` mapping is authorized here.

---

## 4. Stable A/B identity

If these candidates are carried into the future session, neutral stable identities may be assigned:

```text
CS-PR-01-A
CS-PR-01-B
...
```

with the invariants:

```text
A != left
B != right
A != +1
B != -1
```

Concrete screen position remains event-level presentation telemetry.

---

## 5. Current binary provenance blocker

The Wave 1 deployment manifest references the twelve `.webp` files, but the base repository snapshot does not contain the referenced `deploy/wave1-hostinger/assets/` directory.

The root `.gitignore` does not explain the omission.

Therefore the repository currently proves:

```text
pair IDs
asset filenames
runtime references
```

but does not prove:

```text
the exact canonical image bytes
```

A filename alone is insufficient for reproducible stimulus identity.

---

## 6. F0–F3 freeze states

### F0 — Candidate inventory

Requirements:

- identifiable pair;
- neutral A/B identity can be assigned;
- no directional claim.

**Current state:** PASS for the six Wave 1 controlled pairs above.

### F1 — Asset freeze

Requirements:

- exact canonical bytes available;
- versioned repository-relative path;
- stable asset ID;
- SHA-256 matches exact bytes;
- MIME/extension contract valid;
- A and B are not identical bytes;
- `is_training` fixed.

**Current state:** BLOCKED because the twelve canonical binary assets are not available in the repository baseline.

### F2 — Presentation release

Requirements:

- F1 passed;
- stimulus-set version `RELEASED` and immutable;
- rendering/loading QA passed;
- exact pair order/randomization/counterbalancing contract fixed.

**Current state:** NOT READY.

### F3 — Directional interpretation release

Requirements:

- Gate D passed for the exact released pair/assets;
- mapping version immutable;
- evidence source/protocol documented;
- portability to the future rapid shared-budget protocol explicitly addressed.

**Current state:** NONE.

Gate E remains a separate later requirement for domain aggregation.

---

## 7. Canonical asset contract

`config/future-session/stimulus-set-v1.json` now requires factual asset provenance fields for every configured pair:

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

`source_family` records design provenance. It does not authorize interpretation.

Recommended canonical location after the real files are recovered:

```text
assets/future-session/stimulus-set-v1/
```

Example factual pair object:

```json
{
  "pair_id": "CS-PR-01",
  "asset_a_id": "CS-PR-01-A",
  "asset_b_id": "CS-PR-01-B",
  "asset_a_path": "assets/future-session/stimulus-set-v1/CS-PR-01-A.webp",
  "asset_b_path": "assets/future-session/stimulus-set-v1/CS-PR-01-B.webp",
  "asset_a_sha256": "<64 lowercase hex chars>",
  "asset_b_sha256": "<64 lowercase hex chars>",
  "asset_a_mime_type": "image/webp",
  "asset_b_mime_type": "image/webp",
  "is_training": false,
  "source_family": "CS-PR"
}
```

No Gate D fields appear in this object.

---

## 8. Automated freeze verifier

Added:

```text
tools/verify_future_stimulus_assets.py
```

The verifier is repository-local and deterministic. It does not download assets and does not infer psychology.

It checks:

- supported stimulus-set schema/version metadata;
- DRAFT vs RELEASED lifecycle invariants;
- required pair fields;
- unique pair IDs;
- stable asset IDs;
- safe repository-relative paths;
- no remote URL/path traversal;
- file existence;
- extension/MIME consistency;
- exact SHA-256 match;
- same asset ID cannot silently point to different provenance;
- one path cannot silently represent two different IDs;
- A/B IDs differ;
- A/B bytes differ;
- RELEASED cannot be empty;
- RELEASED requires `content_status = FROZEN` and `released_at`.

The current intentionally empty DRAFT catalog passes. A future incorrect or incomplete RELEASED catalog must fail CI.

---

## 9. Protocol portability remains separate

Wave 1 and future-session observation conditions differ materially.

```text
Wave 1:
validation flow for individual controlled pairs

Future session:
3 sequential pairs under one shared rapid budget
```

Therefore a future Gate D decision should retain validation scope explicitly. Evidence obtained under Wave 1 must not silently become proof of portability to the rapid shared-budget condition.

Recommended research provenance concept:

```text
validation_protocol: wave1-v0.3
portability_to_future_rapid_block: UNTESTED | SUPPORTED | REJECTED
```

This belongs with mapping/evidence provenance, not in the stimulus identity file.

---

## 10. Current decision

The stimulus problem is now defined precisely:

> We have six plausible controlled **F0 candidate identities**, but no reproducibly frozen **F1 asset set** yet.

The next required action is not inventing more pairs and not assigning directions.

It is:

1. recover the exact twelve canonical image binaries currently used for the six Wave 1 pairs;
2. place those bytes under canonical versioned repository paths;
3. assign stable neutral A/B asset IDs;
4. calculate SHA-256;
5. populate the DRAFT `stimulus-set-v1.json` from those exact bytes;
6. run the automated verifier;
7. review whether all six or a subset enter the future rapid protocol;
8. only after F1/F2 author pair+anchor-specific reflection reasons;
9. keep Gate D independent and non-interpretive until its own empirical criteria are met.

No stimulus release, Gate D mapping, Gate E aggregation, or Reflection UI is authorized by this audit.
