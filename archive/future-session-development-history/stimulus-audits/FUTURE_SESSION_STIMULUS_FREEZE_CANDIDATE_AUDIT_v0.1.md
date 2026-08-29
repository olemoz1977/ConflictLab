# ConflictLab — Future Session Stimulus Freeze Candidate Audit v0.1

**Date:** 2026-08-14  
**Status:** DRAFT CANDIDATE AUDIT — NO STIMULUS RELEASE  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Architecture baseline:** `RESULT_CALCULATION_ARCH_v0.2` + ADR-010/011/012

## 1. Purpose

Identify which existing ConflictLab visual material can legitimately become candidate content for `config/future-session/stimulus-set-v1.json` without importing legacy signal assumptions, provisional mappings, or unreproducible assets.

This audit separates three questions that must not be collapsed:

```text
CANDIDATE IDENTITY
Is this an exact pair we may preserve and test further?

ASSET FREEZE
Can the exact image bytes be reproduced and verified later?

SIGNAL VALIDITY
Does a participant choice between these exact assets have an empirically supported directional interpretation?
```

Passing one layer does not imply passing the next.

---

## 2. Sources reviewed

- `stimuli/README.md`
- legacy `stimuli/ST-*/stimulus.yaml` examples
- `docs/experiments/pair-p0/pair-set-prototype-nine-v1.json`
- `docs/experiments/pair-p0/PAIR_P0_STATE.md`
- `docs/experiments/stimulus-validation/LEGACY_PAIR_SALVAGE_AUDIT_2026-08-12.md`
- `docs/experiments/stimulus-validation/SESSION_CHECKPOINT_2026-08-12.md`
- `docs/experiments/stimulus-validation/WAVE1_PLAN.md`
- `docs/adr/ADR-011-stimulus-signal-separation.md`
- `deploy/wave1-hostinger/index.html`
- repository tree at base commit `44426f715103a90bc79967d2655b75c1f33bbd2c`

---

## 3. Legacy `stimuli/ST-*` library — not direct future-session candidates

The old stimulus library uses a different interaction model:

```text
single visual stimulus
+
textual response alternatives
```

The future-session rapid block requires:

```text
two simultaneous visual assets
+
A / B / timeout
+
no textual interpretation during rapid choice
```

Several old stimulus files also carry provisional, explicitly unvalidated signal weights.

### Decision

**Do not migrate `ST-*` entries directly into `stimulus-set-v1`.**

They may remain historical design references, but their old AW/CS/CR labels, weights, or approval states do not transfer into the paired-visual protocol.

AW is additionally outside the active v0.2 result architecture.

---

## 4. `prototype-nine-v1` — technical/UX reference, not freeze source

`pair-set-prototype-nine-v1.json` contains nine paired visuals, but the artifact explicitly states:

> PROTOTYPE ONLY. Not for methodology analysis.

The 2026-08-12 salvage audit further weakens direct reuse:

- **P0-001** — reject/supersede: multiple semantic and stylistic properties change together;
- **P0-002** — AW; not part of active v0.2 scoring architecture;
- **P0-003** — superseded as CS candidate by newer controlled assets; uneven photographic conditions and weaker controlled contrast;
- **N0-004..N0-009** — internal QA/prototype/unresolved/placeholder or known-confound material and not analysis eligible.

### Decision

**Do not populate future `stimulus-set-v1` from `prototype-nine-v1`.**

Its value remains technical/UX regression reference only.

---

## 5. Current Wave 1 controlled pairs — strongest identity candidates

The 2026-08-12 stimulus-validation line defines six newer controlled paired visuals. Human curation marked all six `KEEP for Wave 1`, while ADR-011 correctly keeps their signal mapping at `NONE`.

These are the strongest existing candidates for future-session **identity inventory**, not for directional interpretation.

| Pair | Design family | Current asset X | Current asset Y | Human curation | Future identity status | Gate D status |
|---|---|---|---|---|---|---|
| `CS-PR-01` | CS / partial reveal | `more-reveal.webp` | `less-reveal.webp` | KEEP | `DRAFT_CANDIDATE` | `NONE` |
| `CS-CO-01` | CS / compression | `sharp-photo.webp` | `compressed-photo.webp` | KEEP | `DRAFT_CANDIDATE` | `NONE` |
| `CS-OC-01` | CS / occlusion | `object-clear.webp` | `object-occluded.webp` | KEEP | `DRAFT_CANDIDATE` | `NONE` |
| `CR-PZ-01` | CR / puzzle | `puzzle-complete.webp` | `puzzle-piece-missing.webp` | KEEP | `DRAFT_CANDIDATE` | `NONE` |
| `CR-SY-01` | CR / symmetry | `symmetry-perfect.webp` | `symmetry-disturbed.webp` | KEEP | `DRAFT_CANDIDATE` | `NONE` |
| `CR-OR-01` | CR / order | `objects-aligned.webp` | `objects-one-shifted.webp` | KEEP | `DRAFT_CANDIDATE` | `NONE` |

### Critical interpretation rule

The `CS` and `CR` strings above are **design-family provenance**, not participant signal.

They must not create:

```text
asset X -> +1
asset Y -> -1
```

or any equivalent directional mapping until Gate D explicitly passes for the exact released asset contrast.

---

## 6. Stable A/B identity can be defined, but not yet released

