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
