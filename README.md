# ConflictLab

**Epistemic Reflection Framework** — eksperimentinė savirefleksijos sistema, skirta stebėti spontaniškas reakcijas į kontroliuojamus vizualinius skirtumus, o ne klasifikuoti žmogų.

> Mes nepadedame žmogui greičiau suprasti save. Mes padedame jam išmokti geriau stebėti save.

---

## Dabartinis etapas — v0.8 Human Wave 1

**Aktyvus tyrimo etapas:** šešių stimulus-manipuliacijų šeimų aklas žmogaus reakcijų patikrinimas.

- 6/6 Wave 1 šeimos praėjo vidinę kuraciją (`KEEP for Wave 1`)
- 12/12 galutinių assetų yra repo
- visoms poroms `signal_mapping_status: NONE`
- X/Y pasirinkimas neturi iš anksto priskirtos psichologinės krypties
- AW kaip atskira statinių stimulų ašis yra **SUSPENDED**
- naujų stimulų iki Human Wave 1 duomenų **negeneruojame**

**Human Wave 1 live:** `https://omesg360.eu/wave1/`

Hostinger diegimas šiuo metu yra pre-pilot stadijoje. Techninis handoff aprašytas `deploy/wave1-hostinger/README.md`. Tikslus live source mirror į repo dar nebaigtas, todėl repo neturi būti laikomas Hostinger PHP kodo byte-for-byte kopija.

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

## Projekto sluoksniai

| Sluoksnis | Statusas | Paskirtis |
|---|---|---|
| **Human Wave 1** | ACTIVE / PRE-PILOT | realių dalyvių blind multi-pair sesija |
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
6. `REPOSITORY_INVENTORY.md` — failų statusai ir istorinis sluoksnis

---

## Repo struktūra

```text
ConflictLab/
├── PROJECT_STATE.md
├── README.md
├── REPOSITORY_INVENTORY.md
├── WHY_CONFLICTLAB.md              ← istorinis / teorinis rationale; ne vienintelis v0.8 truth source
├── deploy/
│   └── wave1-hostinger/            ← deployment handoff; source mirror pending
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
