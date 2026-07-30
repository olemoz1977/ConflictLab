# ConflictLab — Behavior Translation Architecture v1.0

**Data:** 2026-07-31
**Versija:** v1.1 — P9 Trajectory, vidinis klausimas, filosofinis teiginys
**Statusas:** Patvirtinta — laukia implementacijos
**Paskirtis:** Architektūrinis dokumentas. Ne kodas.
**ADR:** ADR-009 — Behavior Translation Engine

---

## Kontekstas

Dabartinė sistema:
```
Stimuli → Signals → Text
```

Problema: "Text" generuojamas tiesiai iš signalų skaičių.
Rezultatas primena testą, ne dialogą.

Nauja architektūra:
```
Stimuli → Signals → Pattern Detection → Behavior Translation → AHA Detection → Result
```

Kiekvienas sluoksnis turi aiškią atsakomybę.
Kiekvienas sluoksnis gali būti testuojamas nepriklausomai.

---

## Pagrindinė filosofija

> ConflictLab nėra psichologas. ConflictLab yra vertėjas.

Sistema verčia signalus į žmogaus patirtį — ne į diagnozę.

**Leidžiama kalbėti apie:**
- Šios sesijos reakcijų kryptį
- Pasikartojančius dėsningumus per sesijas
- Konkretų stimulą ir konkretų pasirinkimą

**Draudžiama:**
- Asmenybės etiketės
- Psichologiniai tipai (MBTI stiliaus)
- Laisva AI interpretacija be signalų pagrindo
- Teiginiai apie žmogų apskritai (ne apie jo reakcijas)

---

## Sluoksnių schema

```
┌─────────────────────────────────────────────────┐
│  STIMULI LAYER (jau veikia)                     │
│  Vaizdas + 3 pasirinkimai + aw/cs/cr svoriai    │
└──────────────────────┬──────────────────────────┘
                       │ raw responses + latencies
┌──────────────────────▼──────────────────────────┐
│  SIGNAL LAYER (jau veikia)                      │
│  aw, cs, cr agregavimas per sesiją              │
│  Latency → confidence proxy                     │
└──────────────────────┬──────────────────────────┘
                       │ signal vectors + metadata
┌──────────────────────▼──────────────────────────┐
│  PATTERN DETECTION LAYER (naujas)               │
│  Aptinka dėsningumus vienos ir kelių sesijų     │
│  kontekste                                      │
└──────────────────────┬──────────────────────────┘
                       │ detected patterns + confidence
┌──────────────────────▼──────────────────────────┐
│  BEHAVIOR TRANSLATION LAYER (naujas)            │
│  Verčia patterns į žmogaus patirties kalbą      │
│  Remiasi Voice v1.0 principais                  │
└──────────────────────┬──────────────────────────┘
                       │ candidate insights
┌──────────────────────▼──────────────────────────┐
│  AHA DETECTION LAYER (naujas)                   │
│  Atrenka tik tas įžvalgas kurios:               │
│  - pagrįstos duomenimis                         │
│  - gali nustebinti                              │
│  - nėra Barnum efektas                          │
└──────────────────────┬──────────────────────────┘
                       │ selected insight(s)
┌──────────────────────▼──────────────────────────┐
│  RESULT LAYER (pagerintas)                      │
│  Viena įžvalga + vienas klausimas               │
│  Per Voice v1.0 filtrą                          │
└─────────────────────────────────────────────────┘
```

---

## 1. Pattern Detection Layer

### Atsakomybė
Aptikti statistiškai ar kokybiškai reikšmingus dėsningumus signalų duomenyse. Ne interpretuoti — tik aptikti.

### Vienos sesijos dėsningumai

**P1 — Krypties stiprumas**
Ar signalas yra stiprus ar silpnas?
```
|signal| > 0.35 → stiprus
|signal| 0.15–0.35 → vidutinis
|signal| < 0.15 → silpnas / neutralus
```

**P2 — Ašių konfliktas**
Ar dvi ašys rodo priešingas kryptis vienu metu?
```
Pvz: aw- + cr+ → atsitraukimas + kontrolės siekimas
(žmogus nori išeiti, bet ir kontroliuoti situaciją)
```
Tai yra informatyviausi momentai — nekeičiami AI fantazija.

