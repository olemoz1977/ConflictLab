# Decision Drivers — 8×8 prototype v0.2

**Status:** owner-only product/measurement prototype.  
**Date:** 2026-08-29.  
**Naming:** `Decision Drivers` is a neutral working label only. The product is not named ConflictLab or 2Pair.

## Purpose

Prototype the participant experience around the current candidate measurement object:

> What tends to win when meaningful motives compete in forced visual choices?

This is not a validated psychological test and must not be used for individual claims.

## Eight candidate directions

- Opportunity / Galimybė
- Protection / Apsauga
- Autonomy / Laisvė rinktis
- Certainty / Aiškumas
- Exploration / Tyrinėjimas
- Mastery / Meistriškumas
- Connection / Ryšys
- Influence / Poveikis

## Prototype design

- 12 visual duels.
- Each candidate direction appears exactly 3 times (balanced 3-regular comparison graph).
- A/B display side and duel order are randomized.
- No visible timer.
- `Neturiu aiškaus pasirinkimo` remains available.
- No reflection after each choice.
- No server upload; all events remain in-memory in the browser.
- Latency is recorded locally for owner inspection only and has no psychological meaning.
- Result uses wins / clear duels, not personality percentages.

## Evidence boundary

Existing assets are reused without new image generation.

Three internal asset grades are shown only in Owner technical view:

- `SEED` — legacy evidence contains a plausible semantic bridge to the new driver collision.
- `EXPERIMENTAL` — useful existing scene, but new mapping has not been validated.
- `WEAK` — included to expose UX/coverage gaps, especially Influence; not a defensible scoring item.

The prototype deliberately exposes weak coverage rather than pretending all eight directions already have equal stimulus validity.

## Important methodological warning

The 8×8 result is a **product architecture mock result**, not a research result. Existing legacy image choices must not be retroactively scored under the new driver ontology.

Before any candidate collision becomes scoring-eligible it still needs the V2 process:

construct specification → independent exemplars → confound audit → blind semantic coding → research-only reason capture → cross-exemplar convergence → external validation → paired-comparison calibration.

## Runtime boundary

This prototype is separate from the frozen Integrated v0.1 pilot. It changes no production/research runtime, database, collection mode, Gate D/E, or frozen procedure.
