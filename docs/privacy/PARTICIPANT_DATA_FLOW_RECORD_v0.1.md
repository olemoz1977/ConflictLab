# ConflictLab — Participant Data Flow Record v0.1

**Date:** 2026-08-15  
**Status:** CURRENT ARCHITECTURAL BOUNDARY  
**Controller:** Oleg Mozochin  
**Privacy contact:** info@omesg360.eu

## 1. Scope

This record defines where participant data may flow in the current ConflictLab / OMESG360 `wave` research environment.

## 2. GitHub boundary

GitHub is used only for:

- source code;
- configuration;
- methodology and architecture documentation;
- version history / audit trail;
- build and release artifacts where applicable.

Current rule:

```text
PARTICIPANT RESEARCH DATA -> NOT STORED IN GITHUB
PARTICIPANT SESSION TELEMETRY -> NOT STORED IN GITHUB
PARTICIPANT FREE TEXT -> NOT STORED IN GITHUB
PARTICIPANT IDENTIFIERS -> NOT STORED IN GITHUB
```

GitHub is therefore **outside the intended participant-research data flow** for the current Hostinger `wave` study.

This statement must be revisited if a future implementation sends participant events, analytics, issue reports, crash logs, uploads, GitHub Pages telemetry under project control, or any other participant-derived content to GitHub services.

## 3. Runtime participant-data environment

The participant-facing research runtime is hosted in the Hostinger environment under the OMESG360 domain / `wave` project deployment.

Current intended flow:

```text
Participant browser
  -> HTTPS
Hostinger-hosted ConflictLab / wave runtime
  -> isolated Hostinger research database
  -> authenticated Hostinger admin interface / export
```

No research-data synchronization to GitHub is authorized.

## 4. Local-only browser data

Where the product-shaped flow uses local reflection or other local-only state:

```text
browser/local state
-> remains on participant device
-> is not uploaded to GitHub
-> is not uploaded to Hostinger research DB unless a future explicit protocol authorizes it
```

Current timing-study rule keeps reflection/reason/intensity content outside the research server payload.

## 5. Hosting/security logs

Hostinger infrastructure may separately process request/security logs needed to operate and secure the hosting service. Those logs are not the ConflictLab research dataset and must not be joined to research telemetry for construct analysis.

## 6. Compliance consequence

For the current participant study, the processor/data-host review focuses on the Hostinger runtime, database, backups, logs, admin/export path, subprocessors and transfer routes.

GitHub remains relevant to software-development security and provenance, but not as a repository of participant research records under the current design.

## 7. Change control

Any future feature that sends participant-derived data to GitHub requires:

1. a new version of this record;
2. privacy/data-flow review;
3. lawful-basis / transparency update where applicable;
4. processor/transfer assessment before activation.