**P3 — Latency signalas**
Ar žmogus ilgai delsė prieš pasirinkdamas?
```
latency > 8s → hesitation signal (micro-pause)
latency < 2s → automatic response
latency 2–8s → reflective response
```

**P4 — Šeimos koncentracija**
Ar visi 4 stimulai buvo iš skirtingų šeimų, ar iš panašių?
(Naudoja `family` metaduomenis)

### Kelių sesijų dėsningumai

**P5 — Pasikartojimas**
Ta pati ašies kryptis ≥ 2 iš 3 sesijų.
```
Pvz: cs+ × 3 sesijos → stabilus aiškumo siekimo dėsningumas
```
Minimalus pagrindas: 2 sesijos (ne 1).

**P6 — Kontrastas**
Skirtingos sesijos rodė priešingas kryptis.
```
Pvz: sesija 1 aw- → sesija 2 aw+ → galimas situacinis pokytis
```
Tai NĖRA diagnozė — tai klausimo šaltinis.

**P7 — Paradoksas**
Žmogus nuosekliai renkasi priešingą vieno stimulo reakciją
skirtingomis dienomis.

**P8 — Stabilumas**
Neutralūs signalai visuose trijuose ašyse per kelias sesijas.
Tai nėra "nėra duomenų" — tai yra duomenys.

**P9 — Trajektorija (pokytis)**
Signalas nuosekliai juda viena kryptimi per sesijas.
```
Pvz: S1: aw-0.40 → S2: aw-0.10 → S3: aw+0.25
→ Žmogus juda nuo atsitraukimo link artėjimo
```
Tai NĖRA tas pats kaip P5 (pasikartojimas).
P5 matuoja stabilumą. P9 matuoja judėjimą.
Trajektorija gali būti svarbesnė nei bet kuris atskiras taškas —
nes rodo ne kas žmogus yra, o kas su juo vyksta.

Minimali trajektorijai: 3 sesijos, nuoseklus pokytis ≥ 0.20 per sesiją.

### Išvestis
```json
{
  "session_patterns": ["P1:cs+strong", "P3:hesitation:L07"],
  "cross_session_patterns": ["P5:cs+:2of3"],
  "confidence": {
    "data_sufficiency": 0.6,
    "signal_clarity": 0.8,
    "session_count": 2
  }
}
```

---

## 2. Behavior Translation Layer

### Atsakomybė
Paversti aptiktus pattern'us žmogaus patirties kalba. Ne apibūdinti žmogų — aprašyti tai kas vyko jo reakcijose.

### Vertimo principai

**Principas A — Konkretus, ne abstraktus**
```
❌ "Tavo aw signalas buvo neigiamas"
❌ "Pasireiškė atsitraukimo tendencija"
✅ "Du kartus iš keturių tavo pirmoji mintis buvo eiti nuo situacijos"
```

**Principas B — Situacinis, ne asmeninis**
```
❌ "Tu esi žmogus, kuris vengia artimų kontaktų"
✅ "Šioje sesijoje, kai pasirodė du žmonės veidu į veidą,
    pirmoji mintis buvo apie diskomfortą dėl artumo"
```

**Principas C — Dinaminis, ne statinis**
```
❌ "Tavo profilis rodo kontrolės siekimą"
✅ "Kaskart kai situacija buvo neaišku kas vyksta,
    impulsas krypo link: ką čia galėčiau padaryti?"
```

### Vertimo žodynas

Kiekvienas pattern turi savo vertimo šabloną. Šablonai nėra galutiniai — jie yra pradiniai taškai Claude API promptui.

| Pattern | Šablonas |
|---|---|
| P1 cs+ strong | "Šioje sesijoje pasirodė aiškus impulsas žinoti kas vyksta..." |
| P1 aw- strong | "Šioje sesijoje pirmoji reakcija dažniau krypo nuo, o ne link..." |
| P1 cr+ strong | "Šioje sesijoje impulsas krypo link: ką čia galėčiau padaryti..." |
| P2 aw- + cr+ | "Pasirodė įdomus momentas: norėjosi atsitraukti, bet kartu ir kontroliuoti..." |
| P3 hesitation | "Prie [stimulo] tavo dėmesys sustojo ilgiau..." |
| P5 cs+ repeat | "Tris sesijas iš eilės pasirodė tas pats impulsas — žinoti kas vyksta..." |
| P6 contrast | "Pirmoje sesijoje viena kryptis, šioje — kita. Kas pasikeitė?" |
| P8 stable | "Trijose sesijose signalas buvo neutralus. Tai gali reikšti pusiausvyrą — arba kad stimulai nepasiekė to, kas šiandien svarbu." |