For future-session architecture, the current Wave 1 X/Y assets may be assigned stable neutral identities such as:

```text
CS-PR-01-A -> more-reveal.webp
CS-PR-01-B -> less-reveal.webp
```

The letters are identity only:

```text
A != left
B != right
A != +1
B != -1
```

Position remains randomized/counterbalanced independently per presentation.

However, assigning an ID is not enough for an asset freeze.

---

## 7. Blocking provenance gap — image bytes are not in the repository baseline

`deploy/wave1-hostinger/index.html` references the twelve Wave 1 assets through paths such as:

```text
assets/more-reveal.webp
assets/less-reveal.webp
...
```

But at base commit `44426f7...` the tracked `deploy/wave1-hostinger/` directory contains the HTML/API/config example and **does not contain the referenced `assets/` directory**.

The root `.gitignore` does not exclude those assets.

Therefore the repository currently preserves:

```text
pair ID
file name
runtime reference
```

but not a repository-verifiable copy of the exact image bytes.

### Consequence

The six pairs can be called **DRAFT identity candidates**, but they cannot yet be called reproducibly frozen assets.

A file with the same name could later contain different pixels while appearing to be the same stimulus in methodology documents.

---

## 8. Required asset-freeze rule

Before `stimulus-set-v1` can become `RELEASED`, every asset must have an immutable provenance record.

Preferred future structure:

```text
assets/future-session/stimulus-set-v1/
  CS-PR-01-A.webp
  CS-PR-01-B.webp
  ...
```

and the versioned stimulus catalog should retain at minimum:

```text
asset_id
file_path
sha256
mime_type
```

Recommended pair object:

```json
{
  "pair_id": "CS-PR-01",
  "asset_a_id": "CS-PR-01-A",
  "asset_b_id": "CS-PR-01-B",
  "asset_a_path": "assets/future-session/stimulus-set-v1/CS-PR-01-A.webp",
  "asset_b_path": "assets/future-session/stimulus-set-v1/CS-PR-01-B.webp",
  "asset_a_sha256": "...",
  "asset_b_sha256": "...",
  "is_training": false,
  "source_family": "CS-PR",
  "signal_mapping_status": "NONE"
}
```

The hash protects **asset identity**. It does not validate psychological meaning.

---

## 9. Wave 1 evidence and future rapid protocol must remain separate

Current Wave 1 collection is a validation protocol for these exact visual contrasts under its own presentation/response conditions.

The future-session architecture changes the observation condition materially:

```text
Wave 1
individual pair timing / current validation flow

Future session
3 sequential pairs under one shared rapid budget
```

Therefore even if Wave 1 later supports a pair-level interpretation, that evidence must not be silently treated as proof that the same interpretation is portable to the rapid shared-budget protocol.

Any Gate D release must state its **validation scope**, for example:

```text
validation_protocol = wave1-v0.3
portability_to_future_rapid_block = UNTESTED | SUPPORTED | REJECTED
```

Until portability is explicitly resolved, future rapid results remain constrained accordingly.

---

## 10. Freeze levels

To avoid ambiguous use of the word “frozen”, use four explicit levels.

### F0 — Candidate inventory

Requirements:

- pair exists;
- stable neutral A/B identity proposed;
- no signal claim.

Current state for the six Wave 1 pairs: **PASS**.

### F1 — Asset freeze

Requirements:

- canonical asset bytes retained;
- stable path;
- SHA-256 stored;
- pair identity and training status fixed.

Current state: **BLOCKED — canonical binaries are not present in the repository baseline.**

### F2 — Presentation release

Requirements:

- F1 passed;
- exact stimulus-set version released and immutable;
- loading/rendering QA passed;
- pair-position randomization/counterbalancing contract fixed.

This permits presentation/collection only. It does **not** imply Gate D.

Current state: **NOT READY**.

### F3 — Directional interpretation release

Requirements:

- Gate D passed for exact pair/assets;
- mapping version immutable;
- validation protocol and portability scope explicit;
- Gate E still required separately before domain aggregation.

Current state: **NONE of the six pairs are F3.**

---

## 11. Candidate disposition

### Carry forward as DRAFT identity candidates

```text
CS-PR-01
CS-CO-01
CS-OC-01
CR-PZ-01
CR-SY-01
CR-OR-01
```

### Do not carry forward directly

```text
legacy ST-*          protocol mismatch
P0-001               superseded / confounded
P0-002               AW outside active v0.2 result domains
P0-003               superseded / weaker controlled contrast
N0-004..N0-009       QA/prototype/unresolved/placeholder/confounded
```

---

## 12. Decision

The stimulus-freeze blocker is now more precise:

**We do have six plausible controlled pair identities. We do not yet have a reproducibly frozen future stimulus set.**

The immediate blocker is no longer “find a third pair”. It is:

1. recover the exact twelve canonical Wave 1 image binaries;
2. preserve them under versioned asset identity;
3. calculate/store SHA-256 hashes;
4. populate `stimulus-set-v1.json` as DRAFT from those exact bytes;
5. review whether all six, or a subset, enter the future rapid protocol;
6. only after asset freeze author pair+anchor-specific reflection reason content;
7. keep Gate D at `NONE` until empirical mapping criteria are met;
8. treat portability from Wave 1 to shared-budget rapid presentation as a separate explicit validation question.

No stimulus-set release and no Gate D mapping are authorized by this audit.
