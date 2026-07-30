# ConflictLab — Architecture Blueprint v1.0

**Data:** 2026-07-30
**Versija:** Post-audit, Pre-v1
**Autorius:** Auditas atliktas remiantis pilnu repository skeanavimu

---

## PROJEKTO MISIJA

ConflictLab padeda žmogui pastebėti savo pasikartojančius
reakcijų ir interpretacijos dėsningumus.

**Ne:** diagnozuoti, prognozuoti, vertinti asmenybę.
**Taip:** sudaryti sąlygas savirefleksijai per stebėjimą.

Architektūros vertinimo kriterijus:
> Ar kiekvienas elemento padeda žmogui geriau suprasti
> savo pasikartojančius reakcijų dėsningumus?

---

## 1. REPOSITORY INVENTORIUS

### 1.1 AKTYVŪS — naudojami šiandien

| Failas | Paskirtis | Naudoja | V1? |
|---|---|---|---|
| `docs/index.html` | Visas UI (v0.6.0) | Vartotojas | ✅ CORE |
| `docs/media/*.png` | 12 stimulų nuotraukos | index.html | ✅ CORE |
| `docs/architecture_decisions.md` | 8 ADR | Komanda | ✅ CORE |
| `docs/philosophy.md` | Projekto filosofija | Komanda | ✅ |
| `src/core/signal_orientation.py` | SignalOrientation klasė | tik Python | ⚠️ NEPASIEKIA UI |
| `src/core/evidence_graph.py` | EvidenceGraph/Signal Trace | tik Python | ⚠️ NEPASIEKIA UI |
| `src/core/event_log.py` | Append-only EventLog | tik Python | ⚠️ NEPASIEKIA UI |
| `src/engine/uncertainty_engine.py` | 5D Uncertainty | tik Python | ⚠️ NEPASIEKIA UI |
| `src/frameworks/model_registry.py` | 14 teorijų registras | tik Python | ⚠️ NEPASIEKIA UI |
| `src/mirror/reflection_contract.py` | ReflectionContract | tik Python | ⚠️ NEPASIEKIA UI |
| `integration_test.py` | Pilno pipeline demo | tik Python | ✅ DEMO |

### 1.2 ARCHYVINIAI — saugomi, nenaudojami

| Failas | Paskirtis | Statusas |
|---|---|---|
| `archive/v1/*` | Senoji architektūra | ARCHYVAS |
| `docs/index_v04_backup.html` | v0.4 UI backup | ARCHYVAS |
| `model/belief_engine.py` | Senas hipotezių variklis | ARCHYVAS — dubliuojasi su src/ |
| `model/belief_engine.md` | Dokumentacija | ARCHYVAS |
| `model/contradiction_rules.md` | Taisyklės | ARCHYVAS |
| `model/hypothesis_weights.md` | Svoriai | ARCHYVAS |

### 1.3 DOKUMENTAI — aktualūs bet nenaudojami sistemoje

| Failas | Paskirtis | V1? |
|---|---|---|
| `theories/*.md` (14 failų) | Teorijų aprašymai | ⚠️ NEPASIEKIA UI |
| `hypotheses/H001-H004.md` | Hipotezės | ⚠️ NEPASIEKIA UI |
| `core/human_model.md` | 13 etapų modelis | ⚠️ NEPASIEKIA UI |
| `core/interpretation_filter.md` | 10 filtro komponentų | ⚠️ NEPASIEKIA UI |
| `stimuli/*.md` | Stimulų katalogas | ⚠️ NEPASIEKIA UI |
| `engine/*.md` | Pipeline dokumentai | ⚠️ NEPASIEKIA UI |
| `validation/scenarios/*.md` | 3 scenarijai | ⚠️ NENAUDOJAMI |
| `examples/*.md` | 4 pavyzdžiai | TUŠTI |
| `perception/feature_extraction.md` | Percepcija | NEBAIGTA |
| `research/*.md` | Tyrimų klausimai | NEBAIGTA |
| `adaptive/stimulus_selector.md` | Adaptyvus pasirinkimas | NEBAIGTA |
| `user_state/privacy_architecture.md` | GDPR spec | V2 |

### 1.4 PERTEKLINIAI / PROBLEMATIŠKI

| Failas | Problema |
|---|---|
| `./{docs,mirror,frameworks,...}` | Klaida — tuščias aplankas su blogu pavadinimu |
| `core/reaction_pattern.md` | TUŠČIAS |
| `core/transformation_path.md` | TUŠČIAS |
| `ideas/backlog.md` | TUŠČIAS |
| `docs/ui/` | TUŠČIAS aplankas |

