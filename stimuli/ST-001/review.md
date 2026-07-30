# ST-001 — Stimulus Review

**Stimulo ID:** ST-001
**Peržiūros data:** 2026-07-30
**Recenzentas:** Claude (ConflictLab v0.6 auditas)
**Remtasi:** `docs/methodology/stimulus_validation_protocol.md` v1.0
**Statusas po peržiūros:** review

---

> ⚠ Šis review užpildomas tik pagal Validation Protocol v1.0.
> Jei review prieštarauja Protocol — taisomas review, o ne Protocol.

---

## V1. Vizualinė validacija

### V1.1 Neutralumas
**Įvertinimas:** 3/5
**Paaiškinimas:** Vaizdas leidžia bent dvi interpretacijas: žmogus laukia, žmogus atsitraukia, žmogus kontempliuoja. Tačiau lietus + nugara sukuria stiprią melancholijos nuotaiką kuri gali dominuoti prieš kitas interpretacijas.
**Rastos problemos:** Estetinis "melancholijos" signalas gali viršyti 20–70% neapibrėžtumo ribą kai kuriose demografinėse grupėse.
**Rekomendacija:** Priimti su žyma `cultural_flag: lietus`

### V1.2 AI artefaktai
**Įvertinimas:** 5/5
**Paaiškinimas:** Vaizdas fotografinis, jokių AI artefaktų. Figūra natūrali, langas tikroviškas, lietaus lašai autentiški.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V1.3 Kultūrinis šališkumas
**Įvertinimas:** 3/5
**Paaiškinimas:** Europiečių kontekstas (langas, miesto vaizdas). Lietaus konotacijos skirtingose kultūrose: Europoje — melancholija; tropikuose — gyvybė, šventė. Gali veikti interpretaciją.
**Rastos problemos:** cultural_flag užfiksuotas `stimulus.yaml`.
**Rekomendacija:** Priimti su žyma

### V1.4 Lyties / amžiaus / statuso signalai
**Įvertinimas:** 4/5
**Paaiškinimas:** Figūra matoma tik nugara, viso ūgio. Lytis neatpažįstama. Amžius neatpažįstamas. Statusas nenurodomas. Lengvas vyriškos figūros įspūdis dėl pečių linijos — bet nekonkretus.
**Rastos problemos:** Pečių linija gali signalizuoti vyriškumą kai kuriems žiūrovams.
**Rekomendacija:** Priimti

### V1.5 Neapibrėžtumo lygis
**Įvertinimas:** 20–70% (optimalus)
**Paaiškinimas:** Trijų variantų pasirinkimas pagrįstas — visi trys galimi kaip tikros pirmosios reakcijos. Neapibrėžtumas pakankamas bet ne per didelis.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

---

## V2. Psichologinė validacija

### V2.1 Reakcija, ne nuomonė
**Įvertinimas:** 3/5
**Paaiškinimas:** A ir B variantai yra tikros pirmosios reakcijos. C variantas "Laukimas — normalu" yra racionalizacija — reikalauja kognityvinės refleksijos, ne momentinės reakcijos.
**Rastos problemos:** C variantas pažeidžia V2.1 kriterijų — tai nuomonė, ne reakcija.
**Rekomendacija:** Perrašyti C variantą. Siūloma: *"Pastebėjau, kad stoviu ir neskubu"* — tai yra stebėjimas, ne vertinimas.

### V2.2 Socialiai pageidaujamas atsakymas
**Įvertinimas:** 4/5
**Paaiškinimas:** A variantas ("pabūti vienam") nėra aiškiai socialiai pageidaujamas. B ("galvojau kas lauke") — neutralus. C ("normalu") — ribinai — žodis "normalu" yra Protocol V2.2 pavojingų žodžių sąraše.
**Rastos problemos:** C variantas turi žodį "normalu" — socialinio pageidaujamumo rizika.
**Rekomendacija:** Perrašyti C variantą (tai šalina ir V2.1 problemą vienu metu).

