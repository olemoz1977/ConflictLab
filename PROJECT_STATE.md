# ConflictLab — Project State

**Last updated:** 2026-08-13  
**Purpose:** current-state source for humans and AI. Read this first.

---

## 1. CURRENT MILESTONE

**v0.8 Human Wave 1 — PRE-PILOT HARDENING.**

Stimulus curation is complete. A Human Wave 1 platform has been deployed on Hostinger and is reported working end-to-end. Before inviting a wider participant group, the capture flow and deployment need a final hardening pass.

**Live Human Wave 1:** `https://omesg360.eu/wave1/`

**Important provenance note:** Hostinger deployment details below come from the 2026-08-13 technical handoff. The exact live PHP/HTML source has **not yet been mirrored into this repository**. Do not reconstruct or overwrite live code from documentation alone.

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
- domain-specific response trajectory is an **active hypothesis / not validated**
- product engagement and session completion must not be used as automatic trajectory evidence

Current decision: `docs/experiments/pair-p0/AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md`.

---

## 4. STIMULUS VALIDATION WAVE 1 — INTERNAL CURATION COMPLETE

All 6 families = **KEEP for Wave 1**. All 12 assets are committed.

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

## 5. HUMAN WAVE 1 — HOSTINGER DEPLOYMENT

Technical handoff dated 2026-08-13 reports:

```text
Hostinger site: omesg360.eu
Path: /wave1/
UI: HTML + vanilla JS
API: PHP
Storage: MySQL
Assets: local /wave1/assets/
```

Current reported flow:

1. intro → Start
2. six pairs in randomized order
3. left/right randomized per pair
4. participant selects left, right, or `no_clear_choice`
5. left/right choice → free text + intensity screen
6. `no_clear_choice` currently skips reason capture
7. response POST → PHP API → MySQL
8. thank-you screen

Current DB handoff schema stores:

```text
participant_id
candidate_id
left_asset
right_asset
choice
free_text
intensity
latency_ms
created_at
```

Reported working at handoff:

- mobile UI loads
- six pairs render
- randomized pair order and left/right flip work
- API writes to DB
- 28 records were present at handoff

**Those 28 records have not been classified in repo as test vs real participant data. Do not delete them blindly.**

### Known pre-pilot hardening gaps

1. Public `check.php` should be removed or access-protected before wider rollout.
2. `no_clear_choice` should still allow/ask for spontaneous reason capture; current flow skips it.
3. `hard_to_identify` is not yet stored as a distinct state from `no_clear_choice` or simple text skipping.
4. DB/event schema does not yet store `protocol_version` or `presentation_index`.
5. Duplicate/retry idempotency should be verified beyond the current rate limit.
6. Verify that `latency_ms` starts only after both images are actually loaded/displayed.
7. There is no admin CSV/JSON export yet; phpMyAdmin/direct SQL is the current access route.
8. UI is Lithuanian only; this is not a blocker for the first LT pilot.
9. Exact live Hostinger source is not yet version-controlled in this repo.

Deployment handoff mirror: `deploy/wave1-hostinger/README.md`.

---

## 6. NEXT ACTIONS — ORDERED

Before wider participant rollout:

1. **Pre-pilot hardening on Hostinger** — address the capture/security gaps above without altering stimulus assets or methodology.
2. **Verify hardening with real-device smoke test** — all 6 pairs, all response paths, DB persistence, retry behavior.
3. **Classify existing DB records** — determine which are technical test records before any cleanup.
4. **Mirror deployment source to GitHub without secrets** — exact `index.html`, `api.php`, schema/migration, and `config.example.php`; never commit live DB credentials.
5. **Freeze a Human Wave 1 protocol/deployment version** before inviting the research sample.
6. Only then begin the first real Human Wave 1 participant cycle.

Do not expand the stimulus library before evidence from this cycle.

---

## 7. PROJECT LAYERS

| Layer | Status | Meaning |
|---|---|---|
| Human Wave 1 | ACTIVE / PRE-PILOT | live Hostinger validation platform |
| Stimulus Validation Wave 1 | CURATION COMPLETE | 6 families / 12 assets |
| `prototype-nine-v1` | FROZEN TECHNICAL/UX REFERENCE | historical prototype behavior, not current v0.8 method truth |
| Pair P0 documentation | MIXED | current methodological decisions + historical prototype records |
| v0.7 | FROZEN BASELINE | reusable methodological/architecture source, not active product development |

The old `3 AW + 3 CS + 3 CR` and `18 unique pairs` model is historical/prototype planning, **not a current scientific minimum**.

---

## 8. SOURCE OF TRUTH HIERARCHY

Read in this order:

1. `PROJECT_STATE.md` — current operational state
2. `docs/experiments/stimulus-validation/WAVE1_PLAN.md` — current Wave 1 human protocol
3. `docs/adr/ADR-011-stimulus-signal-separation.md` — scene property ≠ response ≠ signal
4. `docs/experiments/pair-p0/METHODOLOGY_DELTA_2026-08-10.md` — newer decisions that supersede conflicting V1.3 text
5. `docs/experiments/pair-p0/AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md` — AW suspension
6. `docs/experiments/pair-p0/STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md` — candidate design spec, subject to newer delta/ADR decisions
7. `docs/experiments/stimulus-validation/SESSION_CHECKPOINT_2026-08-12.md` — frozen curation checkpoint
8. `deploy/wave1-hostinger/README.md` — external live deployment handoff
9. `REPOSITORY_INVENTORY.md` — file status map

`WHY_CONFLICTLAB.md`, v0.7 methodology files, Pair P0 prototype docs, N0 docs and beta-test packs are useful history/reference but must not override the hierarchy above.

---

## 9. FROZEN / HISTORICAL REFERENCES

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

## 10. REPOSITORY HOUSEKEEPING STATUS — 2026-08-13

This consolidation pass:

- refreshes README / PROJECT_STATE / REPOSITORY_INVENTORY
- preserves live/frozen Pair P0 and v0.7 paths
- archives confirmed obsolete root `validation/` content to `archive/v0.4-validation/`
- archives the obsolete single-image `docs/review.html` and old `docs/generator.html` to `archive/legacy-tools/`
- leaves `docs/beta-test/`, N0 documents and old release/tester docs in place as historical references where moving them could break milestone documentation
- adds a non-secret Hostinger deployment handoff folder

No stimulus assets, stable tags, Pair P0 code, v0.7 code, or methodology decisions are changed by this housekeeping pass.

---

## 11. FOR AI ASSISTANTS

1. Do not infer signal polarity from stimulus X/Y.
2. Do not create AW-specific static-image assets.
3. Do not generate additional Wave 1 stimuli before human evidence.
4. Do not treat product continuation as domain trajectory evidence.
5. Do not modify frozen Pair P0/v0.7 flows without explicit instruction.
6. Do not reconstruct live Hostinger source from this document; obtain the actual files first.
7. Never commit Hostinger DB passwords, API keys or live `config.php` secrets.
8. When state conflicts exist, prefer the source-of-truth hierarchy above.
