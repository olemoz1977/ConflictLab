# Validacijos Scenarijus V001
# "Neatsakyta žinutė"

**Kodas:** V001
**Kalba:** Lietuvių
**Kontekstas:** Darbo aplinka
**Hipotezė:** H002 — nerimastingo prisirišimo ir dviprasmiškų signalų interpretacija
**Statusas:** 🟡 Laukiama žmogaus grįžtamojo ryšio

---

## Situacijos aprašymas

Žmogus išsiuntė svarbų pasiūlymą kolegai. Kolega peržiūri žinutę (matosi "skaitytas" statusas), bet neatsako 4 valandas.

---

## Stimulai

| ID | Modalija | Aprašas |
|---|---|---|
| STIM_AUD_001 | Audio | Šaltas, lygus balso tonas (pseudokalba, 3 sek.) |
| STIM_VIS_001 | Visual | Dvi figūros — viena atsisuka |
| STIM_SCEN_001 | Scenario | "Išsiuntei pasiūlymą. Kolega matė. Neatsako 4 val." |

---

## Laukiami signalų vektoriai

```json
{
  "approach_withdrawal": -0.55,
  "control_release": +0.30,
  "certainty_seeking": +0.70
}
```

---

## Taikomi teoriniai rėmeliai

- **AT-001** Attachment Theory — pirminė hipotezė
- **SC-001** SCARF — alternatyva (Relatedness threat)
- **CD-001** Cognitive Distortions — mind reading galimybė

---

## Laukiamas neapibrėžtumo profilis

| Dimensija | Laukiama reikšmė | Priežastis |
|---|---|---|
| data_insufficiency | 0.50 | 3 stebėjimai — pakankama tentative signalui |
| signal_conflict | 0.40–0.50 | Scenarijuje galimas priešingas signalas |
| source_diversity_gap | 0.10 | 3 modalijos — trianguliacija įvykdyta |
| temporal_instability | 0.20 | Viena sesija — negalima vertinti stabilumo |
| model_assumption_gap | 0.15 | AT-001 aukštas patikimumas |

---

## Pavyzdinis ReflectionContract

```json
{
  "observation": "2 iš 3 stimulų (audio ir vizualinis) užfiksuotas atsitraukimo signalas, reakcijos laikas < 1.1 sek. Scenarijuje (4.2 sek.) pasirinkta nedelsiant rašyti patikslinimą.",
  "context": "Sesija V001 | H002 | Modalijos: audio, vizualinė, scenarijus",
  "uncertainty_note": "Refleksija paremta 3 stebėjimais iš vienos sesijos. Greiti atsitraukimo signalai gali atspindėti konkrečius stimulus, o ne pasikartojantį dėsningumą. Scenarijaus atsakas (lėtesnis, konstruktyvus) rodo galimą kognityvinio valdymo elementą, kurio AT-001 nepaaiškina.",
  "reflection_question": "Kai pastebėjai impulsą interpretuoti tylą kaip atmetimą — kas tuo metu vyko tavyje ir kas paskatino vis tiek rašyti?",
  "model_context": {
    "framework": "AT-001 — Attachment Theory",
    "confidence_level": "high",
    "assumptions_applied": ["Dviprasmiški signalai interpretuojami per ankstesnių santykių lęšį"]
  },
  "reflection_scope": {
    "valid_for": "Trys konkretūs stimulai šioje sesijoje",
    "not_valid_for": "Bendras asmens elgesio modelis ar santykiai su šiuo kolega"
  }
}
```

---

## Žmogaus grįžtamojo ryšio struktūra

### Rezonansas
- [ ] Refleksija jautėsi tiksli
- [ ] Klausimas buvo prasmingas
- [ ] Neapibrėžtumo pastabos buvo sąžiningos

### Nesutarimas
- [ ] Interpretacija neteisinga
- [ ] Teorinis rėmelis netiko
- [ ] Scenarijus nerealistinis

### Nesutarimo pastabos (laisvas tekstas)
```
[čia įrašomas žmogaus komentaras]
```

### Kokia teorija būtų tikslesnė?
```
[pvz. SC-001 — statuso grėsmė, o ne atmetimo baimė]
```

---

## Modelio prielaidų spragų stebėjimas

Jei žmogus nesutinka — užrašyti:

| Prielaida | Ar tiko? | Pastaba |
|---|---|---|
| Dviprasmiškas signalas = atmetimo baimė | ☐ Taip ☐ Ne | |
| Greita reakcija = nesąmoninga | ☐ Taip ☐ Ne | |
| AT-001 taikytina darbo kontekste | ☐ Taip ☐ Ne | |

---

## Validacijos istorija

| Data | Testeris | Rezultatas |
|---|---|---|
| — | — | Laukiama |
