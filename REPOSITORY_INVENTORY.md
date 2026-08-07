# ConflictLab — Repository Inventory

**Data:** 2026-08-08
**Pagrindas:** pilnas repo auditas 2026-08-08
**Versija:** v0.7 (frozen) + Pair P0 (active)

Kategorijos: **ACTIVE** / **FROZEN** / **EXPERIMENTAL** / **SUPPORTING** / **LEGACY** / **ARCHIVE** / **STALE**

---

## ACTIVE — Pair P0 aktyvus darbas

| Failas | Paskirtis |
|---|---|
| `docs/experiments/pair-p0/index.html` | Pagrindinis Pair P0 produktas (4500+ eilučių) |
| `docs/experiments/pair-p0/pair-set-prototype-nine-v1.json` | Aktyvus 9 porų rinkinys |
| `docs/experiments/pair-p0/pair-cue-prototype-nine-v1.json` | Aktyvus 9 porų cue rinkinys |
| `docs/experiments/pair-p0/lang.json` | LT/EN vertimų failas |
| `docs/experiments/pair-p0/images/` | P0/N0 vaizdai (p0-001–003, n0-004–009) |
| `docs/experiments/pair-p0/audio/open-window.mp3` | UI garsas |
| `docs/experiments/pair-p0/PAIR_P0_STATE.md` | P0 tiesos šaltinis ir OQ žurnalas |
| `docs/experiments/pair-p0/RADAR_BLOCK_MODEL_V1.md` | Architektūros specifikacija |
| `docs/experiments/pair-p0/PROGRESS.md` | Chronologinis žurnalas |
| `tests/pair_p0_attainable_envelope.py` | Attainable envelope audito skriptas |
| `PROJECT_STATE.md` | Dabartinės būsenos dokumentas |
| `REPOSITORY_INVENTORY.md` | Šis failas |

---

## FROZEN BASELINE — v0.7 (nekeisti, naudoti kaip šaltinį)

| Failas/Katalogas | Paskirtis |
|---|---|
| `docs/index.html` | v0.7 pagrindinis UI (1335 eilučių, tiesioginiai Claude API kvietimai) |
| `docs/methodology/METHODOLOGY_FREEZE_v1.md` | Metodikos užšaldymo dokumentas |
| `docs/methodology/conflictlab_voice_v1.md` | Kaip sistema kalba |
| `docs/methodology/behavior_translation_architecture_v1.md` | Reflection Engine architektūra |
| `docs/methodology/stimulus_validation_protocol.md` | Stimulus vertinimo protokolas |
| `docs/methodology/stimulus_matrix_v1.md` | Bibliotekos planavimas |
| `docs/methodology/stimulus_cue_rules_v1.md` | F1–F7 cue kūrimo taisyklės |
| `docs/methodology/stimulus_lifecycle_v1.md` | Gamybos procesas |
| `docs/methodology/micro_dialogue_dsm_v1.md` | DSM specifikacija |
| `docs/methodology/reflection_language_standard_v1.md` | R1–R8 refleksijos standartai |
| `docs/methodology/reflection_safety_principles_v1.md` | S1–S5 saugos principai |
| `docs/adr/ADR-010-observation-engine.md` | Observation Engine sprendimas |
| `docs/architecture/adr/ADR-009-behavior-translation-engine.md` | Behavior Translation Engine |
| `docs/beta_research_protocol_v1.md` | H1–H4 tyrimo hipotezės |
| `docs/media/` | v0.7 stimulų vaizdai ir vaizdo įrašai |
| `src/engine/behavior_translation/` | Python engine (P1–P9, AHA, Reflection) |
| `stimuli/ST-001–010/` | v0.7 stimulų biblioteka (PROVISIONAL vektoriai) |
| `WHY_CONFLICTLAB.md` | Filosofija |
| `README.md` | Viešas pristatymas |

---

## EXPERIMENTAL — eksperimentiniai rinkiniai

| Failas | Paskirtis | Pastaba |
|---|---|---|
| `docs/experiments/pair-p0/pair-set-n0-six-v3.json` | 6 porų n0-six-v3 rinkinys | Neaktyvus šiuo metu |
| `docs/experiments/pair-p0/pair-cue-n0-six-v3.json` | n0-six-v3 cue rinkinys | Neaktyvus |

---

## SUPPORTING — infrastruktūra ir protokolai

| Failas | Paskirtis |
|---|---|
| `tests/test_behavior_translation.py` | v0.7 Python engine testai (13/13) |
| `docs/beta-test/` | Beta testavimo protokolai |
| `docs/external-review/` | Išorinio peržiūros paketas |
| `docs/tester_instructions.md` | Testerių instrukcijos |
| `docs/product_experience_audit_v1.md` | Produkto patirties auditas |
| `stimuli/_templates/` | Šablonai naujiems stimulams |

