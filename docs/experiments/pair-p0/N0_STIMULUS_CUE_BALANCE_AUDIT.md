# N0 — Stimulus and Cue Balance Audit

**Date:** 2026-08-05
**Base:** `pair-p0-m0-remote-beta-stable`
**Scope:** Documentation only. No code, JSON, or scheduler changes in this stage.

> **Audit integrity note (added during review):**
> An earlier draft of this document contained numeric values labeled as "semantic distance" (e.g., 0.45, 0.48, 0.49–1.23) presented as if they were computed measurements. These values have been removed because no embedding model, distance metric, language, normalization procedure, or reproducible computation was specified or documented. They are not valid measurements. All judgments about cue overlap in this document are **manual audit judgments** based on reading and comparison, not computed distances.

---

## 1. Purpose

Evaluate the current 3 Pair P0 image pairs and their cue sets against a methodological standard, before designing the remaining 6 pairs needed for a 9-pair, non-repeating 3-session library. This document is the first deliverable; it precedes any implementation.

---

## 2. Audit criteria (per pair)

- **Visual balance** — do the two images differ only in the intended dimension, or do other visual factors (lighting, framing, color temperature, composition) differ enough to introduce noise?
- **Emotional valence** — does one image read as more positive/negative than the other independent of the intended axis?
- **Arousal level** — does one image appear calmer/more agitated than the other for reasons unrelated to the intended contrast?
- **Image complexity** — do the two images differ in visual complexity (detail density, clutter) in a way that could bias attention rather than reflect the intended choice?
- **Social content** — does either image contain people, faces, or implied social presence that the other lacks?
- **Interpretive openness** — how many plausible readings does each image support, and are those readings roughly symmetric between A and B?
- **Position bias risk** — is there anything in the images themselves (not just position randomization in code) that could systematically favor top/bottom or left/right?
- **Axis/direction coverage** — which of AW/CS/CR each pair's cues are designed to probe, and whether the three current pairs together already cover a spread or cluster narrowly.
- **Semantic overlap across cues** — do any two cues within the same image cover such similar ground that a participant could plausibly choose either one for the same reason? *(Manual audit judgment — no computed metric.)*
- **Cue valence balance** — do the three cues for one image skew toward one emotional tone?
- **Cue strength vs. image strength** — could a cue's wording be strong enough to overwrite the visual impression rather than merely naming a reaction to it?
- **Cue attractiveness asymmetry** — is any single cue phrased in a way that feels obviously more articulate, socially desirable, or "correct" than its siblings, which could pull disproportionate selection regardless of the person's actual reaction?

---

## 3. Pair-by-pair audit

> **Key to annotation type:**
> - `[OBSERVED FACT]` — directly verifiable from the image or JSON
> - `[MANUAL AUDIT JUDGMENT]` — based on reading and comparison, not measurement
> - `[METHODOLOGICAL RECOMMENDATION]` — a proposed course of action
> - `[UNRESOLVED QUESTION]` — requires human methodological decision

### P0-001 — Shoes (formal black vs. casual brown)

| Dimension | Observation |
|---|---|
| Visual balance | `[OBSERVED FACT]` Same table, same floor, same lighting, same rain-drop overlay on both images. Framing and composition are near-identical — this is the best-balanced pair visually of the three. |
| Emotional valence | `[MANUAL AUDIT JUDGMENT]` Roughly symmetric — neither shoe style reads as clearly more positive or negative; the contrast is closer to "formal/structured" vs. "casual/free" than "good/bad." |
| Arousal | `[MANUAL AUDIT JUDGMENT]` Low and comparable on both sides; this is a calm, static scene either way. |
| Complexity | `[OBSERVED FACT]` Nearly identical — same number of visual elements, same background detail level. |
| Social content | `[OBSERVED FACT]` None in either image. |
| Interpretive openness | `[MANUAL AUDIT JUDGMENT]` Both images support a similarly narrow set of readings (readiness/formality vs. freedom/casualness). Fairly symmetric. |
| Position bias risk | `[MANUAL AUDIT JUDGMENT]` Low — the visual balance minimizes this. |
| Axis coverage | `[OBSERVED FACT]` `primary_axis: cr` for both images — this pair probes control/structure vs. release, consistent with its dev_notes framing. |
| Cue semantic overlap | `[MANUAL AUDIT JUDGMENT]` Image A cues C1 ("Noriu būti pasiruošęs") and C3 ("Atrodo patikima") cover similar ground — both express readiness/reliability and could plausibly be chosen for the same reason. This is a **high semantic overlap** judgment based on reading, not a computed distance. |
| Cue valence balance | `[MANUAL AUDIT JUDGMENT]` Image A: C1 and C3 both lean mildly positive/neutral, C2 ("Per daug įpareigoja") is the lone negative-leaning cue — 2:1 skew. Image B is better balanced (C1 positive, C2 negative, C3 neutral-active). |
| Cue vs. image strength | `[MANUAL AUDIT JUDGMENT]` None of the six cues appear to overpower the visual — wording stays at the level of a personal reaction. |
| Cue attractiveness asymmetry | `[MANUAL AUDIT JUDGMENT]` Image A's C3 ("Atrodo patikima") reads as a slightly more socially comfortable/articulate answer than C2, which risks becoming a default "safe pick." |

