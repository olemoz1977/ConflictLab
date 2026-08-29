# ConflictLab Hostinger release scaffold

**Status:** repository-only deployment scaffold; no live change.

This directory defines how future ConflictLab releases are packaged and promoted on Hostinger without overwriting the frozen Wave 1 v0.3 deployment before explicit owner authorization.

## Intended live layout

```text
public_html/
├── index.html                    # OMESG360 root; unchanged by this workflow
├── wave1/                        # stable public entrypoint; current v0.3 remains live
└── conflictlab/
    └── releases/
        └── <release-id>/         # immutable candidate/approved release
```

## Promotion sequence

```text
LAB
→ OWNER APPROVAL
→ PUBLIC SWITCH
→ optional ROLLBACK
```

The candidate release is tested directly at its versioned path first. A public switch must never require rebuilding or changing the approved release bytes.

## Files in this scaffold

- `templates/PUBLIC_ENTRYPOINT_SWITCH_TEMPLATE.md` — non-executable operator template for the future `/wave1/` switch.
- `templates/release-manifest.example.json` — audit manifest template for each immutable release.

## Non-negotiable safety rules

- Do not edit `deploy/wave1-hostinger/` as part of building a new release.
- Do not deploy anything to `/wave1/` during LAB or OWNER APPROVAL.
- Do not modify the OMESG360 root for calibration deployment.
- Never commit real Hostinger credentials, DB credentials, passwords or participant data.
- OWNER_APPROVED is not the same as PUBLIC.
- PUBLIC requires a separate explicit owner authorization.
- Rollback restores the previous `/wave1/index.html`; it does not delete the new release.

Architecture source:

`docs/architecture/HOSTINGER_RELEASE_ROUTING_v0.1.md`
