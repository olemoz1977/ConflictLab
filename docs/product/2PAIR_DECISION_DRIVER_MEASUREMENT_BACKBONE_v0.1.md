# 2Pair — Decision Driver Measurement Backbone v0.1

**Date:** 2026-08-29  
**Status:** FUTURE METHODOLOGY CANDIDATE / DESIGN BASELINE  
**Scope:** proposed measurement architecture for a future 2Pair version.  
**Non-impact boundary:** this document does **not** change, unfreeze, redeploy, re-score, or reinterpret `2pair-integrated-v0.1`. Current Gate D/E remain NONE.

---

## 0. Why this document exists

The current 2Pair research path successfully protected against overclaiming, but the protection became product-poor: a participant could end up seeing only a neutral trace of obvious image choices.

The product purpose is stronger:

> **Help a person notice what tends to pull their decisions when meaningful motives compete.**

The future measurement target is therefore not:

- personality type;
- innate vs acquired trait;
- a neurological label;
- aesthetic image preference;
- response speed as a proxy for subconscious strength;
- a hand-assigned score attached to a single image.

The candidate target is:

> **context-bound relative motivational priority under forced trade-offs.**

In ordinary language:

> **What tends to win when you cannot have everything at once?**

This restores participant value without claiming that a visual choice reveals a person's essence.

---

## 1. Core measurement object

For a participant `p`, context `c`, and candidate decision drivers `d1...dk`, 2Pair aims to estimate **relative utility weights** that best explain a network of forced choices.

The primary observation is always:

```text
OPTION A vs OPTION B
        ↓
participant selects A / B / no clear choice
```

The interpretation comes only after independently validated stimulus mappings exist.

### 1.1 The critical distinction

```text
driver importance in a specific choice
!= stable personality trait
!= innate need
!= acquired habit
!= diagnosis
```

A future result may say:

> When autonomy and certainty competed in this session, autonomy won more often.

It must not silently transform this into:

> You are an autonomous type.

### 1.2 Independence of drivers

Candidate drivers are **not bipolar personality axes**.

A person may show strong evidence for both:

```text
Autonomy
AND
Certainty
```

The informative observation is what happens when they directly compete.

---

## 2. Theory Pack V2 — three layers

Theories are separated by function so that adding theoretical coverage does not become theory-shopping.

### Layer A — Measurement construct foundations

These frameworks are candidates for defining what is deliberately put into a future forced trade-off.

| Foundation | Measurement contribution |
|---|---|
| Revised Reinforcement Sensitivity Theory (rRST) | reward/approach, defensive avoidance, conflict-monitoring hypotheses |
| Regulatory Focus Theory | promotion/growth vs prevention/security goal pursuit |
| Schwartz Refined Theory of Basic Human Values | structured value priorities and trade-offs; openness, conservation, self-enhancement, self-transcendence |
| Self-Determination Theory (SDT) | autonomy, competence, relatedness |
| Need for Cognitive Closure | predictability/order/ambiguity tolerance candidate for Certainty |
| Paired-comparison / Random Utility methods | formal choice model; choices first, psychological claims later |
| Best-Worst / conjoint preference elicitation | explicit trade-off design precedent |
| Thurstonian forced-choice / IRT | later-stage person/item parameter modeling after a defensible calibrated item bank exists |

### Layer B — Decision modifiers and validation tasks

These are useful for testing **when** driver weights change, but should not automatically become permanent person scores.

| Method / theory | Candidate role |
|---|---|
| Prospect Theory / reference dependence | gain/loss framing modifier; not automatically a stable “loss-aversion trait” |
| Delay discounting | immediate-vs-delayed value modifier |
| Explore–Exploit paradigms | exploration strategy validation task; current evidence warns about task-specific reliability |
| Dual Process Theory | rationale for limiting deliberative self-presentation; does not make latency a psychological score |
| Cognitive Appraisal | context/meaning formation hypothesis |
| Gross Emotion Regulation | post-choice regulation/strategy lens |