**Decision: REVISE**
`[METHODOLOGICAL RECOMMENDATION]`
Primary reason: Image A's cue set has a semantic overlap risk between C1 and C3 (manual audit judgment), and a 2:1 valence skew. The visual pairing itself is sound and should be kept as-is; only the cue set for Image A needs rebalancing.

---

### P0-002 — Gate (open vs. closed)

| Dimension | Observation |
|---|---|
| Visual balance | `[OBSERVED FACT]` Both images share the same gate, same stonework, same garden framing, same lighting. Very tightly matched — essentially the same photograph with the gate state changed. |
| Emotional valence | `[MANUAL AUDIT JUDGMENT]` The "open" state has a naturally more inviting/positive connotation and the "closed" state a naturally more restrictive/negative one, independent of any cue. This is an inherent valence asymmetry built into the visual premise itself (open vs. closed as a concept), not a photography flaw. It is worth naming explicitly, since it could pre-bias interpretation before any cue is even shown. |
| Arousal | `[MANUAL AUDIT JUDGMENT]` Comparable — static garden scene either way. |
| Complexity | `[OBSERVED FACT]` Identical framing, foliage, and stonework on both sides. |
| Social content | `[OBSERVED FACT]` None. |
| Interpretive openness | `[MANUAL AUDIT JUDGMENT]` Moderate on both, but "open gate" more strongly pulls toward a single dominant reading (invitation/passage) than "closed gate," which supports more varied readings (safety, exclusion, privacy, unfinished business). |
| Position bias risk | `[MANUAL AUDIT JUDGMENT]` Low from the image content itself. |
| Axis coverage | `[OBSERVED FACT]` `primary_axis: aw` (approach/withdrawal) for both — this pair is the project's clearest AW probe. |
| Cue semantic overlap | `[MANUAL AUDIT JUDGMENT]` Reasonably distinct within each image — no near-duplicate cue pairs identified in manual review. **Sufficiently distinct in manual review.** |
| Cue valence balance | `[MANUAL AUDIT JUDGMENT]` Image A: C1 positive, C2 negative, C3 neutral/ambivalent — well balanced. Image B: C1 positive-leaning ("Čia saugiau"), C2 negative ("Mane stabdo"), C3 curious/neutral — also balanced. |
| Cue vs. image strength | `[MANUAL AUDIT JUDGMENT]` Fine — none of the cues make a stronger claim than the image supports. |
| Cue attractiveness asymmetry | `[MANUAL AUDIT JUDGMENT]` None of the cues stands out as an obviously "better" answer; the set reads as genuinely open-ended. |

**Decision: KEEP WITH CAVEAT**
`[METHODOLOGICAL RECOMMENDATION]`
This is the most methodically solid pair of the three. The caveat (not a defect requiring rework, but a documented limitation): the built-in valence asymmetry of "open" vs. "closed" as a concept should inform how future open/closed-type pairs in the library are designed, so the effect is not silently repeated across multiple pairs.

`[UNRESOLVED QUESTION]` Whether this inherent conceptual asymmetry is considered an acceptable disclosed limitation, or whether future "state contrast" pairs should actively avoid concepts with a built-in positive/negative lean, requires human methodological decision.

---

### P0-003 — Box (open with tissue paper vs. closed and taped)