---

## 2. DEPENDENCY GRAPH — sistemos logika

```
ŠIANDIEN (v0.6.0):
─────────────────────────────────────────

Vartotojas
    │
    ▼
[docs/index.html]
    │
    ├── Stimulus Library (12 vaizdai, hardcoded JS)
    │       │
    │       ▼
    │   Photo → 3 pasirinkimai → {aw, cs, cr} svoriai
    │
    ├── Adaptive Selector (JS logika)
    │       │
    │       └── Renkasi stimulus pagal ankstesnių
    │           sesijų aw/cs/cr vidurkius
    │
    ├── localStorage → sesijų istorija
    │
    └── Claude API (claude-sonnet-4-6)
            │
            └── Gauna: reakcijų seką + aw/cs/cr
                Grąžina: trajectory + limits + question

TEORIŠKAI SUKURTA, BET NEPRIJUNGTA:
─────────────────────────────────────────

src/core/signal_orientation.py  ──┐
src/core/evidence_graph.py      ──┤
src/core/event_log.py           ──┤── NEVERČIAMI Į UI
src/engine/uncertainty_engine.py──┤
src/frameworks/model_registry.py──┤    Veikia tik Python
src/mirror/reflection_contract.py─┘    aplinkoje
```

---

## 3. THEORY USAGE MATRIX

| Teorija | Registruota | Stimule | UI matoma | Signalą interpretuoja | Pasiekia Reflection |
|---|---|---|---|---|---|
| AT-001 Attachment Theory | ✅ model_registry.py | ❌ | ❌ | ❌ | ❌ |
| CD-001 Cognitive Distortions | ✅ | ❌ | ❌ | ❌ | ❌ |
| SC-001 SCARF Model | ✅ | ❌ | ❌ | ❌ | ❌ |
| ER-001 Emotion Regulation | ✅ | ❌ | ❌ | ❌ | ❌ |
| DP-001 Dual Process | ✅ | ❌ | ❌ | ❌ | ❌ |
| KD-001 Karpman | ✅ | ❌ | ❌ | ❌ | ❌ |
| TA-001 Transact. Analysis | ✅ | ❌ | ❌ | ❌ | ❌ |
| PV-001 Polyvagal | ✅ | ❌ | ❌ | ❌ | ❌ |
| AT-001..SC-001 (v0.4 UI) | — | — | ✅ buvęs | — | ✅ buvęs |
| **aw/cs/cr ašys (v0.6)** | ⚠️ | ✅ | ✅ | ✅ JS | ✅ per API |

**Diagnozė:** Teorijos yra gerai sukurtos, bet atsijungusios nuo UI.
v0.6 UI naudoja tik signalų ašis (aw/cs/cr) — be teorijų deklaracijos.

---

## 4. DATA FLOW AUDITAS

```
TEORINIS SRAUTAS (v0.4 Python):
────────────────────────────────────────────────────────

Stimulus
    ↓
Selection + Latency
    ↓
EvidenceNode {stimulus_ref, response, signal_weight, modality}
    ↓
EvidenceGraph {nodes, edges, provenance_chain}
    ↓ ← MISSING: EvidenceGraph nepasiekia UI
Hypothesis {H001..H004}
    ↓ ← MISSING: Hipotezės nenaudojamos UI
Theory Selection (ModelRegistry → AT-001, CD-001...)
    ↓ ← MISSING: Teorijų pasirinkimas nenaudojamas UI
UncertaintyEngine {5 dimensijos}
    ↓ ← MISSING: Uncertainty nepasiekia UI
ReflectionContract {7 laukai, validacija}
    ↓ ← MISSING: Kontraktas nenaudojamas UI
User

REALUS SRAUTAS (v0.6 UI):
────────────────────────────────────────────────────────

Vaizdas (PNG)
    ↓
Pasirinkimas (3 opcijos)
    ↓
{aw, cs, cr} svoriai (hardcoded JS)
    ↓
Sumuojami per 4 stimulus → vidurkiai
    ↓
Claude API prompt:
  "Reakcijų seka + aw/cs/cr vidurkiai →
   trajectory + limits + question"
    ↓
Refleksija vartotojui

GRANDINĖS NUTRŪKIMO VIETOS:
────────────────────────────────────────────────────────
⚠️ MISSING-1: EvidenceGraph → nėra provenance chain UI
⚠️ MISSING-2: Hipotezės → nenaudojamos
⚠️ MISSING-3: Teorijų deklaracija → nerodoma vartotojui
⚠️ MISSING-4: UncertaintyEngine → nėra 5D uncertainty UI
⚠️ MISSING-5: ReflectionContract → validacija neveikia UI
⚠️ MISSING-6: EventLog → localStorage, ne append-only events
```

