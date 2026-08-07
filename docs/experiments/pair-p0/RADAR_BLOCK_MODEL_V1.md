# Radar Block Model V1

**Dokumentas:** `docs/experiments/pair-p0/RADAR_BLOCK_MODEL_V1.md`
**Versija:** V1.1
**Data:** 2026-08-08
**Statusas:** PATVIRTINTA — architektūrinė taisyklė

---

## Terminai

| Terminas | Apibrėžimas |
|---|---|
| **Pora** | Vienas vaizdų porų stimulas (A/B pasirinkimas) |
| **Sesija** | 3 vaizdų poros → 3 pasirinkimai |
| **Radaro blokas** | 3 sesijos → 9 pasirinkimai → 1 radaras |
| **Biblioteka** | Visų galimų porų fondas |

---

## Fiksuota sesijų-radaro struktūra

```
Blokas 1:  sesijos 1–3  →  Radar 1
Blokas 2:  sesijos 4–6  →  Radar 2
Blokas 3:  sesijos 7–9  →  Radar 3
...
```

Radaras rodomas **tik po pilno bloko** (3 sesijų). Po pavienės ar dalinės sesijos radaro **nerodome**.

---

## Routing modelis

| Completed sessions | blockProgress | Ekranas |
|---|---|---|
| 0 | — | Intro / Expectation |
| 1 | 1/3 | Progress „1 iš 3 sesijų" |
| 2 | 2/3 | Progress „2 iš 3 sesijų" |
| **3** | **3/3** | **Radar 1** |
| 4 | 1/3 | Progress „1 iš 3 iki kito palyginimo" |
| 5 | 2/3 | Progress „2 iš 3 iki kito palyginimo" |
| **6** | **3/3** | **Radar 2 + comparison** |
| 7 | 1/3 | Progress |
| 8 | 2/3 | Progress |
| **9** | **3/3** | **Radar 3 + comparison** |

### Kritinė taisyklė

```
hasUnlockedRadar() ≠ "rodyk radarą dabar"
```

`hasUnlockedRadar()` reiškia tik: **bent vienas pilnas radaras egzistuoja istorijoje**.

Radaro renderinimą lemia išimtinai: `isP9BlockComplete(currentBlockIndex) === true`

---

## Konstrukcinis balansas per bloką

Kiekvienas radaro blokas:
- 3 sesijos
- 3 poros sesijoje
- **9 unikalios poros** bloke

Tikslinis ašių balansas:

```
3 AW (Awareness)
3 CS (Connection-Seeking)
3 CR (Control-Resistance)
```

Kiekvienoje sesijoje: 1 AW + 1 CS + 1 CR

**3×3 nėra statistinė garantija — tai konstrukcinis balansas**, skirtas mažinti vienos ašies, vieno stimulo ar pateikimo eilės dominavimą.

---

## Vizualizacijos architektūra

### Kodėl bipolar map, ne 6-spoke radar

Metodologiškai turime **3 bipolarines dimensijas**, ne 6 nepriklausomus matmenis.

Senas 6-spoke radaras išskaidydavo kiekvieną signed reikšmę į du vienpusius spindulius (`aw+` ir `aw-`), kur vienas visada buvo 0 — tai kūrė dirbtinę 6-matmenų iliuziją.

Naujas bipolar map:
- 3 pilni diametrai (ne 6 spinduliai)
- Kiekviena reikšmė → **1 signed taškas** ant atitinkamo diametro
- 3 taškai → trikampė forma

### 3 bipolarinės ašys

| Ašis | Teigiama pusė | Neigiama pusė | SVG kampas |
|---|---|---|---|
| AW | Artėti (Approach) | Atsitraukti (Step back) | -90° |
| CS | Aiškumas (Clarity) | Neapibrėžtumas (Ambiguity) | 210° |
| CR | Struktūra (Structure) | Laisvumas (Flexibility) | -30° |

### Taško skaičiavimas

```
point = (center + cos(posAngle) * value * maxRadius,
         center + sin(posAngle) * value * maxRadius)
```

Kur `value = p9RawToDisplay(raw)` — **tik SVG koordinatėms**.

---

## RAW vs DISPLAY — du sluoksniai

### RAW / Internal

RAW AW/CS/CR naudojamas:
- bloko vektoriaus skaičiavimui (`computeP9BlockTrace`)
- eksportui
- delta skaičiavimui
- comparison teksto generavimui (automatiniai sakiniai)
- audit/QA

RAW **niekada nekeičiamas ir neclampinamas**.

### DISPLAY / SVG koordinatės

Tik SVG taškų pozicijoms:

