# ConflictLab — Project State

**Last updated:** 2026-08-13  
**Purpose:** current-state source for humans and AI. Read this first.

---

## 1. CURRENT MILESTONE

**v0.8 Human Wave 1 — PILOT READY.**

Stimulus curation is complete. The Human Wave 1 platform is live on Hostinger, pre-pilot hardening is complete, non-secret deployment source is mirrored in this repository, and a real-device live data-capture smoke test has passed.

**Live Human Wave 1:** `https://omesg360.eu/wave1/`  
**Frozen pilot protocol:** `wave1-v0.2`

Deployment source:

```text
deploy/wave1-hostinger/index.html
deploy/wave1-hostinger/api.php
deploy/wave1-hostinger/config.example.php
deploy/wave1-hostinger/migrate_wave1.sql
deploy/wave1-hostinger/README.md
```

The committed v0.2 artifacts were supplied for deployment and then verified through the live mobile flow and MySQL rows. They were not independently downloaded back from Hostinger for a byte-for-byte server comparison.

---

## 2. CONSTITUTIONAL METHODOLOGY BOUNDARY

```text
SCENE PROPERTY / VISUAL MANIPULATION
        ↓
PARTICIPANT RESPONSE
        ↓
DERIVED SIGNAL
```

These levels must not be collapsed.

- raw A/B choice has no inherent psychological polarity
- a stimulus variant is not AW+, AW-, CS+, CS-, CR+ or CR-
- `signal_mapping_status: NONE` remains in force for all Wave 1 pairs
- Gate D / empirical evidence is required before defensible signal mapping

Current authoritative boundary: `docs/adr/ADR-011-stimulus-signal-separation.md`.

---

## 3. AW STATUS

AW as a peer **static-stimulus axis is SUSPENDED** for active v0.8 development.

- do not create new AW-specific static-image assets
- previous AW candidates remain historical exploratory evidence
- `prototype-nine-v1` AW behavior remains frozen technical/UX prototype behavior
- domain-specific response trajectory is an active hypothesis, not validated
- product engagement and session completion must not be used as automatic trajectory evidence

Current decision: `docs/experiments/pair-p0/AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md`.

---

## 4. STIMULUS VALIDATION WAVE 1 — INTERNAL CURATION COMPLETE

All 6 families = **KEEP for Human Wave 1**. All 12 assets are committed.

### CS
1. `CS-PR-01` — Partial Reveal
   - X `more-reveal.webp`
   - Y `less-reveal.jpg`
2. `CS-RE-01` — Relation Evidence
   - X `more-evidence.png`
   - Y `less-evidence.png`
3. `CS-CA-01` — Context / Reference Availability
   - X `more-reference.png`
   - Y `less-reference.png`

### CR
4. `CR-PZ-01` — Predefined Zones
   - X `no-predefined-zones.png`
   - Y `predefined-zones.png`
5. `CR-FS-01` — Fixed Slots vs Continuous Capacity
   - X `fixed-slots.png`
   - Y `continuous-capacity.png`
6. `CR-PO-01` — Partitioned vs Open Functional Space
   - X `partitioned-space.png`
   - Y `open-space.png`

Rules:

- `signal_mapping_status: NONE` for all pairs
- X/Y has no inherent CS/CR polarity
- no new stimulus generation before Human Wave 1 evidence
- Human Wave 1 is one blind multi-pair session using all six exemplars
- no CS/CR/family labels shown to participants

Active plan: `docs/experiments/stimulus-validation/WAVE1_PLAN.md`.

---

## 5. HUMAN WAVE 1 — FROZEN PILOT IMPLEMENTATION

Live stack:

```text
Hostinger site: omesg360.eu
Path: /wave1/
UI: HTML + vanilla JS
API: PHP
Storage: MySQL
Assets: local /wave1/assets/
Protocol: wave1-v0.2
```

Current participant flow:

1. intro → Start
2. six pairs in randomized order
3. left/right randomized per pair
4. participant selects left, right, or `no_clear_choice`
5. after left/right choice:
   - optional free-text reason
   - optional reaction intensity 1–5
   - independent `hard_to_identify` option
6. after `no_clear_choice`:
   - optional free-text reason
   - independent `hard_to_identify` option
7. response must save successfully before next pair
8. thank-you screen after six stored responses

Important raw-state distinction:

```text
no_clear_choice != hard_to_identify != empty free text
```

`reaction_intensity` remains an optional ordinal 1–5 self-report. It is not confidence, latency, valence, or vector magnitude, and must not be multiplied into a signal vector.

Current response capture:

```text
participant_id
candidate_id
protocol_version
presentation_index
left_asset
right_asset
choice
free_text
intensity
hard_to_identify
latency_ms
created_at
```

DB duplicate protection:

```text
UNIQUE (participant_id, candidate_id)
```

API controls include candidate and asset whitelists, UUID validation, choice/index/intensity/latency validation, duplicate protection and failure-aware progression.

The public `check.php` inspection helper has been removed. `setup.php` is not part of the live deployment.

No live credentials or participant dataset belong in GitHub.

---

## 6. LIVE SMOKE TEST — PASS

Real-device verification on 2026-08-13 confirmed:

- all six pairs complete
- one session writes exactly six rows under one `participant_id`
- `presentation_index` persists as 1–6
- new rows persist `protocol_version = wave1-v0.2`
- randomized `left_asset` / `right_asset` persist
- left/right and `no_clear_choice` paths persist
- optional free text persists when entered
- optional intensity persists
- `hard_to_identify` persists independently, including with a left/right choice and intensity
- `latency_ms` is populated

