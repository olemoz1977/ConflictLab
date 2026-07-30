# ConflictLab — Stimulus Library

Kiekvienas stimulas saugomas atskirame aplanke.

## Struktūra

```
stimuli/
├── _templates/          ← Šablonai naujiems stimulams
│   ├── review.md        ← Peržiūros šablonas
│   ├── status.yaml      ← Statuso šablonas
│   └── stimulus.yaml    ← Duomenų šablonas
├── ST-001/              ← Stimulas (pilnas pavyzdys)
│   ├── image.png        ← Nuotrauka
│   ├── stimulus.yaml    ← Duomenys (aw/cs/cr svoriai)
│   ├── review.md        ← Peržiūra pagal Protocol v1.0
│   └── status.yaml      ← Dabartinis statusas
└── README.md            ← Šis failas
```

## Stimulo gyvavimo ciklas

```
draft → review → beta → approved
                            ↓
                        archived
```

## Kaip pridėti naują stimulą

1. Sukurk naują aplanką: `stimuli/ST-XXX/`
2. Nukopijuok šablonus iš `_templates/`
3. Įdėk nuotrauką kaip `image.png`
4. Užpildyk `stimulus.yaml` (tik duomenys)
5. Nustatyk `status.yaml` → `draft`
6. Užpildyk `review.md` **tik pagal** `docs/methodology/stimulus_validation_protocol.md`
7. Po sėkmingos peržiūros → pakeisk statusą į `beta`

## Validacijos standartas

Visi stimulai validuojami pagal:
`docs/methodology/stimulus_validation_protocol.md` v1.0

**Validation Protocol yra aukštesnio prioriteto negu bet kuris Review.**

## Stimulų sąrašas

| ID | Ašis | Statusas | Pastabos |
|---|---|---|---|
| ST-001 | aw | review | C variantas reikalauja perrašymo |
