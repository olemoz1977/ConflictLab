# ConflictLab — Micro-Dialogue State Machine v1.0

**Data:** 2026-07-31
**Statusas:** Specifikacija — laukia implementacijos
**Paskirtis:** Adaptyvus dialogas kaip paskutinė sesijos dalis

> Mikro-dialogas nėra priedas po sesijos.
> Jis yra paskutinė sesijos dalis.

---

## Principas

**Ne:** trijų klausimų seka (apklausa)
**O:** būsenų mašina (Dialogue State Machine)

Klausimai yra tik vienas iš galimų kiekvienos būsenos realizavimo būdų.
Ateityje ta pati architektūra gali generuoti skirtingus klausimus pagal:
- signalo tipą (clarity_seeking vs withdrawal_impulse)
- confidence lygį (aukštas vs žemas)
- sesijos numerį (1-a vs 5-a)
- ankstesnių atsakymų istoriją

---

## Būsenų schema

```
┌─────────────────────────────────────────┐
│  REFLECTION                             │
│  (Observation + What + Why + Question)  │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  STATE 0: AGREEMENT                     │
│  Q: Ar tai tau pažįstama?               │
└─────┬─────────────┬───────────────┬─────┘
      │             │               │
   TAIP           NE           NEŽINAU
      │             │               │
      ▼             ▼               ▼
  STATE 2A      STATE 2B        STATE 2C
  Recognition   Disagreement    Uncertainty

      │             │               │
      └─────────────┴───────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│  STATE 3: MIRROR                        │
│  Sistema atspindi — ne interpretuoja    │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  STATE 4: BRIDGE                        │
│  Jungtis į kitą sesiją                  │
└─────────────────────────────────────────┘
```

---

## Būsenų specifikacija

### STATE 0 — Agreement

**Trigeris:** Refleksijos klausimas parodytas
**Žmogaus pasirinkimai:**
- `TAIP` — pažįstama → STATE 2A
- `NE` — čia kitaip → STATE 2B
- `NEŽINAU` — sunku pasakyti → STATE 2C

**Sistema:** Laukia. Nesiūlo interpretacijos.

---

### STATE 2A — Recognition

**Trigeris:** Žmogus pasakė "Taip, pažįstama"
**Klausimas:** "Kas buvo panašiausia?"

**Pasirinkimai (šiandien):**
```
○ Pirmoji mintis
○ Jausmas situacijoje
○ Mano veiksmas
○ Kito žmogaus elgesys
○ Sunku pasakyti
```

**Ateityje:** Pasirinkimai gali keistis pagal signalą.
- `clarity_seeking` → klausimai apie informacijos ieškojimą
- `withdrawal_impulse` → klausimai apie atsitraukimo situacijas

**Signalai:** Pasirinkimas saugomas kaip `recognition_type` kontekstas.
→ STATE 3: MIRROR

---

### STATE 2B — Disagreement

**Trigeris:** Žmogus pasakė "Ne, čia kitaip"
**Klausimas:** "Kas kitaip?"

**Pasirinkimai:**
```
○ Situacija buvo kitokia
○ Mano reakcija paprastai kitokia
○ Klausimas nepritaikomas
○ Sunku pasakyti
```

**Svarbu:** Nesutarimas yra vertinga informacija — ne klaida.
Sistema nepriešinasi ir neaiškina kodėl ji teisi.

**Signalai:** Pasirinkimas saugomas kaip `disagreement_type`.
→ STATE 3: MIRROR

---

### STATE 2C — Uncertainty

**Trigeris:** Žmogus pasakė "Nežinau"
**Elgesys:** Sistema priima nežinomybę be papildomų klausimų.

**Galimas klausimas:** "Ar norėtum grįžti prie šio po kitos sesijos?"
```
○ Taip
○ Ne
```

**Signalai:** `uncertainty_acknowledged = true`
→ STATE 3: MIRROR

---

### STATE 3 — Mirror

**Tikslas:** Sistema atspindi — ne interpretuoja.
**Principas:** Naudoja tik žmogaus pasirinkimų žodžius — ne savus.

