 # ConflictLab

**Epistemic Reflection Framework** — savirefleksijos platforma, padedanti žmonėms geriau stebėti savo spontaniškas reakcijų dėsningumus.

> *Mes nepadedame žmogui greičiau suprasti save. Mes padedame jam išmokti geriau stebėti save.*

**Versija:** v0.7-beta (Feature Freeze)
**Gyvas produktas:** https://olemoz1977.github.io/ConflictLab/

---

## Kas tai yra

ConflictLab **nėra**:
- psichologinis testas
- asmenybės diagnostika
- elgesio prognozavimo sistema

ConflictLab **yra**:
- episteminis refleksijos įrankis
- stimulais grįstas dėmesio krypties stebėjimas
- hipotezėmis pagrįstas savirefleksijos tyrimas

---

## Kaip veikia

```
Stimulai (vaizdai)
    ↓ pirma spontaniška reakcija
Signal Engine (aw/cs/cr ašys)
    ↓ semantic observations
Observation Engine
    ↓ structured facts
Claude API (Reflection Engine)
    ↓ žmogaus kalba pagal R1-R8
Reflection + Dialogue State Machine
    ↓
Žmogus sprendžia ar rezonuoja
```

**Sesija:** 4 stimulai → Reflection → DSM dialogas (S0→Mirror→Bridge)

**Po 3 sesijų:** Pattern ekranas su pasikartojančių dėsningumų analize

---

## Repozitorijos struktūra

```
ConflictLab/
├── docs/
│   ├── index.html              ← produktas (GitHub Pages)
│   ├── media/                  ← stimulų vaizdai
│   ├── methodology/            ← užšaldyta metodologija (v1.0)
│   │   ├── METHODOLOGY_FREEZE_v1.md    ← pradėk čia
│   │   ├── stimulus_cue_rules_v1.md    ← F1-F7 standartai
│   │   ├── reflection_language_standard_v1.md  ← R1-R8
│   │   ├── reflection_safety_principles_v1.md  ← S1-S5
│   │   ├── micro_dialogue_dsm_v1.md    ← DSM specifikacija
│   │   └── ...
│   ├── adr/                    ← architektūros sprendimai
│   └── beta_research_protocol_v1.md   ← H1-H4, SC1-SC5
├── stimuli/                    ← stimulų biblioteka (ST-001÷ST-010)
│   └── _templates/             ← šablonai naujiems stimulams
├── src/engine/behavior_translation/   ← Python engine (validuotas)
├── tests/                      ← 13/13 testai
└── archive/v0.7-freeze/        ← istorija (nieko netrinant)
```

---

## Pradėti nuo

1. **Metodologija:** `docs/methodology/METHODOLOGY_FREEZE_v1.md`
2. **Produktas:** https://olemoz1977.github.io/ConflictLab/
3. **Beta tyrimas:** `docs/beta_research_protocol_v1.md`
4. **Stimulų kūrimas:** `docs/methodology/stimulus_cue_rules_v1.md`

---

## Metodologijos standartai

| Dokumentas | Aprašas |
|---|---|
| Stimulus Language Standard (F1-F7) | Kaip kurti attention cues |
| Reflection Language Standard (R1-R8) | Kaip sistema kalba po sesijos |
| Reflection Safety Principles (S1-S5) | Ko sistema niekada nedaro |
| Micro-Dialogue DSM | State Machine specifikacija |
| Stimulus Lifecycle | 9 etapų gamybos procesas |
| Beta Research Protocol | H1-H4 hipotezės, SC1-SC5 sėkmės kriterijai |

**Methodology Freeze:** pakeitimai priimami tik kai beta duomenys rodo SC1-SC5 netenkinimą.

---

## Beta testas

**Tikslas:** 10-15 žmonių, ≥3 sesijos kiekvienas.

**Klausimai:** Ar žmonės sako *"to nebuvau pastebėjęs"*? (SC3)

**Debug duomenys:** `localStorage['cl_debug_log']` — paskutinės 50 sesijų

---

*ConflictLab — nebe Architecture. Evidence.*

---

## Du atskiri ConflictLab frontas

> **Svarbu naujam AI:** šiame repo yra du visiškai atskiri darbų frontas. Jie dalinasi repozitorija, bet ne architektūra, metodologija ar gamybos statusu.

### 1. Main produktas — v0.7 (Feature Freeze / Beta Ready)

- Gyvas: `https://olemoz1977.github.io/ConflictLab/`
- Observation Engine + Claude API refleksijų sluoksnis
- ST-001–ST-010 stimulų biblioteka (10 aktyvių stimulų)
- Methodology Freeze v1.0 — pakeitimai priimami tik esant beta duomenų įrodymams
- **Dabartinis statusas:** feature freeze, laukiama beta dalyvių
- **Blokeris:** generator.html CORS problema (neišspręsta)
- **Beta protokolas:** `docs/beta_research_protocol_v1.md`

### 2. Pair P0 eksperimentas — izoliuotas metodinis tyrimas

Katalogas: `docs/experiments/pair-p0/`

- **Kas tai:** izoliuotas eksperimentas su vaizdų poromis ir trijų cue rinkiniais
- **Naudoja LLM:** ne — refleksija remiasi pasirinktu cue ir žmogaus tekstu, ne AI interpretacija
- **Techninis srautas:** M0 remote beta stabilizuotas; stable tag: `pair-p0-m0-remote-beta-stable`
- **Realus telefono QA:** 6/6 scenarijai praėjo (Edge mobile)
- **Dabartinis frontas:** N0 stimulus ir cue metodinis auditas
- **Tikslas:** 9 porų biblioteka (3 sesijos × 3 poros)
- **N1 scheduler:** dar nepradėtas — laukia bibliotekos patvirtinimo

**N0 kandidatų dabartiniai statusai:**

| Kandidatas | Statusas |
|---|---|
| N0-004-C1 Miško takas | ADVANCE — endpoint refinement needed |
| N0-005-C1 Augalo stadijos | CONCEPT UNDER REVIEW — inherent valence asymmetry unresolved |
| N0-006-C1 Akmens tekstūra | ADVANCE TO PROTOTYPE |
| N0-006-C2 Audinio tekstūra | RESERVE |
| N0-007-C1 Objekto orientacija | HOLD — concept not operationally clean |
| N0-008-C1 Debesuota/saulės šviesa | ADVANCE, AXIS UNRESOLVED — do not produce yet |
| N0-009-C1 Socialinis atstumas | EXPERIMENTAL HOLD |

**Metodologinis atskyrimas:**
- Branduolinė metodologija (Methodology Freeze v1.0): užšaldyta
- Stimulus ir cue operacionalizacija (Pair P0): dar neparuošta išoriniam beta testui
- Pair P0 techninis srautas: stabilus
