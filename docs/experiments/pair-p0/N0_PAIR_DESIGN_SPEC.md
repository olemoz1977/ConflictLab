# N0 — Pair Design Specification

**Date:** 2026-08-05
**Based on:** N0_DECISIONS.md (commit 8d216909e431014eb209649401ca03ebcd0755ff)
**Scope:** Documentation only. No code, JSON, scheduler, or cue changes.

---

## 1. Library balance requirements (9-pair target)

### 1.1 Axis coverage

| Axis | Current pairs | New pairs needed | Final target |
|---|---|---|---|
| AW (approach/withdrawal) | P0-002 | 2 | 3 |
| CS (clarity-seeking / ambiguity-tolerance) | P0-003 | 2 | 3 |
| CR (control/release) | P0-001 | 2 | 3 |

**Requirement:** the full 9-pair library must contain exactly 3 AW + 3 CS + 3 CR pairs.

> **Important:** stimulus family does not determine axis. Axis is confirmed only after reviewing the specific A/B contrast, the interpretive field, and the cue structure of a concrete pair concept. A "spatial" pair could probe AW, CS, or CR depending on what the contrast actually makes available to the participant.

### 1.2 Stimulus family diversity

- No stimulus family used by P0-001–P0-003 may be reused: no "paired manufactured objects differing in style," no "barrier/threshold state," no "container open/closed state"
- No two new pairs should belong to the same stimulus family
- At least one pair should introduce implied motion or temporal change (currently absent from all 3 existing pairs)

### 1.3 Social content

- Exactly 1 of the 9 pairs may include implied social presence
- That pair must meet the constraints defined in §3.6 (N0-009)
- All other pairs: zero social content

### 1.4 Valence balance

- Across the full library, no axis group (AW / CS / CR) should have all its pairs skewed toward the same emotional pole
- Within each pair, Image A and Image B should not both carry the same dominant valence (both inviting, both aversive)

### 1.5 Visual intensity balance

- No more than 2 pairs in the full library should rely on a high-arousal visual (strong color contrast, implied urgency, dramatic light)
- At least 2 pairs should use a low-arousal, neutral visual register (the current 3 pairs all use low-to-medium arousal)

### 1.6 Repetition control

- No two pairs should use the same primary visual concept (open/closed, near/far, light/dark) as their organizing contrast
- Visual concepts may recur only if the stimulus family and interpretive field are sufficiently distinct

### 1.7 Independence from cues

- Each pair's A/B image contrast must be interpretively meaningful before any cue is shown — the visual alone should support multiple plausible readings without the cue resolving them
- No pair should require its cues to create the contrast; cues name reactions, they do not manufacture them

---

## 2. Provisional axis assignments

| Pair | Provisional axis | Stimulus family | Status |
|---|---|---|---|
| N0-004 | AW | Spatial / environmental | Provisional design target |
| N0-005 | CS | Process / temporal | Provisional design target |
| N0-006 | CR | Texture / material | Provisional design target |
| N0-007 | AW | Direction / orientation | Provisional design target |
| N0-008 | CS or CR | Light / weather | **[PROVISIONAL — axis confirmed after stimulus-concept review]** |
| N0-009 | Unresolved | Neutral social proximity | **[UNRESOLVED — axis assigned after stimulus-concept review]** |

N0-004–N0-007 are provisional design targets, not locked assignments. N0-008 and N0-009 axis assignments are explicitly deferred until a concrete A/B contrast concept exists and can be evaluated.

---

## 3. Per-pair design requirements

---

### N0-004 — Spatial / Environmental
**Provisional axis:** AW

| Field | Specification |
|---|---|
| Coverage gap filled | All 3 current pairs use manufactured objects. No pair uses natural or architectural space as the primary stimulus. |
| Interpretive field | The contrast should make available: moving toward / moving away from; entering / not entering; open space / bounded space. |
| Forbidden confounds | Do not introduce social presence. Do not use a barrier/threshold concept (would echo P0-002). Do not use a container concept. |
| Visual balance requirements | Both images must come from the same shoot or generation setup. Same lighting temperature, same time of day, same camera distance. The only deliberate variable is the spatial condition being contrasted. |
| Cue structure requirements | 3 cues per image. Each cue expresses a personal reaction to the space, not a description of it. No two cues within the same image should cover such similar ground that a participant could plausibly choose either for the same reason (manual judgment during authoring). Valence balance: not 2:1 or 3:0 skewed. No cue should read as the obviously "most resolved" answer. |
| Differentiation from existing pairs | Must not use a gate, door, threshold, or any barrier concept (P0-002). Must not use manufactured objects as the primary visual element (P0-001). |
| Primary methodological risk | Spatial scenes can carry strong cultural or personal associations (e.g., a forest path vs. an urban alley) that introduce uncontrolled valence independent of the intended contrast. |
| Acceptance criteria | The A/B contrast is interpretively meaningful without cues. The pair does not repeat any concept from P0-001–P0-003. Visual production is matched. Axis assignment is confirmed after stimulus-concept review. |

