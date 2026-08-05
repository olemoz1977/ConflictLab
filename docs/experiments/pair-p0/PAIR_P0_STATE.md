# ConflictLab Pair P0 — Būsena (po J0 etapo)

**Data:** 2026-08-05
**Stabilus tag:** `pair-p0-j0-stable`
**Statusas:** I ir J0 etapai realiai patvirtinti telefone. Toliau — K0 (External Evaluation Pack).

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
