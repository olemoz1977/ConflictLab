# ConflictLab — Session interruption and deletion-code boundary v0.1

**Date:** 2026-08-15  
**Status:** IMPLEMENTED IN LAB CODE / LIVE TECHNICAL SMOKE STILL REQUIRED

## Rule

For consented timing research, the participant must possess the plaintext deletion code **before any timing-research payload can be uploaded**.

Flow:

```text
consent + 18+
-> browser generates random 32-hex deletion code
-> participant sees code
-> participant confirms code was saved
-> main timing block starts
-> completed/final-allowed timing block may upload
-> browser hashes code with SHA-256
-> server receives only deletion_token_hash
```

## Interruption semantics

```text
close before consent                         -> no research DB row
close on consent screen                      -> no research DB row
local-only route                             -> no research DB row
close after code shown but before block      -> no research DB row; code is unused
close during unfinished measured block       -> no research DB row; code is unused
completed/final-allowed block + upload OK     -> timing row may exist; participant already has code
close during/after reflection                 -> timing row may exist; reflection remains local
upload failure                               -> no successful research row assumed; shown code may be unused
```

Partial measured choices are not streamed to the research DB. Upload occurs only after the rapid block reaches the terminal state that proceeds to reflection.

## Fail-closed controls

- consented route generates the deletion code before entering the measured-block intro;
- participant must acknowledge that the code was saved before proceeding;
- `postCalibration()` no longer silently creates a late deletion code;
- if no prepared deletion code exists, upload fails locally with `DELETION_TOKEN_NOT_PREPARED`;
- server continues to require a valid lowercase SHA-256 `deletionTokenHash` for CALIBRATION ingestion;
- plaintext deletion code is never stored server-side.

## Implementation

Deploy code commit:

`2f20b765afeeac2b635871da222dc4025edd03dc`

CI:

```text
workflow run 31853788841 (#487)
SUCCESS
artifact id 9238372916
artifact digest sha256:d69d4ec72c6b735578952908ea364bf2e956fc22176efa941049c8955b698555
```

The Hostinger `index.php` delivery adapter applies the pre-upload gate to the validated `index.html` source and fails with HTTP 500 if its expected source anchors no longer match. This is intentional drift protection for the current LAB release.

## Methodology/privacy boundary

This change does not alter:

```text
collection_mode = TECHNICAL
Gate D = NONE
Gate E = NONE
6000 ms = unvalidated mechanical candidate
participant directional result = NOT AUTHORIZED
/wave1/ = unchanged
```

Before external CALIBRATION activation, public privacy wording must state that the deletion code is generated/shown before the research upload, while only its hash is sent to the server.
