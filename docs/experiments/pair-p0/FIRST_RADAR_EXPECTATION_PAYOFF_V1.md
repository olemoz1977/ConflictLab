# First Radar Expectation & Payoff Layer — v1

**Date:** 2026-08-06
**Version:** `first-radar-v1`
**Applies to:** `?set=prototype-nine-v1` only

---

## Problem

During testing with a new user, three gaps emerged:

1. Before starting, users did not understand that 3 sessions are required before seeing any result
2. After session 1 and 2, it was unclear why there was no result yet
3. After session 3, the radar alone was insufficient — users expected a "test result" or label
4. The product's epistemic commitment (no type, no diagnosis) was invisible to the user

---

## Solution

A layered expectation and payoff sequence that makes the 3-session promise explicit, provides progress context after each intermediate session, and delivers a meaningful but epistemically honest result after session 3.

---

## Screen sequence

### 1. Expectation screen (before session 1)

Shown only if:
- User is in `prototype-nine-v1` mode
- No P9 sessions completed yet
- Intro not previously seen (`p9_ui_state.intro_seen` not set)
- No unfinished session in progress

Not shown on resume or in M0 / n0-six-v3 mode.

**LT:**
- Antraštė: „Pirmas bendras vaizdas — po 3 trumpų sesijų"
- Paaiškinimas: „Kiekvienoje sesijoje pamatysi 3 skirtingas situacijų poras. Po trečios sesijos parodysime, kas kartojosi visuose 9 pasirinkimuose."
- Kelio seka: 1 sesija — pirmas sluoksnis / 2 sesija — palyginimas / 3 sesija — bendras pėdsakas
- Pastaba: „Tai nėra asmenybės testas ir ne galutinis tavo apibūdinimas."

**EN:**
- Title: „Your first full picture — after 3 short sessions"
- Desc: „In each session you will see 3 different situation pairs. After the third session we will show what repeated across all 9 choices."
- Steps: Session 1 — first layer / Session 2 — comparison / Session 3 — full picture

---

### 2. Progress screen after session 1

**LT:** „1 iš 3 sesijų" — užfiksuotas pirmasis pasirinkimų sluoksnis
**EN:** „1 of 3 sessions" — the first layer of choices is recorded

Buttons: Tęsti 2 sesiją / Grįžti vėliau (progress not deleted)

---

### 3. Progress screen after session 2

**LT:** „2 iš 3 sesijų" — šešios skirtingos situacijos, liko viena sesija
**EN:** „2 of 3 sessions" — six situations, one more to go

Buttons: Tęsti 3 sesiją / Grįžti vėliau

---

### 4. Result screen after session 3

The existing radar is preserved. Added around it:

- **Header:** „Tavo dabartinis pasirinkimų pėdsakas"
- **Context:** „Šis vaizdas sudarytas iš 9 pasirinkimų per 3 skirtingas sesijas."
- **Boundary statement:** „Tai ne tavo tipas ir ne galutinis apibūdinimas. Tai pėdsakas, kurį paliko tavo pasirinkimai šiose situacijose."
- **Prototype label preserved:** PROTOTIPO RADARAS — PRELIMINARUS
- **Dynamic counts preserved:** e.g. „Pagrįsta 3 sesijomis · 9 įtraukti pasirinkimai (3 peržiūrėti · 6 prototipo)"

---

### 5. Reflection section (after radar)

**Title:** „Ką verta pastebėti"

**Text:** „Per tris sesijas susidarė pirmas palyginamas tavo pasirinkimų vaizdas. Kryptys pasiskirstė nevienodai — kai kurios reakcijos kartojosi, kitos keitėsi priklausomai nuo situacijos."

Language boundaries — never written:
- „Tu esi..."
- „Tavo asmenybė..."
- „Tau būdinga..."
- „Tai reiškia, kad..."
- „Tu taip renkiesi todėl, kad..."

---

### 6. Question (after reflection)

**LT:** „Kuri šio pėdsako kryptis tau atrodo labiausiai pažįstama — ir kur ją pastebi savo kasdieniuose sprendimuose?"

**EN:** „Which direction in this trace feels most familiar — and where do you notice it in your everyday decisions?"

This is a question to the user, not a system conclusion about the user.

---

### 7. Actions after radar

- Primary: „Tęsti dar vieną sesiją" / „Continue with another session"
- Secondary: „Baigti dabar" / „Finish for now"

Sessions after the first radar are unlimited. The radar updates with each new session.

---

## Why no labels or types

ConflictLab principle: the system observes, it does not interpret. A label would require inferring causes, traits, or stable dispositions from choice data. The system does not have enough data or a validated model to make such inferences responsibly. The radar shows signal direction; interpretation is left to the user.

---

## State management

New localStorage keys under `cl_pair_p0_p9_` namespace:

- `cl_pair_p0_p9_ui_state` — JSON object with:
  - `intro_seen`: boolean — prevents expectation screen from reappearing
  - `result_screen_seen`: boolean
  - `continued_after_first_radar`: boolean

---

## Export metadata (SESSION level)

```json
{
  "set_id": "prototype-nine-v1",
  "expectation_layer_version": "first-radar-v1",
  "first_radar_after_sessions": 3,
  "pairs_per_session": 3,
  "radar_unlocked": true
}
```

`radar_unlocked` reflects actual state at session creation time via `isRadarUnlocked()`.

---

## QA criteria

### Static (code)

1. Expectation screen shown only to new P9 user (0 sessions, intro not seen, no resume)
2. Progress screen shows „1 iš 3" after session 1, „2 iš 3" after session 2
3. Radar shown automatically after session 3
4. Refresh returns to correct progress state
5. „Grįžti vėliau" does not delete progress
6. Result screen has no labels, types, or diagnostic claims
7. Fourth session is possible; radar updates
8. M0 and n0-six-v3 unaffected
9. P9/M0 session isolation unaffected

### Phone QA sequence

1. J0 reset
2. Open `?set=prototype-nine-v1`
3. Verify expectation screen appears (not intro)
4. Start session 1 → complete → verify „1 iš 3" progress screen
5. Close tab, reopen → verify progress screen still shows, not intro
6. Complete session 2 → verify „2 iš 3"
7. Complete session 3 → verify radar appears automatically with result layer
8. Verify reflection text and question visible
9. Verify „Tęsti dar vieną sesiją" starts session 4 without resetting radar
10. Remove `?set=prototype-nine-v1` from URL, reload → verify M0 shows 0/3 and no P9 UI
