# ConflictLab Analizės Algoritmas (Analysis Pipeline Spec)

**Versija:** 2.0 (Adaptyvi Multimodalinė Architektūra)  
**Paskirtis:** Apibrėžti nuoseklų algoritminį procesą, kaip spontaniškos vartotojo mikro-reakcijos į multimodalinius stimulus apdorojamos per `/perception`, `/adaptive` ir `/theories` sluoksnius, sugeneruojant patikrintas elgsenos įžvalgas ir transformacijos kelią.

---

## 🏗️ Algoritmo Schema (System Data Flow)

```text
[ Multimodal Stimulus (/stimuli) ]
               │
               ▼
[ Micro-Reaction (Latency + Choice) ]
               │
               ▼
[ Perception Layer (/perception) ]
               │
               ▼
[ Adaptive Loop (/adaptive) ] ─── (Eksperimento Ciklas)
               │
               ▼
[ Theory & Hypothesis Engine (/theories) ]
               │
               ▼
[ Triangulated Insight (/engine/synthesis.md) ]