### V2.3 Moralinis pasirinkimas
**Įvertinimas:** 5/5
**Paaiškinimas:** Nė vienas variantas neturi moralinės konotacijos. "Pabūti vienam", "galvoti kas lauke", "laukimas" — visi moraliniu požiūriu neutralūs.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V2.4 Projekcija į vaizdą
**Įvertinimas:** 5/5
**Paaiškinimas:** Visi trys variantai yra pirmojo asmens reakcijos apie žiūrovą, ne apie figūrą. "Norėjosi pabūti vienam" — žiūrovas, ne figūra.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V2.5 Akivaizdžiai teisingas variantas
**Įvertinimas:** 4/5
**Paaiškinimas:** Nė vienas variantas nėra akivaizdžiai "teisingesnis". Visus tris galima įsivaizduoti kaip tikras reakcijas skirtingų žmonių.
**Rastos problemos:** C variantas ("normalu") yra pats mažiausiai tikėtinas kaip pirma reakcija — bet tai V2.1/V2.2 problema, ne V2.5.
**Rekomendacija:** Priimti (su perrašymu C)

---

## V3. Konstrukto validacija

### V3.1 Pirminė ašis
**Deklaruota ašis:** aw (approach_withdrawal)
**Įvertinimas:** 5/5
**Paaiškinimas:** A variantas aw: -0.55 (stiprus atsitraukimas). B variantas aw: +0.25 (artėjimas). C variantas aw: -0.10 (neutralus). Pirminė ašis dominuoja visuose variantuose.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V3.2 aw/cs/cr diferenciacija
**Įvertinimas:** 4/5
**Paaiškinimas:** aw ir cr nėra supainiotos. A variantas: aw- (atsitraukimas) + cr- (paleidimas) — abu pagrįsti ir dokumentuoti `stimulus.yaml`. Skirtumas tarp aw- ir cr- išlaikomas.
**Rastos problemos:** Ribinis atvejis A variante — bet dokumentuotas pagrindimas priimtinas.
**Rekomendacija:** Priimti

### V3.3 Mišrūs signalai
**Ar yra mišrūs signalai:** Taip (A variantas)
**Paaiškinimas:** A variante cs- (-0.20) ir cr- (-0.30) yra antriniai signalai. Pagrindimas: noras pabūti vienam natūraliai susietas su neapibrėžtumo tolerancija ir kontrolės paleidimu. Pagrindimas dokumentuotas `stimulus.yaml`.
**Rastos problemos:** Nėra — pagrindimas tinkamas.
**Rekomendacija:** Priimti

### V3.4 Variantų svorių simetrija
**Įvertinimas:** 4/5
**Paaiškinimas:** A: aw-0.55 (stiprus minusas). B: aw+0.25 (teigiamas). C: aw-0.10 (silpnas minusas). Yra ir X+ ir X- variantai. Tačiau du variantai aw- pusėje — ribinai.
**Rastos problemos:** Asimetrija — du aw- prieš vieną aw+. Po C varianto perrašymo reikia patikrinti ar svoriai lieka subalansuoti.
**Rekomendacija:** Priimti, bet po C perrašymo patikrinti svorių balansą.

---

## V4. Daugiateorinė validacija

### Teorija 1: Dual Process Theory (Kahneman)
**Validacijos klausimas:** Ar stimulas sukelia momentinę (System 1) reakciją? Ar variantai nereikalauja ilgos refleksijos?
**Įvertinimas:** Abejoja
**Paaiškinimas:** A ir B variantai yra greitų reakcijų kategorijoje. C variantas ("normalu") reikalauja System 2 — žmogus turi suformuoti nuomonę, kad pasakytų "normalu". Tai pažeidžia Dual Process logikoje System 1 reakcijos principą.

### Teorija 2: Attachment Theory (Bowlby/Ainsworth)
**Validacijos klausimas:** Ar stimulas gali aktyvuoti prisirišimo schemas? Ar aw ašis tinkama prisirišimo dinamikai?
**Įvertinimas:** Patvirtina
**Paaiškinimas:** Žmogus prie lango — universali izoliacijos ar laukimo scena. aw ašis tinkama — prisirišimo teorija patvirtina kad atsitraukimas/artėjimas yra prasmingas konstruktas šiame kontekste.