### Layer C — Human/context interpretation lenses

Historical 14-framework package is retained, but most entries do **not** define the core score.

| Historical framework | Future role |
|---|---|
| Transactional Analysis | interpersonal/context interpretation |
| Karpman Drama Triangle | conflict-role/context hypothesis |
| Polyvagal Theory | contested; hypothesis/metaphor only, never scoring backbone |
| SCARF | social-context/confound lens: status, certainty, autonomy, relatedness, fairness |
| Attachment Theory | relational context / alternative explanation |
| Cognitive Distortions | interpretation/language lens |
| Locus of Control | agency/control alternative explanation |
| Schema Theory | history/context alternative explanation |
| Dual Process Theory | capture-process hypothesis |
| Nonviolent Communication | optional reflection/dialogue language |
| Thomas-Kilmann | conflict-response strategy lens |
| Self-Determination Theory | promoted upward into measurement foundations for autonomy/competence/relatedness |
| Gross Emotion Regulation | response strategy |
| Constructed Emotion Theory | guardrail against fixed emotion inference |

Rule:

> A Layer C theory may explain or challenge a result. It cannot retroactively manufacture the result.

---

## 3. Candidate Decision Drivers v0.1

These are **construct candidates**, not validated 2Pair dimensions.

| ID | Participant-language concept | Operational question | Main theoretical anchors |
|---|---|---|---|
| `DRV-OPP` | **Opportunity / Galimybė** | Does potential gain, growth, achievement, or advancement pull choice? | Regulatory Focus promotion; rRST BAS; Schwartz achievement/openness |
| `DRV-PRO` | **Protection / Apsauga** | Does reducing loss, threat, error, or downside pull choice? | Regulatory Focus prevention; rRST FFFS/BIS; Schwartz security |
| `DRV-AUT` | **Autonomy / Laisvė rinktis** | Does preserving choice, self-direction, or room to act pull choice? | SDT autonomy; Schwartz self-direction; SCARF autonomy |
| `DRV-CER` | **Certainty / Aiškumas** | Does predictability, clear structure, or reduced ambiguity pull choice? | Need for Cognitive Closure; SCARF certainty; Schwartz conservation/security |
| `DRV-EXP` | **Exploration / Tyrinėjimas** | Does novelty, discovery, optionality, or new information pull choice? | Schwartz stimulation/self-direction; explore–exploit as validation task |
| `DRV-MAS` | **Mastery / Meistriškumas** | Does competence, progress, challenge, or getting better pull choice? | SDT competence; Schwartz achievement |
| `DRV-CON` | **Connection / Ryšys** | Does belonging, care, cooperation, or maintaining relationship pull choice? | SDT relatedness; Schwartz benevolence; Attachment/SCARF as context lenses |
| `DRV-INF` | **Influence / Poveikis** | Does having impact, voice, status, or control over outcome pull choice? | Schwartz power/achievement; SCARF status; Thomas-Kilmann assertiveness |

### 3.1 Why eight, not a giant ontology

Eight is a **working candidate set** because it gives broad motivational coverage while remaining testable.

No driver is protected from deletion.

A driver survives only if it demonstrates:

1. semantic validity;
2. discriminant validity from neighboring drivers;
3. repeated response structure across independent exemplars;
4. external convergence where theory predicts it;
5. acceptable test-retest / context behavior;
6. useful participant-facing interpretation.

### 3.2 Known overlaps that must be challenged, not explained away

```text
Opportunity <-> Exploration
Protection  <-> Certainty
Autonomy    <-> Influence
Mastery     <-> Opportunity
Connection  <-> Protection in social contexts
```

The new methodology treats these overlaps as **falsification targets**.

If two proposed drivers cannot be separated empirically, merge or delete them.

---

## 4. Measurement is a tournament, not a questionnaire

