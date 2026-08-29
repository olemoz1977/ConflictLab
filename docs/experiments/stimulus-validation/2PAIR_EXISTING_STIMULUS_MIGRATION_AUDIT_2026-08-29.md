# 2Pair — Existing Stimulus Migration Audit for Decision-Driver V2

**Date:** 2026-08-29  
**Status:** FUTURE V2 MIGRATION AUDIT / NO RUNTIME CHANGE  
**Scope:** current six Wave 1 / Integrated research pairs plus archived ST-001..ST-010 stimulus concepts.  
**Critical boundary:** this audit does not reinterpret historical data as participant driver scores and does not modify `2pair-integrated-v0.1`.

---

## 1. Question

After the methodological pivot from:

```text
image property -> old CS/CR/AW candidate signal
```

toward:

```text
controlled visual trade-off
-> forced choice
-> repeated driver-vs-driver evidence
-> paired-comparison model
-> bounded participant result
```

do the current assets still have value?

### Short answer

**Yes, but not as a complete scoring bank.**

The current material splits into three future roles:

1. **Driver seed** — pair contains a plausible motivational trade-off worth revalidating.
2. **Perceptual control seed** — pair is more useful for estimating aesthetic / visual nuisance preference than a motivational driver.
3. **Scene-shell seed / archive** — scene idea may be reusable when rebuilding a V2 pair, but old hand-assigned AW/CS/CR weights do not migrate.

No existing asset is automatically `SCORING_ELIGIBLE`.

---

## 2. Evidence reviewed

### Current six pair assets

```text
CS-PR-01  more-reveal.webp        vs less-reveal.jpg
CS-RE-01  more-evidence.png       vs less-evidence.png
CS-CA-01  more-reference.png      vs less-reference.png
CR-PZ-01  no-predefined-zones.png vs predefined-zones.png
CR-FS-01  fixed-slots.png         vs continuous-capacity.png
CR-PO-01  partitioned-space.png   vs open-space.png
```

### Wave 1 v0.4 descriptive evidence

Current export reviewed:

```text
48 rows
10 participant IDs
20 non-empty free-text reasons
```

Historical review already established that among the seven complete 6/6 participant IDs, each pair stayed near a 4:3 or 3:4 asset split. That balance is useful for avoiding an obvious dominant image but **does not establish construct validity**.

`CS-PR-01` was already flagged because `hard_to_identify` was 3/7 (42.9%) among complete-session exposures and median latency was 12,543 ms.

### Archived ST library

Historical `Stimulus Matrix v1.0` contained ten candidate scenes:

```text
ST-001 window / withdrawal-waiting
ST-002 abstract figures / interaction
ST-003 blank page / uncertainty-beginning
ST-004 phone / waiting for reply
ST-005 empty table / waiting before interaction
ST-006 lone person in hall / isolation
ST-007 empty conference room / end-beginning
ST-008 corridor / movement-transition
ST-009 person at computer / work-detachment
ST-010 open doors / choice-transition
```

The historical protocol was designed for a different measurement architecture:

```text
single image
-> verbal reaction choices
-> hand-assigned AW/CS/CR weights
```

Therefore its old `review/beta/approved` labels do not mean “V2 scoring eligible.”

---

## 3. Current six-pair migration decisions

| Pair | What participants actually seemed to react to | Candidate V2 role | Migration decision |
|---|---|---|---|
| `CR-PO-01` | partitioning/organization vs freedom/no constraints | **Autonomy ↔ Certainty/Structure** | **KEEP AS PRIMARY V2 SEED; REVALIDATE** |
| `CS-PR-01` | visible detail/no hidden elements vs mystery/partial reveal | **Certainty ↔ Exploration** | **KEEP AS SECONDARY V2 SEED; REDESIGN/REVALIDATE** |
| `CR-PZ-01` | lines, zones, softness, dynamics, “clean” | perceptual segmentation / line-structure control | **CONTROL SEED, NOT DRIVER SCORE** |
| `CR-FS-01` | aesthetics, clarity, unpleasantness, “circles” | pattern/order/spacing nuisance control | **CONTROL SEED / WEAK; NOT DRIVER SCORE** |
| `CS-CA-01` | architectural composition, focus, clean composition | context/boundary/focus nuisance control | **CONTROL SEED, NOT DRIVER SCORE** |
| `CS-RE-01` | sharpness, visual discomfort, connector appearance | texture/sharpness/material nuisance control | **RETIRE AS DRIVER; POSSIBLE CONTROL ONLY** |

---

## 4. Pair-by-pair rationale

### 4.1 `CR-PO-01` — strongest bridge to V2

Assets:

```text
partitioned-space.png
open-space.png
```

Spontaneous Wave 1 reasons included:

```text
partitioned -> “Organized”
open        -> “Be suvaržymų”
open        -> “Laisvė, impeovizacija”
```

This is the only current pair where the participant language spontaneously landed very close to a **meaningful motivational trade-off** rather than merely image composition.

Candidate V2 mapping:

