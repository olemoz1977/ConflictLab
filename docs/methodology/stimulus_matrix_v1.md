# ConflictLab — Stimulus Matrix v1.0

**Data:** 2026-07-30
**Paskirtis:** Bibliotekos planavimo dokumentas. Ne metodologija.
**Principas:** Stimulai kuriami kryptingai, ne atsitiktinai.

---

## Esami stimulai

| ID | Vaizdas | Universali situacija | Ašis | Statusas | Balas |
|---|---|---|---|---|---|
| ST-001 | Žmogus prie lango | Atsitraukimas / laukimas | aw- | review | 76 |
| ST-002 | Dvi abstrakčios figūros | Susitikimas / sąveika | aw+ | beta | 84 |
| ST-003 | Tuščias lapas | Neapibrėžtumas / pradžia | cs- | beta | 84 |
| ST-004 | Telefonas ant stalo | Laukimas atsakymo | cs+ | beta | 83 |
| ST-005 | Tuščias stalas | Laukimas prieš sąveiką | cr- | beta | 80 |
| ST-006 | Žmogus vienas salėje | Vienatvė po grupės | aw- | review | 65 |
| ST-007 | Tuščia konferencijų salė | Pabaiga / pradžia | cr+ | beta | 88 |
| ST-008 | Koridorius | Judėjimas po įvykio | aw- | review | 74 |
| ST-009 | Žmogus prie kompiuterio | Darbas / atsiribojimas | cr+ | beta | 84 |
| ST-010 | Atviros durys | Pasirinkimas / perėjimas | cr- | **approved** | 93 |

---

## Padengtos situacijų klasės

### ✅ Gerai padengta

| Klasė | Stimulai | Pastaba |
|---|---|---|
| Laukimas (socialinis) | ST-004 (telefonas), ST-005 (stalas) | Abu cs ir cr dimensijose |
| Perėjimas / pabaiga | ST-007 (salė), ST-010 (durys) | Abu cr ašyje |
| Vieno žmogaus vidinė erdvė | ST-001 (langas), ST-003 (lapas) | aw- ir cs- |
| Darbas ir koncentracija | ST-009 (kompiuteris) | cr+ |
| Dviejų žmonių sąveika | ST-002 (figūros) | aw+ |

### ⚠ Silpnai padengta

| Klasė | Problema | Rekomendacija |
|---|---|---|
| Atsitraukimas (dinaminis) | ST-008 per institucinis | Pakeisti arba papildyti |
| Vienatvė (socialinis kontekstas) | ST-006 per didelis FC-001 | Pakeisti vaizdą |
| Kontrolė / struktūra | cr+ tik ST-007 ir ST-009 | Pridėti dar vieną cr+ |

### ❌ Nepadengta

| Klasė | Aprašas | Prioritetas |
|---|---|---|
| Konfliktas | Du subjektai aiškioje įtampoje | Aukštas |
| Praradimas | Tuščia erdvė po kažko buvimo | Vidutinis |
| Atsakomybė | Sprendimo momento vaizdas | Vidutinis |
| Gamta / organinė erdvė | Jokio socialinio ar darbo konteksto | Žemas |
| Kūnas / fizinė būsena | Rankos, gestai, poza | Žemas |

---

## Ašių balansas

| Ašis | Stimulai | Procentas | Optimalus |
|---|---|---|---|
| aw | ST-001, ST-002, ST-006, ST-008 | 40% | 33% |
| cs | ST-003, ST-004 | 20% | 33% |
| cr | ST-005, ST-007, ST-009, ST-010 | 40% | 33% |

**Disbalansas:** cs ašis nepakankamai reprezentuota (20% vs. 33%).
**Rekomendacija:** Sekantys 2-3 stimulai turėtų būti cs ašies.

---

## Kontekstų pasiskirstymas

| Kontekstas | Stimulai | Procentas | Tikslas |
|---|---|---|---|
| Darbo aplinka | ST-007, ST-008, ST-009 | 30% | 20-30% ✓ |
| Tarpasmeniniai | ST-002, ST-005, ST-006 | 30% | 20-30% ✓ |
| Vidinė erdvė | ST-001, ST-003, ST-010 | 30% | 15-25% ⚠ |
| Technologinis | ST-004 | 10% | 10-20% ✓ |
| Gamta/abstraktus | — | 0% | 10-20% ❌ |

---

## Micro-pause efekto vertinimas

| Stiprumas | Stimulai |
|---|---|
| ✓✓ Stiprus | ST-007, ST-009, ST-010 |
| ✓ Vidutinis | ST-001, ST-002, ST-004, ST-005, ST-008 |
| ⚠ Silpnas | ST-003, ST-006 |

---

## Prioritetiniai trūkstami stimulai

Sekantys stimulai turėtų būti kuriami šia tvarka:

**1. cs+ su gamtos/abstrakčia aplinka**
- Situacija: neapibrėžtumas be socialinio konteksto
- Pavyzdys: horizontas, kelias į nežinomybę, migla

**2. aw- su konflikto kontekstu**
- Situacija: atsitraukimas nuo konflikto
- Pavyzdys: du subjektai nugaromis vienas kito link

**3. cr+ su atsakomybės momentu**
- Situacija: sprendimo taško vaizdas
- Pavyzdys: ranka ant mygtuko, dokumentas su parašo vieta

**4. cs- su kūrybiniu kontekstu**
- Situacija: neapibrėžtumas kaip galimybė
- Pavyzdys: tuščias drobė, neužpildyta erdvė

---

## Bibliotekos kokybės suvestinė

| Metrika | Reikšmė |
|---|---|
| Iš viso kandidatų | 10 |
| Approved | 1 (ST-010) |
| Beta | 6 (ST-002, ST-003, ST-004, ST-005, ST-007, ST-009) |
| Needs refinement | 3 (ST-001, ST-006, ST-008) |
| Rejected | 0 |
| Vidurkinis balas | 81/100 |
| Stipriausias | ST-010 (93/100) |
| Silpniausias | ST-006 (65/100) |

---

*Stimulus Matrix v1.0 — ConflictLab bibliotekos planavimo dokumentas*
*Atnaujinti po kiekvieno naujo stimulo pridėjimo*