### Vidinis klausimas prieš vertimą

Prieš kiekvieną pattern vertimą sistema turi atsakyti į:

> **"Kodėl šis dėsningumas galėtų būti svarbus šiam žmogui?"**

Šis klausimas nėra rodomas vartotojui.
Jis yra AHA Detection atrankos pagrindas.

```
Pattern: P5 cs+ × 3 sesijos
Vidinis klausimas: Kodėl nuolatinis aiškumo siekimas gali būti svarbu?
  → Galbūt žmogus šiuo metu patiria daug neapibrėžtumo?
  → Galbūt tai yra giliau įsišaknijęs impulsas?
  → Ar tai sutampa su disagreement duomenimis?
Jei atsakymas nėra konkretus → AHA Detection atmes

Pattern: P9 trajectory aw- → aw+
Vidinis klausimas: Kodėl pokytis nuo atsitraukimo link artėjimo gali būti svarbu?
  → Žmogus keičiasi — tai pats retas ir vertingiausias signalas
  → Ar pokytis nuoseklus ar atsitiktinis?
```

Šis vidinis klausimas verčia sistemą ieškoti prasmės,
o ne mechaniškai taikyti šablonus.

### Draudžiami vertimo keliai

Šie pattern'ai NEGALI būti verčiami į teiginius:

| Pattern | Kodėl draudžiama |
|---|---|
| Neutralus vienas kartas | Per mažai duomenų |
| Bet koks 1 sesijos pattern | Situacinis, ne dėsningumas |
| P7 paradoksas | Reikia žmogaus paaiškinimo, ne AI interpretacijos |

---

## 3. AHA Detection Layer

### Atsakomybė
Iš visų candidate insights atrinkti tik tas, kurios atitinka AHA kriterijus. Geriau nerodyti nieko negu rodyti Barnum efektą.

### AHA kriterijai

**K1 — Duomenų pagrindas (būtinas)**
Įžvalga turi būti tiesiogiai paremta aptiktu pattern'u.
```
Leistina: "2 iš 3 sesijų..." (P5 duomenys)
Neleistina: "Tu tikriausiai..." (spėjimas)
```

**K2 — Specifiškumas (būtinas)**
Įžvalga turi būti specifinė šiam žmogui, ne universali.
```
Barnum testas: ar šis sakinys tiktų 80% žmonių?
Jei taip → atmesti.

❌ "Kartais nori pabūti vienam, kartais su kitais"
✅ "3 iš 4 kartų kai pasirodė neapibrėžtumas, pirmoji mintis
    buvo ieškoti struktūros — ne laukti"
```

**K3 — Nustebinimo potencialas (rekomenduojamas)**
Ar ši įžvalga gali pasakyti kažką, ko žmogus pats galbūt nepastebėjo?
```
Mažas nustebinimo potencialas: "Norėjosi pabūti vienas"
  (žmogus pats tai parinko)
Didelis nustebinimas: "Kaskart kai buvo du žmonės vaizdas,
  dėmesys sustojo ilgiau negu ties vieno žmogaus vaizdais"
  (latency duomenys, kurių žmogus neseka)
```

**K4 — Anti-Barnum filtras (būtinas)**
Prieš bet kurią įžvalgą — testas:
```
Ar šis sakinys galėtų atsidurtu horoskope?
Jei taip → perrašyti arba atmesti.
```

### Atrankos logika

```
Candidate insights → K1 filtras → K2 filtras → K4 filtras → Ranked by K3
                                                              ↓
                                                     Rodyti top 1
                                                     (ne daugiau)
```

Viena sesija → maksimaliai 1 įžvalga.
Trys sesijos (pattern) → maksimaliai 1 įžvalga + 1 klausimas.

