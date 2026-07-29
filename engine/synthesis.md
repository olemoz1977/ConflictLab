# Synthesizer Engine (Įžvalgų ir Refleksijos Generatorius)

**Versija:** 2.0  
**Paskirtis:** Apibrėžti nuostatas ir taisykles, kaip matematiniai `/model` duomenys ($Confidence \ge 0.80$, trianguliacija per 3 medijas, latency $\Delta t$) konvertuojami į žmogišką, empatišką, vidinį valdymo lokusą grąžinančią įžvalgą (**Reflection Mirror**).

---

## 🏗️ Sintetinimo Logika (Translation Logic)

Duomenų srautas iš skaičių į kalbą vyksta pagal šią formulę:

$$\text{Triangulated Model Data} \longrightarrow \text{Theory Mapping} \longrightarrow \text{Locus Shift} \longrightarrow \text{Reflection Mirror}$$

---

## 📐 4 Kertiniai Įžvalgos Formavimo Statramsčiai

Kiekviena sugeneruota išvestis privalo susidėti iš 4 elementų:

### 1. Objektyvus Stebėjimas (Observation - Zero Judgement)
- **Taisyklė:** Remiamasi TIK faktais ir laiko matmenimis. Nėra teisiančių žodžių.
- **Pavyzdys:** *„Trijuose skirtinguose žaidimuose (paveikslėlyje ir balso įraše) tavo reakcijos laikas buvo mažesnis nei 1.3 sek., ir visus tris kartus pasirinkai atsitraukimą.“*

### 2. Teorinis Sustiprinimas (Theoretical Context)
- **Taisyklė:** Paaiškinama, ką tai reiškia autonominės nervų sistemos ar SCARF lygmenyje, nenaudojant klinikinio žargono.
- **Pavyzdys:** *„Tai rodo, kad tavo nervų sistema neapibrėžtą toną atpažįsta kaip staigią grėsmę saugumui arba santykiui, todėl kūnas automatiškai įjungia apsauginį pasitraukimo mechanizmą.“*

### 3. Valdymo Lokuso Perjungimas (Locus Shift)
- **Taisyklė:** Pervadinti patirtį iš išorinio lokuso („mane atstumia“) į vidinį lokusą („aš jaučiu norą trauktis, kai...“).
- **Pavyzdys:** *„Ne pats balso tonas tave atstumia, o tavo automatinė interpretacija, kad šaltumas reiškia atmetimą.“*

### 4. Saugus Elgesio Eksperimentas (Micro-Behavioral Experiment)
- **Taisyklė:** Pasiūlyti mažą, saugų veiksmą realybėje, kuris tikrina naują elgesio alternatyvą.
- **Pavyzdys:** *„Kito pokalbio metu, kai pajusi norą atsitraukti, padaryk 3 sekundžių pauzę ir paklausk neutralaus klausimo: 'Ar gali patikslinti, ką turėjai omenyje?'.“*

---

## 💬 Kalbos ir Stiliaus Taisyklės (Tone & Voice Guidelines)

1. **Ne Etiketė, o Veidrodis:**
   - ❌ *„Tu esi vengiančio tipo asmenybė.“*
   - ✅ *„Pastebimas pasikartojantis atsitraukimo modelis, kai situacijoje trūksta aiškumo.“*
2. **Kvietimas Tyrinėti (Inquiry):**
   - Kiekviena įžvalga turi baigtis atviru klausimu, perduodančiu autorystę vartotojui (*„Kaip šis dėsningumas reiškiasi tavo darbe ar asmeniniame gyvenime?“*).
3. **Prieštaravimų Refreiminimas:**
   - Jei `/model/contradiction_rules.md` užfiksavo skirtumą tarp greitos ir lėtos reakcijos:
   - ✅ *„Tavo pirmoji, reakcija rodo norą atsitraukti, tačiau ilgiau pamąstęs renkiesi atvirą dialogą. Tai rodo tavo siekį būti konstruktyviam, nors pirminė emocija jaučia grėsmę.“*

---

## 📊 Išvesties JSON Šablonas (Engine Output Specification)

```json
{
  "synthesis_id": "SYN_99201",
  "hypothesis_ref": "H002",
  "confidence_score": 0.84,
  "reflection_mirror": {
    "observation_statement": "Pastarosiose 3 situacijose tavo pasirinkimo greitis buvo < 1.3 s., ir tu visus kartus pasirinkai pasyvų pasitraukimą.",
    "neuro_explanation": "Kūnas reaguoja į dviprasmiškumą kaip į grėsmę santykiui (SCARF Relatedness threat).",
    "locus_shift_statement": "Reakciją valdo ne kitas asmuo, o tavo vidinis noras apsisaugoti nuo galimo atstumimo.",
    "reflection_question": "Ar pastebi, kad kasdienybėje dažniau pasitrauki dar iki tam tapus tikra problema?",
    "behavioral_experiment": "Sekantį kartą, kai pajusi impulsą atsitraukti, išbūk pauzėje 3 sekundes ir užduok neutralų klausimą."
  }
}
