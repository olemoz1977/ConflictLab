# ConflictLab — Methodology Freeze v1.0

**Data:** 2026-07-31
**Statusas:** AKTYVUS

---

## Užšaldyta metodika

Šie dokumentai yra užšaldyti. Nekeičiami be beta duomenų pagrindo.

| Dokumentas | Versija | Aprašas |
|---|---|---|
| `conflictlab_voice_v1.md` | v1.0 | Kaip sistema kalba su žmogumi |
| `behavior_translation_architecture_v1.md` | v1.1 | Reflection Engine architektūra |
| `stimulus_validation_protocol.md` | v1.0.1 | Kaip vertinti stimulus |
| `stimulus_matrix_v1.md` | v1.0.1 | Bibliotekos planavimas |
| `stimulus_language_standard.md` | v1.2 | F1–F7 cue kūrimo taisyklės |
| `stimulus_lifecycle_v1.md` | v1.0 | Gamybos procesas |
| `beta_research_protocol_v1.md` | v1.0 | H1–H4 tyrimo hipotezės |

---

## Kas leidžiama

- Kurti naujus stimulus pagal esamus standartus
- Taisyti kodus kai aptinkamos klaidos
- Rinkti beta duomenis

## Kas draudžiama

- Nauji metodologiniai dokumentai
- Nauji filtrai (F8, F9...)
- Nauji ADR be kritinės priežasties
- Architektūros pakeitimai

---

## Trys prioritetai iki pirmos beta analizės

**1. 10–15 etaloninių stimulų**
Nepriekaištingai atitinkančių F1–F7 ir Lifecycle procesą.

**2. Ribota beta**
10–15 žmonių, ≥3 sesijos. H1–H4 tikrinimas.

**3. Taisyti tik pagal duomenis**
Ne pagal nuojautą. Ne pagal diskusiją. Tik pagal tai ką parodys realūs žmonės.

---

## Kitas metodologinis atnaujinimas

**Kada:** po pirmosios beta analizės (≥30 sesijų)
**Sąlyga:** duomenys aiškiai rodo konkrečią spragą
**Procesas:** atidaryti Freeze → keisti → užšaldyti iš naujo

---

## Success Criteria v1.0

Beta laikoma sėkminga ne tada kai nėra klaidų — o tada kai pasiekiami šie kriterijai.

**SC1 — Natūrali reakcija**
Dauguma dalyvių renkasi spontaniškai, nejaučia kad ieško „teisingo atsakymo".

**SC2 — Refleksijos rezonansas**
Rezultatas atrodo susijęs su jų pačių patirtimi — ne kaip bendrinė frazė.

**SC3 — AHA momentas**
Dalis dalyvių pasako kažką panašaus į: *„Apie tai nebuvau pagalvojęs."*
Tai svarbiau nei „patiko".

**SC4 — Pasitikėjimas**
Vartotojas nejaučia kad sistema jį vertina ar diagnozuoja.

**SC5 — Pakartotinis naudojimas**
Po pirmos sesijos žmogus nori grįžti ne todėl kad gautų kitą „rezultatą" — o todėl kad nori geriau suprasti savo reakcijų dėsningumus.

---

## Ryšys su beta hipotezėmis

| Success Criteria | Beta hipotezė |
|---|---|
| SC1 | H1 (≥70% AHA) + stebėjimas |
| SC2 | H1 (Q2 — „to nebuvau pastebėjęs") |
| SC3 | H1 tiesioginė |
| SC4 | H4 (nesutarimų kokybė) |
| SC5 | Grįžtamumo metrika — nauja |

---

## Methodology Freeze Commitment

> Nuo šio momento metodologijos pakeitimai priimami tik tada, jei beta duomenys aiškiai rodo, kad dabartinė metodika nepasiekia SC1–SC5 kriterijų. Idėjos, intuicija ar pavienės nuomonės nebėra pakankamas pagrindas keisti sistemą.

---

*"Nebe Architecture. Evidence."*
