# 2Pair — V2 Stimulus & Calibration Protocol v0.1

**Date:** 2026-08-29  
**Status:** FUTURE RESEARCH PROTOCOL DRAFT  
**Applies to:** Decision Driver V2 only.  
**Does not supersede:** frozen Integrated Pilot v0.1 or its historical Wave 1 / timing analysis rules.

---

## 1. Purpose

The V2 item bank must answer a harder question than the historical library:

> Can a controlled visual pair create a reproducible trade-off between two candidate motives strongly enough that repeated choices can support a participant-facing statement about what pulled the decision?

The unit of validation is therefore no longer a single image.

It is:

> **a driver collision represented by multiple independent visual pairs.**

---

## 2. Required object hierarchy

```text
DRIVER
  └── COLLISION (Driver A vs Driver B)
        └── SCENE FAMILY 1
              └── PAIR EXEMPLAR
        └── SCENE FAMILY 2
              └── PAIR EXEMPLAR
        └── SCENE FAMILY 3+
              └── PAIR EXEMPLAR
```

A participant result is never supported by only one exemplar.

---

## 3. Candidate collision matrix

Legend:

- `P1` = high-priority clean theoretical trade-off
- `P2` = useful but more context-dependent
- `X` = substantial construct overlap; poor early target

| A \ B | Opportunity | Protection | Autonomy | Certainty | Exploration | Mastery | Connection | Influence |
|---|---|---|---|---|---|---|---|---|
| **Opportunity** | — | **P1** | P2 | P2 | X | X | **P1** | X/P2 |
| **Protection** |  | — | **P1** | X | **P1** | P2 | P2 | P2 |
| **Autonomy** |  |  | — | **P1** | X | P2 | **P1** | P2 |
| **Certainty** |  |  |  | — | **P1** | P2 | P2 | P2 |
| **Exploration** |  |  |  |  | — | P2 | P2 | P2 |
| **Mastery** |  |  |  |  |  | — | **P1** | X/P2 |
| **Connection** |  |  |  |  |  |  | — | **P1** |
| **Influence** |  |  |  |  |  |  |  | — |

### Recommended initial P1 set

1. **Autonomy ↔ Certainty**
2. **Opportunity ↔ Protection**
3. **Certainty ↔ Exploration**
4. **Connection ↔ Influence**
5. **Mastery ↔ Connection**
6. **Protection ↔ Autonomy**
7. **Opportunity ↔ Connection**
8. **Autonomy ↔ Connection**
9. **Protection ↔ Exploration**

Not all nine need to survive.

The first bank should deliberately include collisions likely to falsify overlaps.

---

## 4. Item design contract

Every V2 pair candidate must have an internal preregistration card before generation.

### 4.1 Required fields

```yaml
pair_id: neutral opaque ID
collision_id: internal blinded mapping
driver_A:
driver_B:
scene_family:
participant_task: choose the image that pulls you more
A_intended_affordance:
B_intended_affordance:
alternative_explanations:
visual_confound_targets:
demand_characteristic_risks:
social_desirability_risk:
cultural_risk:
generation_constraints:
validation_status:
scoring_status: false
```

### 4.2 Neutral IDs

Do not use filenames like:

```text
more-autonomy.png
less-certainty.png
promotion.png
protection.png
```

Use opaque IDs in all participant assets and blind-validation packages.

The mapping lives in a protected manifest used only after coding.

---

## 5. Visual generation rule

The goal is not to make driver concepts obvious.

Bad:

```text
Autonomy = broken chains
Protection = locked safe
Connection = hugging people
Influence = crown
```

That measures construct recognition and desired self-image.

Better:

> Two credible options in the same decision context, where each option affords a different benefit.

Example conceptual template:

```text
same workspace / same task / same visual quality

A:
flexible movable elements
multiple valid ways to configure

B:
predefined lanes
clear placement and predictable arrangement
```

Candidate collision:

```text
Autonomy ↔ Certainty
```

The participant should be able to prefer either image for a psychologically plausible reason without seeing the hidden construct label.

---

## 6. Validation stages

### V2-S0 — Asset integrity

Check:

- identical display dimensions where possible;
- no compression-format asymmetry;
- no AI artifacts;
- no accidental text;
- no human demographic cue unless explicitly required;
- equivalent image quality.

Fail -> rebuild.

### V2-S1 — Perceptual confound audit

Quantify and/or blind-rate:

- mean luminance;
- contrast;
- colorfulness;
- edge density;
- visual complexity;
- symmetry;
- whitespace;
- object salience;
- aesthetic appeal;
- emotional valence.