**Live data-capture smoke test: PASS.**

Rows created before the pilot freeze should be treated as pre-pilot technical data unless separately documented otherwise. Do not mix them into Human Wave 1 analysis solely because they remain in the same table.

---

## 7. NEXT ACTIONS — ORDERED

1. **Begin the first real Human Wave 1 participant cycle using only `wave1-v0.2`.**
2. Preserve the v0.2 participant flow and capture semantics during the pilot.
3. Exclude pre-pilot technical rows from research analysis using protocol/inclusion rules; do not delete historical test rows blindly.
4. After the planned Human Wave 1 sample, analyze each manipulation family for:
   - supported
   - cross-load
   - insufficient
   - NONE
   plus dominant confounds.
5. Decide KEEP / REVISE / REJECT by family from human evidence.
6. Only surviving families may receive second exemplars.

Do not expand the stimulus library before evidence from this cycle.

Any participant-facing or capture-semantics change after pilot start requires a new protocol version (for example `wave1-v0.3`) and an explicit delta before additional research data are collected.

---

## 8. PROJECT LAYERS

| Layer | Status | Meaning |
|---|---|---|
| Human Wave 1 | **PILOT READY / v0.2 FROZEN** | live Hostinger blind validation platform |
| Stimulus Validation Wave 1 | CURATION COMPLETE | 6 families / 12 assets |
| `prototype-nine-v1` | FROZEN TECHNICAL/UX REFERENCE | historical prototype behavior, not current v0.8 method truth |
| Pair P0 documentation | MIXED | current methodological decisions + historical prototype records |
| v0.7 | FROZEN BASELINE | reusable methodological/architecture source, not active product development |

The old `3 AW + 3 CS + 3 CR` and `18 unique pairs` model is historical/prototype planning, **not a current scientific minimum**.

---

## 9. SOURCE OF TRUTH HIERARCHY

Read in this order:

1. `PROJECT_STATE.md` — current operational state
2. `docs/experiments/stimulus-validation/WAVE1_PLAN.md` — current Wave 1 human protocol
3. `docs/adr/ADR-011-stimulus-signal-separation.md` — scene property ≠ response ≠ signal
4. `docs/experiments/pair-p0/METHODOLOGY_DELTA_2026-08-10.md` — newer decisions that supersede conflicting V1.3 text
5. `docs/experiments/pair-p0/AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md` — AW suspension
6. `docs/experiments/pair-p0/STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md` — candidate design spec, subject to newer delta/ADR decisions
7. `docs/experiments/stimulus-validation/SESSION_CHECKPOINT_2026-08-12.md` — frozen curation checkpoint
8. `deploy/wave1-hostinger/README.md` — current v0.2 deployment record
9. `REPOSITORY_INVENTORY.md` — file status map

`WHY_CONFLICTLAB.md`, v0.7 methodology files, Pair P0 prototype docs, N0 docs and beta-test packs are useful history/reference but must not override the hierarchy above.

---

## 10. FROZEN / HISTORICAL REFERENCES

### prototype-nine-v1 / Pair P0

Stable tag: `pair-p0-prototype-nine-v1-radar-ux-stable`

Technically verified historical reference includes:

- 3-session × 3-pair blocks
- radar after complete block
- block comparison overlay
- provenance export
- LT/EN parity

Historical only for v0.8 methodology:

- AW/CS/CR as three equivalent stimulus axes
- `3+3+3` balance
- choice → cue → predefined vector logic
- 18 unique pairs as scientific requirement

Do not rewrite the frozen prototype solely to mirror current v0.8 methodology.

### v0.7

`docs/index.html`, `docs/methodology/`, `src/engine/`, `stimuli/ST-001–010` are frozen/reference material. Do not actively develop them unless explicitly reopened.

---

## 11. REPOSITORY HOUSEKEEPING STATUS — 2026-08-13

Earlier consolidation:

- refreshed README / PROJECT_STATE / REPOSITORY_INVENTORY
- preserved live/frozen Pair P0 and v0.7 paths
- archived confirmed obsolete root `validation/` content to `archive/v0.4-validation/`
- archived obsolete single-image `docs/review.html` and old `docs/generator.html` to `archive/legacy-tools/`

Current pilot-freeze update:

- mirrors non-secret Human Wave 1 v0.2 deployment source under `deploy/wave1-hostinger/`
- records the applied DB migration and safe config template
- records removal of public `check.php`
- records live smoke-test PASS
- freezes `wave1-v0.2` as the pilot baseline

No stimulus assets, stable tags, Pair P0 code, v0.7 code, or signal-mapping decisions are changed by this deployment freeze.

---

## 12. FOR AI ASSISTANTS

1. Do not infer signal polarity from stimulus X/Y.
2. Do not create AW-specific static-image assets.
3. Do not generate additional Wave 1 stimuli before human evidence.
4. Do not treat product continuation as domain trajectory evidence.
5. Do not modify frozen Pair P0/v0.7 flows without explicit instruction.
6. Treat `wave1-v0.2` as frozen once real pilot collection begins; participant-facing/capture changes require a new protocol version.
7. Never commit Hostinger DB passwords, API keys, live `config.php`, or participant data.
8. When state conflicts exist, prefer the source-of-truth hierarchy above.
