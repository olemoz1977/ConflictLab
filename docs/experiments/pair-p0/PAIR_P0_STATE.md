# ConflictLab Pair P0 — Būsena (po M0 stable)

**Data:** 2026-08-05
**Stabilus tag:** `pair-p0-m0-remote-beta-stable`
**Tag commit:** `dd3ea6bd444f5f538917fd76f3c6d93c1e44caa7`
**Statusas:** M0 (nuotolinis beta testavimo režimas) pilnai įgyvendintas ir realiai patvirtintas telefone (6/6 QA scenarijų). Kitas žingsnis — N0 (9 porų ir cue balanso auditas).

---

## M0 etapas — nuotolinis beta testavimo režimas

- **Statusas:** implemented and real-device tested (6/6 QA scenarios)
- **Stable tag:** `pair-p0-m0-remote-beta-stable` → commit `dd3ea6bd444f5f538917fd76f3c6d93c1e44caa7`

### Svarbi architektūrinė pastaba dėl commit atsekamumo

Tag'as `pair-p0-m0-remote-beta-stable` nurodo į commit `dd3ea6b`, tačiau šis commit yra **tik dokumentacijos/pavadinimo žymuo be kodo pakeitimų** (tuščias commit, sukurtas pavadinimo aiškumui). **Tikras funkcinis pakeitimas**, kuris suvienodino radaro duomenų šaltinį su pirmomis 3 beta sesijomis, yra commit **`436218282c0de10ad44d8eeb89f0c486de9a8db1`** ("fix(pair-p0): unify radar data source with beta 3-session scope"). Ateityje analizuojant istoriją, logikos atsiradimą reikia sieti su `4362182`, ne su `dd3ea6b`.

### Realiai patikrinti QA scenarijai (6/6)
1. Nebaigtos sesijos atkūrimas (tikslus cue/reflection žingsnis)
2. Discard runtime state pilnas išvalymas
3. P01/P02 dalyvių atskyrimas
4. Radaro peržiūra privaloma prieš interviu (abu keliai — istorija ir pabaigos ekranas)
5. 3 sesijų beta JSON eksportas (patvirtinta su realiais P01, P03 eksportais)
6. J0 duomenų valymas

### Papildomi fix'ai šiame etape
- 3 sesijų kieta riba (niekada "4 iš 3" ar "5 iš 3")
- Radaro eligibility, radaro turinys ir eksportas visi remiasi tuo pačiu pirmų 3 beta sesijų rinkiniu (commit `4362182`)
- LT cue lokalizacija — persiverčia kalbos keitimo metu

---

## Dokumentacijos paketų statusas

### K0 — External Evaluation Pack
- **Statusas:** completed
- **Tag:** `external-review-pack-v1`
- **Commit:** `f6f1c5ee5581ad797473c6ae774912a76880b328`
- **Turinys:** 7 dokumentai `docs/external-review/` — epistemines ribas, Claim Status Matrix, metodo ribotumus, realų srautą, atviras tyrimo temas, vertintojo gaires

### Beta test documentation pack
- **Statusas:** completed
- **Tag:** `pair-p0-beta-test-pack-v1`
- **Commit:** `4fc192342440dca034cb4f1c3a90320b4cf19671`
- **Turinys:** 5 dokumentai `docs/beta-test/` — tester protocol, participant instructions, session observation form, post-test interview (10 pagrindinių klausimų + optional probes), results summary template
- **Test scope:** 5 participants, minimum 3 sessions each
- **Purpose:** usability, epistemic safety, reflection value, return intention
- **Explicit limitation:** this is not a validation study — it is a small usability and reflection-value test

---

## Etapų validacijos statusas

### I etapas — konkretus sesijos atspindys be interpretacijos
- **Statusas:** implemented and real-device tested
- **UX refactor commit:** `abb8e1c19febd2104b2719a784442deb10adc705`
- Pilnai realiai patvirtinta telefone: "Ką pasirinkai šioje sesijoje" blokas, šaltinio prioritetas (žmogaus tekstas > cue > neįvardyta), refleksinis klausimas su trimis atsakymais, vienas bendras CTA (be atskiro "Išsaugoti" mygtuko)

