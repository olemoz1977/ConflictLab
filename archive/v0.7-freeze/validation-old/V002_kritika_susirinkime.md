# Validacijos Scenarijus V002
# "Kritika susirinkime"

**Kodas:** V002
**Kalba:** Lietuvių
**Kontekstas:** Darbo aplinka — komandos susirinkimas
**Hipotezė:** H001 — pasikartojantys reakcijų modeliai streso situacijose
**Statusas:** 🟡 Laukiama žmogaus grįžtamojo ryšio

---

## Situacijos aprašymas

Susirinkimo metu viršininkas paminėjo, kad ataskaitoje yra dvi klaidos — prieš visą komandą. Žmogus to nesitikėjo.

---

## Stimulai

| ID | Modalija | Aprašas |
|---|---|---|
| STIM_AUD_002 | Audio | Autoritarinis balso tonas, pakylėtas garsas (pseudokalba) |
| STIM_VIS_002 | Visual | Figūra centre, kitos figūros žiūri į ją |
| STIM_SCEN_002 | Scenario | "Viršininkas susirinkime pasakė, kad tavo ataskaitoje yra klaidos." |

---

## Laukiami signalų vektoriai

```json
{
  "approach_withdrawal": -0.40,
  "control_release": -0.60,
  "certainty_seeking": +0.55
}
```

**Pastaba:** control_release = -0.60 reiškia signalą **release** kryptimi — galimas paralyžiaus / sustingimo atsakas, o ne kontrolės siekimas.

---

## Taikomi teoriniai rėmeliai

- **SC-001** SCARF — Status ir Fairness grėsmė (pirminė)
- **CD-001** Cognitive Distortions — personalizavimas, katastrofizavimas
- **DP-001** Dual Process — greita System 1 reakcija (gėda/gynyba)

---

## Laukiamas neapibrėžtumo profilis

| Dimensija | Laukiama reikšmė | Priežastis |
|---|---|---|
| data_insufficiency | 0.50 | 3 stebėjimai |
| signal_conflict | 0.20–0.35 | Tikimasi nuoseklesnio signalo nei V001 |
| source_diversity_gap | 0.10 | 3 modalijos |
| temporal_instability | 0.20 | Viena sesija |
| model_assumption_gap | 0.40 | SC-001 vidutinis patikimumas |

---

## Pavyzdinis ReflectionContract

```json
{
  "observation": "Visuose 3 stimuluose užfiksuotas atsitraukimo ir kontrolės atsisakymo signalas. Reakcijos laikas: audio 890ms, vizualinis 760ms, scenarijus 5100ms. Lėtas scenarijaus atsakas gali rodyti kognityvinio peržiūrėjimo bandymą.",
  "context": "Sesija V002 | H001 | Modalijos: audio, vizualinė, scenarijus",
  "uncertainty_note": "SC-001 prielaidos apie statuso grėsmę gali netikti — kitos interpretacijos įmanomos (pvz., nuovargis, laiko spaudimas, tikras susirūpinimas dėl klaidos). Viena sesija neatskleidžia, ar tai pasikartojantis dėsningumas.",
  "reflection_question": "Kai išgirdai, kad ataskaitoje yra klaidos — kas pirmiausia šovė į galvą, ir kiek laiko praėjo prieš tau pradedant galvoti apie tai, ką atsakyti?",
  "model_context": {
    "framework": "SC-001 — SCARF Model",
    "confidence_level": "medium",
    "assumptions_applied": ["Viešas klaidos paminėjimas aktyvuoja statuso grėsmę"]
  },
  "reflection_scope": {
    "valid_for": "Trys stimulai šioje sesijoje, susirinkimo kontekstas",
    "not_valid_for": "Asmens bendras santykis su kritika ar su šiuo viršininku"
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
[pvz. CD-001 — personalizavimas, o ne statuso grėsmė]
```

---

## Modelio prielaidų spragų stebėjimas

| Prielaida | Ar tiko? | Pastaba |
|---|---|---|
| Viešas komentaras = statuso grėsmė | ☐ Taip ☐ Ne | |
| Greita reakcija = nesąmoninga | ☐ Taip ☐ Ne | |
| SC-001 taikytinas hierarchijos kontekste | ☐ Taip ☐ Ne | |

---

## Validacijos istorija

| Data | Testeris | Rezultatas |
|---|---|---|
| — | — | Laukiama |
