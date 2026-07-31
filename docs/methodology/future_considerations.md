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

---

## FC-003: Simetrijos efektas (Symmetry Effect)

**Pastebėta:** ST-002 v2 audito metu (2026-07-30)
**Šaltinis:** Nepriklausomas auditas

**Aprašas:**
Kai dvi figūros yra beveik veidrodinės (simetriškos), žiūrovas gali reaguoti į estetinį "dviejų vienodų objektų" suvokimą, o ne į tarpusavio sąveikos dinamiką. Nedidelis figūrų asimetrija (laikysena, galvos kampas, atstumas) gali sukurti natūralesnį efektą neprarandant neutralumo.

**ST-002 pavyzdys:**
Abstrakčios figūros yra beveik identiškos formos ir laikysenos. Tai gali skatinti estetinę, o ne situacinę reakciją.

**Skirtumas nuo esamų kriterijų:**
Nėra tiesiogiai aprėptas Protocol — susijęs su V1.1 (neutralumas), bet specifinis figūrų kompozicijai.

**Stebėjimų skaičius:** 1/3
**Statusas:** Stebima


---

## FC-004 — Attention Anchors Research

**Data:** 2026-07-31
**Statusas:** Research — ne Beta, ne MVP
**Prioritetas:** v2.0

### Hipotezė

Ar spontaniškai pasirinktas dėmesio objektas (vizualinis elementas vaizde) gali būti ankstyvesnis ir patikimesnis signalas nei reakcijos aprašymas?

### Kontekstas

ConflictLab šiandien matuoja: **žmogaus pasirinktą reakciją į stimulą.**

Attention Anchors matuotų: **vizualinį dėmesį prieš interpretaciją.**

Tai yra skirtinga architektūra — ne geresnis ar blogesnis metodas, bet kita hipotezė:

```
Dabar:   Stimulas → reakcija → pasirinkimas → SignalOrientation
Anchors: Stimulas → vizualinis dėmesys → interpretacija → pasirinkimas → SignalOrientation
```

### Kodėl atidedame

1. **Episteminė problema:** "siluetas → aw:-0.55" yra spėjimas, ne kalibruotas ryšys. ConflictLab buvo kuriamas kad sistema kuo mažiau spėliotų.

2. **Nauja kalibravimo metodika:** svoriai buvo kalibruoti pagal reakcijų aprašymus. Anchors reikalauja atskiro validacijos etapo.

3. **Skirtinga grandinė:** tai nėra polish — tai yra naujas SignalOrientation žemėlapis.

### Kas reikalinga prieš tęsiant

- Nauja signalų kalibravimo metodika (kaip priskirti aw/cs/cr fiziniam vaizdo elementui)
- Atskiras validacijos etapas su bent 50 sesijomis
- Tikėtina naujas stimulus bibliotekos kūrimo principas

### Ryšys su beta

Beta vyksta su B variantu (attention cues — trumpos frazės).
FC-004 gali tapti atskiru tyrimu po beta duomenų analizės.


---

## FC-005 — Stimulus Design Standard

**Data:** 2026-07-31
**Statusas:** Planuojama — prieš bibliotekos plėtimą virš 15 stimulų
**Prioritetas:** Prieš v2.0 bibliotekos plėtrą

### Tikslas

Net geriausi cues neišgelbės prasto stimulo.
Stimulus Design Standard apibrėš kokie vaizdai apskritai tinka ConflictLab.

### Klausimai, į kuriuos turi atsakyti dokumentas

**Vaizdo struktūra:**
- Kiek objektų gali būti viename stimule?
- Kiek vizualinio triukšmo leidžiama?
- Koks optimalus detalumo lygis?

**Žmonės vaizde:**
- Kiek žmonių? (0, 1, 2, grupė)
- Ar veidas matomas? Ar nugara?
- Ar lytis/amžius/rasė neutralūs?

**Dviprasmybė:**
- Koks minimalus interpretacijos erdvės kiekis?
- Kaip išvengti vienos dominuojančios istorijos?
- Micro-pause potencialas — kaip jį įvertinti?

**Techniniai apribojimai:**
- Tekstas vaizde — draudžiamas (AI artefaktai, kulturinis šališkumas)
- Spalvų schema — neutrali ar specifinė?
- Kadravimas, kampas, apšvietimas

### Ryšys su Stimulus Language Standard

F6 (Visual Fidelity) reikalauja, kad cues atitiktų tai, kas matoma.
Stimulus Design Standard apibrėš, **kas turi būti matoma**.

Abu dokumentai kartu sudaro pilną stimulus kūrimo metodiką.

### Kada kurti

Po beta etapo — kai bus empirinių duomenų apie tai:
- Kurie stimulai sukelia stipriausią micro-pause
- Kurie generuoja daugiausia AHA momentų
- Kurie dažniausiai sulaukia "Ne, čia kitaip" atsakymų
