# ConflictLab — Stimulus Matrix v1.0
**Data:** 2026-07-30 | **Statusas:** Užšaldyta po architektūrinio audito
**Versija:** v1.0.1 — redakcinis: pridėti Energija, Kontekstas, Psichologinis momentas

> Šis dokumentas apibrėžia bibliotekos projektavimo kalbą.
> Keičiamas tik kai biblioteka pasiekia 20+ stimulų arba po empirinio testavimo.

---

## Stimulo komponentų struktūra

Kiekvieną stimulą apibūdina **trys lygiai** (skirtingi — ne sinonimiškai):

| Lygis | Klausimas | Pavyzdys |
|---|---|---|
| **Situacija** | Kas vyksta? | Laukimas, Susitikimas, Perėjimas |
| **Kontekstas** | Kur vyksta? | Darbo aplinka, Socialinis, Neutralus |
| **Psichologinis momentas** | Ką žmogus patiria viduje? | Neapibrėžtumas, Sprendimas, Atvirumas |

Ir ketvirtasis parametras:

| Lygis | Klausimas | Skalė |
|---|---|---|
| **Energija** | Kiek stimulas mobilizuoja dėmesį? | L1 (tylu) · L2 (vidutinis) · L3 (intensyvus) |

> Energija nėra emocija. Nėra valentingumas.
> Tai dėmesio mobilizacijos lygis — kiek stimulas "sustabdo" žiūrovą.

---

## Esami stimulai

| ID | Situacija | Kontekstas | Psichologinis momentas | Ašis | Energija | Statusas | Balas |
|---|---|---|---|---|---|---|---|
| ST-001 | Atsitraukimas | Vidinė erdvė | Izoliacija | aw- | L1 | review | 76 |
| ST-002 | Susitikimas | Socialinis | Artumas/įtampa | aw+ | L2 | beta | 84 |
| ST-003 | Neapibrėžtumas | Vidinė erdvė | Tuštuma/galimybė | cs- | L1 | beta | 84 |
| ST-004 | Laukimas | Technologinis | Nerimas/tikrinimas | cs+ | L2 | beta | 83 |
| ST-005 | Laukimas prieš sąveiką | Socialinis | Potencialas | cr- | L1 | beta | 80 |
| ST-006 | Vienatvė | Socialinis | Atskirtis | aw- | L2 | review | 65 |
| ST-007 | Pabaiga/pradžia | Darbo aplinka | Perėjimas | cr+ | L3 | beta | 88 |
| ST-008 | Judėjimas | Darbo aplinka | Atsitraukimas | aw- | L2 | review | 74 |
| ST-009 | Koncentracija | Darbo aplinka | Kontrolė | cr+ | L2 | beta | 84 |
| ST-010 | Pasirinkimas | Neutralus | Sprendimas | cr- | L3 | approved | 93 |

---

## Ašių balansas

| Ašis | Stimulai | % | Optimalus |
|---|---|---|---|
| aw | ST-001, ST-002, ST-006, ST-008 | 40% | 33% |
| cs | ST-003, ST-004 | 20% | 33% ⚠ |
| cr | ST-005, ST-007, ST-009, ST-010 | 40% | 33% |

**Prioritetas:** Sekantys stimulai — cs ašis.

---

## Energijos pasiskirstymas

| Energija | Stimulai | Aprašas |
|---|---|---|
| L1 — Tylu | ST-001, ST-003, ST-005 | Ramūs, kontempliatyvūs. Nedidelis mobilizacijos lygis. |
| L2 — Vidutinis | ST-002, ST-004, ST-006, ST-008, ST-009 | Aiški situacija. Normalus dėmesio lygis. |
| L3 — Intensyvus | ST-007, ST-010 | Stiprus micro-pause efektas. Didelė mobilizacija. |

**Sesijos ritmo pastaba:** Per daug L1 iš eilės sukuria monotoniją. Per daug L3 — nuovargį.
Rekomenduojama sesijos struktūra: L1–L2–L2–L3 arba L2–L1–L2–L3.

---

## Micro-pause rodiklis

> Ar žmogus automatiškai pasirenka atsakymą, ar bent sekundei sustoja?