```javascript
const P9_DISPLAY_CALIBRATION_VERSION = 'p9-display-v1';
const P9_DISPLAY_BOUND = 0.65;

function p9RawToDisplay(rawValue) {
  const d = rawValue / P9_DISPLAY_BOUND;
  return Math.max(-1, Math.min(1, d));  // clamp tik SVG saugai
}
```

**Transformacija:**
- `raw = 0` → centras
- `raw = +0.65` → teigiamas kraštas
- `raw = -0.65` → neigiamas kraštas
- Tiesinė, vienoda visoms 3 ašims

### Kodėl viena bendra skalė (ne per-axis)

Cue vektoriai yra **multi-axis** (100% cue turi >1 ne-nulinę ašį). Per-axis scaling pakeistų AW/CS/CR tarpusavio geometriją — trikampis taptų iškraipytas, neatspindėdamas realių skaičiavimų proporcijų.

**Kodėl draudžiamas block-specific autoscale:**
- Block 1 ir Block 2 overlay turi naudoti tą pačią skalę abiem blokams
- Skirtingos skalės sugadintų cross-block palyginamumą
- `display1 = raw1 / 0.65` ir `display2 = raw2 / 0.65` — vienodas bound, lygiaverčiai blokai

### Kodėl 0.65

Grįsta `tests/pair_p0_attainable_envelope.py` auditu:
- Realus P9 cue max absoliutus dydis = **0.65** (N=1 atveju)
- 9/9 envelope: AW ±0.372, CS ±0.383, CR ±0.333
- Vienas cue (N=1) gali pasiekti iki ±0.65

**0.65 nėra universali ConflictLab konstanta** — ji galioja tik `prototype-nine-v1 / p9-display-v1`. Pakeitus stimulų/cue biblioteką, reikalingas naujas auditas ir nauja versija.

---

## Radarų palyginimo taisyklė

### Pagrindinis palyginimas

```
Blokas 2 (sesijos 4–6) vs Blokas 1 (sesijos 1–3)
Blokas 3 (sesijos 7–9) vs Blokas 2 (sesijos 4–6)
```

### Draudžiama

```
❌  Kumuliatyvus 1–6 radaras
❌  Blokas 1 vs kumuliatyvus 1–6
```

Kiekvienas radaras skaičiuojamas **tik iš savo 3 sesijų bloko**.

---

## Comparison vizualas (Block 2+)

Vienas overlay SVG su abiem blokais:
- **Pilkas polygon:** ankstesnis blokas (Block 1 arba N-1)
- **Žalias polygon:** dabartinis blokas (Block 2 arba N)
- Legenda: „● 1 blokas  ● 2 blokas" (arba EN)

Tekstinis palyginimas: automatiškai generuojami neutralūs sakiniai kiekvienai ašiai (7 atvejų logika — ženklo pasikeitimas, ta pati pusė, centras ir t.t.).

---

## Dabartinė bibliotekos riba

Šiuo metu: **9 prototipo poros** (P0-001–003, N0-004–009).

Sesijose 4–6 kartojami tie patys stimulai → comparison žymima:
```
comparison_status: "prototype_repeated_stimuli"
```

Tai tinka techniniam flow testui, bet nėra švarus pokyčio matavimas.

### Tikslas — 18 unikalių porų

```
Blokas 1 = P0-001–003 + N0-004–009  (9 unikalios)
Blokas 2 = N0-010–018               (9 unikalios, dar nekurtos)
```

---

## P9/M0 izoliacija (OQ-001 — CLOSED)

P9 ir M0 sesijos izoliuotos pagal `set_id`. M0 legacy `renderRadarSVG()` nepakeistas.

| Srautas | `set_id` | Vizualizacija |
|---|---|---|
| prototype-nine-v1 | `"prototype-nine-v1"` | `renderP9BipolarMapSVG()` |
| M0 | `"m0-default"` / legacy | `renderRadarSVG()` (nepakeista) |

---

## Susijęs kodas

- `P9_FIRST_RADAR_AFTER = 3` — pirmojo radaro slenkstis
- `isP9BlockComplete(blockIndex)` — ar blokas pilnas (3 sesijos)
- `hasUnlockedRadar()` — ar bent vienas pilnas radaras egzistuoja (≠ "rodyk dabar")
- `computeP9BlockTrace(blockIndex)` — bloko RAW vektorius
- `renderP9BipolarMapSVG(trace, opts)` — P9 vizualizacija
- `p9RawToDisplay(raw)` — RAW→DISPLAY transformacija
- `renderP9BlockComparison(body, prev, curr, blockIndex)` — tekstinis palyginimas
