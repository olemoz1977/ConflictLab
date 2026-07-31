# ConflictLab — Repository Inventory
**Data:** 2026-07-31 | **Versija:** v0.7 Feature Freeze

---

## ✅ ACTIVE — naudojama, nekeisti

### Pagrindinis produktas
- `docs/index.html` — ConflictLab UI (GitHub Pages)
- `docs/media/` — aktyvūs stimulų vaizdai (10 PNG + video)

### Metodologija (užšaldyta)
- `docs/methodology/METHODOLOGY_FREEZE_v1.md`
- `docs/methodology/stimulus_validation_protocol.md`
- `docs/methodology/stimulus_matrix_v1.md`
- `docs/methodology/stimulus_cue_rules_v1.md` (Stimulus Language Standard)
- `docs/methodology/stimulus_lifecycle_v1.md`
- `docs/methodology/conflictlab_voice_v1.md`
- `docs/methodology/reflection_language_standard_v1.md`
- `docs/methodology/reflection_safety_principles_v1.md`
- `docs/methodology/micro_dialogue_dsm_v1.md`
- `docs/methodology/behavior_translation_architecture_v1.md`
- `docs/methodology/future_considerations.md`
- `docs/beta_research_protocol_v1.md`

### Architektūra
- `docs/adr/ADR-010-observation-engine.md`
- `docs/architecture/adr/ADR-009-behavior-translation-engine.md`

### Python Engine (validuotas)
- `src/engine/behavior_translation/` — P1-P9, AHA, Reflection Engine
- `tests/test_behavior_translation.py` — 13/13 testai

### Stimulų biblioteka
- `stimuli/ST-001` ÷ `ST-010` — 10 stimulų su review/status/yaml
- `stimuli/_templates/` — šablonai naujiems stimulams

### Beta testas
- `docs/tester_instructions.md`
- `docs/product_experience_audit_v1.md`

---

## 🟡 LEGACY — nuoroda, bet nebeatnaujinama

- `docs/methodology/stimulus_cue_redesign_v1.md` — supresidenta `stimulus_cue_rules_v1.md`
- `docs/methodology/aha_engine.md` — tuščias, supresidenta `src/engine/behavior_translation/`
- `docs/methodology/behavior_translation_engine.md` — tuščias, supresidenta architektūros doc
- `docs/methodology/reflection_engine_validation_v1.md` — istorinis validacijos protokolas
- `docs/RELEASE_NOTES_v0.6.0-beta.md` — senesnis release
- `docs/architecture_blueprint_v1.md` — senesnė architektūra
- `docs/architecture_decisions.md` — supresidenta ADR dokumentais
- `docs/manifesto.md` — supresidenta Philosophy Statement (METHODOLOGY_FREEZE)
- `docs/principles.md` — supresidenta methodology dokumentais
- `docs/philosophy.md` — supresidenta
- `docs/roadmap.md` — pasenęs
- `docs/ui/` — tuščias katalogas
- `mirror/reflection_contract.md` — supresidenta `reflection_language_standard_v1.md`
- `adaptive/stimulus_selector.md` — koncepcija, dar neimplementuota

---

## 📦 ARCHIVE — perkelti į archive/

### Šakniniame kataloge (neturėtų būti)
- `ax_approach.png`, `ax_release.png`, `ax_uncertainty.png`
- `p1_phone_table.png`, `p2_window_silhouette.png`, `p3_chat_screen.png`
- `p4_empty_table.png`, `p5_person_laptop.png`
- `v2_p1_empty_room.png`, `v2_p2_corridor.png`, `v2_p3_notebook.png`, `v2_p4_person_alone.png`
*(duplikatai — originalai yra `docs/media/`)*

- `RELEASE_NOTES_v0.4.md`, `VERSION_v0.4_RC1.txt` — seni
- `stimulus_review_package_v1.md` — supresidenta stimuli/ katalogo

### Senesni katalogai (visas turinys → archive)
- `core/` — human_model, interpretation_filter, reaction_pattern, transformation_path
- `engine/` — analysis_pipeline, confidence_score, evidence_mapper, hypothesis_generator...
- `examples/` — conflict_with_colleague, criticism_at_work...
- `frameworks/` — model_transparency
- `hypotheses/` — H001-H004
- `ideas/backlog.md`
- `model/` — belief_engine.py, contradiction_rules...
- `perception/` — feature_extraction
- `research/` — bibliography, experiments, research_questions
- `theories/` — 15 teorijų dokumentų
- `user_state/` — privacy_architecture
- `validation/scenarios/` — V001-V003 (seni scenarijai)
- `integration_test.py`
- `{docs,mirror,frameworks,...}` — klaidingi katalogai (sukurti per bash klaidą)

### `src/` katalogas (Python moduliai neintegruoti į UI)
- `src/core/` — event_log, evidence_graph, signal_orientation
- `src/frameworks/` — model_registry
- `src/mirror/` — reflection_contract
- `src/engine/uncertainty_engine.py`
*(Aktyvus tik `src/engine/behavior_translation/` — likusi dalis archyvuotina)*

---

## ❌ DELETE — duplikatai arba klaidingi failai

- `./{docs,mirror,frameworks,validation` — neteisingi katalogai (bash klaida)
- `./{docs,mirror,frameworks,validation/scenarios,src` — tas pats
- `./{docs,mirror,frameworks,validation/scenarios,src/{core,engine,frameworks,mirror}}` — tas pats
- `docs/index_v04_backup.html` — senas backup

---

## Siūloma galutinė struktūra (po cleanup)

```
ConflictLab/
├── README.md                    # atnaujintas
├── docs/
│   ├── index.html               # produktas
│   ├── media/                   # stimulų vaizdai
│   ├── methodology/             # užšaldyta metodologija
│   ├── adr/                     # architektūros sprendimai
│   ├── beta_research_protocol_v1.md
│   ├── tester_instructions.md
│   └── product_experience_audit_v1.md
├── stimuli/                     # stimulų biblioteka
│   ├── ST-001/ ÷ ST-010/
│   └── _templates/
├── src/
│   └── engine/
│       └── behavior_translation/  # aktyvus Python engine
├── tests/
│   └── test_behavior_translation.py
└── archive/                     # viskas kita
    ├── v0.4/
    ├── theories/
    ├── research/
    └── ...
```