The earlier value-clarification exercise used a simple but important mechanism:

```text
value A vs value B -> choose one
every value competes with every other
winner receives evidence
```

2Pair generalizes this idea from consciously named values to validated visual trade-offs.

### 4.1 Full round-robin reference design

Eight drivers have:

```text
8 × 7 / 2 = 28
```

unique driver-vs-driver collisions.

A full 28-collision round robin is a useful **calibration reference**, but may be too long for the final FUN experience.

### 4.2 Future adaptive tournament

A candidate product flow:

```text
BALANCED SCREEN
8–12 comparisons
each driver receives minimum coverage

        ↓

ADAPTIVE TOURNAMENT
next comparison selected where the current ordering is most uncertain
approximately 6–10 further comparisons

        ↓

OPTIONAL TIE-BREAK
0–4 comparisons if useful

        ↓

RESULT
```

Target product length for simulation/testing:

```text
~16–24 meaningful choices
```

This is a **design target, not a validated test length**.

The final stopping rule must be established through simulation and empirical calibration.

### 4.3 Winner-stays is useful UX, not enough statistics

A visible or hidden “winner faces a new opponent” mechanic can make the experience understandable and fun.

However, pure winner-stays has a weakness: early chance/item bias can dominate later ranking.

Therefore the statistical engine should ensure:

- balanced driver exposure;
- left/right counterbalancing;
- enough cross-links between drivers;
- occasional challenge of a current leader;
- no driver eliminated permanently after one loss.

---

## 5. Choice model

### 5.1 First defensible model: paired-comparison / random utility

For participant `p`, option feature vectors `xA`, `xB`, and participant driver weights `βp`:

```text
P(A chosen) =
logistic(
    βp · (xA - xB)
    + pair/item effects
    + position effects
    + validated perceptual-confound terms
)
```

This is a conceptual specification, not production code.

### 5.2 Why this is better than “one win = one point”

Simple win counts are acceptable for an early transparent prototype, but they cannot separate:

- easy vs difficult pairings;
- item dominance;
- presentation position;
- unequal comparison networks;
- perceptual bias;
- participant-specific trade-off strength.

The model should eventually estimate:

```text
participant driver weights
item/pair bias
position bias
uncertainty
```

rather than pretending each click carries equal information.

### 5.3 When Thurstonian IRT becomes relevant

Forced-choice IRT is promising **after**:

- items have defensible loadings;
- a sufficient calibrated pool exists;
- dimensionality has survived validation;
- simulations show adequate person-score recovery.

Do not use sophisticated IRT to formalize an unvalidated stimulus ontology.

### 5.4 “No clear choice”

`no_clear_choice` is not zero and not missing by default.

It may indicate:

- close utility / indifference;
- unclear stimulus;
- unresolved trade-off;
- technical/time failure.

Future analysis should distinguish these states. A tie-capable paired-comparison model may later be evaluated.

---

## 6. Latency has a bounded role

Current rule remains:

```text
CHOICE -> candidate driver evidence
LATENCY -> process telemetry
```

Latency does not multiply a driver score.

Future research may ask:

> Are some driver conflicts systematically slower than others?

But until independently established:

```text
fast != subconscious
slow != weak
timeout != neutrality
```

---

## 7. Future stimulus ontology

A future scoring item is not “a pretty pair of pictures.”

It is:

```text
VALIDATED DRIVER COLLISION
        +
CONTROLLED VISUAL REALIZATION
        +
KNOWN ITEM / POSITION / CONFOUND PROPERTIES
```

### 7.1 Each candidate pair requires

```text
neutral_pair_id
driver_A_candidate
driver_B_candidate
scene_family
variant_A_asset
variant_B_asset
visual_confound_metrics
blind_semantic_evidence
choice-distribution evidence
cross-exemplar evidence
external-validation evidence
scoring_status
```