```text
partitioned -> Certainty / Structure
open        -> Autonomy / Freedom
```

Why this matters:

- both sides can be attractive;
- there is no morally “correct” answer;
- the trade-off is immediately participant-useful;
- it matches two independently grounded candidate drivers;
- it creates the kind of tension the future result can explain.

But it is **not yet scoring eligible** because:

1. one pair cannot define either driver;
2. partition walls also increase edge/segmentation complexity;
3. “organized” may reflect pure visual-order preference rather than decision motivation;
4. the same `Autonomy ↔ Certainty` relationship must replicate across independent scenes.

**Decision:** preserve as a V2 **seed exemplar**, create multiple independent versions, and validate blind semantics.

---

### 4.2 `CS-PR-01` — promising but difficult

Assets:

```text
more-reveal.webp
less-reveal.jpg
```

Spontaneous reasons:

```text
more -> “Be paslėptų detalių”
less -> “Paslaptingumas”
```

Candidate mapping:

```text
more reveal -> Certainty / informational clarity
less reveal -> Exploration / mystery / discovery
```

This is conceptually useful because both sides can be positively valued.

However current evidence also shows a major warning:

```text
hard_to_identify = 42.9% among complete-session exposures
median latency = 12,543 ms
```

Additional confounds:

- the sculpture’s visibility changes;
- the revealed object itself can be the main salience reward;
- one file is WEBP and one JPG in the historical pair;
- “mystery” may be an aesthetic preference rather than an exploration motive.

**Decision:** keep the *idea*, not the current pair as a scoring item. Rebuild with matched format and several new scene families.

---

### 4.3 `CR-PZ-01` — useful as a perceptual control

Spontaneous reasons:

```text
“Clean”
“Šviesa ir linijos.”
“Švelnios formos”
“Linijos suteikia dinamikos”
```

The response language is about **lines, cleanliness, softness and visual dynamics**, not a clear motivational conflict.

This makes the pair valuable in a different way.

Candidate V2 role:

> perceptual nuisance/control probe for segmentation, boundary lines and order.

If a participant repeatedly prefers partitions and zone lines in non-semantic controls, a supposed `Certainty` effect in motivational pairs may partly be visual-order preference.

**Decision:** do not score psychologically; consider retaining as a nuisance-control seed.

---

### 4.4 `CR-FS-01` — weak control, not a driver pair

Spontaneous reasons:

```text
“Esthetic look”
“Aiškesnis vaizdas.”
“Kažkodėl nemalonus buvo pirmas”
“Rutuliukai”
```

The intended fixed-slots / continuous-capacity concept is too subtle. Observed reasons mostly concern aesthetics, clarity, discomfort and object identity.

**Decision:** not suitable for Decision Driver scoring. It may be useful as a low-level pattern/order control after redesign, otherwise archive.

---

### 4.5 `CS-CA-01` — composition/focus control

Spontaneous reasons:

```text
“Architectural look”
“Pilnas fokusas į vazą, bet blaškančių elementų”
“Švari kompozicija”
```

The pair clearly changes visual composition and reference/boundary context.

It does **not** currently create a meaningful participant-level decision-driver collision.

Potential V2 control role:

```text
context boundary
visual focus
composition simplicity
```

**Decision:** control seed, not participant driver evidence.

---

### 4.6 `CS-RE-01` — no defensible driver mapping

Reasons include:

```text
“Sharper look”
“Pirmasis vertė jaustis nejaukiai”
“Ryskiau”
```

Historical v0.3 free-text also included difficulty understanding the depicted object.

The difference between a transparent/metal connector and a solid connector is visually noticeable but motivationally unclear.

**Decision:** retire as a driver item. Only retain if a precise perceptual-control purpose is defined and validated.

---

## 5. Preliminary low-level visual audit

A private engineering audit computed basic grayscale/edge metrics from the current exact assets.

These are **not psychophysical validation**. They are only a quick confound screen.

Approximate within-pair structural similarity (SSIM; 1.0 = more visually similar):

| Pair | SSIM | Preliminary note |
|---|---:|---|
| `CR-PZ-01` | 0.971 | extremely similar; added lines are a concentrated manipulation |
| `CS-CA-01` | 0.955 | very similar composition; boundary/reference manipulation |
| `CS-RE-01` | 0.932 | connector material/edge difference |
| `CS-PR-01` | 0.920 | object reveal / occlusion difference |
| `CR-FS-01` | 0.911 | item position / pattern difference |
| `CR-PO-01` | 0.856 | strongest structural manipulation due to partition walls |

Other basic metrics show, for example, that `CR-PO-01` partitioning adds edge density and changes luminance/contrast slightly, while `CR-PZ-01` adds line-edge density despite otherwise high structural similarity.

Implication:

> V2 must model low-level perceptual differences as possible nuisance variables rather than assuming that a matched scene guarantees a motivational manipulation.

---

## 6. Archived ST-001..ST-010 migration

### 6.1 General verdict

The old library remains valuable as a **scene/concept archive**, but its scoring architecture should not migrate.

