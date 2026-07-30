# ConflictLab — Stimulus Library

Kiekvienas stimulas saugomas atskirame aplanke.

## Struktūra

```
stimuli/
├── _templates/          ← Šablonai naujiems stimulams
│   ├── review.md
│   ├── status.yaml
│   └── stimulus.yaml
├── ST-001/              ← aw- (atsitraukimas)
├── ST-002/              ← aw+ (artėjimas) — taisomas
└── README.md
```

## Stimulo gyvavimo ciklas

```
draft → review → beta → approved
                            ↓
                        archived
```

## Kaip pridėti naują stimulą

1. Sukurk `stimuli/ST-XXX/`
2. Nukopijuok šablonus iš `_templates/`
3. Įdėk `image.png`
4. Užpildyk `stimulus.yaml` (tik duomenys)
5. Nustatyk `status.yaml` → `draft`
6. Užpildyk `review.md` pagal `docs/methodology/stimulus_validation_protocol.md`

## Validacijos standartas

`docs/methodology/stimulus_validation_protocol.md` v1.0.1
**Protocol > Review.**

## Stimulų sąrašas

| ID | Ašis | Polius | Kontekstas | Statusas | Pastabos |
|---|---|---|---|---|---|
| ST-001 | aw | - (atsitraukimas) | vidine_erdve | review | C variantas reikalauja perrašymo |
| ST-002 | aw | + (artėjimas) | tarpasmeniniai | review | 🟡 Beta po pataisymo — naratyvinis šališkumas |