---

## 5. REFLECTION AUDIT

| Klausimas | Šiandien | Komentaras |
|---|---|---|
| Ar sistema **matuoja**? | ✅ Taip | aw/cs/cr per 4 stimulus |
| Ar sistema **interpretuoja**? | ⚠️ Iš dalies | Claude API generuoja tekstą, bet be teorijų konteksto |
| Ar sistema **padeda reflektuoti**? | ⚠️ Silpnai | Klausimas atviras, bet nėra erdvės po jo |
| Ar sistema **padeda keisti elgesį**? | ❌ Ne | Nėra jokio tęsinio po refleksijos |

**Vertė baigiasi:** po refleksinio klausimo. Žmogus lieka su klausimu be jokios struktūros kaip su juo dirbti.

**Gemini diagnozė patvirtinta:**
> "Puikus jutiklis, bet dar ne veidrodis."

---

## 6. ARCHITECTURE DEBT

### Kritinis

| Problema | Aprašas | Poveikis |
|---|---|---|
| **Python ↔ UI praraja** | 6 Python moduliai sukurti, bet neprijungti prie UI | Visas src/ yra dead code UI kontekste |
| **Teorijų atsijungimas** | 14 teorijų registruota, nė viena nepasiekia vartotojo | Teorinis pamatas neveikia |
| **Refleksija be tęsinio** | Klausimas pateikiamas, bet nėra erdvės po jo | Vartotojas "paliekamas kaboti" |

### Vidutinis

| Problema | Aprašas |
|---|---|
| **Hardcoded signalai** | aw/cs/cr svoriai hardcoded JS — sunku keisti |
| **Nėra validacijos** | ReflectionContract validacija neveikia — Claude gali grąžinti bet ką |
| **localStorage ≠ EventLog** | Vietoj append-only events — mutable localStorage |
| **Stimulus biblioteka mažyta** | 12 nuotraukų — per mažai adaptyvumui |

### Žemas (saugoma, bet perteklinė)

| Failas | Problema |
|---|---|
| `model/belief_engine.py` | Dubliuojasi su src/ moduliais |
| `docs/index_v04_backup.html` | Backup — gerai, bet reikia žymėjimo |
| `{docs,mirror,...}` aplankas | Blogas pavadinimas — reikia ištrinti |
| `examples/*.md` | Visi tušti |
| `./__pycache__/` | Neturėtų būti repo |

---

## 7. V1 BLUEPRINT

### V1 misija (vienas sakinys)

> Vartotojas atlieka 3 sesijas, gauna prasmingą
> dėsningumo refleksiją ir atpažįsta save joje.

### V1 architektūra — tik tai kas būtina

```
┌─────────────────────────────────────────────┐
│                   UI LAYER                  │
│                                             │
│  Intro → Stimulus → Reaction → Loading      │
│       ↓                                     │
│  SignalOrientation {aw, cs, cr}             │
│       ↓                                     │
│  localStorage (sesijų istorija)             │
│       ↓                                     │
│  Claude API                                 │
│       ↓                                     │
│  Reflection Screen                          │
│  ├── Trajectory (be verdikto)               │
│  ├── Theory Context (kuri teorija, kodėl)   │ ← MISSING šiandien
│  ├── Uncertainty Note (ko nežinome)         │
│  └── Reflective Question                    │
│            ↓                               │
│  Post-Reflection Space                      │ ← MISSING šiandien
│  └── "Ar atpažįsti?"                        │
└─────────────────────────────────────────────┘
```

### V1 komponentai

**IŠLAIKOMA (veikia dabar):**
- Stimulus biblioteka (12 nuotraukų, 3 ašys)
- Adaptive selector (JS)
- localStorage sesijų istorija
- Claude API trajectory generation
- SignalOrientation aw/cs/cr matematika

**PRIDEDAMA V1 (trūksta):**

1. **Theory Context UI** — po trajectory rodyti kurią teoriją Claude naudojo ir kodėl. Naudoti `model_registry.py` deklaracijas. Vartotojas mato: *"Šis dėsningumas žiūrimas per Dual Process Theory lęšį. Ši teorija nepaaiškina [X]."*

2. **Post-Reflection Space** — po klausimo: 30 sekundžių tyla + vienas laukas tekstui sau. Jokio patarinėjimo.