Šiuo metu vertinama subjektyviai. Ateityje — empiriškai (reakcijos laikas).

| Stiprumas | Stimulai | Pastaba |
|---|---|---|
| ✓✓ Stiprus | ST-007, ST-010 | L3 energija + archetipinis vaizdas |
| ✓ Vidutinis | ST-001, ST-002, ST-004, ST-005, ST-009 | |
| ⚠ Silpnas | ST-003, ST-006 | ST-003 per abstraktus, ST-006 per daug naratyvo |

---

## Kontekstų pasiskirstymas

| Kontekstas | Stimulai | % | Tikslas |
|---|---|---|---|
| Darbo aplinka | ST-007, ST-008, ST-009 | 30% | 20–30% ✓ |
| Socialinis | ST-002, ST-005, ST-006 | 30% | 20–30% ✓ |
| Vidinė erdvė | ST-001, ST-003 | 20% | 15–25% ✓ |
| Technologinis | ST-004 | 10% | 10–20% ✓ |
| Neutralus | ST-010 | 10% | 10–20% ✓ |
| Gamta/organiškas | — | 0% | 10–20% ❌ |

---

## Psichologinių momentų aprėptis

| Momentas | Stimulai | Ar padengta? |
|---|---|---|
| Neapibrėžtumas | ST-003, ST-004 | ✓ |
| Sprendimas | ST-010 | ✓ (tik vienas) |
| Atsitraukimas | ST-001, ST-008 | ✓ |
| Artumas/įtampa | ST-002 | ✓ |
| Kontrolė | ST-009 | ✓ |
| Potencialas | ST-005 | ✓ |
| Perėjimas | ST-007 | ✓ |
| Izoliacija | ST-001, ST-006 | ⚠ du stimulai |
| **Konfliktas** | — | ❌ |
| **Praradimas** | — | ❌ |
| **Neapibrėžtas pasirinkimas** | — | ❌ |

> **Neapibrėžtas pasirinkimas** — situacija kur žmogus nežino kas vyksta,
> bet jaučia kad turi apsispręsti. Galimas cs+cr+ derinys.
> Prioritetinis trūkstamas momentas.

---

## Prioritetiniai trūkstami stimulai

| Prioritetas | Situacija | Kontekstas | Momentas | Ašis | Energija |
|---|---|---|---|---|---|
| 🔴 Aukštas | Neapibrėžtas pasirinkimas | Neutralus | Apsisprendimas be informacijos | cs+cr+ | L3 |
| 🔴 Aukštas | cs ašies stimulas | Gamta | Neapibrėžtumas | cs+ arba cs- | L2 |
| 🟡 Vidutinis | Konfliktas | Socialinis | Įtampa | aw- | L2–L3 |
| 🟡 Vidutinis | Praradimas | Vidinė erdvė | Tuštuma po | cr- | L1 |
| 🟢 Žemas | Organiškas/gamtos kontekstas | Gamta | Ramybė | cr- | L1 |

---

## Bibliotekos kokybės suvestinė

| Metrika | Reikšmė |
|---|---|
| Iš viso stimulų | 10 |
| Approved | 1 — ST-010 (93) |
| Beta | 6 — vidurkis 83/100 |
| Needs refinement | 3 — ST-001, ST-006, ST-008 |
| Rejected | 0 |
| Vidurkinis balas | 81/100 |
| Stipriausias micro-pause | ST-010, ST-007 |
| cs disbalansas | ⚠ 20% (reikia 33%) |

---

## Sesijų ritmo rekomendacijos

Empiriškai nepatikrinta — teorinė rekomendacija.

**4 stimulų sesija:** L1 → L2 → L2 → L3
**Logika:** Pradėti ramiai, leisti žiūrovui įsijungti. Pabaiga su stipriu micro-pause.

**Vengti:** L3 → L3 (per intensyvu), L1 → L1 → L1 (monotonija)

---

*Stimulus Matrix v1.0 — ConflictLab bibliotekos projektavimo kalba*
*Užšaldyta: 2026-07-30. Kitas atnaujinimas: po empirinio testavimo arba 20+ stimulų.*
