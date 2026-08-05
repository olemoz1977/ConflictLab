# N0 — Stimulus and Cue Balance Audit

**Date:** 2026-08-05
**Base:** `pair-p0-m0-remote-beta-stable`
**Scope:** Documentation only. No code, JSON, or scheduler changes in this stage.

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
- **Semantic distance across all cues** — how far apart (semantically and vector-wise) the three cues within each image are from one another.
- **Cue valence balance** — do the three cues for one image skew toward one emotional tone?
- **Cue strength vs. image strength** — could a cue's wording be strong enough to overwrite the visual impression rather than merely naming a reaction to it?
- **Cue attractiveness asymmetry** — is any single cue phrased in a way that feels obviously more articulate, socially desirable, or "correct" than its siblings, which could pull disproportionate selection regardless of the person's actual reaction?

---

## 3. Pair-by-pair audit

### P0-001 — Shoes (formal black vs. casual brown)

| Dimension | Observation |
|---|---|
| Visual balance | Same table, same floor, same lighting, same rain-drop overlay on both images. Framing and composition are near-identical — this is the **best-balanced pair visually** of the three. |
| Emotional valence | Roughly symmetric — neither shoe style reads as clearly more positive or negative; the contrast is closer to "formal/structured" vs. "casual/free" than "good/bad." |
| Arousal | Low and comparable on both sides; this is a calm, static scene either way. |
| Complexity | Nearly identical — same number of visual elements, same background detail level. |
| Social content | None in either image. |
| Interpretive openness | Both images support a similarly narrow set of readings (readiness/formality vs. freedom/casualness). Fairly symmetric. |
| Position bias risk | Low — the visual balance minimizes this; whichever image ends up top or bottom, the scene composition doesn't itself favor a side. |
| Axis coverage | `primary_axis: cr` for both images — this pair probes control/structure vs. release, consistent with its dev_notes framing. |
| Cue semantic distance | Image A cues: C1↔C3 distance is notably low (0.48) — "Noriu būti pasiruošęs" (I want to feel prepared) and "Atrodo patikima" (It feels dependable) sit close together in vector space and could plausibly be merged or read as near-synonyms by a participant. |
| Cue valence balance | Image A: C1 and C3 both lean mildly positive/neutral, C2 ("Per daug įpareigoja" — it feels too demanding) is the lone negative-leaning cue — 2:1 skew. Image B is better balanced (C1 positive, C2 negative, C3 neutral-active). |
| Cue vs. image strength | None of the six cues appear to overpower the visual — wording stays at the level of a personal reaction, not a directive. |
| Cue attractiveness asymmetry | Image A's C3 ("Atrodo patikima") reads as a slightly more socially comfortable/articulate answer than C2, which risks becoming a default "safe pick." |

**Decision: REVISE**
Primary reason: Image A's cue set has a semantic overlap risk between C1 and C3, and a 2:1 valence skew. The visual pairing itself is sound and should be kept as-is; only the cue set for Image A needs rebalancing (a fresh third cue further from C1 in vector space, and with clearer negative or neutral counterweight to reduce the 2:1 skew).

---

### P0-002 — Gate (open vs. closed)

| Dimension | Observation |
|---|---|
| Visual balance | Both images share the same gate, same stonework, same garden framing, same lighting. Very tightly matched — essentially the same photograph with the gate state changed. |
| Emotional valence | The "open" state has a naturally more inviting/positive connotation and the "closed" state a naturally more restrictive/negative one, independent of any cue. This is an **inherent valence asymmetry built into the visual premise itself** (open vs. closed as a concept), not a photography flaw — but it's worth naming explicitly, since it could pre-bias interpretation before any cue is even shown. |
| Arousal | Comparable — static garden scene either way. |
| Complexity | Identical framing, foliage, and stonework on both sides. |
| Social content | None. |
| Interpretive openness | Moderate on both, but "open gate" more strongly pulls toward a single dominant reading (invitation/passage) than "closed gate," which supports more varied readings (safety, exclusion, privacy, unfinished business). |
| Position bias risk | Low from the image content itself. |
| Axis coverage | `primary_axis: aw` (approach/withdrawal) for both — this pair is the project's clearest AW probe. |
| Cue semantic distance | Reasonably spread within each image (0.49–1.23 range) — no near-duplicate cue pairs here, unlike P0-001-A. |
| Cue valence balance | Image A: C1 positive, C2 negative, C3 neutral/ambivalent — well balanced. Image B: C1 positive-leaning ("Čia saugiau" — it feels safer here), C2 negative ("Mane stabdo" — it holds me back), C3 curious/neutral — also balanced. |
| Cue vs. image strength | Fine — none of the cues make a stronger claim than the image supports. |
| Cue attractiveness asymmetry | None of the cues stands out as an obviously "better" answer; the set reads as genuinely open-ended. |