| Dimension | Observation |
|---|---|
| Visual balance | `[OBSERVED FACT]` The two photographs do not appear to come from the same shoot — different table surface (warm wood-tone vs. cool white/grey), different background (bookshelf visible vs. blurred furniture), different lighting temperature. This is the weakest visual match of the three pairs. |
| Emotional valence | `[MANUAL AUDIT JUDGMENT]` The open box (soft tissue paper, warm lighting) reads as more inviting; the closed, taped box (cooler lighting, visible tape seam) reads as more neutral-to-guarded. This adds an emotional cue on top of the intended open/closed contrast. |
| Arousal | `[MANUAL AUDIT JUDGMENT]` Comparable, both static tabletop scenes. |
| Complexity | `[MANUAL AUDIT JUDGMENT]` Similar object complexity, but background complexity differs (bookshelf with visible books vs. blurred indistinct furniture) — a confound the other two pairs avoid. |
| Social content | `[OBSERVED FACT]` None. |
| Interpretive openness | `[MANUAL AUDIT JUDGMENT]` Comparable to P0-002; open/closed box supports similar readings (curiosity, anticipation vs. completion, restraint). |
| Position bias risk | `[MANUAL AUDIT JUDGMENT]` The lighting/color-temperature difference could create a subtle preference for the "warmer" image regardless of open/closed state — this is a confound worth controlling in a revision. |
| Axis coverage | `[OBSERVED FACT]` `primary_axis: cs` (clarity-seeking/ambiguity-tolerance) for both — the project's clearest CS probe. |
| Cue semantic overlap | `[MANUAL AUDIT JUDGMENT]` Image A cues C1 ("Pagaliau aišku") and C3 ("Kažko trūksta") cover partially overlapping ground — both relate to a sense of resolution/incompleteness and could be read as expressing similar states. **Partial semantic overlap** — manual audit judgment, not a computed distance. |
| Cue valence balance | `[MANUAL AUDIT JUDGMENT]` Image A: C1 positive/resolved, C2 negative/wistful, C3 negative/unsettled — 2:1 skew toward the negative pole. Image B is better balanced (curious, patient, avoidant — three genuinely distinct tones). |
| Cue vs. image strength | `[MANUAL AUDIT JUDGMENT]` Acceptable, no cue overpowers the image. |
| Cue attractiveness asymmetry | `[MANUAL AUDIT JUDGMENT]` Image A's C1 ("Pagaliau aišku") reads as the most immediately satisfying/resolved answer and may pull disproportionate selection as a "close the loop" default, independent of the person's actual felt reaction. |

**Decision: REVISE**
`[METHODOLOGICAL RECOMMENDATION]`
Two independent issues, separated:
1. **Visual production issue** `[OBSERVED FACT]` — the two photographs do not appear to come from a matched shoot. This is an asset problem, not a cue-wording problem, and should be corrected by reshooting or better-matching the pair before wider use.
2. **Cue-set issue** `[MANUAL AUDIT JUDGMENT]` — partial semantic overlap between C1 and C3, and a valence skew (2 negative, 1 positive) in Image A.

---

## 4. Summary table

| Pair | Image A risk | Image B risk | Visual balance | Cue balance | Axis coverage | Cue overlap (manual) | Main distortion risk | Decision |
|---|---|---|---|---|---|---|---|---|
| P0-001 (shoes) | Medium (cue overlap + valence skew) | Low | High | Medium | CR | High — C1 and C3 cover similar ground | A cue's C3 reads as the "safe/articulate" default answer | **REVISE** |
| P0-002 (gate) | Low | Low | High | High | AW | Sufficiently distinct | Inherent open/closed valence asymmetry (conceptual, not photographic) | **KEEP WITH CAVEAT** |
| P0-003 (box) | High (visual mismatch + cue overlap + valence skew) | Low | Low | Medium | CS | Partial — C1 and C3 cover partially overlapping ground | Different shoot/lighting; A's C1 reads as the "resolved" default answer | **REVISE** |

> `[INTEGRITY NOTE]` The earlier draft of this table contained numeric distance values (0.45, 0.48, 0.49–1.23). These have been removed. No embedding model, metric, language, or computation was defined. The cue overlap column now reflects manual audit judgment only.

---

## 5. Requirements for the remaining 6 pairs

### 5.1 Stimulus families to add

The current 3 pairs cover three concrete, literal object-states (footwear formality, gate state, box state). To reach 9 pairs without visual/semantic repetition, the additional 6 should span families distinct from "single object, two states":

**5 non-social pairs:**

- A **spatial/environmental** family (e.g., a path forking, a room seen from two vantage points) — tests approach/withdrawal without relying on a manufactured object.
- A **temporal/process** family (e.g., something mid-repair vs. finished, a plant early vs. late in growth) — tests clarity-seeking/ambiguity-tolerance via process state rather than container state, avoiding a second "box" or "container" pair.
- A **texture/material contrast** family unrelated to open/closed states (e.g., rough vs. smooth surface, natural vs. manufactured material) — to avoid the library becoming dominated by an "open vs. closed" theme.
- A **light/weather** family where the only deliberate variable is ambient condition (e.g., overcast vs. sunlit version of the same otherwise-identical scene) — this would isolate arousal/valence effects of lighting itself, which the current 3 pairs conflate with their primary contrast.
- A **direction/orientation** family (e.g., an object or path oriented toward vs. away from the viewer) — to test approach/withdrawal through spatial framing rather than an object's open/closed state.