```
STATE 2A pavyzdys:
"Tu pažymėjai, kad labiausiai pažįstama buvo pirmoji mintis.
 Šį stebėjimą naudosime kitame tyrimo etape."

STATE 2B pavyzdys:
"Tu pažymėjai, kad situacija buvo kitokia.
 Tai svarbu — kitoje sesijoje patikrinsime skirtingose situacijose."

STATE 2C pavyzdys:
"Nežinomybė taip pat yra stebėjimas."
```

**Draudžiama:** Sistema nekuria naujų interpretacijų iš pasirinkimų.
→ STATE 4: BRIDGE

---

### STATE 4 — Bridge

**Tikslas:** Jungtis į kitą sesiją. Kalbėti apie tikslą, ne apie algoritmą.

**Draudžiama:**
```
❌ "Kita sesija remsis tuo, ką ką tik pastebėjome." ← atskleidžia mechaniką
```

**Leidžiama:**
```
✓ "Kitoje sesijoje patikrinsime, ar šis stebėjimas kartojasi kitose situacijose."
✓ "Kitoje sesijoje tęsime šį tyrinėjimą."
✓ "Gal šiandien dar pastebėsi kažką, ko anksčiau nepastebėdavai."
```

**Po pirmosios sesijos:** nėra Bridge — žmogus dar negali palyginti.
**Po antrosios+:** Bridge aktyvuojamas.

---

## Kognityvinio nepertraukiamumo taisyklė

Sesija psichologiškai baigiasi STATE 4 — ne po ketvirto stimulo.

```
TEISINGAS srautas:
Stimulai → Reflection → Mikro-dialogas → Bridge → [Sesija baigta]

KLAIDINGAS srautas:
Stimulai → [Sesija baigta] → Dar truputį pakalbėkime
```

Žodžiai "Sesija baigta" rodomi TIK po STATE 4.

---

## Duomenų struktūra

Kiekviena mikro-dialogo sesija išsaugoma `cl_debug_log`:

```json
{
  "micro_dialogue": {
    "state_path": ["S0", "S2A", "S3", "S4"],
    "agreement": "yes",
    "recognition_type": "first_thought",
    "mirror_shown": true,
    "bridge_shown": true
  }
}
```

---

## Ką DSM apsaugo

1. **Nuo apklausos:** Klausimai nėra fiksuota seka — jie priklauso nuo būsenos
2. **Nuo interpretacijos:** STATE 3 (Mirror) naudoja tik žmogaus žodžius
3. **Nuo algoritmo atskleidimo:** STATE 4 (Bridge) kalba apie tikslą
4. **Nuo kognityvinio pertrūkio:** Sesija baigiasi STATE 4, ne po stimulų

---

## Plėtros kryptys (neimplementuoti dabar)

- STATE 2A klausimai pagal signalo tipą
- STATE 2B gilesnis nesutarimo tyrimas
- STATE 4 tekstas pagal sesijos numerį ir trajektoriją
- Kelių sesijų micro-dialogue history

---


---

## Du architektūriniai principai

### Progressive Commitment

> Kiekviena būsena gali paprašyti tik vieno mažo įsipareigojimo iš vartotojo.

Jei vienoje būsenoje paprašoma prisiminti, paaiškinti, parašyti ir įvertinti —
žmogus pereina į racionalizavimą. ConflictLab metodologija remiasi
mažais, natūraliais refleksijos žingsniais.

```
S0: Ar tai pažįstama?           ← vienas klausimas
S2: Kas pažįstama?              ← vienas klausimas
S3: Sistema atspindi            ← jokio klausimo
S4: Kitas etapas atsidaro       ← jokio klausimo
```

### State Independence

> Kiekviena būsena turi vieną tikslą.

| Būsena | Tikslas |
|---|---|
| S0 | Patikrinti rezonansą |
| S2A | Identifikuoti kas rezonuoja |
| S2B | Suprasti nesutikimo tipą |
| S2C | Pripažinti neapibrėžtumą |
| S3 | Atspindėti |
| S4 | Sukurti tiltą į kitą etapą |

Jokia būsena neturi bandyti atlikti dviejų funkcijų vienu metu.

---

## Apibrėžimas

> Refleksija nėra klausimynas.
> Tai būsenomis valdomas dialogas, kuris seka žmogaus kognityvinę būseną.

---

*Micro-Dialogue State Machine v1.1 — Progressive Commitment + State Independence*
*ConflictLab — žmogus yra bendratyrėjas, ne objektas*