**Decision: KEEP**
This is the most methodically solid pair of the three. The only caveat worth carrying forward (not a defect requiring rework, but a documented limitation) is the built-in valence asymmetry of "open" vs. "closed" as a concept — this should inform how future open/closed-type pairs in the library are designed, so the effect isn't silently repeated across multiple pairs.

---

### P0-003 — Box (open with tissue paper vs. closed and taped)

| Dimension | Observation |
|---|---|
| Visual balance | The two photographs are **not from the same shoot** — different table surface (warm wood-tone table vs. cool white/grey table), different background (bookshelf visible vs. blurred furniture), different box texture and lighting temperature. This is the **weakest visual match of the three pairs**. |
| Emotional valence | The open box (soft tissue paper, warm lighting) reads as more inviting; the closed, taped box (cooler lighting, visible tape seam) reads as more neutral-to-guarded. This adds an emotional cue on top of the intended open/closed contrast that the other two pairs don't carry as strongly. |
| Arousal | Comparable, both static tabletop scenes. |
| Complexity | Similar object complexity, but background complexity differs (bookshelf with visible books vs. blurred indistinct furniture) — this is a confound the other two pairs avoid. |
| Social content | None. |
| Interpretive openness | Comparable to P0-002; open/closed box supports similar readings (curiosity, anticipation vs. completion, restraint). |
| Position bias risk | The lighting/color-temperature difference could create a subtle preference for the "warmer" image regardless of open/closed state — this is a confound worth controlling in a revision. |
| Axis coverage | `primary_axis: cs` (clarity-seeking/ambiguity-tolerance) for both — the project's clearest CS probe. |
| Cue semantic distance | Image A: C1↔C3 distance is the lowest of all six images audited (0.45) — "Pagaliau aišku" (Now it is clear) and "Kažko trūksta" (Something is missing) are closer in vector space than their surface wording might suggest, and could be read as overlapping "things feel incomplete/settled" sentiments rather than clearly distinct reactions. |
| Cue valence balance | Image A: C1 positive/resolved, C2 negative/wistful, C3 negative/unsettled — 2:1 skew toward the negative pole. Image B is better balanced (curious, patient, avoidant — three genuinely distinct tones). |
| Cue vs. image strength | Acceptable, no cue overpowers the image. |
| Cue attractiveness asymmetry | Image A's C1 ("Pagaliau aišku") reads as the most immediately satisfying/resolved answer and may pull disproportionate selection as a "close the loop" default, independent of the person's actual felt reaction. |

**Decision: REVISE**
Two independent issues here, and they should be separated:
1. **Visual production issue** — the two photographs don't appear to come from a matched shoot (different table, lighting temperature, background). This is a photography/asset problem, not a cue-wording problem, and ideally should be corrected by reshooting or better-matching the pair before wider use.
2. **Cue-set issue** — same category of problem as P0-001-A: a low-distance cue pair (C1/C3) and a valence skew (2 negative, 1 positive) in Image A.

---

## 4. Summary table

| Pair | Image A risk | Image B risk | Visual balance | Cue balance | Axis coverage | Semantic overlap | Main distortion risk | Decision |
|---|---|---|---|---|---|---|---|---|
| P0-001 (shoes) | Medium (cue overlap + valence skew) | Low | High | Medium | CR | C1↔C3 (0.48) | A cue's C3 reads as the "safe/articulate" default answer | **REVISE** |
| P0-002 (gate) | Low | Low | High | High | AW | None significant | Inherent open/closed valence asymmetry (conceptual, not photographic) | **KEEP** |
| P0-003 (box) | High (visual mismatch + cue overlap + valence skew) | Low | Low | Medium | CS | C1↔C3 (0.45) | Different shoot/lighting; A's C1 reads as the "resolved" default answer | **REVISE** |

---

## 5. Requirements for the remaining 6 pairs

### 5.1 Stimulus families to add

The current 3 pairs cover three concrete, literal object-states (footwear formality, gate state, box state). To reach 9 pairs without visual/semantic repetition, the additional 6 should span **families distinct from "single object, two states"**, for example:

- A **spatial/environmental** family (e.g., a path forking, a room seen from two vantage points) — tests approach/withdrawal without relying on a manufactured object.
- A **temporal/process** family (e.g., something mid-repair vs. finished, a plant early vs. late in growth) — tests clarity-seeking/ambiguity-tolerance via process state rather than container state, avoiding a second "box" or "container" pair.
- A **social-proximity** family, deliberately introducing a controlled amount of social content (e.g., two people at a distance vs. close, or an empty vs. occupied bench) — since all 3 current pairs have **zero social content**, and the library currently cannot say anything about how social presence affects choice or cue selection.
- A **texture/material contrast** family unrelated to open/closed states (e.g., rough vs. smooth surface, natural vs. manufactured material) — to avoid the library becoming dominated by an "open vs. closed" or "structured vs. unstructured" theme across every pair.
- A **light/weather** family where the *only* deliberate variable is ambient condition (e.g., overcast vs. sunlit version of the same otherwise-identical scene) — this would isolate arousal/valence effects of lighting itself, which the current 3 pairs conflate with their primary contrast (especially visible in P0-003's mismatched lighting).
- A **direction/orientation** family (e.g., an object or path oriented toward vs. away from the viewer) — to test approach/withdrawal through spatial framing rather than an object's open/closed state, since P0-002 currently owns that axis alone.

### 5.2 Directions currently under-covered

- All 3 current pairs use **cr, aw, cs as isolated primary axes**, one per pair — there is no current pair designed to probe a **blended or ambiguous** axis combination, which may be needed if the methodology eventually wants pairs that don't map cleanly to one dominant direction.
- **No pair currently includes any social content.** This is the single largest coverage gap.
- **No pair currently isolates lighting/weather as the sole variable** — every current pair's intended contrast is confounded (to varying degrees) with production differences.
- **No pair uses a moving or implied-motion visual** — all 3 are static tabletop or garden scenes.

### 5.3 Avoiding visual and semantic repetition with the current 3

- Do not reuse "container with contents" as a concept (avoids echoing P0-003).
- Do not reuse "barrier/threshold" as a concept (avoids echoing P0-002).
- Do not reuse "paired manufactured objects differing only in style" as a concept (avoids echoing P0-001).
- Ensure new pairs are shot (or generated) as **genuinely matched pairs from the same setup** — same lighting temperature, same background, same camera distance — learning directly from the production inconsistency identified in P0-003.
- Ensure no two pairs in the full 9-pair set share the same primary_axis assignment more than 3 times, to keep axis coverage roughly even (3 pairs per axis across a 9-pair, 3-axis system, assuming AW/CS/CR remain the only axes).

### 5.4 Cue structure requirements for new pairs

- Each image's 3 cues should maintain a **minimum semantic/vector distance** among themselves — as a working reference point, no two cues within the same image should fall under the ~0.45–0.48 distance observed as problematic in P0-001-A and P0-003-A.
- Each image's 3 cues should maintain **valence balance** — not 2:1 or 3:0 skewed toward one emotional pole, unless that skew is a deliberate, documented methodological choice for a specific pair.
- No single cue within a set should be phrased so as to be the obvious "most resolved," "most correct," or "most articulate" answer relative to its siblings — this is the same attractiveness-asymmetry risk flagged in both P0-001-A (C3) and P0-003-A (C1).
- Cue wording should stay at the level of a personal reaction ("I want...", "It feels...") rather than a diagnostic or interpretive claim, consistent with the existing constitutional rule already followed in the current 3 pairs.

---

## 6. Open questions requiring human methodological judgment

1. **P0-003 visual mismatch** — should this pair be reshot/regenerated to match lighting and background before any wider test, or is the current version acceptable for continued internal QA while a matched replacement is prepared separately?
2. **P0-002's inherent open/closed valence asymmetry** — is this considered an acceptable, disclosed limitation (since it stems from the concept itself, not the execution), or should future "state contrast" pairs actively avoid concepts with a built-in positive/negative lean?
3. **Social content family** — introducing any pair with implied people raises new interpretive and ethical considerations (e.g., participant projection onto ambiguous figures) that go beyond the current audit's scope. Does the project want to proceed with a social-content pair at all in the next 6, or defer it to a later library expansion after more methodological groundwork?
4. **Blended-axis pairs** — should any of the 6 new pairs be designed to deliberately combine two axes (e.g., an image that plausibly reads as both an AW and CS probe), or should the library stay strictly one-axis-per-pair for consistency with the current 3?
5. **Minimum semantic distance threshold** — this document uses ~0.45–0.48 as an informal "too close" reference point, based only on the two problematic cases found in the existing 3 pairs. Is there a more principled threshold the project wants to standardize on (e.g., a fixed Euclidean distance in the aw/cs/cr vector space), or should this remain a case-by-case judgment during cue authoring?
6. **P0-001-A and P0-003-A cue revisions** — should these be corrected now (before N1 scheduling work begins), or held until the full 9-pair set is drafted so all cue rebalancing happens in one pass?
