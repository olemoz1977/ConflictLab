# Radar Block Model V1

**Dokumentas:** `docs/experiments/pair-p0/RADAR_BLOCK_MODEL_V1.md`
**Versija:** V1
**Data:** 2026-08-07
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
Blokas 1:  sesijos 1–3  →  pirmas radaras
Blokas 2:  sesijos 4–6  →  antras radaras
Blokas 3:  sesijos 7–9  →  trečias radaras
...
```

Radaras rodomas **tik po pilno bloko** (3 sesijų). Po pavienės sesijos radaro **nerodome**.

---

## Konstrukcinis balansas per bloką

Kiekvienas radaro blokas turi:
- 3 sesijas
- 3 poras sesijoje
- **9 unikalias poras** bloke

Tikslinis ašių balansas per bloką:

```
3 AW (Awareness)
3 CS (Connection-Seeking)
3 CR (Control-Resistance)
```

Kiekvienoje sesijoje:

```
1 AW
1 CS
1 CR
```

Randomizacija leidžiama tik **nepažeidžiant šio balanso** — porų eilė sesijoje gali būti randomizuojama, bet sesijos ašių sudėtis fiksuota.

### Svarbi pastaba apie balansą

**3×3 nėra įrodymas apie 100 % statistinę normalizaciją.**

Tai **konstrukcinis balansas**, skirtas mažinti:
- vienos ašies dominavimą viename bloke
- vieno stimulo dominavimą
- pateikimo eilės įtaką
- vienos stimulų šeimos perteklių

Balansas yra metodologinė priemonė, ne statistinis garantas.

---

## Radarų palyginimo taisyklė

### Pagrindinis palyginimas (kiekvienas radaras lygina su ankstesniu bloku)

```
Blokas 2 (sesijos 4–6)  prieš  Bloką 1 (sesijos 1–3)
Blokas 3 (sesijos 7–9)  prieš  Bloką 2 (sesijos 4–6)
Blokas 4 (sesijos 10–12) prieš Bloką 3 (sesijos 7–9)
```

Papildomai ateityje galima rodyti pokytį nuo pirmojo bloko (1–3), bet tai nėra pagrindinis palyginimas.

### Draudžiama naudoti

```
❌  Blokas 1 (1–3)  prieš  Kaupiamą (1–6)
```

**Priežastis:** duomenų apimtis nevienoda — palyginimas tampa beprasmis.

**Taisyklė:** kiekvienas radaras skaičiuojamas **tik iš savo 3 sesijų bloko**, niekada iš kaupiamo skaičiaus.

---

## Expectation / progress layer

Prieš pirmą sesiją vartotojas mato:
> „Pirmas bendras vaizdas — po 3 trumpų sesijų"

Po kiekvienos sesijos:

| Sesijų baigta | Rodoma |
|---|---|
| 0 | Expectation ekranas |
| 1 | „1 iš 3 sesijų" |
| 2 | „2 iš 3 sesijų" |
| 3 | Pirmas radaras |
| 4 | „1 iš 3 sesijų iki kito palyginimo" |
| 5 | „2 iš 3 sesijų iki kito palyginimo" |
| 6 | Antras radaras |

---

## Dabartinė bibliotekos riba ir antras blokas

### Dabartinė būsena

Šiuo metu turime **9 prototipo poras** (P0-001–003, N0-004–009).

Tai reiškia: sesijose 4–6 tektų **kartoti** tuos pačius stimulus.

| Naudojimas | Statusas |
|---|---|
| Techninis antro radaro srauto testas | Leidžiama |
| Švarus reakcijų pokyčio matavimas | **Ne** — vartotojas atpažins vaizdus |

Kai kartojami stimulai, dokumentuoti:
```
comparison_status: "prototype_repeated_stimuli"
```

### Tikslas — 18 unikalių porų

Reikia dar 9 naujų porų: **N0-010–N0-018**

```
3 AW
3 CS
3 CR
```

Tuomet:
```
Blokas 1 = P0-001–003 + N0-004–009  (9 unikalios poros)
Blokas 2 = N0-010–018               (9 unikalios poros)
```

Tai leis švariai palyginti du lygiaverčius 3×3 blokus be pakartotinių stimulų.

---

## P9/M0 izoliacija (OQ-001 — CLOSED)

**Patvirtinta architektūrinė taisyklė:**

P9 ir M0 sesijos izoliuojamos pagal `set_id` — kiekvienas radaras skaičiuojamas tik iš savo sesijų.

| Srautas | `set_id` | Radaras |
|---|---|---|
| prototype-nine-v1 | `"prototype-nine-v1"` | P9 radaras |
| M0 | `"m0-default"` arba legacy (visos poros P0-001/002/003) | M0 radaras |
| n0-six-v3 | `"n0-six-v3"` | Nė vienas |

`n0-six-v3` sesijos **negali** patekti nei į M0, nei į P9 radarą.

Legacy M0 sesijos be `set_id` priimamos tik jei visos poros yra P0-001, P0-002, P0-003.

---

## Dabartiniai patvirtinti blokai

### Blokas 1 — prototype-nine-v1

| Sesija | Poros | Ašys |
|---|---|---|
| Sesija 1 | P0-001, P0-002, P0-003 | AW, CS, CR |
| Sesija 2 | N0-004, N0-005, N0-006 | AW, CS, CR |
| Sesija 3 | N0-007, N0-008, N0-009 | AW, CS, CR |

**Pastaba:** N0-004–009 šiuo metu yra `prototype_only` — vektoriai nekalibruoti, `analysis_eligible: false`. Prototipo režime naudojami `prototype_vector`. M0 radaras šių sesijų naudoti negali.

---

## Susijęs kodas

- `P9_FIRST_RADAR_AFTER = 3` — pirmasis radaro slenkstis
- `isRadarUnlocked()` — tikrina ar `getCompletedSessionCount() >= getFirstRadarThreshold()`
- `isSessionRadarEligible(s, mode)` — filtruoja sesijas pagal `set_id`
- `SESSION.radar_unlocked` — atspindi būseną **po** sesijos užbaigimo (fix: commit `b3dcbf6`)