### Kai nėra AHA

Jei nė vienas candidate nepraeina filtrų → fallback:
```
"Šiandien aiškaus dėsningumo neatsirado.
 Ar yra kažkas, apie ką šiandien galvoji labiau nei paprastai?"
```

Tai nėra nesėkmė — tai sąžiningumas.

---

## 4. Multi-Session Evolution

### Logika (be UI spec)

**Sesija 1 → Observation**
Sistema tik stebi. Nekuria hipotezių.
Rezultatas: vienas stebėjimas + vienas klausimas.

**Sesija 2 → Preliminary signal**
Sistema tikrina ar 1 sesijos pattern kartojasi.
Jei kartojasi → žemas confidence hipotezė.
Jei ne → kontrastas (P6).
Rezultatas: stebėjimas + konteksto pastaba.

**Sesija 3 → Pattern candidate**
Jei pattern matomas 2 iš 3 sesijų → AHA kandidatas (P5).
Jei signalas kinta kryptingai → Trajectory kandidatas (P9).
Jei pattern nestabilus → "Trys sesijos parodė skirtingas kryptis."
Rezultatas: pirmasis multi-session insight (jei AHA praeina filtrus).

> P9 Trajectory yra prioritetinis pattern — nes judėjimas
> dažnai yra informatyvesnis nei stabilumas.

**Sesija 4+ → Pattern confirmation / evolution**
Sistema seka ar pattern stiprėja, silpnėja, ar keičiasi.
Keičiantis pattern'ui → kontrastas tampa nauja įžvalga.

### Multi-session duomenų struktūra

```json
{
  "session_history": [
    {
      "id": 1,
      "ts": 1722340000,
      "axes": {"aw": -0.35, "cs": 0.42, "cr": 0.18},
      "patterns": ["P1:cs+strong", "P3:hesitation:L07"],
      "stimuliUsed": ["L05","L01","L09","L07"],
      "families": ["waiting","withdrawal","work","open_space"],
      "latencies": [4200, 6800, 3100, 11200],
      "feedback": "yes"
    }
  ],
  "cross_patterns": {
    "detected": ["P5:cs+:2of3"],
    "confidence": 0.65,
    "session_count": 3
  }
}
```

---

## 5. Duomenų srautas

```
INPUT per sesiją:
  - stimuliUsed: string[]
  - responses: {stimId, choiceText, aw, cs, cr, latency}[]
  - feedback: 'yes'|'no'
  - disagreementNote?: string

PATTERN DETECTION:
  - Skaičiuoja signal aggregates
  - Lygina su history
  - Generuoja patterns[]

BEHAVIOR TRANSLATION:
  - Parenka šablonus pagal patterns[]
  - Perduoda į Claude API su:
    * aptiktais patterns
    * Voice v1.0 principais
    * draudžiamų teiginių sąrašu
    * latency duomenimis

AHA DETECTION:
  - Tikrina K1-K4
  - Atrenka top 1 candidate
  - Jei nėra → fallback

RESULT:
  - trajectory (iš Behavior Translation)
  - limits (statiškas, iš Voice principų)
  - question (iš AHA Detection)
```

---

## 6. Claude API vaidmuo

### Dabartinė problema
Claude API kviečiamas su skaičiais ir gali generuoti bet ką. Nėra griežtų ribų.

### Nauja funkcija
Claude API yra tik **formuluotės įrankis** — ne interpretacijos variklis.

```
Claude API gauna:
  - Aptiktus patterns (ne skaičius)
  - Konkrečius šablonus (Behavior Translation iš)
  - Voice v1.0 principus
  - Draudžiamų teiginių sąrašą

Claude API NEGALI:
  - Kurti naujų interpretacijų be pattern pagrindo
  - Pridėti psichologinio konteksto
  - Apibendrinti žmogaus asmenybę
```

### Prompt struktūra (spec, ne galutinis)

```
APTIKTI DĖSNINGUMAI: [patterns list]
VERTIMO ŠABLONAS: [iš Behavior Translation Layer]
LATENCY DUOMENYS: [jei P3]

TAISYKLĖS:
- Formuluok tik tai kas aptikta
- Subjektas: reakcija/dėmesys, ne žmogus
- Jokių teiginių apie asmenybę
- Vienas klausimas pabaigoje

DRAUDŽIAMA: [Voice v1.0 draudžiamų frazių sąrašas]

FORMATAS: {"trajectory":"...","limits":"...","question":"..."}
```