---

## LEGACY — senos versijos, dar saugomos

| Failas | Paskirtis | Pastaba |
|---|---|---|
| `docs/experiments/pair-p0/pair-set.json` | M0 numatytasis rinkinys (3 poros) | Naudojamas M0 legacy kelyje |
| `docs/experiments/pair-p0/pair-cue-v0.1.json` | M0 senasis cue rinkinys | Naudojamas M0 legacy kelyje |
| `docs/experiments/pair-p0/archive/index_v1_before_rewrite.html` | Sena P0 versija prieš perašymą | Istorinė nuoroda |
| `docs/generator.html` | Stimulus generatorius | CORS problema, rankinis naudojimas |
| `docs/RELEASE_NOTES_v0.6.0-beta.md` | v0.6 release notes | |
| `docs/methodology/stimulus_cue_redesign_v1.md` | Supresidenta `stimulus_cue_rules_v1.md` | |
| `docs/methodology/aha_engine.md` | Tuščias, supresidenta `src/` | |
| `docs/methodology/behavior_translation_engine.md` | Tuščias, supresidenta ADR | |
| `docs/methodology/reflection_engine_validation_v1.md` | Istorinis validacijos protokolas | |
| `docs/methodology/future_considerations.md` | Senesni planavimai | |

---

## ARCHIVE — istorinis turinys

| Katalogas | Turinys |
|---|---|
| `archive/v0.7-freeze/` | Užšaldytas v0.7 archyvas: senas engine, teorijos, hipotezės, pavyzdžiai |
| `archive/v0.7-freeze/theories/` | 16 teorinių pagrindų dokumentų |
| `archive/v0.7-freeze/misc/src-core/` | v0.4 Python moduliai (SignalOrientation, EvidenceGraph, EventLog ir kt.) |
| `archive/v0.7-freeze/old-engine/` | Senas analizės pipeline |
| `archive/v1/` | Labai sena v1 architektūra |

---

## STALE / MISLEADING — pasenę, gali klaidinti

| Failas | Problema |
|---|---|
| `validation/README.md` | „ConflictLab v0.4 — Validation Phase" — visiškai nebeaktuali era |
| `validation/disagreement_log.md` | v0.4 era, tuščias |
| `docs/review.html` | Nežinoma paskirtis, nėra konteksto |

---

## Pair P0 dokumentų grupė

| Failas | Paskirtis | Statusas |
|---|---|---|
| `PAIR_P0_STATE.md` | Pagrindinis būsenos dokumentas | ✅ Atnaujintas |
| `RADAR_BLOCK_MODEL_V1.md` | Architektūros specifikacija | ✅ Atnaujintas |
| `PROGRESS.md` | Chronologinis žurnalas | ✅ Atnaujintas |
| `FIRST_RADAR_EXPECTATION_PAYOFF_V1.md` | Expectation/payoff UX spec | Istorinis, galioja |
| `N0_STIMULUS_CUE_BALANCE_AUDIT.md` | 3 esamų porų auditas | Galioja |
| `N0_DECISIONS.md` | Metodiniai sprendimai | Galioja |
| `N0_PAIR_DESIGN_SPEC.md` | 6 naujų porų projektavimo reikalavimai | Galioja |
| `N0_MANUAL_CUE_AUDIT_PROTOCOL.md` | Rankinio audito protokolas | Galioja |
| `N0_PAIR_CONCEPT_CANDIDATES.md` | 14 kandidatų su vertinimu | Galioja |
| `N0_INDEPENDENT_CONCEPT_REVIEW.md` | Triviečiai sprendimai | Galioja |
| `N0_CONCEPT_REFINEMENT.md` | Gamybos specifikacijos | Galioja |
| `N0_PRODUCTION_PROMPTS.md` | Gamybos promptai | Galioja |
| `N0_SIX_PAIR_CUE_DRAFT.md` | Senas draftas | LEGACY (superseded by _v3) |
| `N0_SIX_PAIR_CUE_DRAFT_v2.md` | Senas draftas | LEGACY (superseded by _v3) |
| `N0_SIX_PAIR_CUE_DRAFT_v3.md` | Galutinė versija | Galioja |

---

## Git Tags

| Tag | Reikšmė |
|---|---|
| `pair-p0-m0-remote-beta-stable` | M0 remote beta |
| `pair-p0-prototype-nine-v1-flow-stable` | 3×3 flow, provenance, radar unlocked |
| `pair-p0-prototype-nine-v1-radar-ux-stable` | Bipolar map, calibration v1, routing fix |
| `external-review-pack-v1` | Išorinio review paketas |
| `pair-p0-beta-test-pack-v1` | Beta test paketas |
| `pair-p0-flow-stable`, `pair-p0-h/i/j0-stable` | Ankstesni M0 etapai |
