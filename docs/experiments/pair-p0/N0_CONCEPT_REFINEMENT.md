# N0 — Concept Refinement

**Date:** 2026-08-05
**Based on:** N0_INDEPENDENT_CONCEPT_REVIEW.md (commit 9152a91613223a43e4764ad5f8ef5cf74004ab60)
**Scope:** Documentation only. No code, JSON, cue texts, or scheduler changes.

> **Purpose:** Specify each of the 5 ADVANCE concepts precisely enough for production, without writing final cues. Each concept is defined by: the single permitted A/B difference, what must remain identical, disqualifying confounds, production method, acceptance criteria, and rejection criteria.

> **N0-009 is not developed here** — remains EXPERIMENTAL HOLD pending separate social projection concept review.

---

## N0-004-C1 — Forest path: continues vs. ends at clearing

**Slot:** N0-004 | **Provisional axis:** AW | **Production method:** Generated prototype first, then real photography audit

### Current status

**ADVANCE — visually matched, semantic endpoint still requires refinement**

A first generated visual prototype exists. Observations from prototype review:

- `[OBSERVED FACT]` Scene and lighting are sufficiently similar between the two images
- `[OBSERVED FACT]` The contrast between path continuation and path ending is already readable
- `[MANUAL AUDIT JUDGMENT]` In the "ending" variant, the path changes geometry too much — it curves or turns, which introduces a directional change rather than a simple endpoint
- `[METHODOLOGICAL REQUIREMENT]` In the final variant, only the furthest visible section of the path may change; everything else must be identical
- `[METHODOLOGICAL REQUIREMENT]` Path width, foreground, lighting, tree density, and color temperature must remain the same between A and B
- `[METHODOLOGICAL REQUIREMENT]` The clearing (Image B endpoint) must not be brighter, more open, more inviting, or visually "better" than Image A's continuation — this would introduce valence asymmetry into the endpoint itself

### Single permitted A/B difference

The furthest visible section of the path:
- **Image A:** path continues forward, disappearing into trees — destination not visible
- **Image B:** path arrives at an open area — the path ends, space opens, but the opening is not brighter, larger, or more inviting than the path itself

### What must remain identical

- Path width at all visible points except the furthest section
- Foreground (first 2–3 meters of path in frame)
- Tree density and species on both sides
- Lighting direction and color temperature
- Camera position, height, and focal length
- Time of day (implied by shadow angle and sky tone)

### Disqualifying confounds

- `[REJECT IF]` The clearing in Image B is visibly brighter than the forest in Image A — this introduces a light/openness valence asymmetry independent of the path/clearing contrast
- `[REJECT IF]` The path in Image B curves significantly before ending — a directional change is not the same as a path ending; it introduces a different spatial experience
- `[REJECT IF]` The two images differ in foreground or mid-ground — only the far end of the path may differ
- `[REJECT IF]` The endpoint (clearing) introduces any social content — open field with visible houses, people, or structures

### Acceptance criteria

- A reviewer unfamiliar with the project can identify the A/B difference as "the path continues" vs. "the path ends" without being told
- Neither endpoint reads as clearly preferable — the continuation and the clearing both support at least two plausible reactions
- Visual parameters (lighting, path width, foreground) appear matched to a non-expert viewer

### Rejection criteria

- Any of the disqualifying confounds above
- The semantic difference is not readable without an explanation
- The clearing reads as arrival/relief rather than merely as a different spatial state

### Next step

Refine the generated prototype: constrain the endpoint to be a flat, same-brightness opening without path curvature. Review against acceptance criteria before moving to real photography.

---

## N0-005-C1 — Plant: early sprout vs. established growth

**Slot:** N0-005 | **Provisional axis:** CS | **Production method:** Generated controlled prototype first — real photography over time introduces too many uncontrolled variables (soil changes, light shifts, pot weathering) to produce a reliably matched pair

### Current status

**ADVANCE TO CONCEPT REFINEMENT**

No prototype exists yet. Human decision recorded: the contrast must be between two viable growth stages of the same plant — not "young vs. beautiful mature," but early and later stages that are both alive and developing.

### Single permitted A/B difference

Growth stage of the plant:
- **Image A:** early stage — sprout visible, form not yet defined, growth direction open
- **Image B:** later stage — form established, growth direction clear, structure visible