3. **Pattern Screen** — po 3 sesijų: ne skaičiai, o natūralios kalbos dėsningumas. Pvz: *"3 iš 3 sesijų greičiausiai reaguoji į aiškumo trūkumą (cs: +0.42 vidurkis)."*

**PERKELIAMA Į V2:**
- Python modulių prijungimas prie UI
- Backend serveris
- EventLog (tikras append-only)
- UncertaintyEngine (5D UI)
- ReflectionContract validacija
- Pilna teorijų deklaracija UI

---

## 8. REPOSITORY STRUKTŪRA — V1

```
ConflictLab/
│
├── docs/                    ← GitHub Pages (V1 core)
│   ├── index.html           ← Visas UI
│   ├── architecture_decisions.md
│   ├── philosophy.md
│   └── media/               ← 12 stimulus + 3 ašių nuotraukos
│
├── src/                     ← Python moduliai (V2 pagrindas)
│   ├── core/
│   │   ├── signal_orientation.py   ← Veikia, neprijungtas
│   │   ├── evidence_graph.py       ← Veikia, neprijungtas
│   │   └── event_log.py            ← Veikia, neprijungtas
│   ├── engine/
│   │   └── uncertainty_engine.py   ← Veikia, neprijungtas
│   ├── frameworks/
│   │   └── model_registry.py       ← Veikia, neprijungtas
│   └── mirror/
│       └── reflection_contract.py  ← Veikia, neprijungtas
│
├── theories/                ← 14 teorijų dokumentacija (V2)
├── hypotheses/              ← H001-H004 (V2)
├── validation/              ← Validacijos scenarijai
├── archive/                 ← Istorija (neliečiama)
└── integration_test.py      ← Pilno pipeline demo
```

---

## 9. V2 BACKLOG

| Prioritetas | Elementas | Priklausomybė |
|---|---|---|
| P1 | Python → UI bridge (API serveris) | Backend |
| P1 | ReflectionContract validacija UI | Python bridge |
| P1 | EventLog vietoj localStorage | Backend |
| P2 | UncertaintyEngine UI (5D) | Python bridge |
| P2 | Teorijų deklaracija UI | ModelRegistry bridge |
| P2 | Stimulus biblioteka (50+) | Nuotraukos + klasifikacija |
| P3 | EvidenceGraph vizualizacija | Python bridge |
| P3 | GDPR duomenų eksportas | Backend |
| P3 | Multi-user | Backend |

---

## 10. REKOMENDACIJOS

### Ką daryti dabar (prieš kodavimą)

**1. Validacija su žmonėmis — DABAR**
Sistema yra pakankamai brandaus MVP. 5-10 žmonių, 3 sesijos kiekvienas.
Klausti tik: *"Ar atpažįsti save rezultate?"*
Jei ne — sustoti ir iš naujo vertinti stimulus.
Jei taip — tęsti su V1 papildymais.

**2. Theory Context UI — PIRMAS KODAS**
Vienas papildymas: po trajectory rodyti kurią teoriją Claude naudojo.
Tai užpildo "jutiklis → veidrodis" prarają be didelių architektūros pokyčių.

**3. Post-Reflection Space — ANTRAS KODAS**
30 sekundžių tyla + laukas tekstui sau.
Tai atsakymas į Gemini klausimą: "ką žmogus daro po refleksijos?"

### Ko nedaryti dabar

- Nereikia prijungti Python modulių prie UI — tai V2 darbas
- Nereikia daugiau stimulus (kol nėra validacijos)
- Nereikia backend serverio (localStorage pakanka MVP)
- Nereikia naujų teorijų

---

## SUMMARY

| Dimensija | Šiandien | V1 tikslas |
|---|---|---|
| Teorinis pamatas | 9/10 (Gemini) | 9/10 — išlaikomas |
| Matavimas | 8/10 | 8/10 — išlaikomas |
| UX aiškumas | 5/10 | 7/10 — Theory Context + Space |
| Refleksijos vertė | 4/10 | 7/10 — po validacijos |
| Architektūros nuoseklumas | 6/10 | 8/10 — po V1 |

**Pagrindinė įžvalga:**
ConflictLab turi išskirtinai brandų architektūrinį pagrindą.
Problema nėra technologinė — problema yra praraja tarp
mataviamo signalo ir žmogiškai prasmingos refleksijos.

Šios praragos neužpildys daugiau kodo.
Ją užpildys realūs žmonės su realiu grįžtamuoju ryšiu.

---

*ConflictLab Architecture Blueprint v1.0*
*Auditas: 2026-07-30*
*Kitas žingsnis: Validacija su žmonėmis → Theory Context UI*
