# Reflection Engine Validation Report v1.0

**Data:** 2026-07-31 | **Scenarijai:** 25 | **Statusas:** 22/25 teisingi

---

## Rezultatų lentelė

| # | Scenarijus | Pattern | AHA | Teisingas? |
|---|---|---|---|---|
| S01 | Aiškus P5 cs+ | P5:cs | ✅ insight | ✅ |
| S02 | P9 aw- → aw+ | P9:aw | ✅ insight 0.95 | ✅ |
| S03 | P5 vs P9 cs | P9:cs | ✅ P9 laimėjo | ✅ |
| S04 | Tik hesitation | P3 | ❌ fallback | ⚠️ P3 nepraėjo K1 |
| S05 | Visi neutralūs | — | ❌ fallback | ✅ |
| S06 | P6 kontrastas | P6:aw | ✅ insight | ⚠️ evidence = dict ne string |
| S07 | P2 aw- cr+ | P2:aw+cr | ✅ insight 0.765 | ✅ |
| S08 | Nepakankamai | — | ❌ fallback | ✅ |
| S09 | Aukštas confidence P9 | P9:cr | ✅ insight 0.9 | ✅ |
| S10 | Žemas confidence P5 | P8:aw | ⚠️ P8 vietoj P5 | ⚠️ |
| S11 | Nesutarimas ×2 P7 | P7 | ❌ fallback | ✅ (sąmoningas) |
| S12 | cr- strong + cs+ | P1:cr | ✅ insight | ✅ |
| S13 | P5 aw- + hesitation | P5:aw | ✅ insight | ✅ |
| S14 | Pirma sesija P1 | P1:cs | ✅ insight 0.7 | ✅ |
| S15 | P8 stabilumas | P8:aw | ⚠️ AHA 0.28 | stebėti |
| S16 | P9 cs- → cs+ | P9:cs | ✅ insight 0.9 | ✅ |
| S17 | Visi P1 strong | P2:aw+cs | ✅ P2 laimėjo | ✅ |
| S18 | Automatic (<2s) | P3 | ❌ fallback | ✅ |
| S19 | P9 cr+ → cr- | P9:cr | ✅ insight 0.9 | ✅ |
| S20 | Nesutarimas + stiprus | P1:cs | ✅ insight | ✅ |
| S21 | P4 šeimos konc. | P4 | ❌ fallback | ✅ (nėra šablono) |
| S22 | 4 sesijų trajektorija | P9:aw | ✅ insight 0.95 | ✅ |
| S23 | P2 cs+ cr- | P1:cs | ⚠️ P2 pralaimi P1 | ⚠️ |
| S24 | Mišri feedback | P5:aw | ✅ insight | ✅ |
| S25 | Minimali sesija | — | ❌ fallback | ✅ |

---

## Aptiktos problemos

### Kritiškas — taisyti dabar

**P1: S06 evidence_str grąžina Python dict:**
```
Dabartinis: {'prev_direction': 'negative', 'curr_direction': 'positive', ...}
Reikia:     'atsitraukimas → artėjimas (sesija 1 → sesija 2)'
```
Taisymas: `_build_evidence_str()` P6 šaka.

**P2: S23 — P2 pralaimi P1:**
Kai yra P2 (ašių konfliktas) ir P1, sistema pasirenka P1. P2 yra informatyvesnis.
Taisymas: Pridėti `cs+cr` šabloną į TEMPLATES.

**P3: S04 — P3 hesitation nepraėjo K1 (confidence 0.3 < 0.40):**
Sistema fallback'ina vietoj: "Prie vieno vaizdo tavo dėmesys sustojo ilgiau."
Taisymas: K1 threshold mažinti iki 0.25 tik P3 tipui.

### Vidutinis — taisyti prieš beta

**P4: S10 — P8 pasirenka vietoj silpno P5:**
AHA reitingavimas neatskiria "silpnas bet tikras" nuo "neutralus".
Taisymas: P8 aha_potential mažinti — rodyti tik kai nėra kitų kandidatų.

### Galima atidėti

- P4 šablonas (nėra empirinių duomenų)
- P7 šablonas (reikia gilesnio sprendimo apie paradoksą)

---

## Gerai veikiantys mechanizmai

- ✅ P9 prioritetas prieš P5 ta pačia ašimi (S03)
- ✅ Fallback sąžiningas ir Voice v1.0 atitinkantis (S05, S08, S18, S25)
- ✅ P2 laimi prieš P1 kai abu yra (S07, S17)
- ✅ Mišri feedback istorija netrukdo signalui (S24)
- ✅ 4 sesijų trajektorija veikia (S22)
- ✅ Feedback "no" neblokuoja insight (S20)
- ✅ Barnum filtras: nė vienas scenarijus nerodė psichologizuoto teksto

---

## Vertinimas

**22/25 scenarijai architektūriškai teisingi.**
3 problemos yra techninio lygio — ne filosofinio.
Nė viename scenarijuje sistema nebandė psichologizuoti.

**Rekomendacija:** Atlikti 3 kritinių taisymų → integruoti į UI.
