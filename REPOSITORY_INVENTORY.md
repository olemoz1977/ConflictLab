# ConflictLab — Repository Inventory

**Date:** 2026-08-13  
**Scope:** current `main` state + Human Wave 1 v0.2 deployment freeze  
**Purpose:** prevent current, frozen and historical artifacts from being mixed into one methodology.

## Classification

- **CURRENT** — current operational/methodological truth
- **ACTIVE-EXPERIMENT** — being tested now; not validated truth
- **FROZEN-REFERENCE** — technically useful, must not be silently rewritten
- **HISTORICAL-PROTOTYPE** — records earlier design/logic; not current v0.8 truth
- **SUPPORTING** — useful evidence, audit or tooling
- **ARCHIVE** — intentionally removed from active paths
- **EXTERNAL-LIVE** — deployed outside GitHub
- **DEPLOYMENT-MIRROR** — non-secret source artifact corresponding to the current deployed baseline

---

## 1. ROOT

| Path | Class | Purpose / note |
|---|---|---|
| `PROJECT_STATE.md` | **CURRENT** | read first; current milestone, methodology boundary, deployment status |
| `README.md` | **CURRENT** | public project overview aligned to v0.8 Human Wave 1 |
| `REPOSITORY_INVENTORY.md` | **CURRENT** | this status map |
| `WHY_CONFLICTLAB.md` | HISTORICAL-PROTOTYPE / SUPPORTING | valuable rationale, but several v0.7-era claims are not current v0.8 truth |
| `.gitignore` | CURRENT | local/tooling ignores; deployment secrets must remain untracked |
| `archive/` | ARCHIVE | historical project material |
| `docs/` | MIXED | frozen baseline + active experiments + methodology |
| `src/` | FROZEN-REFERENCE | v0.7 Python engine |
| `stimuli/` | FROZEN-REFERENCE | v0.7 provisional stimulus library |
| `tests/` | SUPPORTING | engine/prototype tests |

Top-level `validation/` was v0.4-era stale material and was moved to `archive/v0.4-validation/` in the 2026-08-13 housekeeping pass.

---

## 2. CURRENT HUMAN WAVE 1 / STIMULUS VALIDATION

Directory: `docs/experiments/stimulus-validation/`

| Path | Class | Status |
|---|---|---|
| `WAVE1_PLAN.md` | **CURRENT** | six-family blind human validation protocol |
| `SESSION_CHECKPOINT_2026-08-12.md` | CURRENT / CHECKPOINT | 6/6 KEEP, 12 assets, X/Y conventions |
| `assets/` | **CURRENT** | frozen Wave 1 binary assets; do not regenerate before evidence |
| `pair-review.html` | SUPPORTING | internal Pair Candidate Review tool; curation complete |
| `CS_RE_01_ASSET_BRIEF.md` | HISTORICAL-PROTOTYPE / SUPPORTING | production brief for a completed pair; not a next action |
| `LEGACY_PAIR_SALVAGE_AUDIT_2026-08-12.md` | SUPPORTING | audit evidence, not current stimulus plan |

### Frozen Wave 1 asset set

```text
CS-PR-01/more-reveal.webp + less-reveal.jpg
CS-RE-01/more-evidence.png + less-evidence.png
CS-CA-01/more-reference.png + less-reference.png
CR-PZ-01/no-predefined-zones.png + predefined-zones.png
CR-FS-01/fixed-slots.png + continuous-capacity.png
CR-PO-01/partitioned-space.png + open-space.png
```

All: `signal_mapping_status: NONE`.

---

## 3. CURRENT METHODOLOGICAL DECISIONS

| Path | Class | Note |
|---|---|---|
| `docs/adr/ADR-011-stimulus-signal-separation.md` | **CURRENT** | absolute boundary: scene property ≠ response ≠ signal |
| `docs/experiments/pair-p0/METHODOLOGY_DELTA_2026-08-10.md` | **CURRENT** | newer than V1.3 where they conflict |
| `docs/experiments/pair-p0/AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md` | **CURRENT** | AW static-stimulus program suspended |
| `docs/experiments/pair-p0/STIMULUS_OPERATIONALIZATION_SPEC_V1.3.md` | CURRENT CANDIDATE SPEC | use subject to ADR-011 + methodology delta |
| `docs/experiments/pair-p0/STIMULUS_EXPERIENCE_CARD_V1.md` | CURRENT / SUPPORTING | CONTROL + EXPERIENCE + INTERPRETABILITY working unit |

