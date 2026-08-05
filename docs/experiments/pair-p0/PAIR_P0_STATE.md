# ConflictLab Pair P0 — Būsena (užšaldyta po H etapo)

**Data:** 2026-08-05
**Stabilus tag:** `pair-p0-h-stable` (commit `8a4e7a0`)
**Statusas:** Techninė plėtra sustabdyta. Laukiama išorinio vartotojų testo rezultatų.

---

## Kas veikia (patvirtinta realiais testais, ne tik logika)

### Pagrindinis srautas
- Poros → vaizdo pasirinkimas (latency matavimas, pozicijos randomizacija)
- Cue pasirinkimas (18 standartinių cue, arba "Kita mintis" custom tekstas, arba "Sunku pasakyti")
- Individuali refleksija (iki 5 žodžių, susieta su konkrečiu cue)
- Sesijos refleksija (bendras pastebėjimas po visų 3 vaizdų, arba "Kol kas neįvardysiu")
- Sesijos rezultatas (visi pasirinkimai + pastebėjimas + metodinė riba)
- Feedback (4 klausimai apie patirtį)
- Sesijos užbaigimas → `completed_sessions`

### Istorija ir duomenys
- `active_session` / `completed_sessions` atskyrimas — tik pilnai užbaigtos sesijos patenka į istoriją
- Istorijos sąrašas + detalus vaizdas kiekvienai sesijai
- Tuščios istorijos paaiškinimas (WebView/naršyklės skirtumo užuomina)

### Radaras (E/E.1 etapai)
- 3 tinkamų (eligible) sesijų reikalavimas prieš rodant
- Šešių krypčių dvipolė geometrija (aw+/aw−/cs+/cs−/cr+/cr−), 0 visada centre
- Švelni netiesinė vizualinė skalė (`pow(x, 0.7)`) su metodine pastaba apie mastelį
- Eligibility filtras: `session_vector` egzistuoja, `valid_vector_responses>=2`, confidence baigtinis, `vector_model_version` sutampa, ašys `[-1,1]` ribose

### Palyginimas (F etapas)
- Nuo 6 eligible sesijų — "Dabar" (paskutinės 3) vs "Anksčiau" (prieš tai buvusios 3)
- Confidence svertinis vidurkis periodams
- Perdengtas radaras (vientisas vs punktyrinis kontūras)
- Neutralus tekstas pagal amplitudės slenksčius, be vertinimo žodžių

### Istorijos eksportas/importas (H etapas)
- Švarus eksporto failas (`conflictlab-history-YYYY-MM-DD.json`) — tik completed sesijos
- Importas su schema/lauko validacija, merge pagal `session_id`, dublikatų apsauga
- Vietinis įrašas niekada neperrašomas importuotu
- Importo santrauka (Imported/Duplicates/Invalid) — **realiai patikrinta** dviejuose naršyklėse

---

## Kas sąmoningai NEĮTRAUKTA į P0

- **G etapas (teminis palyginimas)** — pradėtas, bet **atšauktas** dėl klaidingo cue→tema žemėlapio (A/B priskyrimo klaida). Patvirtintas teisingas 18 cue → 1 tema žemėlapis paruoštas, bet **neįdiegtas** — reikalauja atsargesnio testavimo prieš grąžinant
- AI interpretacija ar analizė bet kuriame etape
- Paskyros, prisijungimas, debesies sinchronizacija
- Šifravimas, QR kodai, Google Drive integracija
- Asmenybės teiginiai, priežasties aiškinimai, "tu esi/tapai" formuluotės — griežtai vengta visur

---

## Atlikti testai

| Sluoksnis | Testavimo būdas | Statusas |
|---|---|---|
| Pagrindinis srautas (A–D) | Realus vartotojo testavimas keliais naršyklėmis | ✅ |
| Radaro geometrija (E/E.1) | Rankinis matematikos patikrinimas + realus screenshot | ✅ |
| Palyginimas (F) | Formulės patikra principu | ✅ (logika), dar nepatikrinta realiu 6+ sesijų scenarijum po paskutinių pataisymų |
| Eksportas/importas (H) | **Realus testas 2 naršyklėse** — tuščia→pilna, dublikatai, santrauka | ✅ |

---

## Žinomos techninės pastabos ateičiai

- **Chrome mobile** turėjo pasikartojančias viewport/layout problemas (žr. Claude atmintį) — dabartinė versija naudoja natūralų document flow, sprendžia daugumą atvejų, bet nebuvo išsamiai retestuota Chrome po paskutinių pakeitimų
- **G etapo cue→tema žemėlapis** paruoštas ir patvirtintas tekste, bet neįdiegtas kode — jei grąžinamas, būtina dar kartą sutikrinti su gyvu `pair-cue-v0.1.json` katalogu prieš keliant

---

## Atviri klausimai (atsakys išorinis testas)

1. Ar žmogus supranta, ką daryti kiekviename žingsnyje be papildomo paaiškinimo?
2. Ar žmogus nori įvardyti savo pastebėjimą, ar dažniausiai renkasi "Kol kas neįvardysiu"?
3. Ar istorijos peržiūra padeda prisiminti ankstesnes reakcijas, ar lieka nepastebėta?
4. Ar radaras suteikia prasmės savaime, be paaiškinimo, ar atrodo tik "gražus piešinys"?
5. Ar žmogus norėtų grįžti ir atlikti dar vieną sesiją savanoriškai?

## Sprendimas po testo

Remiantis atsakymais į aukščiau esančius klausimus:
- **Tęsti Pair P0** — jei atsakymai teigiami, grąžinti G etapą, pridėti daugiau stimulų porų
- **Keisti refleksijos mechaniką** — jei žmonės nesupranta arba nenori įvardyti
- **Atsisakyti radaro** — jei jis nesuteikia prasmės be paaiškinimo
- **Grįžti prie pagrindinio ConflictLab produkto** — jei P0 hipotezė (poros vietoj tiesioginių klausimų) nepasitvirtina apskritai
