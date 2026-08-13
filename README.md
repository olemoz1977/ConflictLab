# ConflictLab

**Epistemic Reflection Framework** — eksperimentinė savirefleksijos sistema, skirta stebėti spontaniškas reakcijas į kontroliuojamus vizualinius skirtumus, o ne klasifikuoti žmogų.

> Mes nepadedame žmogui greičiau suprasti save. Mes padedame jam išmokti geriau stebėti save.

---

## Dabartinis etapas — v0.8 Human Wave 1

**Statusas:** `PILOT READY / wave1-v0.2 FROZEN`

Aktyvus tyrimo etapas — šešių stimulus-manipuliacijų šeimų aklas žmogaus reakcijų patikrinimas.

- 6/6 Wave 1 šeimos praėjo vidinę kuraciją (`KEEP for Wave 1`)
- 12/12 galutinių assetų yra repo
- visoms poroms `signal_mapping_status: NONE`
- X/Y pasirinkimas neturi iš anksto priskirtos psichologinės krypties
- AW kaip atskira statinių stimulų ašis yra **SUSPENDED**
- naujų stimulų iki Human Wave 1 duomenų **negeneruojame**
- Hostinger Human Wave 1 v0.2 hardening baigtas
- live mobile + MySQL smoke test: **PASS**

**Human Wave 1 live:** `https://omesg360.eu/wave1/`

Ne-slaptas v0.2 deployment source dabar saugomas `deploy/wave1-hostinger/`. Tikras `config.php`, DB slaptažodžiai ir dalyvių duomenys į repo nekeliami.

---

## Metodologinė riba

```text
SCENE PROPERTY / VISUAL MANIPULATION
        ↓
PARTICIPANT RESPONSE
        ↓
DERIVED SIGNAL — tik po empirinio Gate D
```

**Negalima** iš vaizdo savybės ar A/B pasirinkimo automatiškai išvesti AW/CS/CR signalo.

Dabartiniai aktyvūs stimulus-response kandidatų domenai:

- **CS** — Clarity / Ambiguity
- **CR** — Structure / Flexibility

AW statinių vaizdų programa sustabdyta. Galimas domain-specific response trajectory sluoksnis yra tik hipotezė ir nėra validuotas.

---

## Wave 1 šeimos

### CS
1. `CS-PR-01` — Partial Reveal
2. `CS-RE-01` — Relation Evidence
3. `CS-CA-01` — Context / Reference Availability

### CR
4. `CR-PZ-01` — Predefined Zones
5. `CR-FS-01` — Fixed Slots vs Continuous Capacity
6. `CR-PO-01` — Partitioned vs Open Functional Space

Aktyvus planas: `docs/experiments/stimulus-validation/WAVE1_PLAN.md`

---

## Human Wave 1 v0.2

Vienoje blind sesijoje:

- 6 poros, jų tvarka randomizuojama
- left/right pozicija randomizuojama kiekvienai porai
- pasirinkimas: `left`, `right` arba `no_clear_choice`
- priežasties free text — neprivalomas
- reakcijos stiprumas 1–5 — neprivalomas
- `hard_to_identify` fiksuojamas atskirai nuo `no_clear_choice`
- `presentation_index` = 1–6
- `latency_ms` pradedamas skaičiuoti tik sėkmingai užsikrovus abiem vaizdams
- atsakymas turi sėkmingai išsisaugoti prieš pereinant prie kitos poros

Svarbi raw-state riba:

```text
no_clear_choice != hard_to_identify != empty free text
```

`reaction_intensity` nėra confidence, latency, valence ar signal vector magnitude.

---

## Projekto sluoksniai

| Sluoksnis | Statusas | Paskirtis |
|---|---|---|
| **Human Wave 1** | **PILOT READY / v0.2 FROZEN** | realių dalyvių blind multi-pair sesija |
| **Stimulus Validation Wave 1** | INTERNAL CURATION COMPLETE | 6 šeimos, 12 assetų |
| **prototype-nine-v1 / Pair P0** | FROZEN TECHNICAL/UX REFERENCE | ankstesnio srauto ir radaro techninis etalonas, ne dabartinė metodologinė tiesa |
| **v0.7** | FROZEN BASELINE | metodologinių ir architektūrinių komponentų šaltinis |

Ankstesnis `3 AW + 3 CS + 3 CR` ir „18 porų minimumo“ modelis **nėra dabartinis v0.8 metodologinis reikalavimas**.

---

## Kur pradėti

Naujas žmogus ar AI turėtų skaityti tokia tvarka:

1. `PROJECT_STATE.md` — dabartinė projekto būsena
2. `docs/experiments/stimulus-validation/WAVE1_PLAN.md` — aktyvus Human Wave 1 protokolas
3. `docs/adr/ADR-011-stimulus-signal-separation.md` — stimulus ≠ response ≠ signal riba
4. `docs/experiments/pair-p0/METHODOLOGY_DELTA_2026-08-10.md` — V1.3 naujesni sprendimai
5. `docs/experiments/pair-p0/AW_TRAJECTORY_HYPOTHESIS_2026-08-10.md` — AW suspension
6. `deploy/wave1-hostinger/README.md` — v0.2 deployment freeze
7. `REPOSITORY_INVENTORY.md` — failų statusai ir istorinis sluoksnis

---

## Repo struktūra

```text
ConflictLab/
├── PROJECT_STATE.md
├── README.md
├── REPOSITORY_INVENTORY.md
├── WHY_CONFLICTLAB.md              ← istorinis / teorinis rationale; ne vienintelis v0.8 truth source
├── deploy/
│   └── wave1-hostinger/            ← v0.2 non-secret deployment mirror
│       ├── index.html
│       ├── api.php
│       ├── config.example.php
│       ├── migrate_wave1.sql
│       └── README.md
├── docs/
│   ├── index.html                  ← v0.7 frozen baseline
│   ├── methodology/                ← v0.7 frozen methodology
│   ├── adr/
│   └── experiments/
│       ├── pair-p0/                ← current decisions + frozen prototype references
│       └── stimulus-validation/     ← ACTIVE Wave 1 research files + assets
├── src/                            ← v0.7 frozen engine
├── stimuli/                        ← v0.7 frozen stimulus library
├── tests/
└── archive/                        ← istorinis / nebenaudojamas turinys
```

---

## Ko ConflictLab nėra

- psichologinis testas
- diagnostika
- asmenybės tipologija
- elgesio prognozavimo sistema
- automatinis žmogaus „scoringas“ pagal vieną pasirinkimą

**ConflictLab — stebėjimas, ne nuosprendis.**