---

## 4. HUMAN WAVE 1 DEPLOYMENT — v0.2 FROZEN

| Location | Class | Note |
|---|---|---|
| `https://omesg360.eu/wave1/` | **EXTERNAL-LIVE** | Hostinger Human Wave 1 platform; live smoke test PASS |
| `deploy/wave1-hostinger/README.md` | **CURRENT** | v0.2 deployment record, verification and freeze rules |
| `deploy/wave1-hostinger/index.html` | **DEPLOYMENT-MIRROR** | participant UI, protocol `wave1-v0.2` |
| `deploy/wave1-hostinger/api.php` | **DEPLOYMENT-MIRROR** | hardened response API, explicitly writes `wave1-v0.2` |
| `deploy/wave1-hostinger/migrate_wave1.sql` | **DEPLOYMENT-MIRROR / SUPPORTING** | applied pre-freeze DB migration |
| `deploy/wave1-hostinger/config.example.php` | **DEPLOYMENT-MIRROR** | non-secret config template only |
| live Hostinger `config.php` | **EXTERNAL-LIVE / SECRET** | never commit |

The committed v0.2 artifacts were supplied for deployment and then verified through the live mobile flow and MySQL row inspection. No independent byte-for-byte download-back comparison from Hostinger has been performed.

Current raw capture includes:

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

Important distinctions:

```text
no_clear_choice != hard_to_identify != empty free text
```

Current DB duplicate protection: `UNIQUE (participant_id, candidate_id)`.

`setup.php` and public `check.php` are not part of the live pilot baseline.

Live mobile smoke test verified one session as six rows under one participant, `presentation_index` 1–6, `protocol_version = wave1-v0.2`, persisted left/right presentation, choice paths, optional reason, optional intensity, independent `hard_to_identify`, and populated latency.

Status: **PILOT READY / v0.2 FROZEN**.

---

## 5. PAIR P0 / prototype-nine-v1

### Keep at existing paths — FROZEN technical/UX reference

| Path | Class |
|---|---|
| `docs/experiments/pair-p0/index.html` | FROZEN-REFERENCE |
| `pair-set-prototype-nine-v1.json` | FROZEN-REFERENCE |
| `pair-cue-prototype-nine-v1.json` | HISTORICAL-PROTOTYPE / FROZEN-REFERENCE |
| `lang.json` | FROZEN-REFERENCE |
| `images/` | FROZEN-REFERENCE |
| `audio/` | FROZEN-REFERENCE |
| `RADAR_BLOCK_MODEL_V1.md` | FROZEN-REFERENCE |
| `PAIR_P0_STATE.md` | HISTORICAL-PROTOTYPE / milestone history |
| `PROGRESS.md` | HISTORICAL-PROTOTYPE / chronology |
| `FIRST_RADAR_EXPECTATION_PAYOFF_V1.md` | FROZEN-REFERENCE / UX history |

Stable tag: `pair-p0-prototype-nine-v1-radar-ux-stable`.

Do not move or rewrite these solely to make them look like current v0.8 methodology. Their value is historical/technical traceability.

### Superseded / historical Pair P0 research records — leave in place for traceability

- `AW_REDEFINITION_NOTE_v0.1.md`
- `AW_EPISTEMIC_CANDIDATES_v0.1.md`
- `EXTERNAL_AI_HANDOFF_2026-08-10.md`
- `N0_*` design/cue/review documents
- `pair-set-n0-six-v3.json`
- `pair-cue-n0-six-v3.json`
- legacy M0 pair/cue files

Class: **HISTORICAL-PROTOTYPE** unless a newer current document explicitly says otherwise.

---

## 6. v0.7 FROZEN BASELINE

Keep as reference; do not actively develop unless explicitly reopened.

