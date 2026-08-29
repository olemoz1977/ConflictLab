# 2Pair — Experience Principles v0.1

**Date:** 2026-08-24  
**Status:** PRODUCT DIRECTION / NOT YET IMPLEMENTED  
**Scope:** participant-facing 2Pair experience; does not change current Calibration methodology or data rules.

## Core observation

2Pair should not require the result to be interesting. **The act of choosing should already feel interesting.**

A useful contrast emerged while reviewing a visual rapid-choice tool (AgileBrain): its strongest product advantage is not necessarily the interpretation layer, but the participant experience — many images, color, motion, rhythm, immediate visual payoff, and a sense that something is happening.

Current 2Pair is methodologically restrained, but can feel more like an experiment than an experience.

### Product principle

> **Do not copy stronger interpretation. Copy stronger FUN.**

FUN here means visual energy, rhythm, curiosity, movement and payoff — not gamified scoring, personality labels or psychological certainty.

---

## 1. Research core must remain protected

The calibrated research core remains separate from experience decoration:

```text
3 rapid pairs
shared 6000 ms candidate budget
mechanical timing only
no Gate D / Gate E interpretation
no personality label
no psychological meaning assigned to latency
```

Visual effects must not contaminate the measured interval. Animation, celebratory feedback or transitions that could affect the next response should occur only outside the timing-critical window or be explicitly validated.

---

## 2. Make the interaction itself rewarding

The participant should feel progression during the three choices.

Possible future directions:

- full-screen or near-full-screen visual pairs;
- strong but controlled color and visual contrast;
- very short post-choice transitions;
- a three-step progress rhythm rather than form-like UI;
- subtle motion after a response, not before or during measured perception;
- avoid clinical/admin/test aesthetics.

The intended feeling is closer to:

> **Look at two. Choose one. Look again.**

than to:

> Complete item 1 of 3.

---

## 3. Add a participant payoff without inventing a diagnosis

2Pair needs an immediate post-choice payoff even when the scientifically correct result is still `NOT_ESTIMABLE`.

Candidate concept: **Choice Trace / pasirinkimų pėdsakas**.

It may show the three actual choices visually without translating them into a personality trait or construct label.

Example conceptual language:

```text
3 choices.
3 different contexts.
No interpretation yet.

Did you notice what pulled your attention?
```

This supports the 2RASI philosophy: the system helps the participant notice rather than tells the participant who they are.

---

## 4. Color may carry experience, not psychological meaning

Color can make the session memorable without becoming a hidden scoring code.

Possible use:

- session-specific visual accents;
- each completed choice leaves a visual trace;
- traces combine at the end into a small session artifact.

Avoid participant-facing semantics such as:

```text
red = dominance
blue = analytical
color X = psychological construct Y
```

unless such mapping is independently justified and validated in a future methodology.

---

## 5. More images can increase FUN, but research and exploration must be separated

Three pairs are intentionally small for the current Calibration core. A future product experience may contain an optional **Explore** layer after the measured core.

Conceptual split:

```text
RESEARCH CORE
3 pairs / calibrated timing / research rules

EXPLORE
additional optional visual choices
not part of the Calibration N/20 dataset
not used to retroactively alter the measured core
```

This could provide more visual variety and curiosity without compromising the calibrated measurement.

---

## 6. Avoid semantically obvious stimuli

A visual can become too easy to "read" as a psychological label.

Risk:

```text
stimulus -> participant recognizes construct -> participant chooses the self-image they want to report
```

instead of:

```text
stimulus -> rapid preference/attention choice -> repeated observable signal
```

Generative-AI images require special care because they can become semantically hyper-explicit: "recognition" becomes applause/awards, "autonomy" becomes chains vs freedom, etc.

Therefore future stimulus review should evaluate not only visual quality but also **construct legibility / demand-characteristic risk**.

---

## 7. Product north-star implication

2Pair should aim to combine:

```text
methodological restraint
+
visual curiosity
+
fast interaction
+
immediate non-diagnostic payoff
```

The target is not "a more colorful test".

The target is:

> **an experience where the participant enjoys observing their own choices before any interpretation exists.**

---

## Boundary

This note records product/UX direction only. It does **not** authorize:

- Gate D or Gate E;
- psychological/personality scoring;
- construct interpretation from the current 6000 ms Calibration;
- use of optional Explore choices as Calibration evidence;
- changing the current active Calibration artifact without a separate implementation and validation decision.