---

### N0-005 — Process / Temporal
**Provisional axis:** CS

| Field | Specification |
|---|---|
| Coverage gap filled | No current pair uses process state or temporal change as the organizing contrast. All 3 existing pairs show static end-states (formal/casual, open/closed). |
| Interpretive field | The contrast should make available: knowing what comes next / not knowing; something resolved / something in-progress; completed / unfinished. |
| Forbidden confounds | Do not use a container concept (would echo P0-003 — open/closed box). Do not use a barrier concept. Avoid contrasts where one state is universally read as "better" (e.g., finished product vs. broken object). |
| Visual balance requirements | Both images must be from the same setup. The only deliberate variable is the process state (e.g., mid-point vs. endpoint, early vs. late stage). Lighting, background, and framing must be matched. |
| Cue structure requirements | Same as N0-004. Cues should reflect the participant's orientation toward the process state, not describe it. |
| Differentiation from existing pairs | Must not be a container with contents (P0-003). Must not be a static style contrast (P0-001). |
| Primary methodological risk | Process contrasts (mid vs. finished) can carry a strong implicit preference for completion, introducing valence asymmetry similar to P0-002's open/closed conceptual asymmetry. |
| Acceptance criteria | The contrast does not implicitly favor one state as obviously "better." The visual is sufficiently ambiguous that multiple reactions to the same image are plausible. Axis confirmed after concept review. |

---

### N0-006 — Texture / Material
**Provisional axis:** CR

| Field | Specification |
|---|---|
| Coverage gap filled | No current pair uses texture or material quality as the primary contrast. All 3 existing pairs use shape/state contrasts (style, open/closed). |
| Interpretive field | The contrast should make available: structured / unstructured; predictable / variable; controlled / yielding. Material or surface contrasts can probe CR without requiring an open/closed or formal/casual concept. |
| Forbidden confounds | Do not introduce cleanliness/dirtiness as an implicit variable (would add hygiene valence). Do not introduce natural vs. manufactured if that introduces a strong cultural preference in one direction. |
| Visual balance requirements | Both images must show the same type of object or surface context — only the texture or material quality varies. Lighting must be matched to avoid one texture appearing more "premium" due to light rather than material. |
| Cue structure requirements | Same as N0-004. Cues should express the participant's felt reaction to the texture or material, not label it. |
| Differentiation from existing pairs | Must not be footwear or clothing (P0-001). Must not be an architectural surface that reads as a barrier (P0-002). |
| Primary methodological risk | Texture contrasts can carry strong haptic associations (rough = uncomfortable, smooth = pleasant) that pre-resolve the contrast before the participant engages with it. |
| Acceptance criteria | Neither texture reads as obviously preferable on a universal comfort scale. The contrast generates genuine ambiguity about which state a participant might be drawn to. Axis confirmed after concept review. |

---

### N0-007 — Direction / Orientation
**Provisional axis:** AW

| Field | Specification |
|---|---|
| Coverage gap filled | No current pair uses spatial orientation or implied direction as the contrast. P0-002 uses a barrier state (open/closed gate) to probe AW; this pair probes AW through directional framing rather than object state. |
| Interpretive field | The contrast should make available: moving toward / moving away from; facing / turning away; approaching / receding. The object or scene is the same in both images; only orientation or direction relative to the viewer changes. |
| Forbidden confounds | Do not introduce a barrier or threshold (would echo P0-002). Do not introduce social presence. Avoid contrasts where one direction carries a universally positive valence (e.g., "toward the light" vs. "away from the light" would introduce a cultural/symbolic loading). |
| Visual balance requirements | Ideally the same object or scene in two orientations, shot from the same position. If generated, both images must share identical background, lighting, and composition except for the directional variable. |
| Cue structure requirements | Same as N0-004. Cues should reflect the participant's reaction to the directional relationship, not describe which direction the object faces. |
| Differentiation from existing pairs | Must not use a gate or barrier (P0-002). Must not rely on open/closed state to convey direction. |
| Primary methodological risk | Directional contrasts can collapse into a simple "toward = good, away = bad" binary that pre-resolves the intended ambiguity. The design must ensure both orientations carry plausible positive and negative readings. |
| Acceptance criteria | Both orientations support genuinely multiple readings. The contrast does not collapse into a universal preference for one direction. Axis confirmed after concept review. |

---

### N0-008 — Light / Weather
**Provisional axis:** CS or CR — [PROVISIONAL]