Participant-facing assets never expose internal driver labels.

### 7.2 One pair can never define a driver

Minimum design principle:

> A driver must appear through multiple visually and contextually independent exemplars.

A single “Autonomy” picture is exactly the failure mode 2Pair must avoid.

### 7.3 Aesthetic nuisance model

Some pairs should deliberately function as **perceptual control probes** rather than psychological items.

Examples of nuisance preferences:

- brightness;
- contrast;
- symmetry;
- segmentation;
- visual complexity;
- object visibility;
- whitespace;
- sharp vs soft edges;
- left/right or top/bottom preference.

These can help estimate whether a supposed driver effect is actually an aesthetic preference.

---

## 8. Validation stack V2

A scoring item moves through explicit gates.

```text
S0 — SCENE / ASSET INTEGRITY
same intended context, no obvious defects

S1 — PERCEPTUAL CONFOUND AUDIT
brightness/contrast/complexity/salience/aesthetic dominance challenged

S2 — BLIND SEMANTIC VALIDATION
independent raters, unaware of driver labels, describe what differs

S3 — DRIVER DISCRIMINATION
target driver contrast beats neighboring-driver explanations

S4 — CHOICE REPRODUCIBILITY
effect survives position, form, device and independent exemplar changes

S5 — CROSS-EXEMPLAR CONVERGENCE
multiple scenes representing the same driver relationship cohere

S6 — EXTERNAL VALIDATION
expected convergence/discrimination against established measures/tasks

S7 — PERSON-PARAMETER RECOVERY
simulation + empirical model show that useful individual estimates are recoverable

S8 — SCORING ELIGIBLE
only now may the pair contribute to participant-facing driver inference
```

No `S8` item exists merely because it looks theoretically correct.

---

## 9. External-validation map

Candidate convergent checks:

| 2Pair candidate | External reference candidates |
|---|---|
| Opportunity | Regulatory Focus promotion; rRST BAS |
| Protection | Regulatory Focus prevention; rRST defensive systems; Schwartz security |
| Autonomy | SDT autonomy; Schwartz self-direction |
| Certainty | Need for Cognitive Closure; related order/predictability measures |
| Exploration | Schwartz stimulation/self-direction; multi-task exploration factor only with caution |
| Mastery | SDT competence; Schwartz achievement |
| Connection | SDT relatedness; Schwartz benevolence |
| Influence | Schwartz power/achievement; independent assertiveness/status measures |

Big Five / HEXACO are useful **discriminant and nomological validation references**, not the 2Pair result ontology.

---

## 10. Result architecture

The result must justify the effort of completing the experience.

### Layer 1 — Immediate visual payoff

Title candidate:

> **Kas stūmė tavo pasirinkimus?**

Show a visual map of the strongest supported pulls, not all internal psychometrics.

### Layer 2 — Decisive trade-offs

Examples:

> **Laisvė > Aiškumas**  
> Kai reikėjo rinktis tarp daugiau veikimo laisvės ir daugiau išankstinės struktūros, laisvė laimėjo dažniau.

> **Apsauga > Galimybė**  
> Kai atsirasdavo aiški praradimo rizika, apsauga dažniau nusverdavo papildomos naudos galimybę.

### Layer 3 — Close calls

Examples:

> **Ryšys ↔ Poveikis**  
> Čia aiškaus laimėtojo nebuvo. Tavo pasirinkimai keitėsi priklausomai nuo situacijos.

Close calls are useful, not failed scores.

### Layer 4 — “What changes your choice?”

Only after modifier experiments are validated:

- gain vs loss framing;
- time horizon;
- social vs nonsocial context;
- ambiguity;
- effort/cost.

### Layer 5 — Across sessions

The long-term differentiator:

```text
SESSION 1
SESSION 2
SESSION 3
        ↓
what persisted?
what changed?
under what contexts?
```

### Layer 6 — Optional reflection, not forced interrogation