### J0 etapas — saugus vietinių duomenų valymas
- **Statusas:** implemented and real-device tested
- **Commit:** `80ef78431e2b40e9648ef8d5317e2f326ff168ad`
- **A–D testai atlikti realiame telefone:**
  - A — tuščios naršyklės būsena: destruktyvus modalas neatidaromas, rodomas "nėra duomenų" statusas
  - B — completed sesijų valymas: checkbox apsauga, istorija tampa tuščia, sesijos neatsiranda po perkrovimo
  - C — aktyvios sesijos pašalinimas: veikia, aktyvi sesija neatkuriama po perkrovimo
  - D — eksportuoti → išvalyti → importuoti: pilnas ciklas veikia, sesijos grįžta su I etapo refleksijos tekstais
- **E testas (namespace apsauga) patvirtintas logikos lygiu:**
  - `localStorage.clear()` niekur nenaudojamas
  - Valomi tik raktai, prasidedantys `cl_pair_p0_` prefiksu
  - Kito namespace duomenys (v0.7, kiti eksperimentai) apsaugoti

---

## Kas veikia (visas srautas)

### Pagrindinis srautas
- Poros → vaizdo pasirinkimas (latency matavimas, pozicijos randomizacija)
- Cue pasirinkimas (18 standartinių cue, arba "Kita mintis" custom tekstas, arba "Sunku pasakyti")
- Individuali refleksija (iki 5 žodžių, susieta su konkrečiu cue)
- Sesijos refleksija (bendras pastebėjimas po visų 3 vaizdų, arba "Kol kas neįvardysiu")
- **I etapas:** "Ką pasirinkai šioje sesijoje" — konkretus, neinterpretuojamas atspindys
- **I etapas:** refleksinis klausimas apie ryšį tarp pasirinkimų (text/not_seen_yet/prefer_not_to_state)
- Sesijos rezultatas (visi pasirinkimai + abu pastebėjimai + metodinė riba)
- Feedback (4 klausimai apie patirtį)
- Sesijos užbaigimas → `completed_sessions`

### Istorija ir duomenys
- `active_session` / `completed_sessions` atskyrimas
- Istorijos sąrašas + detalus vaizdas kiekvienai sesijai
- **I etapo prioriteto taisyklė:** jei `session_connection_reflection` egzistuoja, senas `session_reflection` istorijoje nerodomas — jokio prieštaravimo tarp senų/naujų tekstų
- Tuščios istorijos paaiškinimas (WebView/naršyklės skirtumo užuomina)

### Radaras (E/E.1 etapai) — nepakeista šiuose etapuose
- 3 tinkamų sesijų reikalavimas, šešių krypčių dvipolė geometrija, netiesinė vizualinė skalė

### Palyginimas (F etapas) — nepakeista šiuose etapuose
- Nuo 6 eligible sesijų — Dabar/Anksčiau periodų palyginimas

### Istorijos eksportas/importas (H etapas) — nepakeista šiuose etapuose
- Švarus eksporto failas, merge pagal `session_id`, dublikatų apsauga

### **J0 etapas — saugus duomenų valymas (naujas)**
- "Duomenų valdymas" blokas istorijos ekrane, vizualiai atskirtas nuo pagrindinių veiksmų
- "Išvalyti šios naršyklės duomenis" ir "Eksportuoti ir išvalyti" — du atskiri veiksmai
- Patvirtinimo modalas su privalomu checkbox prieš galutinį veiksmą
- Aktyvios sesijos perspėjimas (kai yra pasirinkimų)
- Nulinės istorijos informacinis pranešimas be destruktyvaus modalo
- Namespace-saugus valymas: tik `cl_pair_p0_` prefiksas, niekada `localStorage.clear()`

---

## Kas sąmoningai NEĮTRAUKTA į P0

- **G etapas (teminis palyginimas)** — buvo bandytas du kartus, du kartus atmestas dėl klaidingų cue→tema žemėlapių ir realaus UI lūžio. Patvirtinta viena-tema-vienam-cue lentelė paruošta, bet **neįdiegta**
- AI interpretacija ar analizė bet kuriame etape
- Paskyros, prisijungimas, debesies sinchronizacija
- Šifravimas, QR kodai, Google Drive integracija

