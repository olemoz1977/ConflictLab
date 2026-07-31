# ADR-010 — Observation Engine

**Data:** 2026-07-31
**Statusas:** Patvirtinta

## Kontekstas

Reflection kortelė rodė abstrakčius teiginius be grindžiamojo fakto.
Žmogus buvo prašomas tikėti sistemos išvada — o ne tikrinti jos stebėjimą.
Tai prieštaravo ConflictLab filosofijai: *sistema stebi, žmogus sprendžia*.

## Sprendimas

Naujas sluoksnis tarp Signal Engine ir Claude API:

```
Stimuli → Signal Engine → Observation Engine → Claude API → Reflection
```

## Keturi principai

**1. Semantic signals, ne axis labels**
Engine grąžina `"clarity_seeking"`, ne `"cs+"`.
Axis yra vidinė reprezentacija — aukštesnis sluoksnis jos nemato.

**2. Observations array, ne dominant_axis**
Reflection sluoksnis pasirenka kurį stebėjimą rodyti.
Observation Engine šio sprendimo nepriima — jis yra "šaltas".

**3. Engine yra "šaltas" ir objektyvus**
Generuoja tik stebėjimus. Niekada jų nevertina pagal psichologinę reikšmę.

**4. Claude API konstitucija**
```
NEVER infer causes.
NEVER explain personality traits.
NEVER predict future behavior.
NEVER create facts beyond provided data.
DESCRIBE only observed patterns.
USE only provided numbers and families.
```

## Observation struktūra

```json
{
  "observations": [
    {
      "signal": "clarity_seeking",
      "strength": 0.81,
      "occurrences": 3,
      "total": 4,
      "families": ["waiting", "open_space"],
      "latency": "hesitation"
    }
  ],
  "cross_session": false,
  "session_count": 1
}
```

## Semantic signal žodynas

| Signal | Aprašas | Ašis |
|---|---|---|
| `clarity_seeking` | Aiškumo ieškojimas | cs+ |
| `ambiguity_tolerance` | Neapibrėžtumo tolerancija | cs- |
| `approach_impulse` | Artėjimo impulsas | aw+ |
| `withdrawal_impulse` | Atsitraukimo impulsas | aw- |
| `structure_seeking` | Struktūros siekimas | cr+ |
| `release_impulse` | Paleidimo impulsas | cr- |
| `hesitation_before_choice` | Latency >8s | P3 |
| `trajectory_shift` | Kryptis kito per sesijas | P9 |
| `axis_conflict` | Dvi priešingos kryptys | P2 |

## Atsakomybių riba

| Sluoksnis | Atsakomybė |
|---|---|
| Signal Engine | aw/cs/cr iš pasirinkimų |
| Observation Engine | Semantic observations[] |
| Claude API | Žmogaus kalba pagal R1-R8 |
| Žmogus | Ar rezonuoja su patirtimi |