The final product should not require a reason/intensity form after every pair.

Optional result-stage prompts may ask:

> Atpažįsti tai?

```text
TAIP / NE / NEŽINAU
```

or allow the participant simply to inspect the result.

Research validation can retain richer reason/free-text capture in a separate harness.

---

## 11. What 2Pair does and does not claim

### Candidate claim if validated

> Across multiple controlled trade-offs in this session, some motives had more influence on your choices than others.

### Not supported by this model alone

```text
This is innate.
This is acquired.
This is subconscious.
This is your personality type.
This predicts what you will do tomorrow.
This reveals your brain system.
```

These would require separate evidence.

---

## 12. Evidence from the scientific measurement literature

The backbone is intentionally assembled from established measurement families rather than a proprietary scoring invention.

Key current references:

1. Schwartz PVQ-RR cross-cultural psychometrics: 49 cultural groups, N=53,472, 32 language versions; value structure and trade-offs supported.  
   PMCID: `PMC9131418`, PMID: `33682477`.

2. Regulatory Focus: modern IPIP-RFS validation used 14 samples, N=4,867, including expert review, factor analysis, IRT, invariance, convergent/discriminant/predictive validity.  
   PMID: `39072767`, DOI: `10.1111/jopy.12962`.

3. SDT needs: 2024 meta-analysis, 4,561 effects from 881 independent samples, N=443,556, supports distinct autonomy/competence/relatedness support relationships.  
   PMID: `38635183`.

4. rRST: RST-PQ development and validation identified FFFS, BIS and four BAS facets with convergent/discriminant evidence.  
   PMID: `26845224`, DOI: `10.1037/pas0000273`.

5. Need for Cognitive Closure has an established individual-differences measurement tradition covering predictability, order/structure, ambiguity discomfort, decisiveness and closed-mindedness.  
   PMID: `7815301`.

6. Best-Worst Scaling and conjoint methods explicitly measure preferences through forced trade-offs rather than independent ratings.  
   PMID: `26743636`.

7. Thurstonian forced-choice models can recover person parameters, but recent methodological reviews emphasize serious design/model limitations; sophisticated scoring is not a substitute for valid item design.  
   PMID: `39055095`; PMID: `39601492`.

8. Adaptive forced-choice testing can reduce administration time, but benefits depend on calibrated items and test length; adaptive selection is a later optimization, not the first validation step.  
   PMID: `36750522`.

9. Explore–exploit individual-difference tasks currently show substantial task-specific psychometric limitations; a recent large study found single parameters had mediocre reliability and poor cross-task/external convergence, although a latent value-guided exploration factor improved to reliability ~0.78.  
   PMID: `40721436`.

10. Behavioral risk measures should not be assumed to reflect one stable universal trait: a 2025 meta-analysis of 358 measures / 579,114 respondents found low convergence and much lower reliability for behavioral than self-reported measures.  
    PMID: `39870880`.

11. Delay/probability discounting has a stronger measurement tradition, but a 2024 meta-analysis still found only modest omnibus test-retest reliability (`r ≈ .67`) with substantial moderators.  
    PMID: `38499476`.

Implication:

> The target should remain **decision-driver evidence in controlled contexts**, with stability treated as an empirical result rather than an assumption.

---

## 13. Version boundary

```text
2Pair Integrated Pilot v0.1
= frozen current research artifact
= historical CS/CR stimulus-validation + timing/UX evidence
= no driver scoring

2Pair Decision Driver Backbone v0.1
= future methodology design
= no current runtime change
= no Gate D/E promotion
= no participant claim yet
```

The current pilot can continue generating historical validation evidence while V2 develops a new item bank and validation contracts.

---

## 14. One-sentence future product definition

> **2Pair uses a sequence of controlled visual trade-offs to estimate which motives most often pull a person’s choices in the observed contexts, then shows those tensions back to the person without turning them into a type.**
