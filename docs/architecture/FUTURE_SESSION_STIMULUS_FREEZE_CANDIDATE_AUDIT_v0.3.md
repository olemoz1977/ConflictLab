# ConflictLab — Future Session Stimulus Freeze Candidate Audit v0.3

**Date:** 2026-08-14  
**Status:** CORRECTED F1 AUDIT — DRAFT MATERIALIZED, NOT RELEASED  
**Supersedes:** `archive/future-session-development-history/stimulus-audits/FUTURE_SESSION_STIMULUS_FREEZE_CANDIDATE_AUDIT_v0.2.md`  
**Branch:** `arch/result-v0.2-implementation-baseline`

## 1. Correction

The previous audit incorrectly concluded that the exact Wave 1 binary assets were absent from the repository and also listed the wrong six current Wave 1 candidates.

Both points are corrected here.

The active Wave 1 deployment manifest (`wave1-v0.3`) contains exactly these six pairs:

```text
CS-PR-01
CS-RE-01
CS-CA-01
CR-PZ-01
CR-FS-01
CR-PO-01
```

The exact image binaries referenced by those pairs are already stored in the repository under:

```text
docs/experiments/stimulus-validation/assets/<pair_id>/
```

Therefore external ZIP recovery is not required for asset provenance.

---

## 2. Current Wave 1 factual inventory

The corrected repository-bound candidate manifest is:

```text
config/future-session/wave1-candidate-manifest-v0.2.json
```

It binds each current Wave 1 pair to:

```text
pair_id
stable neutral A/B IDs
repository-relative asset paths
Git blob SHA for exact source bytes
MIME type
is_training
source family
source protocol
source commit
```

The six factual A/B definitions are:

| Pair | A asset currently used by Wave 1 | B asset currently used by Wave 1 |
|---|---|---|
| `CS-PR-01` | `more-reveal.webp` | `less-reveal.jpg` |
| `CS-RE-01` | `more-evidence.png` | `less-evidence.png` |
| `CS-CA-01` | `more-reference.png` | `less-reference.png` |
| `CR-PZ-01` | `no-predefined-zones.png` | `predefined-zones.png` |
| `CR-FS-01` | `fixed-slots.png` | `continuous-capacity.png` |
| `CR-PO-01` | `partitioned-space.png` | `open-space.png` |

These A/B labels reproduce the factual Wave 1 manifest only.

They do **not** mean:

```text
A = left
B = right
A = +1
B = -1
```

Screen position remains presentation telemetry. Psychological direction remains Gate D only.

---

## 3. Provenance state

The repository proves the exact source bytes without relying on filenames alone.

For every asset, the corrected source manifest records:

```text
repository path
+
Git content-addressed blob SHA
+
source commit
```

The DRAFT future stimulus catalog additionally records SHA-256 of the exact bytes and is verified directly against repository files.

---

## 4. Revised F0–F3 state

### F0 — Candidate inventory

**Current state: PASS** for all six current Wave 1 pairs.

### F1a — Source asset provenance

**Current state: PASS.**

### F1b — Future stimulus-set materialization

All six current Wave 1 pairs were explicitly retained as the initial future-session DRAFT candidate composition.

`config/future-session/stimulus-set-v1.json` now binds:

```text
6 pair IDs
12 stable neutral asset IDs
12 exact repository paths
12 SHA-256 digests
MIME types
is_training = false
source-family provenance
```

The repository verifier passes with:

```text
verified_pair_count = 6
verified_asset_count = 12
```

**Current state: PASS AS DRAFT.**

Decision record:

```text
docs/architecture/FUTURE_SESSION_STIMULUS_F1_DECISION_v0.1.md
```

### F2 — Presentation release

Requirements:

- review future rapid three-pair block composition using the six F1 candidates;
- define pair-order randomization/counterbalancing;
- define A/B screen-position counterbalancing;
- define preload/readiness semantics before the monotonic experimental clock;
- define asset-load failure handling;
- review whether later Wave 1 descriptive QA suggests excluding a pair;
- explicitly release `stimulus-set-v1` only after review.

**Current state: NOT READY / NEXT GATE.**

### F3 — Directional interpretation release

Requirements:

- Gate D evidence for exact released pair/assets;
- mapping version immutable;
- protocol scope documented;
- portability from Wave 1 to the future shared-budget rapid protocol addressed explicitly.

**Current state: NONE.**

Gate E remains independent and later.

---

## 5. Source-of-truth separation remains unchanged

### Stimulus identity

```text
stimulus-set-vN.json
```

Stores factual identity/presentation provenance only.

### Pair-level interpretation

```text
gate-d-vN.json
```

Stores validated A/B directional interpretation only.

### Domain aggregation

```text
gate-e-vN.json
```

Stores whether different validated exemplars may be aggregated into CS/CR.

No stimulus file may duplicate Gate D direction.

---

## 6. What must not happen

The fact that the current Wave 1 folders are named `CS-*` and `CR-*` must not be treated as proof that participant choices already carry a validated CS/CR directional meaning.

Those names are design/research provenance.

Likewise, preserving Wave 1 A/B order in the future stimulus catalog is an identity decision only. It does not authorize scoring.

---

## 7. Current next sequence

```text
1. F1 exact asset identity — COMPLETE AS DRAFT
2. Perform F2 future rapid presentation/protocol review
3. Keep stimulus-set-v1 DRAFT until F2 is explicitly approved
4. Only after F2 author pair+anchor-specific reflection reason content
5. Keep Gate D and Gate E independent until their own evidence gates pass
```

No stimulus release, Gate D mapping, Gate E aggregation or Reflection UI is authorized by F1 alone.