A difference is not automatically disqualifying.

The question is whether it is:

1. necessary to represent the driver, or
2. an unrelated nuisance capable of explaining the choice.

### V2-S2 — Blind semantic coding

Independent raters see only opaque pair IDs.

Prompt:

> What is the most important difference between these two options?

Then code responses without revealing the intended drivers.

Pass criterion is not a fixed percentage yet.

The pair advances only if the intended trade-off appears spontaneously and competing interpretations are understood.

### V2-S3 — Research-only reason capture

Participants choose the image first.

After the choice, outside the measured interval:

```text
Why did this one pull you more?
```

Free text remains valuable **during item validation**.

It is not assumed to remain in the final product.

Reasons are blind-coded into:

```text
target Driver A
target Driver B
aesthetic/perceptual
narrative/context
other construct
unclear
```

The current Wave 1 reason-coding idea survives here, but now the target is an explicit driver collision.

### V2-S4 — Position/form robustness

Re-test with:

- A top / B bottom;
- B top / A bottom;
- alternate equivalent exemplar;
- mobile / desktop where relevant.

A pair that reverses materially due to position or device is not scoring eligible.

### V2-S5 — Cross-exemplar convergence

The same collision must be represented in multiple independent scenes.

Example:

```text
Autonomy ↔ Certainty

scene 1: workspace organization
scene 2: route / path structure
scene 3: planning board
scene 4: modular physical layout
```

The critical question:

> Do choices show a shared participant-level component after item-specific visual preference is modeled?

If not, the collision is scene-specific and should not become a general result.

### V2-S6 — Discriminant validation

Challenge neighboring explanations.

Example:

```text
Autonomy ↔ Certainty
```

must be distinguishable from:

```text
Exploration ↔ Certainty
Influence ↔ Certainty
Autonomy ↔ Protection
```

If participants are actually selecting novelty rather than autonomy, the item must be remapped or rejected.

### V2-S7 — External validation

Use established reference measures as **research instruments**, not as participant result labels.

Candidate battery:

```text
Regulatory Focus IPIP-RFS
RST-PQ / RST-PQ-S
Schwartz PVQ-RR
SDT basic-need measures
Need for Cognitive Closure scale
Big Five / HEXACO for nomological/discriminant checks
```

Decision tasks such as explore–exploit, risk, and delay discounting should be treated cautiously because behavioral-task reliability can be task-specific.

### V2-S8 — Test-retest and context study

Repeat a calibrated subset:

- same day separated block;
- later session;
- changed scene contexts.

Estimate separately:

```text
item reliability
driver ranking stability
context sensitivity
participant-specific change
```

Do not call instability “noise” automatically.

It may be real context dependence.

### V2-S9 — Model recovery / simulation

Before shortening or making the test adaptive:

1. generate synthetic participants with known driver weights;
2. simulate item bias and ties;
3. fit candidate models;
4. measure recovery error;
5. simulate static vs adaptive item selection;
6. estimate how many choices are needed for useful uncertainty.

Only then freeze a test length.

### V2-S10 — Participant result validation

Show the derived result and ask:

```text
Did this say something useful?
Was any wording stronger than the evidence?
Could you trace the statement back to choices?
Was the result surprising but understandable?
Would you do this again?
```

Product resonance does not substitute for construct validity, but construct validity without participant value also fails 2Pair.

---

## 7. Research flow vs final product flow

### Item-validation harness

```text
training
-> choice
-> research reason
-> optional intensity
-> next item
-> external validation battery where appropriate
```

### Final product candidate

```text
training
-> visual choice
-> visual choice
-> visual choice
-> ...
-> result
-> optional “Atpažįsti?” / Explore layer
```

The reflection burden belongs mainly in **validation**, not necessarily in the consumer experience.

---

## 8. Timing protocol implication

The current shared 6000 ms block remains a frozen historical calibration candidate.

V2 adaptive measurement has a different methodological requirement:

> order and item exposure must not determine which driver gets enough evidence.

Therefore V2 must independently evaluate its timing mechanics.

Candidate possibilities to test later:

- per-pair maximum exposure;
- untimed but instruction-to-choose-quickly;
- short fixed exposure + response window;
- small fixed sub-blocks with no shared-budget position penalty.

No timing rule is selected by this document.

Latency remains telemetry until a separate validation establishes a role.

---

## 9. Perceptual-control bank

The current audit suggests preserving some old pairs as **controls**.

A future validation session may interleave non-scoring control pairs that isolate preferences such as:

```text
segmented vs unsegmented
higher vs lower visual complexity
object more vs less revealed
sharp vs soft edges
more vs less whitespace
symmetric vs asymmetric layout
```

Purpose:

> estimate nuisance preference that might otherwise masquerade as Certainty, Exploration, Autonomy, etc.

Controls must never be translated directly into participant psychology.

---

## 10. Scoring eligibility

A pair can contribute to participant Driver inference only when:

```text
scoring_status = true
```

and evidence exists for:

- semantic target;
- perceptual confound handling;
- cross-exemplar relationship;
- position/device robustness;
- discriminant validity;
- model fit/recovery;
- sufficient uncertainty bounds.

The bank may contain many useful research pairs with `scoring_status = false`.

That is expected.

---

## 11. Calculation roadmap

### Prototype 1 — transparent round-robin

Purpose: debug ontology and participant understanding.

Possible calculation:

```text
driver wins / appearances
```

Never market as validated score.

### Prototype 2 — Bradley-Terry / conditional logit

Purpose: estimate relative driver utility while accounting for unequal pairings/item difficulty.

### Prototype 3 — hierarchical random utility

Add:

```text
participant driver effects
item random effects
position effect
perceptual nuisance covariates
context interactions
tie/no-clear model
```

### Prototype 4 — adaptive engine

Select next pair based on expected information, but preserve minimum coverage and cross-links.

### Prototype 5 — Thurstonian / IRT comparison

Evaluate only after a calibrated item bank exists.

Do not assume the most complicated model is the best product model.

---

## 12. Result contract V2

A participant-facing statement needs:

```text
statement
supporting driver collisions
number/diversity of independent exemplars
uncertainty / mixed-evidence state
context scope
```

Preferred result vocabulary:

```text
stronger pull
often won
close call
changed by context
repeated across scenes
```

Avoid:

```text
type
hard-wired
subconscious trait
brain profile
you always
you are
```

Example:

> **Laisvė dažniau nusverdavo aiškumą.**  
> Ši kryptis pasikartojo keliuose skirtinguose pasirinkimuose, kuriuose daugiau veikimo laisvės konfliktavo su aiškesne iš anksto nustatyta struktūra.

This is a conclusion about observed trade-offs, not identity.

---

## 13. Initial V2 research priority

Do not attempt all eight drivers at once.

### Priority A

Build and validate:

```text
Autonomy ↔ Certainty
```

Reason:

- strongest current reusable pair seed (`CR-PO-01`);
- participant reasons already contain “organized” vs “freedom/no constraints” language;
- strong theoretical anchors on both sides;
- immediate participant-facing meaning.

### Priority B

Build and validate:

```text
Certainty ↔ Exploration
```

Reason:

- current `CS-PR-01` provides a weak/promising seed;
- “no hidden details” vs “mystery” appeared spontaneously;
- current item also clearly demonstrates why multiple exemplars and confound controls are needed.

### Priority C

Create new from theory, not legacy assets:

```text
Opportunity ↔ Protection
Connection ↔ Influence
Mastery ↔ Connection
```

These test whether the new architecture can move beyond the visual structure/ambiguity domain inherited from CS/CR.

---

## 14. Scientific references to keep in the research registry

- Schwartz et al. / PVQ-RR cross-cultural psychometrics — PMCID `PMC9131418`.
- Fuglestad et al. Regulatory Focus IPIP-RFS — PMID `39072767`.
- Corr & Cooper RST-PQ — PMID `26845224`.
- Webster & Kruglanski Need for Cognitive Closure — PMID `7815301`.
- Slemp et al. interpersonal supports for SDT needs meta-analysis — PMID `38635183`.
- Best-Worst Scaling overview — PMID `26743636`.
- Thurstonian forced-choice current-status review — PMID `39055095`.
- Person-parameter foundations in TIRT — PMID `39601492`.
- Multidimensional forced-choice adaptive item-selection methods — PMID `36750522`.
- Explore–exploit psychometric caution — PMID `40721436`.
- Risk preference stability/convergence meta-analysis — PMID `39870880`.
- Delay/probability discounting reliability meta-analysis — PMID `38499476`.

---

## 15. Freeze boundary

This protocol authorizes **future V2 research design only**.

It does not authorize:

- changes to the frozen Integrated v0.1 participant flow;
- current pair replacement on the live pilot;
- research-mode activation;
- Gate D/E;
- retroactive scoring of old participants;
- merging or deleting historical assets.

The old pilot remains evidence about the old protocol. V2 starts a new methodological lineage.