---

## Žinomos smulkios pastabos

- **J0 testas C:** aktyvios sesijos perspėjimo tekstas rodomas tik jei `SESSION.choices.length > 0`. Jei vartotojas pradėjo sesiją, bet dar nepasirinko nė vienos poros, duomenys vis tiek pašalinami teisingai, bet perspėjimo tekstas šiuo ribiniu atveju nerodomas. Nelaikoma funkciniu defektu.
- **Chrome mobile** — anksčiau turėjo viewport/layout problemų, dabartinė versija (natūralus document flow) sprendžia daugumą atvejų, bet nebuvo išsamiai retestuota Chrome po visų vėlesnių pakeitimų.

---

## Atviri klausimai — laukia K0 (External Evaluation Pack)

1. Ar žmogus supranta, ką daryti kiekviename žingsnyje be papildomo paaiškinimo?
2. Ar žmogus nori įvardyti savo pastebėjimą, ar dažniausiai renkasi "Kol kas neįvardysiu" / "Dar nematau"?
3. Ar istorijos peržiūra padeda prisiminti ankstesnes reakcijas?
4. Ar radaras suteikia prasmės savaime, be paaiškinimo?
5. Ar žmogus norėtų grįžti ir atlikti dar vieną sesiją savanoriškai?

---

## Atvirų klausimų žurnalas — 2026-08-06

### OQ-001: Prototipo vektorių izoliacijos reikalingumas

**Kontekstas:** Prototype-nine-v1 QA metu įdiegta griežta P9/M0 sesijų izoliacija radaro skaičiavime. Vėliau iškilo klausimas — ar ši izoliacija iš viso reikalinga.

**Problema:**
Prototipo vektoriai (`vector_source: "prototype_only"`) yra arbitraliai priskirti skaičiai — ne išmatuoti, ne kalibruoti. Jei jie patenka į tą patį radarą kaip P0 kalibruoti vektoriai, radaras tampa metodologiškai beprasmis tame sraute.

**Kodėl izoliacija gali būti nereikalinga:**
- Viešame produkte N0 poros bus arba patvirtintos (su tikrais vektoriais), arba pašalintos
- Jei visos poros viešame produkte turės kalibruotus vektorius — atskiro prototipo sluoksnio nereikia
- Izoliacija reikalinga tik prototipo etape, kol viename sraute egzistuoja dviejų skirtingų kokybių duomenys

**Kodėl izoliacija gali būti reikalinga:**
- Kol N0 vektoriai nėra kalibruoti, jie neturėtų veikti radaro — nepriklausomai nuo to, ar tai prototipas ar ne
- `analysis_eligible: false` yra metodologinis sprendimas, ne tik techninis žymeklis
- Jei prototipo duomenys patenka į radarą ir vartotojas jais remiasi — tai klaidinantis rezultatas

**Neišspręstas klausimas:**
Ar viešame produkte kada nors bus situacija, kur `analysis_eligible: false` pora egzistuoja kartu su `analysis_eligible: true` poromis tame pačiame sesijų sraute? Jei taip — izoliacija reikalinga. Jei ne — ją galima supaprastinti.

**Statusas:** OPEN — sprendimas atidėtas iki viešo produkto architektūros patvirtinimo.

---

### OQ-002: Prototipo radaro vektorių skaičiaus rodmuo

**Problema:** Po 3 P9 sesijų radaras rodė `„0 vektorinių pasirinkimų"` net kai sesijos buvo užbaigtos su cue pasirinkimais. Priežastis: `valid_vector_responses` skaičiuojamas iš `reviewed` vektorių — prototipo vektoriai į šį skaičių neįeina.

**Įdiegtas taisymas:** Radaro ekrane dabar rodoma `„X įtraukti pasirinkimai (Y peržiūrėti · Z prototipo)"`.

**Dar nepatikrinta rankiniu testu:** ar skaičiai dinamiškai keičiasi, kai vienoje poroje pasirenkama „Sunku pasakyti" (turėtų sumažėti prototipo skaičius).

**Statusas:** CODE FIXED — rankinis testas laukia.