### Teorija 3: Emotion Regulation (Gross)
**Validacijos klausimas:** Ar stimulas provokuoja reguliacijos strategiją? Ar cr ašis aprėpia šį aspektą?
**Įvertinimas:** Patvirtina
**Paaiškinimas:** A variantas (noras pabūti vienam) yra situacijos pasirinkimo reguliacijos strategija — tai patvirtina cr- signalas A variante. Teorija validuoja mišraus signalo pagrindimą.

### Teoriniai prieštaravimai
**Ar yra prieštaravimų:** Taip (ribinis)
**Aprašymas:** Dual Process Theory abejoja C varianto tinkamumu. Attachment ir Emotion Regulation teorijos patvirtina bendrą stimulo struktūrą.
**Rekomendacija:** Priimti su žyma — C varianto perrašymas išspręs Dual Process problemą.

---

## V5. Bibliotekos validacija

### V5.1 Dublikatai
**Ar yra panašių stimulų:** Taip — L01 (identiškas stimulas senoje bibliotekoje)
**Ar konstruktai skiriasi:** Ne — tas pats vaizdas, ta pati ašis
**Rekomendacija:** ST-001 pakeičia L01. L01 archyvuojamas.

### V5.2 Ašių balansas
**Ašių pasiskirstymas po ST-001 pridėjimo (12 stimulų):**
- aw stimulai: 4/12 (33%) — optimalus
- cs stimulai: 4/12 (33%) — optimalus
- cr stimulai: 4/12 (33%) — optimalus

**Ar laikomasi 25–40% ribų:** Taip
**Rekomendacija:** Priimti

### V5.3 Kontekstų įvairovė
**Stimulo kontekstas:** vidine_erdve
**Ar kontekstas per daug reprezentuotas:** Ribinai — keli kiti stimulai taip pat vidinėje erdvėje
**Rekomendacija:** Priimti — kontekstas skiriasi (langas vs. stalas vs. lapas)

---

## V6. Empirinė validacija

*(Nepildyta — stimulas dar nebuvo testuotas su realiais žmonėmis)*

### V6.1 Beta testavimas
**Statusas:** Laukiama

### V6.2 Pilotinis testavimas
**Statusas:** Laukiama

### V6.3 Pašalinimo kriterijai
**Statusas:** Laukiama

---

## Galutinis vertinimas

| Kriterijus | Svoris | Balas | Svertinis |
|---|---|---|---|
| V1.1 Neutralumas | 15% | 3/5 | 9 |
| V1.2 AI artefaktai | 10% | 5/5 | 10 |
| V1.3 Kultūrinis neutralumas | 10% | 3/5 | 6 |
| V1.4 Lyties/statuso neutralumas | 10% | 4/5 | 8 |
| V2.1 Reakcija, ne nuomonė | 15% | 3/5 | 9 |
| V2.2 Socialinis neutralumas | 15% | 4/5 | 12 |
| V3.1 Pirminė ašis | 10% | 5/5 | 10 |
| V3.4 Svorių simetrija | 10% | 4/5 | 8 |
| V4 Teorijų validacija | 5% | 4/5 | 4 |
| **VISO** | **100%** | | **76/100** |

**Minimalus balas: 70/100**
**Gautas balas: 76/100** ✓

**Sprendimas:** Priimti su sąlyga
**Sąlyga:** C variantas turi būti perrašytas prieš perkeliant į `beta` statusą.

**Žymos:**
- `cultural_flag: lietus-melancholija` — patikrinti su ne-europietiška auditorija
- `c_variant_rewrite_required` — dabartinis C neatitinka V2.1 (racionalizacija)
- `replaces: L01` — archyvuojamas senas stimulas

---

*Review užpildyta pagal: `docs/methodology/stimulus_validation_protocol.md` v1.0*
