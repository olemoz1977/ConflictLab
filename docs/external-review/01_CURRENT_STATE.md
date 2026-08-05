# 01 — Current State

This document describes what currently exists, without theoretical interpretation.

## ConflictLab v0.7 (main product)

- **Status:** feature-frozen, beta-ready (per internal `PROJECT_STATE.md`)
- **Current flow:** 3×4 session structure across three internal axes (aw/cs/cr)
- **Observation Engine:** translates raw axis signals into semantic observation labels (e.g. `clarity_seeking`) before any text is generated. This is a naming convention for internal software functions — see the terminology note in `06_REVIEWER_GUIDE.md`.
- **Micro-dialogue:** cue-based interaction layer; cue-vector assignments across the stimulus set are marked internally as `provisional` / `not validated` and have no documented origin for several secondary axis weights
- **Known gaps:** no normed stimulus set, no validated cue-to-axis mapping, no external psychometric comparison
- **Relationship to Pair P0:** Pair P0 is a separate, isolated experiment. It does not feed into or draw from v0.7's scoring, and v0.7 code was not modified during Pair P0 development.

## Pair P0 (experimental branch)

- **Current stable tag:** `pair-p0-j0-stable`
- **Location:** `docs/experiments/pair-p0/` (fully isolated from v0.7)

### Implemented and real-device tested stages

| Stage | What it does |
|---|---|
| Pair selection | Two images shown per pair; person selects one; latency and position are recorded |
| Cue reflection | Person picks a pre-written phrase, writes their own ("Another thought"), or selects "Hard to say" |
| Session reflection | After all pairs, person sees a summary. The person may write an overall observation or leave it unstated. |
| Session result | Shows the person's own choices; literal display (see next stage); a methodological boundary note |
| **Literal choice reflection (Stage I)** | Shows the exact wording the person chose for each pair, in order, with no grouping or theme assigned; person is then asked whether they notice any connection between the choices, with three explicitly separate answers: name it, "I do not see it yet," or "I prefer not to name it" |
| History | List and detail view of completed sessions only; active (unfinished) sessions are never shown as completed |
| Radar (secondary, experimental layer) | Appears only after 3 sessions meet strict eligibility criteria; visualizes a session-vector average; explicitly labeled as not a personality assessment |
| Export/Import (Stage H) | Local-only JSON export/import of completed sessions; duplicate protection by `session_id`; no server involved |
| Local data reset (Stage J0) | Clears only `cl_pair_p0_` namespaced localStorage keys; requires explicit checkbox confirmation; never uses `localStorage.clear()` |

### What is deliberately not included

- **Stage F (period comparison)** — SUPERSEDED / ROLLED BACK. A "Now vs. Earlier" 3-session-window comparison was implemented and briefly present in the codebase, but the stable Pair P0 line was subsequently rolled back to the last confirmed-stable point before Stage F, and Stage F is not part of the current `pair-p0-j0-stable` implementation. It may be revisited later, but as of this document it does not exist in the running system.
- **Stage G (thematic comparison across sessions)** — attempted twice, rejected both times. First attempt used a cue-to-theme mapping built on an incorrect A/B image assumption, producing wrong thematic labels. A corrected single-theme-per-cue mapping was drafted and verified against the live cue catalog, but a subsequent implementation attempt caused a real UI failure (history and export appeared broken) and was rolled back in full rather than patched. The corrected mapping exists in conversation history but is not implemented in code.
- No AI/LLM interpretation of any user text anywhere in Pair P0
- No accounts, login, or cloud sync
- No encryption, QR codes, or Google Drive integration

### What has been tested on a real device (not simulated)

All Stage H (export/import) scenarios were executed on a physical phone across multiple browsers (Chrome, Edge, and at least one additional browser used as a "clean" test environment). Stage J0 (data reset) scenarios A–D were tested on a physical phone; scenario E (namespace isolation — confirming that clearing Pair P0 data does not touch other localStorage keys) was confirmed through code-logic inspection only, not a live multi-namespace browser test. Stage I (literal choice reflection) button-activation and history-display fixes were also confirmed on a physical device after two rounds of real-device bug reports.