### What must remain identical

- Plant species (same plant)
- Pot or container (same pot, same soil surface)
- Background (same background — wall, shelf, or neutral surface)
- Camera position, height, and focal length
- Lighting direction, color temperature, and intensity
- Soil surface appearance (no added water, no wilting, no decay in either image)

### Disqualifying confounds

- `[REJECT IF]` Different plant species used — species differences introduce uncontrolled visual variables
- `[REJECT IF]` The later-stage plant appears healthier, more lush, or more "beautiful" than the early-stage — this introduces a completion-preference valence asymmetry
- `[REJECT IF]` The pot, background, or lighting differs between the two images
- `[REJECT IF]` Either plant appears unhealthy, wilted, or damaged — introduces a negative valence unrelated to the growth-stage contrast
- `[REJECT IF]` The early stage is so small it disappears in the frame while the established plant fills it — the framing itself becomes a variable

### Acceptance criteria

- Both images show a visibly alive, developing plant
- The growth-stage difference is readable without explanation
- Neither stage reads as clearly preferable — early stage supports openness/potential; established stage supports clarity/defined form — both plausibly positive
- Framing is comparable — the plant occupies a similar proportion of the frame in both images

### Rejection criteria

- Any of the disqualifying confounds above
- The established plant reads as "complete" and the sprout reads as "incomplete" rather than both reading as valid ongoing stages

### Next step

Define production path: real photography (same pot, photograph at two time points) or generated images (same species, same pot model, two growth stages). Human decision required — real photography is more authentic but takes weeks; generation is faster but requires validation that the two images do not introduce uncontrolled variation.

---

## N0-006-C1 — Surface: rough stone vs. smooth stone

**Slot:** N0-006 | **Provisional axis:** CR | **Production method:** Generated or photographed close-up — strict lighting angle control required

### Current status

**ADVANCE TO CONCEPT REFINEMENT**

No prototype exists yet. Human decision recorded: the reflectivity difference between rough and polished stone is a **tolerable known limitation only if** the reflectivity difference is not the primary visual signal the eye receives. If a viewer's first impression is "one is shinier," the concept is disqualified.

### Single permitted A/B difference

Surface texture of the same stone material:
- **Image A:** rough, unfinished surface — irregular, varied, tactilely complex
- **Image B:** polished smooth surface — uniform, regular, tactilely simple

### What must remain identical

- Stone material/type (same stone, different finish)
- Camera distance and focal length
- Lighting direction and angle (this is the critical control — same light source angle for both)
- Frame composition (same portion of the surface visible)
- Color of the stone (rough and polished versions of the same stone type)

### Disqualifying confounds

- `[REJECT IF]` The polished surface reflects a visible highlight or glare that the rough surface does not — if the first visual impression is brightness difference rather than texture difference, the confound is present
- `[REJECT IF]` The two images differ in color temperature — polished stone can appear cooler or warmer depending on what it reflects
- `[REJECT IF]` The stone type differs between images — different minerals, different base color
- `[REJECT IF]` The rough surface reads as dirty, damaged, or degraded rather than simply unfinished — this introduces hygiene or decay valence

### Acceptance criteria

- A viewer's first impression is texture difference, not brightness difference
- Neither surface reads as clearly preferable on a universal comfort or aesthetics scale
- The contrast is readable as a tactile/material quality difference, not a quality or condition difference

### Rejection criteria

- Any of the disqualifying confounds above
- The polished surface reads as "better quality" or "more premium" rather than "differently textured"
- The rough surface reads as damaged or dirty

### Next step

Produce a test image pair with controlled lateral lighting (45-degree angle from the same side for both images). Review first impression: does the eye go to texture or to brightness? If brightness, adjust lighting angle before proceeding.

---

## N0-007-C1 — Object facing toward vs. away from viewer

**Slot:** N0-007 | **Provisional axis:** AW | **Production method:** Generated or photographed — same object, same setting, rotated 180 degrees

### Current status

**HOLD — directional object concept not yet operationally clean**

`[MANUAL AUDIT JUDGMENT]` Review of the three object candidates (ceramic vessel, stool, geometric form) revealed a structural problem with the concept itself, not only with the specific objects proposed:

- An object without a clear front does not produce a readable orientation contrast — "facing toward" and "facing away" are not distinguishable
- An object with a clear front (functional opening, decorated face, or designed front surface) typically carries functional, social, or cultural associations tied to that front — introducing a confound stronger than the orientation itself
- Rotating an object 180 degrees changes the visible surface area, silhouette, or opening — these changes may become the primary visual signal rather than the orientation direction
- None of the three proposed candidates (A / B / C) is confirmed for production

`[UNRESOLVED QUESTION]` Whether a methodologically clean directional object concept is achievable requires further concept development before any production decision. The concept is not rejected — it is held until an operationally viable object and setup can be defined.

No production brief will be written for N0-007 until the concept is operationally resolved.

### Single permitted A/B difference

Orientation of the object relative to the camera:
- **Image A:** object oriented toward the camera — front faces viewer
- **Image B:** same object in same setting, oriented away — back faces viewer

### What must remain identical

- Object (same object, same condition)
- Setting and background
- Camera position and distance (only the object rotates, not the camera)
- Lighting direction and color temperature
- Surface the object rests on

### Disqualifying confounds

- `[REJECT IF]` The object has a front that is visually more complex, decorated, or appealing than its back — this introduces a visual interest asymmetry unrelated to orientation
- `[REJECT IF]` The object's "facing toward" position reads as confrontational or threatening — this introduces a valence asymmetry
- `[REJECT IF]` The object's "away" position reads as departure or rejection in a culturally loaded way
- `[REJECT IF]` The object is a biological entity (animal, plant with a "face") — biological fronts/backs carry strong valence
- `[REJECT IF]` The rotation reveals a significantly different visual mass or silhouette — the two images should look like the same object seen from different sides, not like two different objects

### Acceptance criteria

- Both orientations read as the same object
- Neither orientation carries a strong universal positive or negative valence
- A viewer can describe the difference as "facing me" vs. "facing away" without further explanation
- Both orientations support at least two plausible reactions

### Rejection criteria

- Any of the disqualifying confounds above
- The two orientations produce such different visual impressions that they read as different objects

### Three neutral object candidates

> `[UNRESOLVED — human selection required]` Three candidates are proposed. No candidate is selected here. Selection requires human judgment about which object minimizes directional and cultural associations.

**Candidate A: Simple ceramic bowl or vessel**
- Symmetric form — front and back differ mainly in handle position (if any) or minor surface variation
- No face, no decoration on one side only
- Risk: if the vessel has an opening facing toward the viewer in Image A, the opening itself may carry an invitation/receptiveness valence
- Mitigation: use a closed vessel (lidded jar or rounded bowl without an opening facing the camera)

**Candidate B: Simple wooden stool or low chair**
- Familiar domestic object; front (seat visible) vs. back (legs and back visible) are genuinely different but neither is universally preferred
- Risk: a chair "facing away" is a culturally loaded image in some narrative traditions (absence, departure)
- Mitigation: use a stool without a back — reduces departure/absence association

**Candidate C: Simple geometric form (cube, cylinder, or rectangular block)**
- Minimal intrinsic associations — no functional front/back
- Orientation difference is purely spatial, not functional or cultural
- Risk: the two images may look too similar — if the object is highly symmetric, the A/B difference may not be readable
- Mitigation: choose a form with one clearly distinct face (e.g., a rectangular block where the narrow end vs. the wide face is visible)

### Next step

Human selects one of the three candidates, or proposes an alternative. Production brief is written after selection.

---

## N0-008-C1 — Same outdoor scene: overcast vs. diffuse sunlight

**Slot:** N0-008 | **Provisional axis:** CS or CR [UNRESOLVED] | **Production method:** Generated — same scene, same camera position, weather condition as sole variable

### Current status

**ADVANCE, AXIS UNRESOLVED**

Human decision recorded: axis remains unresolved even after first cue drafts. Cues may not be used to artificially "create" the axis — cues name reactions, they do not manufacture the methodological signal. Axis is confirmed only when a reviewer can independently identify which axis the contrast activates, based on the image pair and candidate cues together.

### Single permitted A/B difference

Ambient lighting condition:
- **Image A:** flat overcast light — no visible shadows, even illumination, sky grey-white or pale white
- **Image B:** diffuse sunlight — soft shadows present, sky pale blue or warm-white, no harsh contrast or direct beam