| Field | Specification |
|---|---|
| Coverage gap filled | No current pair isolates lighting or ambient condition as the sole variable. P0-003's lighting mismatch is a confound; this pair makes lighting the deliberate and only contrast. |
| Interpretive field | The contrast should make available reactions to: clarity vs. ambiguity (CS reading); predictability vs. openness (CR reading); or approach vs. withdrawal (AW reading). The axis assignment depends on which interpretive field the specific contrast actually activates — this cannot be determined without a concrete concept. |
| Forbidden confounds | The two images must be otherwise identical — same scene, same objects, same framing, same camera position. Only the ambient light or weather condition changes. Do not introduce time-of-day changes that bring in social associations (e.g., nighttime vs. daytime carries strong safety/danger valence). |
| Visual balance requirements | Maximum control: the only variable is the lighting/weather condition. All other visual elements identical. |
| Cue structure requirements | Same as N0-004. Cues should reflect the participant's felt reaction to the ambient condition, not describe the weather or light level. |
| Differentiation from existing pairs | No current pair uses ambient condition as the primary contrast — this family is fully novel within the library. |
| Primary methodological risk | Light and weather carry strong universal valence associations (sunny = positive, overcast = negative in many cultural contexts). The contrast must be designed so that the "less bright" condition is not universally read as aversive. |
| Acceptance criteria | Both ambient conditions support genuine interpretive ambiguity. Axis assignment is confirmed only after the specific A/B contrast concept is reviewed — axis is not inferred from the stimulus family alone. |

---

### N0-009 — Neutral Social Proximity
**Axis:** [UNRESOLVED — assigned after stimulus-concept review]

| Field | Specification |
|---|---|
| Coverage gap filled | All 3 current pairs and all other new pairs have zero social content. N0 audit identifies this as the single largest library coverage gap. One pair with minimal, controlled social presence tests whether social proximity affects choice and cue selection differently from object-based stimuli. |
| Interpretive field | The contrast should make available reactions to: spatial distance between implied presences; closeness vs. separation; contact vs. space. The axis (AW / CS / CR) is not pre-assigned because social distance can plausibly activate any of the three — this is an empirical question, not a design assumption. |
| Permitted social content | Implied presence at a distance (two figures, bench-scale or further). No faces in close-up. No explicit interaction or conflict. No status, gender role, or threat interpretation implied by posture or context. Spatial relationship is the only deliberate variable. |
| Forbidden confounds | No facial expressions. No identifiable clothing or cultural markers. No scene that implies a narrative (argument, reunion, waiting). The contrast must be in the spatial relationship only, not in the implied emotional state of the figures. |
| Visual balance requirements | Both images from the same setup. Background, lighting, and framing identical. Only the spatial relationship between the implied presences changes. |
| Cue structure requirements | Same as N0-004. Cues must reflect the participant's reaction to the spatial relationship, not attribute emotional states to the figures. |
| Differentiation from existing pairs | Fully novel — no current pair has any social content. |
| Primary methodological risk | Even minimal implied social presence triggers projection. Participants may attribute emotion, relationship, or narrative to the figures independent of the cues. This is a known limitation that must be documented before the pair is used in any session beyond internal review. |
| Acceptance criteria | The figures in the images do not suggest a specific relationship, narrative, or emotional state. The contrast is legible as a spatial/proximity contrast before any cue is shown. Axis assignment requires a concrete concept review. Human methodological decision required before this pair enters the active library. |

---

## 4. Summary table

| Pair | Provisional axis | Stimulus family | Social content | Axis status | Key risk |
|---|---|---|---|---|---|
| N0-004 | AW | Spatial / environmental | None | Provisional | Cultural/personal spatial associations |
| N0-005 | CS | Process / temporal | None | Provisional | Implicit preference for completion |
| N0-006 | CR | Texture / material | None | Provisional | Haptic valence pre-resolving contrast |
| N0-007 | AW | Direction / orientation | None | Provisional | Toward/away collapsing into simple binary |
| N0-008 | CS or CR | Light / weather | None | **Provisional — axis deferred** | Universal sunny/overcast valence |
| N0-009 | Unresolved | Neutral social proximity | Minimal implied | **Unresolved — axis deferred** | Projection onto figures |

---

## 5. Open questions requiring human decision before production

1. **N0-008 axis assignment** — does the specific light/weather contrast concept activate CS, CR, or AW? Cannot be determined without a concrete A/B concept.

2. **N0-009 axis assignment** — social distance can activate AW, CS, or CR. Axis must be assigned after the stimulus concept is reviewed, not before.

3. **N0-009 inclusion decision** — human methodological decision required: is the projection risk acceptable at this stage, or should the social pair be deferred to a later library expansion?

4. **Concrete stimulus concepts for all 6 pairs** — this document defines requirements only. No specific images, scenes, or visual setups are specified here. Stimulus concepts are the next step.

5. **Cue overlap auditing protocol** — how cue semantic overlap is audited without numeric proxies is not yet defined. A reproducible manual protocol must be established before cue authoring begins.

---

## 6. What this document is not

- This is not a cue authoring document
- This is not an image specification or generation brief
- This is not a scheduler design document
- No new schema fields, status values, or numeric thresholds are introduced here
- Axis assignments marked [PROVISIONAL] or [UNRESOLVED] are not confirmed until a concrete stimulus concept exists and is reviewed
