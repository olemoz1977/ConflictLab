# ConflictLab — Future Considerations

**Paskirtis:** Fiksuoti pastebėtas metodologines idėjas kurios dar nepakankamos Protocol keitimui.
**Taisyklė:** Šis failas yra stebėjimų žurnalas, ne standartas. Idėja tampa kandidatu į Protocol v1.1 tik kai pasikartoja ≥3 skirtinguose stimuluose.

---

## FC-001: Naratyvinis šališkumas (Narrative Bias)

**Pastebėta:** ST-002 audito metu (2026-07-30)
**Šaltinis:** Nepriklausomas auditas

**Aprašas:**
Kai paveikslėlis labai skatina žmogų kurti istoriją apie pavaizduotų figūrų santykį, pirmoji emocinė reakcija gali būti pakeičiama bandymu suprasti siužetą. Tai skiriasi nuo kultūrinio šališkumo ar lyties signalo.

**ST-002 pavyzdys:**
Du žmonės veidu į veidą koridoriuje sukuria klausimą "koks jų santykis?" — vadovas/darbuotojas, kolegos, pora, derybos. Šis naratyvinis sluoksnis gali nustelbti aw signalą.

**Skirtumas nuo esamų kriterijų:**
- V1.3 (kultūrinis šališkumas) — apie kultūrinį kontekstą
- V1.4 (lyties/statuso signalai) — apie figūrų identitetą
- FC-001 (naratyvinis šališkumas) — apie **santykių dinamikos** interpretaciją, kuri gali atsirasti net neutraliose figūrose

**Potencialus kriterijus ateičiai:**
> Vaizdas neturėtų skatinti žiūrovo kurti santykių naratyvą tarp figūrų, jei tas santykis nėra matuojamo konstrukto dalis.

**Stebėjimų skaičius:** 1/3 (reikia ≥3 prieš svarstant Protocol keitimą)
**Statusas:** Stebima

---

## FC-002: Confidence Score diferenciacija

**Pastebėta:** Architecture Blueprint v1.0 audito metu (2026-07-30)
**Šaltinis:** Gemini auditas

**Aprašas:**
Dabartinė sistema grąžina aw/cs/cr reikšmes bet neatskiria signalo stiprumo nuo signalo patikimumo. Žmogus gali turėti silpną signalą dėl abejingumo (neutrali reakcija) arba dėl prieštaravimo (abi kryptys tuo pačiu metu). Rezultatas tas pats skaičius — bet skirtinga prasmė.

**Potencialus sprendimas ateičiai:**
Kiekvienam signalui pridėti `confidence` dimensiją atskirai nuo `value`:
```yaml
signals:
  aw:
    value: -0.25
    confidence: 0.60  # kiek tikėtina kad šis signalas yra tikras
```

**Stebėjimų skaičius:** 1/3
**Statusas:** Stebima

---

## Pastabos

- Idėjos čia nėra patvirtintos metodologijos dalis
- Jos neturi įtakos dabartiniam validacijos procesui
- Protocol keičiamas tik kai idėja pasikartoja ≥3 stimuluose ir yra aiški taisymo formuluotė