### What must remain identical

- Scene content (same outdoor space — courtyard, field edge, simple exterior, or path)
- Camera position, height, and focal length
- Time of day (implied by shadow angle — both images should imply the same approximate time, not morning vs. afternoon)
- All objects and surfaces in the scene
- Color of surfaces (excluding the light cast on them)

### Disqualifying confounds

- `[REJECT IF]` Image B (sunlit) is significantly brighter overall — brightness difference rather than quality-of-light difference is the primary signal
- `[REJECT IF]` The two images imply different times of day — shadow angles diverge noticeably
- `[REJECT IF]` The sky is a significant visual element in the frame — sky color/texture difference would dominate over scene content
- `[REJECT IF]` The sunlit image introduces warm golden tones that read as "beautiful" or "more appealing" — avoid late-afternoon or golden-hour light; use midday diffuse sun only
- `[REJECT IF]` Social content appears in either image

### Acceptance criteria

- The lighting difference is readable as a quality-of-light difference (flat vs. soft shadow), not as a brightness or warmth difference
- Neither lighting condition reads as clearly preferable — overcast can feel calm and even; diffuse sun can feel warm or exposing
- The scene content is visually equivalent in both images — a viewer counts the same objects in the same positions

### Rejection criteria

- Any of the disqualifying confounds above
- The sunlit version reads as "nicer weather" rather than "different light quality"
- The lighting difference is too subtle to read without side-by-side comparison

### Axis confirmation protocol

`[METHODOLOGICAL REQUIREMENT]` Axis is confirmed in a separate step after candidate cues are drafted:
1. Draft candidate cues for both images
2. A reviewer unfamiliar with the axis assignment reads the image pair and candidate cues
3. The reviewer identifies which axis (AW / CS / CR) the contrast seems to activate
4. If the reviewer's identification matches a provisional axis assignment, that axis is confirmed
5. If the reviewer cannot identify an axis, or identifies a different one, the axis assignment is revised or left unresolved until further review
6. Cues may not be rewritten to steer toward a pre-decided axis — if the natural cue set does not activate the intended axis, the axis assignment is wrong, not the cues

### Next step

**Do not produce before contrast refinement.** The overcast/sunlit contrast risks becoming a general scene attractiveness test rather than a quality-of-light probe — the specific scene, framing, and lighting parameters must be specified more precisely before any image is generated. Production is deferred until the contrast can be defined in terms that are verifiably distinct from "nicer weather."

---

## Summary table

| Concept | Slot | Prov. axis | Production method | Prototype exists | Status | Key unresolved |
|---|---|---|---|---|---|---|
| N0-004-C1 Forest path | N0-004 | AW | Generated prototype → real photo audit | Yes — requires endpoint refinement | **ADVANCE, endpoint geometry needs correction** | Clearing must not be brighter or more inviting than path |
| N0-005-C1 Plant sprout | N0-005 | CS | Same plant, same pot — photo over time or generated | No | **ADVANCE TO CONCEPT REFINEMENT** | Production path: real photo vs. generated |
| N0-006-C1 Stone surface | N0-006 | CR | Generated or photo — strict lighting angle control | No | **ADVANCE TO CONCEPT REFINEMENT** | Reflectivity: first impression must be texture, not brightness |
| N0-007-C1 Object facing | N0-007 | AW | — | No | **HOLD — directional object concept not yet operationally clean** | Concept requires further development before any production decision |
| N0-008-C1 Overcast/sunlit | N0-008 | CS or CR | Generated — deferred | No | **ADVANCE, AXIS UNRESOLVED — do not produce before contrast refinement** | Scene and lighting parameters must be more precisely specified first |

---

## Open questions requiring human decision before production proceeds

1. **N0-004-C1** — generate a revised prototype with constrained endpoint geometry (no path curvature, clearing not brighter than forest); then decide whether to proceed to real photography or stay with generated images.

2. **N0-005-C1** — production path decision: real photography (same pot, two time points — weeks apart) or generated images (faster, but requires validation of matching)?

3. **N0-006-C1** — after first test image pair: does the eye go to texture or brightness? Human confirmation required before production brief.

4. **N0-007-C1** — which of the three object candidates (ceramic vessel, stool, geometric form) is selected? Or alternative proposed by human?