| Path | Class |
|---|---|
| `docs/index.html` | FROZEN-REFERENCE |
| `docs/methodology/` | FROZEN-REFERENCE |
| `docs/media/` | FROZEN-REFERENCE |
| `docs/architecture/` | FROZEN-REFERENCE / historical ADRs |
| `src/engine/behavior_translation/` | FROZEN-REFERENCE |
| `stimuli/ST-001–010/` | FROZEN-REFERENCE |
| `tests/test_behavior_translation.py` | SUPPORTING |
| `docs/beta_research_protocol_v1.md` | HISTORICAL-PROTOTYPE / v0.7 research protocol |
| `docs/product_experience_audit_v1.md` | SUPPORTING / historical UX audit |

`docs/index.html` still contains the old direct-browser Claude API architecture; this is not the Human Wave 1 deployment.

---

## 7. HISTORICAL TEST PACKS LEFT IN PLACE

These files are intentionally **not physically moved** because they are referenced by milestone history/tags and moving them would reduce traceability without practical benefit.

| Path | Class |
|---|---|
| `docs/beta-test/` | HISTORICAL-PROTOTYPE — Pair P0 5-person / 3-session usability pack |
| `docs/tester_instructions.md` | HISTORICAL-PROTOTYPE — v0.6 tester instructions |
| `docs/RELEASE_NOTES_v0.6.0-beta.md` | HISTORICAL-PROTOTYPE |

Do not use these as Human Wave 1 participant instructions.

---

## 8. ARCHIVED IN 2026-08-13 HOUSEKEEPING

Moved without changing content:

```text
validation/README.md
validation/disagreement_log.md
validation/feedback_template.md
validation/feedback/.gitkeep
    → archive/v0.4-validation/

docs/review.html
    → archive/legacy-tools/review-single-image.html

docs/generator.html
    → archive/legacy-tools/generator.html
```

Rationale:

- top-level `validation/` was explicitly v0.4-era stale material
- `docs/review.html` is an obsolete single-image review precursor, superseded by `docs/experiments/stimulus-validation/pair-review.html`
- `docs/generator.html` is a legacy generator with the documented CORS problem and is not part of current Wave 1 production

Historical Git tags/commits preserve their original locations.

---

## 9. ARCHIVE

| Path | Contents |
|---|---|
| `archive/v1/` | earliest text-analysis architecture |
| `archive/v0.7-freeze/` | old engines, theory material, v0.4/v0.7-era files |
| `archive/v0.4-validation/` | former stale root validation package |
| `archive/legacy-tools/` | obsolete browser tools removed from active `docs/` paths |
| `archive/README.md` | archive interpretation rules |

---

## 10. CURRENT SOURCE-CONTROL RULES

1. Current truth must be explicit; old files are not made current merely because they remain in `main`.
2. Freeze technically useful historical paths when moving them could break milestone traceability.
3. Archive only confirmed obsolete artifacts with no active dependency.
4. Never commit Hostinger passwords, API keys, live DB credentials, live `config.php`, or participant data.
5. `deploy/wave1-hostinger/` is the non-secret v0.2 deployment mirror; asset binaries remain canonical under `docs/experiments/stimulus-validation/assets/`.
6. Human Wave 1 data itself must not be committed into this public repository.
7. Treat `wave1-v0.2` as frozen once real pilot collection begins. Participant-facing or capture-semantics changes require a new protocol version and documented delta.
8. Before a methodology change, update `PROJECT_STATE.md` and the relevant canonical spec/checkpoint rather than accumulating contradictory notes.

---

## 11. GIT TAGS — IMPORTANT REFERENCES

| Tag | Meaning |
|---|---|
| `pair-p0-m0-remote-beta-stable` | M0 remote beta reference |
| `pair-p0-prototype-nine-v1-flow-stable` | Pair P0 3×3 flow reference |
| `pair-p0-prototype-nine-v1-radar-ux-stable` | frozen P9 radar/UX reference |
| `external-review-pack-v1` | historical external review pack |
| `pair-p0-beta-test-pack-v1` | historical Pair P0 beta-test documentation pack |
