# ConflictLab — Stimulus Lifecycle v1.0

**Data:** 2026-07-31
**Paskirtis:** Gamybos procesas. Kiekvienas stimulas pereina šiuos etapus.

> Nuo idėjos iki etaloninio stimulo.

---

```
1. IDĖJA
   ↓
   Universali situacija identifikuota
   (žr. Stimulus Matrix — kokių situacijų trūksta)

2. VAIZDO ATRANKA
   ↓
   Ar vaizdas atitinka Stimulus Design Standard? (FC-005)
   • Tinkamas objektų skaičius
   • Pakankama dviprasmybė
   • Jokio teksto vaizde
   • Neutralus kultūrinis kontekstas

3. CUE KŪRIMAS
   ↓
   Žiūrėti tik į vaizdą — ne į kitus stimulus
   Parašyti 10+ pirminių asociacijų
   Filtruoti per F1–F7
   Pasirinkti 3, kurie išlaiko Filtrą 4
   (skirtingos prasmės skirtingiems žmonėms)

4. SIGNALŲ PRISKYRIMAS
   ↓
   Kiekvienam choice_id priskirti aw/cs/cr svorius
   Loginis pagrindimas — kodėl šie svoriai?
   Patikrinti svorių simetriją (ne visi + arba visi -)

5. VIDINIS REVIEW
   ↓
   Ar cues praėjo F1–F7?
   Ar F6 — kiekvienas cue matomas vaizde?
   Ar F7 — cues nesikartoja esamoje bibliotekoje?
   Ar klausimas neutralus?
   Ar nė vienas cue nėra socialiai "geresnis"?

6. VALIDACIJA (Stimulus Validation Protocol v1.0.1)
   ↓
   V1: IMAGE audit (neutralumas, AI artefaktai, kultūra)
   V2: CHOICES audit (reakcija ne nuomonė, socialinis neutralumas)
   V3: SIGNALS audit (pirminė ašis, svorių simetrija)
   V4: Teorijų validacija
   Minimalus balas: 70/100

7. BETA
   ↓
   Stimulas rodomas realiems vartotojams
   Stebimas: latency, AHA dažnis, fallback dažnis
   Stebimas: ar cues sukelia atpažinimą ar pasirinkimą?

8. ANALIZĖ
   ↓
   Po ≥ 20 sesijų su stimulu:
   Ar P3 hesitation dažnas? (micro-pause veikia)
   Ar P5/P9 atsiranda? (signalas patikimas)
   Ar fallback dažnas? (signalas per silpnas)

9. SPRENDIMAS
   ↓
   🟢 Etaloninis stimulas — šablonas naujiems
   🟡 Pataisyti — cues, svoriai, arba vaizdas
   🔴 Atmesti — pašalinti iš bibliotekos
```

---

## Etaloninis stimulas

Stimulas tampa etaloniniu kai:

- Validacijos balas ≥ 85/100
- ≥ 20 beta sesijų
- AHA dažnis ≥ 60% (Q2 atsakymai)
- Fallback dažnis ≤ 10%
- Nė vienas F1–F7 pažeidimas

**Etaloniniai stimulai taps šablonais** — ne kopijuojami, bet naudojami kaip kokybės etalonas naujiems.

---

## Bibliotekos plėtros principas

```
Pirma: 10–15 etaloninių stimulų
Tada:  kiekvienas naujas stimulas lyginamas su etaloniniais
       "Ar šis stimulas yra tokio pat lygio kaip ST-010?"
```

Neskubėti plėsti iki 100 stimulus kol neturime 10 etaloninių.

---

## Dokumentų žemėlapis

| Etapas | Dokumentas |
|---|---|
| Situacijos planavimas | `stimulus_matrix_v1.md` |
| Vaizdo reikalavimai | `stimulus_design_standard.md` (FC-005) |
| Cue kūrimas | `stimulus_cue_rules_v1.md` (F1–F7) |
| Validacija | `stimulus_validation_protocol.md` |
| Balsas | `conflictlab_voice_v1.md` |
| Tyrimo protokolas | `beta_research_protocol_v1.md` |

---

*Stimulus Lifecycle v1.0 — ConflictLab gamybos procesas*