5. **N0-008-C1** — after first generated image pair: does the lighting difference read as quality-of-light or as brightness/warmth? Human confirmation required before cue drafting.

---

## Prototype findings (2026-08-05)

> **Annotation type key:** `[OBSERVED FACT]` — directly observed from prototype images; `[MANUAL AUDIT JUDGMENT]` — qualitative assessment during review; `[PRODUCTION FINDING]` — conclusion about production method.

---

### N0-004 — Forest path prototype findings

`[OBSERVED FACT]` A reference-based Gemini edit retains scene consistency better than separate Kling generation — same forest, same lighting, same framing across A and B.

`[OBSERVED FACT]` The strongest prototype has sufficiently matched forest density, lighting, and camera framing between the two images.

`[OBSERVED FACT]` Remaining defect: in the "path ends" variant, the path also changes geometry — it curves or turns before ending. The geometric change is a confound independent of the endpoint itself.

`[METHODOLOGICAL REQUIREMENT]` In the next iteration, only the far end of the path may change. Path width, foreground, mid-ground geometry, tree density, lighting, and color temperature must remain identical. The path must arrive at an open area without first curving or turning.

**Status: ADVANCE — visually matched, endpoint not yet isolated**

---

### N0-005 — Plant growth stage prototype findings

`[OBSERVED FACT]` Multiple plant prototypes were generated across two iterations.

`[OBSERVED FACT]` Reference-based editing improved pot, background, and scene matching significantly — the third iteration had a well-matched pot, soil texture, lighting, and camera angle.

`[OBSERVED FACT]` Even with improved technical matching, a conceptual valence asymmetry persists: more leaves, greater height, and a fuller silhouette are consistently readable as a "better result," independent of cue wording.

`[MANUAL AUDIT JUDGMENT]` The large-difference prototype (clear early sprout vs. established plant) was rejected — Image B was visibly more appealing: richer green, larger leaves, stronger visual presence.

`[MANUAL AUDIT JUDGMENT]` The small-difference prototype (two similar seedling stages) passed technical matching but failed semantic contrast — the A/B difference was too subtle to produce meaningful ambiguity.

`[MANUAL AUDIT JUDGMENT]` The valence asymmetry in this concept is not a production problem — it is a conceptual property of growth stages. A later growth stage carries completion signals that are difficult to neutralize without making the plant appear unhealthy or stunted, which would introduce a different valence problem.

`[UNRESOLVED QUESTION]` Whether this inherent valence asymmetry is an acceptable disclosed limitation (analogous to P0-002's open/closed conceptual asymmetry) — or whether it is strong enough to disqualify the concept — requires human methodological decision.

**Status: HOLD — production can be controlled, conceptual valence asymmetry unresolved**

---

### N0-006 — Stone texture prototype findings

`[OBSERVED FACT]` A first stone texture prototype pair was produced.

`[OBSERVED FACT]` The A/B mismatch was too large across multiple dimensions simultaneously: different shape outline, different contour, different tilt angle, different color tone, visible cracks in Image A, different shadow direction.

`[MANUAL AUDIT JUDGMENT]` The AI rendered roughness as damage and age — rough surface read as cracked, weathered, or degraded rather than simply unfinished. This introduced a condition/quality valence asymmetry rather than a texture contrast.

`[OBSERVED FACT]` The smooth stone image (Image B from the prototype) is visually clean — same rounded form, neutral grey, matte surface, no gloss. It can serve as a reference base for the next iteration.

`[PRODUCTION FINDING]` The next iteration must use the smooth stone image as the reference base and apply only micro-texture change — no cracks, no grooves, no color shift, no change in shadow direction or stone contour. The rough surface must read as unfinished, not damaged.

**Status: REVISE — same-object reference edit required**

---

### General production finding

`[PRODUCTION FINDING]` A base image may be generated independently.

`[PRODUCTION FINDING]` The A/B partner must be produced via reference-based edit of the base image — not as a separate generation. Separate A and B generation introduces too many uncontrolled differences across shape, lighting, color temperature, and composition.

`[MANUAL AUDIT JUDGMENT]` In this prototype round, Gemini's reference editing retained scene consistency better than separate Kling generation. This is a specific observation about these prototypes — not a general model quality claim.