Historical reviews explicitly documented risks that are directly relevant to V2:

- social desirability;
- projection into the depicted figure;
- visual mood/narrative bias;
- AI artifacts;
- AW vs CR construct confusion;
- asymmetric answer options;
- verbal answer choices doing much of the psychological work.

The V2 pivot removes the weakest part:

```text
OLD
image -> verbal interpretation option -> hand-assigned signal weight

V2
paired controlled scenes -> forced visual choice -> calibrated trade-off model
```

### 6.2 Scene-shell migration table

| Old scene | V2 reuse potential | Candidate future use |
|---|---|---|
| `ST-001` person at window | **LOW** | archive / mood-bias example; rain + back-facing figure is too narrative |
| `ST-002` abstract figures | **HIGH** | Connection, Influence, Autonomy social trade-off scene shell |
| `ST-003` blank page | **HIGH** | Exploration ↔ Certainty; Opportunity ↔ Protection if visualized without verbal labels |
| `ST-004` phone waiting | **MEDIUM** | Connection/Certainty context, but narrative assumptions must be controlled |
| `ST-005` empty table | **LOW–MEDIUM** | generic social preparation context; lacks clear trade-off by itself |
| `ST-006` lone person in hall | **LOW** | archive; strong loneliness/isolation narrative |
| `ST-007` empty conference room | **MEDIUM–HIGH** | Opportunity/Mastery/Influence context if rebuilt as a true two-driver choice |
| `ST-008` corridor | **HIGH** | transition context for Exploration/Certainty or Opportunity/Protection |
| `ST-009` person at computer | **MEDIUM** | Mastery/Connection/Autonomy work context, but human/narrative confounds |
| `ST-010` open doors | **HIGH** | excellent neutral transition/choice shell for Opportunity/Protection or Exploration/Certainty |

### 6.3 Historical “approved” does not equal V2 valid

`ST-010` scored 93/100 and was “approved” under the old library protocol.

That status means:

> it performed well against the **old** visual/reaction/AW-CS-CR review criteria.

It does **not** mean:

> it is a validated Autonomy, Opportunity, Protection, or Exploration item.

V2 must run new validation from the construct level upward.

---

## 7. What survives from the old Validation Protocol

The historical protocol’s core principle remains excellent:

> **Stimulas nematuoja žmogaus. Stimulas sukuria sąlygas stebėti reakciją.**

Keep/upgrade:

- visual integrity;
- AI artifact checks;
- cultural/demographic confound review;
- no obvious “good” answer;
- construct discrimination;
- library/context diversity;
- empirical validation;
- explicit removal criteria.

Replace:

- hand-assigned AW/CS/CR weights;
- single-image verbal reaction as the main measurement unit;
- “three theories validate the stimulus” as enough construct evidence;
- old axis-balance rules.

Add:

- explicit driver-vs-driver collision specification;
- blind semantic rating before unblinding;
- paired perceptual confound matching;
- multiple independent exemplars per driver;
- cross-exemplar convergence;
- external convergent/discriminant validation;
- paired-comparison model recovery;
- adaptive-test simulation before product shortening.

---

## 8. V2 asset roles

Future library should explicitly separate:

```text
A. DRIVER ITEMS
meaningful motivational collision
eligible for future scoring only after all validation gates

B. PERCEPTUAL CONTROLS
brightness / order / segmentation / salience / whitespace / complexity
never directly interpreted as a motive

C. SCENE SHELLS
reusable contexts from historical library
not scored until rebuilt and validated

D. HISTORICAL ARCHIVE
kept for provenance only
```

This prevents a recurring mistake:

> every visual difference does not need to “mean something psychological.”

Some differences are useful precisely because they help estimate what **does not** belong to the psychological model.

---

## 9. Current-bank conclusion

### Current six

```text
CR-PO-01  -> strongest V2 motivational seed
CS-PR-01  -> promising V2 seed, requires redesign
CR-PZ-01  -> perceptual control candidate
CR-FS-01  -> weak perceptual control / archive
CS-CA-01  -> perceptual control candidate
CS-RE-01  -> retire as driver; control only if a clear nuisance target is specified
```

### Historical ST library

```text
not discarded
not scored
reclassified as scene-shell / archive material
```

### Current Integrated pilot

```text
UNCHANGED
FROZEN
historical methodology continues as-is
no V2 scoring retrofitted
```

---

## 10. Next build implication

The next new stimulus work should **not** be “make more CS/CR images.”

It should be:

```text
choose one driver collision
-> define both motives in participant language
-> specify falsifiable alternative explanations
-> build 3–4 independent scene exemplars
-> add matched perceptual controls
-> blind semantic validation
-> empirical choice/reason validation
-> only then estimate pairwise driver evidence
```

Recommended first collision because current evidence already contains one strong seed:

> **Autonomy / Laisvė rinktis ↔ Certainty / Aiškumas-struktūra**

Recommended second collision:

> **Certainty / Aiškumas ↔ Exploration / Tyrinėjimas-paslaptis**

These are starting hypotheses, not privileged permanent axes.
