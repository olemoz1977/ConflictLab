# N0 — Production Prompt Specification

**Date:** 2026-08-05
**Scope:** Image generation brief for N0-005-C1 and N0-006-C1 prototypes.
**Tool target:** Gemini image generation / reference-based edit
**Format:** 1:1 square, realistic photography style
**Priority:** Scene matching over aesthetics. A/B pairs must look like the same setup, not like two beautiful photographs.

---

## N0-005-C1 — Plant: early sprout vs. established growth

### BASE IMAGE PROMPT

```
Close-up photograph of a single small healthy green plant seedling in a plain terracotta or matte ceramic pot, filled with dark moist soil. The plant has 2–3 small leaves just emerging, upright and intact. Shot from a slightly elevated front angle, centered in frame. Neutral light grey or off-white background wall. Soft even diffuse lighting from the left, no harsh shadows, no dramatic highlights. Natural daylight color temperature. No flowers, no fruit, no labels, no decorative elements. Square format. Realistic botanical photography style, not stylized.
```

### IMAGE A — Early sprout

```
Edit: keep all elements identical — same pot, same soil surface, same background, same lighting, same camera angle, same framing. Plant shows 2–3 small healthy leaves just emerging from soil. Plant appears alive and growing but form is not yet defined. Stems are thin but upright, not drooping. No damage, no yellowing. This is a viable early stage, not a weak or fragile seedling.
```

### IMAGE B — Established growth (same plant, later stage)

```
Edit: keep all elements identical — same pot, same soil surface, same background, same lighting, same camera angle, same framing. Same plant species, now at a later but pre-flowering stage. Plant has 6–10 leaves, form is defined, growth direction is clear. Plant is the same height proportion relative to pot as the seedling was — adjust framing so the plant occupies a similar visual mass in the frame. No flowers, no fruit, no visible change in soil, pot, or background. Plant appears alive and vigorous but not spectacular — this is a functional growth stage, not a "result." Plant must not be brighter, more colorful, or more lush than Image A. Both images must read as equally healthy.
```

### NEGATIVE PROMPT (both images)

```
No flowers. No fruit. No wilting. No yellowing. No damaged leaves. No soil change. No pot change. No background change. No lighting change. No color temperature change. No decorative elements. No text. No logos. No human hands. No dramatic lighting. No golden hour. No studio spotlight. No depth-of-field change between A and B. No change in camera distance or angle. Do not make Image B more beautiful or appealing than Image A.
```

### MATCHING CHECKLIST

Before accepting the pair, verify:

- [ ] Same pot (shape, color, material)
- [ ] Same soil surface (no added water, moss, or decorative top layer)
- [ ] Same background color and texture
- [ ] Same lighting direction (shadow falls on the same side)
- [ ] Same color temperature (neither image is warmer or cooler)
- [ ] Same camera angle and distance (plant occupies similar visual mass in frame)
- [ ] Both plants appear equally healthy — neither looks stronger or weaker
- [ ] Image B has no flowers, buds, or fruit
- [ ] Image A plant is not drooping, pale, or visibly fragile

### REJECTION CRITERIA

Reject the pair if:

- Image B is noticeably more lush, green, or visually rich than Image A
- Image A plant looks weak, damaged, or unhealthy
- Pot, soil, background, or lighting differs between images
- Image B has flowers or fruit
- Camera angle or framing differs between images
- The primary visual difference is brightness or color saturation rather than growth stage

---

## N0-006-C1 — Stone surface: rough vs. smooth matte

### BASE IMAGE PROMPT

```
Extreme close-up photograph of a single flat stone surface, filling the entire square frame. Stone is medium grey, natural granite or similar material. Stone is the same piece in both images — same shape, same size, same color. Lit from a 45-degree angle from the left with soft diffuse natural light. No background visible — stone fills the frame edge to edge. No water, no gloss, no shine. Square format. Realistic macro photography style, not stylized.
```

### IMAGE A — Rough surface

```
Edit: the stone surface is unfinished and rough. Surface shows natural grain, micro-texture, irregular peaks and valleys visible at close range. The texture reads as tactile complexity — not damaged, not dirty, not crumbling. Same lighting angle as Image B (45 degrees from left, soft diffuse). No visible gloss or wet areas. Stone color is medium grey, uniform across the surface.
```

### IMAGE B — Smooth matte surface

```
Edit: keep all elements identical — same stone piece, same size, same color, same lighting angle (45 degrees from left, soft diffuse), same framing. The stone surface has been finished smooth — surface is even and uniform at close range. Surface is matte, not polished. No sheen, no gloss, no highlight reflections, no wet look. The difference from Image A is tactile smoothness only — the eye should not perceive a brightness difference between the two images, only a texture difference. Stone color remains the same medium grey.
```

### NEGATIVE PROMPT (both images)

```
No gloss. No shine. No wet surface. No reflections. No highlights from polishing. No color change between A and B. No brightness change between A and B. No cracks. No dirt. No stains. No rust. No discoloration. No background. No hands. No tools. No scale reference. No dramatic lighting. No color temperature change. Do not make Image B appear more premium, cleaner, or more appealing than Image A. The difference must be tactile texture only.
```

### MATCHING CHECKLIST

Before accepting the pair, verify:

- [ ] Same stone piece (same shape and size visible in frame)
- [ ] Same stone color (medium grey, no hue shift between images)
- [ ] Same lighting direction (shadow pattern consistent)
- [ ] Same color temperature (neither image warmer or cooler)
- [ ] Same framing (stone fills frame edge to edge in both)
- [ ] Image B surface has no visible gloss or highlight reflections
- [ ] Image A surface is not dirty, cracked, or damaged
- [ ] First visual impression of both images: texture difference, not brightness difference
- [ ] Neither surface reads as clearly "better quality" than the other

### REJECTION CRITERIA

Reject the pair if:

- Image B has any visible gloss, sheen, or highlight reflection
- Image A reads as dirty, damaged, or lower quality rather than simply rougher
- The primary visual difference between A and B is brightness rather than texture
- Stone color or hue differs between images
- Lighting direction or color temperature differs between images
- Image B reads as "more premium" or "cleaner" rather than "differently textured"

---

## Post-generation review protocol

After the first generation round, evaluate only:

1. **Pair cleanliness** — do A and B look like the same setup?
2. **Single variable isolation** — is only one thing different between A and B?
3. **Valence symmetry** — does either image read as clearly preferable?
4. **Rejection criteria** — does any rejection criterion apply?

Do not evaluate which image is "better." Do not assign axis based on which image appears more appealing. Axis assignment is a separate step after both images pass the matching checklist.
