# ConflictLab Analizės Algoritmas (Analysis Pipeline Spec)

**Versija:** 2.0 (Adaptyvi Multimodalinė Architektūra)  
**Paskirtis:** Apibrėžti nuoseklų algoritminį procesą, kaip spontaniškos vartotojo mikro-reakcijos į multimodalinius stimulus apdorojamos per `/perception`, `/adaptive` ir `/theories` sluoksnius, sugeneruojant patikrintas elgsenos įžvalgas ir transformacijos kelią.

---

## 🏗️ Algoritmo Schema (System Data Flow)

$$\begin{aligned}
\text{Multimodal Stimulus } (\text{/stimuli}) &\longrightarrow \text{Micro-Reaction } (\text{Latency + Choice}) \\
&\longrightarrow \text{Perception Layer } (\text{/perception}) \\
&\longrightarrow \text{Adaptive Loop } (\text{/adaptive}) \quad \text{[Eksperimento Ciklas]} \\
&\longrightarrow \text{Theory & Hypothesis Engine } (\text{/theories}) \\
&\longrightarrow \text{Triangulated Insight } (\text{/engine/synthesis.md})
\end{aligned}$$

---

## 🔄 Algoritmo Etapai (Pipeline Stages)

### Etapas 1: Mikro-Stimulo Pateikimas ir Atsako Fiksavimas (Perception Capture)
**Vykdo:** `perception/feature_extraction.md`  
**Atitinka `human_model.md` etapus:** 1–5 (Impulsas, Ankstyvosios patirtys, Fizinė būsena, Nervų sistema, Trigeris).

1. **Stimulo Tipas (`/stimuli`):** 
   - Vizualinis vaizdas, audio su pseudokalbos intonacija arba 2-sekundžių scenarijus.
2. **Duomenų Išgavimas (Feature Extraction):**
   - **Reakcijos greitis (Latency $\Delta t$):**
     - $\Delta t < 1.5\text{ s} \implies$ Spontaniškas autonominės nervų sistemos atsakas (Amigdala / Polyvagal).
     - $\Delta t > 4.0\text{ s} \implies$ Kognityvinė racionalizacija ir gynybinis filtras.
   - **Pasirinkimo Vektorius:** Pasirinkta reakcija (kova, bėgimas, sustingimas, kontrolė, atsitraukimas).

---

### Etapas 2: Pasikartojančių Dėsningumų Diagnostika (Pattern Detection)
**Vykdo:** `perception/feature_extraction.md` ir `hypotheses/`  
**Atitinka `human_model.md` etapus:** 6–8 (Pirminė reakcija, Interpretacijos filtras, Mąstymo klaidos).

1. **Vektorių Grupavimas:**
   - Sistema lygina naują reakciją su ankstesnių sąveikų istorija.
2. **Hipotezės Aktyvavimas (`/hypotheses`):**
   - Tikrinamos hipotezės (pvz., **H002** neigiamas šališkumas ar **H001** autonomijos praradimas).
   - Apskaičiuojamas hipotezės pasitikėjimo laipsnis ($Confidence\ Score$).

---

### Etapas 3: Adaptyvusis Hipotezės Tikrinimas (Adaptive Targeted Loop)
**Vykdo:** `adaptive/stimulus_selector.md`  
**Atitinka `human_model.md` etapus:** Adaptyvusis interviu.

1. **Hipotezės Tikrinimo Taisyklė (Decision Matrix):**
   - *Jei $Confidence < 0.80$*: `/adaptive` modulis generuoja **kitą tikslinį stimulą** kitoje medijos formoje (pvz., jei prieš tai buvo vaizdas, dabar pateikiama pseudokalbos intonacija).
2. **Trianguliacijos Patikra:**
   - Siekiama patvirtinti dėsningumą per 3 skirtingas medijos formas (Vizualinė $\rightarrow$ Garsinė $\rightarrow$ Tekstinis pasirinkimas).

---

### Etapas 4: Teorinis Susiejimas ir Transformacija (Theory Synthesis)
**Vykdo:** `engine/theory_selector.md` ir `engine/synthesis.md`  
**Atitinka `human_model.md` etapus:** 9–12 (Antrinės emocijos, Elgesio modelis, Atsakomybės taškas, Sąmoningas atsakas).

1. **Mokslinis Žemėlapis (`/theories`):**
   - Kai $Confidence \ge 0.80$, reiškinys susiejamas su teorijomis: Polyvagal (`polyvagal_theory.md`), SCARF (`scarf_model.md`), Karpman trikampiu (`drama_triangle.md`) ar Valdymo lokusu (`locus_of_control.md`).
2. **Valdymo Lokuso Perjungimas (Reframing):**
   - Reakcija paverčiama vidinio lokuso teiginiu: nuo *„mane suerzino intonacija“* iki *„aš pajutau grėsmę statusui, kai balso tonas tapo šaltas“*.
3. **Elgesio Eksperimento Suformavimas:**
   - Sukuriamas mažas, saugus elgesio testas realybėje, plečiantis reagavimo ribas.

---

## 📊 Išvesties JSON Kontraktas (Output Contract)

Gauta analizės išvestis privalo atitikti šį duomenų formatą:

```json
{
  "session_id": "sess_982341",
  "observation": {
    "stimulus_id": "STIM_AUDIO_004",
    "stimulus_type": "audio_fake_language",
    "response_latency_ms": 1180,
    "is_spontaneous": true,
    "selected_option": "passive_withdrawal"
  },
  "triangulation_state": {
    "active_hypothesis": "H002",
    "media_vectors_confirmed": ["visual", "audio"],
    "confidence_score": 0.83
  },
  "theoretical_mapping": {
    "polyvagal_state": "Sympathetic / Freeze",
    "scarf_threat": "Relatedness / Status",
    "activated_schema": "Abandonment / Rejection Sensitivity"
  },
  "reflection_mirror": {
    "locus_shift": "Nuo 'šaltas tonas mane atstumia' link 'aš automatiškai traukiuosi, kai pajaučiu neapibrėžtumą'",
    "mirror_insight": "Pastarosiose 3 situacijose (vaizde ir garso įraše) tavo reakcijos laikas buvo < 1.3 s., ir tu abu kartus pasirinkai atsitraukimą. Ar pastebi šį dėsningumą kasdienybėje?",
    "suggested_experiment": "Kito pokalbio metu, pajutęs norą atsitraukti, padaryk 3 sekundžių pauzę ir paklausk neutralaus patikslinančio klausimo."
  }
}
