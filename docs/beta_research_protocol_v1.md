# ConflictLab — Beta Research Protocol v1.0

**Data:** 2026-07-31
**Tipas:** Tyrimas, ne produkto testas
**Versija:** Reflection Engine v1.1 (užšaldyta)
**Dalyviai:** 10–15 žmonių, uždara beta
**Sesijos:** ≥ 3 sesijos vienam dalyviui

---

## Tyrimo tikslas

Patikrinti, ar Reflection Engine pateikia žmogui refleksijas kurios:

1. Yra suprantamos be papildomų paaiškinimų
2. Atspindi kažką ką žmogus pats anksčiau nepastebėjo
3. Nėra universalios (Barnum efektas)
4. Yra pagrįstos faktiniais duomenimis iš sesijų

Tai nėra klausimas "ar patiko". Tai klausimas "ar tikslu".

---

## Hipotezės

| ID | Hipotezė | Sėkmės kriterijus | Matavimas |
|---|---|---|---|
| H1 | ≥ 70% dalyvių bent vieną įžvalgą įvertins kaip "to nebuvau pastebėjęs" | ≥ 7 iš 10 dalyvių | Post-session klausimas Q2 |
| H2 | Fallback dažnis neviršys 20% sesijų | ≤ 1 fallback iš 5 sesijų | cl_debug_log.fallback |
| H3 | P9 įžvalgos sukels daugiau AHA momentų nei P5 | P9 Q2 ≥ P5 Q2 + 15% | Pattern tipo koreliacija su Q2 |
| H4 | Žmogus nesutarimo atveju sugebės įvardyti konkrečią priežastį | ≥ 60% "Ne, čia kitaip" atsakymų turės tekstą | Q3 lauko analizė |

---

## Sesijų protokolas

### Dalyvio instrukcija (trumpa)

> Atlieki 3 sesijas — ne iš karto, o skirtingomis dienomis.
> Po kiekvienos sesijos atsakai į 3 klausimus.
> Tai nėra testas. Mes tikrinami, ne tu.

### Po kiekvienos sesijos — 3 klausimai

**Q1:** Ar refleksija buvo suprantama?
`Taip, iš karto / Reikėjo pagalvoti / Ne, nesupratau`

**Q2:** Ar buvo kažkas, ko pats nebuvai pastebėjęs?
`Taip — [aprašyk] / Ne, žinojau / Iš dalies`

**Q3:** Jei atsakei "Ne, čia kitaip" — kas tiksliai neatitiko?
`[laisvas tekstas arba tuščia]`

### Po 3 sesijų — 2 papildomi klausimai

**Q4:** Ar tarp sesijų pagalvojai apie kurį nors refleksijos klausimą?
`Taip — [kuriuo ir ką] / Ne`

**Q5:** Ar sistema kada nors pasakė kažką, kas atrodė kaip horoskopas — teisingai bet apie visus?
`Taip — [pavyzdys] / Ne`

---

## Duomenų rinkimas

### Subjektyvūs duomenys (iš dalyvių)
Q1–Q5 atsakymai — el. paštu arba žinute po kiekvienos sesijos.

### Objektyvūs duomenys (iš cl_debug_log)

Kiekviena sesija automatiškai saugo:

```javascript
{
  ts: timestamp,
  axes: {aw, cs, cr},
  sp: [{t: "P1", a: "cs", c: "0.84"}, ...],  // session patterns
  cp: [{t: "P9", a: "aw", c: "0.92"}, ...],  // cross patterns
  aha: {pat: "P9", ev: "atsitraukimas → artėjimas", score: 0.95}
  // arba: {fallback: "Nėra kandidatų"}
}
```

Šie duomenys yra anoniminiai pagal apibrėžimą — nėra vardo, IP ar identifikatoriaus.

### Sąsaja tarp duomenų

Po kiekvienos sesijos dalyvys nurodo **sesijos numerį** (1, 2, 3).
Tai leidžia susieti Q2 atsakymą su atitinkamo laikotarpio debug_log įrašu.

---

## Analizės planas

### Po 10 dalyvių / 30 sesijų

**Kiekybinė analizė:**
- H1: Q2 teigiamų atsakymų dalis
- H2: fallback sesijų / visų sesijų
- H3: P9 sesijų Q2 lyginimas su P5 sesijų Q2

**Kokybinė analizė:**
- Q5 "horoskopo" atvejai → identifikuoti kurį pattern ar šabloną pakeisti
- Q3 nesutarimų tekstai → identifikuoti ar sistema klysta sistemingai
- Q4 "pagalvojau tarp sesijų" → identifikuoti kurios įžvalgos paliko pėdsaką

### Debug log tendencijos

```
Klausimas                          Kaip matuoti
─────────────────────────────────────────────────
Kurie patterns dažniausi?          sp/cp dažnio skaičiavimas
Kurie patterns dažniausiai → AHA?  aha.pat dažnis
Kurie patterns niekada → AHA?      sp/cp be atitinkamo aha.pat
Ar latency koreliuoja su H1?       aha.ev turintys "latency" ~ Q2=Taip
```

---

## Etiniai principai

**Dalyviai žino:**
- Tai yra tyrimas, ne galutinis produktas
- Sistema neanalizuoja jų asmenybės
- Duomenys anonimiški
- Jie gali sustoti bet kada

**Sistema garantuoja:**
- Jokių asmens duomenų serveryje (localStorage tik vartotojo įrenginyje)
- Tyrėjas mato tik susumuotus debug log duomenis
- Q1–Q5 atsakymai saugomi tyrėjo privačiai, ne sistemoje

---

## Kas laikoma tyrimo sėkme

**Minimalus sėkmės kriterijus:**
H1 pasitvirtina (≥ 70% AHA) **ir** H2 pasitvirtina (≤ 20% fallback)

**Stiprus rezultatas:**
H1 + H2 + H3 pasitvirtina

**Nepatenkinamas rezultatas:**
H1 < 50% — sistema per dažnai sako kažką žmogui jau žinoma arba nesuprantama.
→ Peržiūrėti Behavior Translation šablonus

H2 > 40% — Pattern Detection per griežtas arba stimulai per silpni.
→ Peržiūrėti P1-P3 confidence thresholds

H4 < 40% — Nesutarimo signalas yra triukšmas, o ne informacija.
→ Pergalvoti "Ne, čia kitaip" klausimo formuluotę

---

## Versijų valdymas tyrimo metu

**Reflection Engine v1.1 — užšaldyta tyrimo laikotarpiui.**

Jokių kodo pakeitimų be:
1. Tyrimo sustabdymo
2. Datos žymos
3. Paaiškinimo kodėl pakeitimas buvo būtinas prieš baigiant tyrimą

Tik tokiu atveju duomenys išlieka palyginami.

---

## Tvarkaraštis

| Etapas | Laikas | Tikslas |
|---|---|---|
| Pirma banga | 1–2 savaitės | 10 dalyvių, ≥ 3 sesijos kiekvienas |
| Tarpinė analizė | Po 30 sesijų | H1-H4 preliminarūs rezultatai |
| Sprendimas | Po analizės | Tęsti / Koreguoti / Stabdyti |
| Antra banga | Jei tęsiama | 15–20 dalyvių, patikrinti pakeitimus |

---

## Vienas sakinys tyrėjui

> Mes ne tikriname ar sistemą pataisėme.
> Mes tikriname ar mūsų hipotezės apie žmogaus refleksiją yra teisingos.

---

*Beta Research Protocol v1.0*
*ConflictLab — nebe Architecture. Evidence.*
