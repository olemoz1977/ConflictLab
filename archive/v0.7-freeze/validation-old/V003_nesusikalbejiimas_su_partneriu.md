# Validacijos Scenarijus V003
# "Nesusikalbėjimas su partneriu"

**Kodas:** V003
**Kalba:** Lietuvių
**Kontekstas:** Asmeniniai santykiai
**Hipotezė:** H004 — vengiantis prisirišimas ir emocinis atsiribojimas
**Statusas:** 🟡 Laukiama žmogaus grįžtamojo ryšio

---

## Situacijos aprašymas

Po ilgos darbo dienos partneris nori kalbėti apie tai, kas jį jaudina. Žmogus jaučiasi išsekęs ir nenori gilintis į emocines temas.

---

## Stimulai

| ID | Modalija | Aprašas |
|---|---|---|
| STIM_AUD_003 | Audio | Emociškai įtempta, prašanti intonacija (pseudokalba) |
| STIM_VIS_003 | Visual | Dvi figūros — viena artėja, kita nejuda |
| STIM_SCEN_003 | Scenario | "Partneris sako: 'Mums reikia pasikalbėti.' Tu labai pavargęs." |

---

## Laukiami signalų vektoriai

```json
{
  "approach_withdrawal": -0.65,
  "control_release": -0.30,
  "certainty_seeking": -0.40
}
```

**Pastaba:** certainty_seeking = -0.40 reiškia tolerancijos neapibrėžtumui signalą — vengiantis stilius dažnai vengia emocinio aiškumo, o ne jo ieško.

---

## Taikomi teoriniai rėmeliai

- **AT-001** Attachment Theory — vengiantis stilius (pirminė)
- **ER-001** Gross Emotion Regulation — situacijos vengimas
- **ST-001** Schema Theory — emocinio atsiribojimo schema

---

## Laukiamas neapibrėžtumo profilis

| Dimensija | Laukiama reikšmė | Priežastis |
|---|---|---|
| data_insufficiency | 0.50 | 3 stebėjimai |
| signal_conflict | 0.15–0.25 | Tikimasi nuoseklaus atsitraukimo signalo |
| source_diversity_gap | 0.10 | 3 modalijos |
| temporal_instability | 0.20 | Viena sesija |
| model_assumption_gap | 0.15 | AT-001 aukštas patikimumas |

**Svarbi pastaba:** Nuovargis yra alternatyvus paaiškinimas, kurį AT-001 neatskiria nuo vengimo. Tai turi atsispindėti `uncertainty_note`.

---

## Pavyzdinis ReflectionContract

```json
{
  "observation": "Visuose 3 stimuluose užfiksuotas aiškus atsitraukimo signalas. Reakcijos laikas: audio 1050ms, vizualinis 880ms, scenarijus 2800ms. Scenarijaus atsakas greitesnis nei tikėtasi — galimas automatinis vengimo modelis.",
  "context": "Sesija V003 | H004 | Modalijos: audio, vizualinė, scenarijus",
  "uncertainty_note": "Šis scenarijus sujungia du veiksnius: emocinę temą IR nuovargį. Sistema negali atskirti, kuri priežastis dominuoja. AT-001 interpretuoja atsitraukimą per prisirišimo istorijos lęšį — bet nuovargis yra lygiai tikėtinas paaiškinimas. Refleksija yra tentative.",
  "reflection_question": "Kai išgirdai 'mums reikia pasikalbėti' — kas pirma: mintis apie tai, ko norėtum šiuo metu, ar jausmas dėl to, ko partneris gali norėti?",
  "model_context": {
    "framework": "AT-001 — Attachment Theory",
    "confidence_level": "high",
    "assumptions_applied": ["Emocinis atsiribojimas gali atspindėti vengiančio stiliaus modelį"]
  },
  "reflection_scope": {
    "valid_for": "Trys stimulai šioje sesijoje — nuovargis + emocinis prašymas",
    "not_valid_for": "Asmens santykiai su partneriu, bendra komunikacijos kokybė"
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
- [ ] Tai buvo tik nuovargis, ne vengimas
- [ ] Teorinis rėmelis netiko
- [ ] Scenarijus nerealistinis

### Nesutarimo pastabos (laisvas tekstas)
```
[čia įrašomas žmogaus komentaras]
```

### Kokia teorija būtų tikslesnė?
```
[pvz. ER-001 — situacijos vengimas dėl resursų trūkumo]
```

---

## Modelio prielaidų spragų stebėjimas

| Prielaida | Ar tiko? | Pastaba |
|---|---|---|
| Atsitraukimas = vengimo modelis (ne nuovargis) | ☐ Taip ☐ Ne | |
| AT-001 taikytinas romantiniuose santykiuose | ☐ Taip ☐ Ne | |
| Greita reakcija = automatinis modelis | ☐ Taip ☐ Ne | |

---

## Validacijos istorija

| Data | Testeris | Rezultatas |
|---|---|---|
| — | — | Laukiama |
