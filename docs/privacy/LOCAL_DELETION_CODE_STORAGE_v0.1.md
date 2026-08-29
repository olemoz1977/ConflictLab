# ConflictLab — Local Deletion Code Storage v0.1

**Date:** 2026-08-15  
**Scope:** `calibration-v0.1` mechanical timing research privacy UX.

## Decision

For consented timing-research sessions, the plaintext participant deletion code is generated in the participant browser **before any research upload**.

The browser attempts to retain recent deletion codes in same-origin `localStorage` under a versioned ConflictLab key so that forgetting to manually copy the code does not unnecessarily prevent later self-service deletion.

## Boundary

```text
browser localStorage:
  plaintext random deletion code(s)
  created-at timestamp
  release id

research server DB:
  SHA-256(deletion code) only

research export:
  no deletion code
  no deletion-token hash
```

The local browser store is not research telemetry, is not uploaded for analysis, is not used as a persistent participant identity, and must not be joined to Gate D/E or psychological interpretation.

## Behaviour

- The code is shown before the main research block.
- The browser attempts to store it locally before the participant can continue.
- Manual copy remains available because local storage can be unavailable or cleared by the user/browser.
- Up to 12 recent codes may be retained locally to avoid overwriting a prior session's code.
- `delete_my_data.php` may prefill the most recent locally stored code on the same browser/origin.
- After a completed deletion request, the submitted code is removed from the local list.
- Clearing browser/site data can remove locally saved codes; no server-side plaintext recovery is possible.

## Privacy meaning

This mechanism deliberately trades a small amount of participant-controlled local persistence for easier exercise of erasure/withdrawal rights without collecting name, email, account identity, or another direct identifier on the research server.

Before external CALIBRATION activation, the participant-facing privacy notice must disclose that the deletion code may be stored locally in the browser for this purpose.
