# Nesutarimų Stebėjimo Žurnalas
# Disagreement Tracking Log

**ConflictLab v0.4.0-RC1**
**Tikslas:** Kiekvienas nesutarimas su refleksija yra episteminis signalas, ne klaida.

---

## Kodėl nesutarimai yra vertingiausi duomenys

Kai žmogus nesutinka su refleksija, sistema sužino:

1. **model_assumption_gap** — teorijos prielaidos netiko šiam kontekstui
2. **signal_conflict** — signalas buvo interpretuotas klaidingai
3. **source_diversity_gap** — trūko kitų modalijų patikrinimui
4. **data_insufficiency** — per mažai stebėjimų išvadai

Kiekvienas nesutarimas → atnaujinamas `ModelRegistry` teorijos `non_applicable` laukas.

---

## Nesutarimų žurnalas

| ID | Scenarijus | Kontraktas | Data | Nesutarimo priežastis | Kuris rėmelis | Veiksmas |
|---|---|---|---|---|---|---|
| D001 | V001 | ref_e3a947f23f9b | 2026-07-29 | "Nebuvo atmetimo baimės — galvojau apie žinutės formuluotę" | AT-001 | SC-001 kaip alternatyva? |
| — | — | — | — | — | — | — |

---

## Nesutarimų analizės šablonas

### Nesutarimas: D___

**Scenarijus:** V___
**Kontraktas:** ref\_\_\_
**Data:** YYYY-MM-DD

**Žmogaus komentaras:**
```
[laisvas tekstas]
```

**Paveikta prielaida:**
```
[kuri FrameworkEntry.assumption netiko]
```

**Alternatyvus paaiškinimas:**
```
[ką žmogus siūlo kaip tikslesnį]
```

**Sistemos atsakas:**
- [ ] Atnaujinti `model_assumption_gap` ribas šiam kontekstui
- [ ] Pridėti `non_applicable` įrašą į atitinkamą FrameworkEntry
- [ ] Sukurti naują scenarijų su šia alternatyva
- [ ] Peržiūrėti `SignalOrientation` ašių reikšmes

---

## Resonance / Disagreement santykis

| Scenarijus | Rezonansai | Nesutarimai | Santykis |
|---|---|---|---|
| V001 | 0 | 1 | 0:1 — SC-001 gali tikti geriau |
| V002 | — | — | — |
| V003 | — | — | — |

---

## Modelio prielaidų spragų suvestinė

| Rėmelis | Dažniausiai nepasiteisina | Kontekstas |
|---|---|---|
| AT-001 | Nuovargis vs. vengimas | Darbas po ilgos dienos |
| SC-001 | Asmeniniai santykiai | Ne organizacinis kontekstas |
| PV-001 | Visi kontekstai | Ginčytinos prielaidos |

---

## Kas keičiasi po kiekvieno nesutarimo

Nesutarimas nekeičia:
- Jokio esamo įvykio
- Jokio esamo kontrakto

Nesutarimas prideda:
- Naują `PERSON_DISAGREED` įvykį `EventLog`
- Naują eilutę šiame žurnale
- Galimą `non_applicable` papildymą `ModelRegistry`

**Immutability principle:** praeitis nesikeičia. Tik ateitis mokosi.