---

## 7. Rizikos ir atviri klausimai

### Rizikos

**R1 — Barnum efektas**
Šablonai gali tapti per universalūs.
Valdymas: K2 filtras + reguliari šablonų peržiūra po beta.

**R2 — Pattern over-detection**
Sistema gali "matyti" dėsningumą kur jo nėra (1 sesija).
Valdymas: Minimum 2 sesijos bet kuriam multi-session pattern.

**R3 — Hesitation signal klaidinga interpretacija**
Ilgas latency gali reikšti distrakciją, ne micro-pause.
Valdymas: Latency naudojamas tik kaip papildomas signalas, ne pagrindinis.

**R4 — Feedback loop problema**
Jei žmogus visada spaudžia "Taip, kažką palietė", sistema neturi signal apie klaidus.
Valdymas: Saugoti nesutarimo pastabas kaip atskirą duomenų srautą.

**R5 — Bibliotekos mažumas**
9 stimulai per maži patikimiems cross-session patterns.
Valdymas: Multi-session patterns tik po 10+ stimulų bibliotekos.

### Atviri klausimai

**AK1 — Confidence threshold**
Kokia minimali `data_sufficiency` reikšmė leidžia rodyti multi-session insight?
Siūlymas: 0.5 — bet reikia empirinio testavimo.

**AK2 — Šeimų kontekstas**
Ar Pattern Detection turi žinoti iš kokios šeimos buvo stimulai?
Pvz: cs+ signal iš 'waiting' šeimos ≠ cs+ signal iš 'open_space' šeimos.
Šiuo metu neatskiriama.

**AK3 — Disagreement datos naudojimas**
Kai žmogus sako "Ne, čia kitaip" — ar sistema turi keisti savo modelį?
Šiuo metu feedback saugomas bet nenaudojamas pattern detection.

**AK4 — Latency kaip micro-pause indikatorius**
Kokia latency riba skiria "automatinį pasirinkimą" nuo "tikros pauzės"?
Siūlymas: 8s — bet reikia empirinio patvirtinimo iš beta.

**AK5 — Pattern decay**
Ar senas pattern (prieš 10 sesijų) turi tą pačią svarbą kaip naujas?
Šiuo metu visi sesijos svoriai lygūs.

---

## 8. Implementacijos seka (po patvirtinimo)

Jei architektūra patvirtinama, rekomenduojama tvarka:

1. **Pattern Detection** — JavaScript funkcijos, be UI
2. **Behavior Translation šablonai** — tekstų biblioteka
3. **AHA Detection filtrai** — logikos sluoksnis
4. **Claude API prompt atnaujinimas** — naudoja naują struktūrą
5. **Multi-session evolution** — po beta, kai bus duomenų

**Kas nekeičiama:**
- Voice v1.0
- Stimulus library
- localStorage struktūra (tik plečiama)
- UI ekranai (tik Result ekranas keičiamas)

---

## Santrauka

| Sluoksnis | Kas daro | Kas negali daryti |
|---|---|---|
| Pattern Detection | Aptinka → skaičiuoja | Interpretuoja → vertina |
| Behavior Translation | Verčia → formuluoja | Diagnozuoja → apibūdina žmogų |
| AHA Detection | Atrenka → filtruoja | Prideda → generuoja be pagrindo |
| Result | Rodo → klausia | Teigia → apibrėžia |

> Geriau viena tiksli įžvalga negu penkios universalios.
> Geriau "nėra ką rodyti" negu Barnum efektas.

**Projekto filosofija (ADR-009 pagrindas):**
> *Better no insight than Barnum.*

Ši eilutė yra ne tik techninis sprendimas.
Ji apibrėžia sistemos santykį su žmogumi:
sistema gerbia žmogų pakankamai, kad tylėtų
kai neturi ką pasakyti.

---

*Behavior Translation Architecture v1.0*
*Laukia patvirtinimo prieš implementaciją*
*ConflictLab ADR-009*