**1 neutral social-proximity pair:**

`[METHODOLOGICAL RECOMMENDATION]` N0 identifies the absence of social content as the single largest coverage gap. One pair — out of six — should introduce a minimal, controlled amount of implied social presence to allow the library to observe whether social proximity affects choice and cue selection.

Constraints for this pair:
- No faces in close-up
- No explicit conflict scene
- No status, gender, or threat interpretation implied
- Contrast based on spatial distance or physical proximity only (e.g., two figures at a distance vs. close, or an empty vs. occupied bench)
- `[UNRESOLVED QUESTION]` The project must decide whether to proceed with this pair. Including it is a recommendation based on the coverage gap; excluding it is also valid if social projection risks are considered premature to introduce at this stage.

### 5.2 Directions currently under-covered

`[OBSERVED FACT]` All 3 current pairs use cr, aw, cs as isolated primary axes, one per pair.

`[OBSERVED FACT]` No pair currently includes any social content.

`[OBSERVED FACT]` No pair currently isolates lighting/weather as the sole variable.

`[OBSERVED FACT]` No pair uses a moving or implied-motion visual.

`[MANUAL AUDIT JUDGMENT]` There is no current pair designed to probe a blended or ambiguous axis combination.

`[UNRESOLVED QUESTION]` Should any of the 6 new pairs deliberately combine two axes? Current recommendation: no — keep one primary axis per pair until the single-axis model has been validated by beta data.

### 5.3 Avoiding visual and semantic repetition

- Do not reuse "container with contents" as a concept (avoids echoing P0-003).
- Do not reuse "barrier/threshold" as a concept (avoids echoing P0-002).
- Do not reuse "paired manufactured objects differing only in style" as a concept (avoids echoing P0-001).
- Ensure new pairs are shot (or generated) as genuinely matched pairs from the same setup — same lighting temperature, same background, same camera distance — learning directly from the production inconsistency identified in P0-003.
- Ensure no two pairs in the full 9-pair set share the same primary_axis assignment more than 3 times (3 pairs per axis across AW/CS/CR).

### 5.4 Cue structure requirements for new pairs

`[METHODOLOGICAL RECOMMENDATION]`
- Each image's 3 cues should be **sufficiently distinct** from one another — meaning no two cues within the same image should cover such similar ground that a participant could plausibly choose either for the same reason. Judgment is manual during cue authoring; no numeric threshold is defined at this stage.
- Each image's 3 cues should maintain **valence balance** — not 2:1 or 3:0 skewed toward one emotional pole, unless that skew is a deliberate, documented methodological choice for a specific pair.
- No single cue within a set should be phrased so as to be the obvious "most resolved," "most correct," or "most articulate" answer relative to its siblings.
- Cue wording should stay at the level of a personal reaction ("I want...", "It feels...") rather than a diagnostic or interpretive claim.

---

## 6. Open questions requiring human methodological judgment

`[UNRESOLVED QUESTION — requires human decision before proceeding]`

1. **P0-003 visual mismatch** — should this pair be reshot/regenerated to match lighting and background before any wider test, or is the current version acceptable for continued internal QA while a matched replacement is prepared separately?

2. **P0-002's inherent open/closed valence asymmetry** — is this considered an acceptable, disclosed limitation (since it stems from the concept itself, not the execution), or should future "state contrast" pairs actively avoid concepts with a built-in positive/negative lean?

3. **Social content pair** — should the library include one neutral social-proximity pair in the next 6, or defer it to a later expansion? This requires human judgment about acceptable interpretive risk at this stage.

4. **Blended-axis pairs** — should any of the 6 new pairs be designed to deliberately combine two axes, or should the library stay strictly one-axis-per-pair for consistency with the current 3? Current recommendation: stay one-axis-per-pair until single-axis model is validated.

5. **Cue overlap threshold** — no numeric threshold for cue semantic distance is defined in this document. Judgment remains manual during cue authoring. If a principled, reproducible threshold is needed in future, it must be defined with: embedding model, metric (cosine similarity / cosine distance / Euclidean), language (LT or EN), normalization procedure, and a documented computation. This is an open infrastructure question, not a resolved one.

6. **P0-001-A and P0-003-A cue revisions** — should these be corrected before the 6 new pairs are designed, or should all cue rebalancing happen in one pass after the full 9-pair set is drafted?
