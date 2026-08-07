# ConflictLab

**Epistemic Reflection Framework** — savirefleksijos platforma, padedanti žmonėms geriau stebėti savo spontaniškas reakcijų dėsningumus.

> *Mes nepadedame žmogui greičiau suprasti save. Mes padedame jam išmokti geriau stebėti save.*

---

## Kas tai yra

ConflictLab **nėra**:
- psichologinis testas
- asmenybės diagnostika
- elgesio prognozavimo sistema

ConflictLab **yra**:
- episteminis refleksijos įrankis
- stimulais grįstas dėmesio krypties stebėjimas
- reakcijų ir pasirinkimų pėdsako fiksavimas

---

## Dabartinė projekto kryptis

| | |
|---|---|
| **v0.7** | Frozen product baseline. Nekeičiama. Šaltinis metodologiniams komponentams. |
| **Pair P0** | Aktyvus v0.8 architektūros kandidatas. Čia vyksta pagrindinis darbas. |
| **prototype-nine-v1** | Techninis/UX stable reference. Ne metodologiškai galutinis stimulus rinkinys. |

**Dabartinis darbas:** naujo stimulus/cue rinkinio kūrimas. Oficialiam švariam kelių blokų palyginimui reikės **18 unikalių metodologiškai priimtinų porų** (9 pirmam blokui, 9 antram).

---

## Pair P0 — aktyvus eksperimentas

**Live:** `https://olemoz1977.github.io/ConflictLab/experiments/pair-p0/?set=prototype-nine-v1`

Katalogas: `docs/experiments/pair-p0/`

**Kas tai:** izoliuotas eksperimentas su vaizdų poromis. Dalyvis mato du vaizdus, pasirenka vieną ir nurodo savo reakciją — tai ir yra visas signalas. Nėra AI generuojamų refleksijų.

**Patvirtinta (2026-08-08):**
- 3 sesijų blokai × 3 poros = 9 pasirinkimų radaras
- Radaras tik po pilno 3 sesijų bloko (sesijos 3, 6, 9...)
- Block 1 vs Block 2 overlay palyginimas
- Pilnas provenance eksportas
- LT + EN palaikymas
- Stable tag: `pair-p0-prototype-nine-v1-radar-ux-stable`

**Laukia:**
- 18 unikalių metodologiškai priimtinų porų (šiuo metu yra 9, kartojamos antrame bloke)
- N0-010–018 naujų porų kūrimas

---

## v0.7 — Frozen Baseline

**Live:** `https://olemoz1977.github.io/ConflictLab/`

Katalogas: `docs/index.html`

Observation Engine + Dialogue State Machine + Claude API refleksijų sluoksnis. Nekeičiama. Naudojama kaip metodologinių principų šaltinis.

---

## 3 signalų ašys (abi versijose)

| Ašis | Teigiama pusė | Neigiama pusė |
|---|---|---|
| AW | Artėti (Approach) | Atsitraukti (Step back) |
| CS | Aiškumas (Clarity) | Neapibrėžtumas (Ambiguity) |
| CR | Struktūra (Structure) | Laisvumas (Flexibility) |

Skalė: [-1.0, +1.0]. Kryptiniai, ne vertinamieji.

---

## Repozitorijos struktūra

```
ConflictLab/
├── PROJECT_STATE.md              ← dabartinės būsenos dokumentas (pradėk čia)
├── REPOSITORY_INVENTORY.md      ← pilna failų inventorizacija
├── docs/
│   ├── index.html               ← v0.7 (frozen)
│   ├── methodology/             ← užšaldyta v0.7 metodika
│   └── experiments/
│       └── pair-p0/             ← AKTYVUS DARBAS
│           ├── index.html       ← pagrindinis P0 produktas
│           ├── PAIR_P0_STATE.md ← P0 tiesos šaltinis
│           └── RADAR_BLOCK_MODEL_V1.md
├── stimuli/                     ← v0.7 stimulų biblioteka (frozen)
├── src/engine/                  ← v0.7 Python engine (frozen)
├── tests/                       ← testai
└── archive/                     ← istorinis turinys
```

---

*ConflictLab — stebėjimas, ne vertinimas.*
