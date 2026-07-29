# ConflictLab Analizės Algoritmas (Analysis Pipeline)

**Versija:** 1.0  
**Paskirtis:** Apibrėžti nuoseklų algoritminį procesą, kaip vartotojo pateiktas tekstas (konflikto aprašymas) apdorojamas per `human_model.md` ir pasitelkiant `/theories` modelius sugeneruojama struktūrizuota įžvalga bei transformacijos planas.

---

## 🏗️ Algoritmo schema (Data Flow Overview)

$$\text{Input Text} \longrightarrow \text{Phase 1: Parsing} \longrightarrow \text{Phase 2: Mapping} \longrightarrow \text{Phase 3: Synthesis} \longrightarrow \text{Output JSON/MD}$$

---

## 🔄 Algoritmo Etapai (Pipeline Stages)

### Etapas 1: Situacijos ir Įvykio Parsavimas (Situation Parsing)
**Vykdo:** `engine/situation_parser.md`  
**Atitinka `human_model.md` etapus:** 1–3 (Impulsas, Ankstyvosios patirtys, Fizinė būsena).

1. **Faktų atskyrimas nuo interpretacijų:**
   - Išskiriami objektyvūs įvykiai (*Trigger / Stimulus*) be vertinamųjų žodžių.
   - Nustatomas konfliktinės situacijos intensyvumo lygis (pagal Glasl modelį).
2. **Fiziologinio ir emociškai palaikomo fono detektavimas:**
   - Išteklių stoka: nuovargis, al alkis, laiko spaudimas, chroniškas stresas.

---

### Etapas 2: Trigerių ir Emocijų Indikavimas (Emotion & Trigger Detection)
**Vykdo:** `engine/evidence_mapper.md`  
**Atitinka `human_model.md` etapus:** 4–6 (Nervų sistema, Trigeris, Pirminė reakcija).

1. **Nervų sistemos būsenos nustatymas (Polivagalinė teorija):**
   - *Ventral vagal* (saugumas / ryšys), *Sympathetic* (kova / bėgimas), *Dorsal vagal* (sustingimas / atsiribojimas).
2. **Kūno pojūčių ir afekto granuliarumas (Constructed Emotion Theory):**
   - Bazinio afekto (valentingumas + sužadinimas) išvertimas į tikslias emocijų sąvokas.
3. **Pirminio trigerio atpažinimas (SCARF Modelis):**
   - *Status*, *Certainty*, *Autonomy*, *Relatedness*, *Fairness* grėsmės identifikavimas.

---

### Etapas 3: Interpretacijos Filtro ir Mąstymo Klaidų Diagnostika (Theory Mapping)
**Vykdo:** `engine/theory_selector.md` ir `engine/hypothesis_generator.md`  
**Atitinka `human_model.md` etapus:** 7–10 (Interpretacijos filtras, Mąstymo klaidos, Antrinės emocijos, Elgesio modelis).

1. **Kognityvinių iškraipymų fiksavimas (Cognitive Distortions):**
   - Nustatomos konkrečios mąstymo klaidos (katastrofizavimas, proto skaitymas, privalomumai).
2. **Giliųjų schemų ir prisirišimo aktyvavimo tikrinimas (Schema & Attachment Theory):**
   - Tikrinamos hipotezės **H001**, **H002**, **H004** (ar reaguojama į dabartį, ar į aktyvuotą vaikystės/praeities schemą).
3. **Socialinio vaidmens nustatymas (Karpman & TA):**
   - Vaidmens trikampyje identifikavimas: Auka, Persekiojojas, Gelbėtojas.
   - Ego būsenos nustatymas: Vaikas, Tėvas, Suaugęs.

---

### Etapas 4: Atsakomybės Taškas ir Pervertinimas (Transformation & Synthesis)
**Vykdo:** `engine/synthesis.md` ir `core/transformation_path.md`  
**Atitinka `human_model.md` etapus:** 11–12 (Atsakomybės taškas, Sąmoningas atsakas).

1. **Valdymo lokuso perjungimas (Locus of Control & Hypothesis H003):**
   - Išorinio lokuso teiginių („jis mane supykdė“) reframe'inimas į vidinį lokusą („aš jaučiu pyktį, nes interpretavau...“).
2. **Dėmesio ir refreimingo taikymas (Gross Emotion Regulation):**
   - Kognityvinis situacijos pervertinimas (*reappraisal*).
3. **Konstruktyvaus atsako suformavimas (NVC / Nonviolent Communication):**
   - Formulė: **Faktai** $\rightarrow$ **Jausmai** $\rightarrow$ **Poreikiai** $\rightarrow$ **Prašymas**.

---

## 📊 Išvesties Struktūra (Output Contract / Schema)

Kiekviena analitinė išvestis privalo atitikti šį struktūrizuotą formatą:

```json
{
  "parsed_situation": {
    "objective_facts": "Kolega per susirinkimą pasakė, kad ataskaitoje yra 2 klaidos.",
    "perceived_trigger": "Viešas kompetencijos užginčijimas"
  },
  "neuro_emotional_state": {
    "polyvagal_state": "Sympathetic (Kova / Gynyba)",
    "scarf_threat": ["Status", "Fairness"],
    "identified_emotions": ["Gėda", "Nesaugumas"]
  },
  "cognitive_filter": {
    "cognitive_distortions": ["Mind Reading", "Catastrophizing"],
    "activated_schema": "Gėdos / Defektyvumo schema",
    "karpman_role": "Auka / Atsakomojo persekiojamojo vaidmuo"
  },
  "transformation": {
    "locus_shift": "Nuo 'Jis mane žemina' link 'Aš jaučiu grėsmę savo statusui'",
    "nvc_response": "Kai susirinkimo metu paminėjai klaidas (Faktas), aš pajutau nepatogumą (Jausmas), nes man svarbus profesionalumas (Poreikis). Ar galėtume kitą kartą klaidas peržvelgti prieš susitikimą? (Prašymas)"
  }
}
