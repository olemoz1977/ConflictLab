# Human Wave 1 — Hostinger deployment handoff

**Status:** EXTERNAL-LIVE / PRE-PILOT  
**Handoff date:** 2026-08-13  
**Live:** `https://omesg360.eu/wave1/`

This folder records the current deployment boundary. It is **not yet a byte-for-byte source mirror** of the live Hostinger installation.

Do not reconstruct or overwrite the live site from this README alone.

---

## Reported live stack

```text
UI         HTML + vanilla JS
API        PHP
Storage    MySQL
Assets     local static files under /wave1/assets/
Hosting    Hostinger
```

Reported live server files:

```text
public_html/wave1/index.html
public_html/wave1/api.php
public_html/wave1/config.php      ← contains deployment secrets; NEVER commit
public_html/wave1/assets/
public_html/wave1/check.php       ← should be removed or protected before wider rollout
```

`setup.php` was reported deleted after setup.

---

## Reported response schema at handoff

```text
id             INT AUTO_INCREMENT PRIMARY KEY
participant_id VARCHAR(36)
candidate_id   VARCHAR(20)
left_asset     VARCHAR(100)
right_asset    VARCHAR(100)
choice         ENUM('left','right','no_clear_choice')
free_text      TEXT nullable
intensity      TINYINT nullable
latency_ms     INT nullable
created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

Indexes reported: primary key, participant index, candidate index.

No DB password, API key or live config value belongs in this public repository.

---

## Reported live behavior

- six Wave 1 pairs
- randomized pair order
- randomized left/right presentation
- left / right / `no_clear_choice`
- left/right choice opens free-text + 1–5 intensity step
- `no_clear_choice` currently skips reason capture
- responses POST to PHP API and are stored in MySQL
- session ends with a thank-you screen

Reported API security controls at handoff:

- candidate whitelist
- `basename()` handling for asset names
- per-participant rate limit

These controls are an implementation handoff, not a formal security audit.

---

## Reported verification

At handoff the following were reported working:

- mobile UI
- all six pairs
- API response
- MySQL writes
- CS and CR family coverage
- 28 DB response records present

The repository does not yet establish whether those 28 rows are all technical test records. Do not delete them without classification.

---

## Pre-pilot hardening checklist

Before wider participant rollout, verify/implement:

- [ ] remove or password-protect public `check.php`
- [ ] collect a reason path for `no_clear_choice` instead of automatically skipping reaction capture
- [ ] add explicit `hard_to_identify` distinct from `no_clear_choice`
- [ ] add `protocol_version`
- [ ] add `presentation_index`
- [ ] verify duplicate/retry idempotency
- [ ] verify latency clock starts only when both images are loaded/displayed
- [ ] real-device smoke test all response paths
- [ ] classify current DB records before cleaning test data

Optional later:

- admin CSV/JSON export
- additional language support

---

## Source mirror rule

When the exact live files are available, commit a sanitized mirror under this directory, for example:

```text
deploy/wave1-hostinger/
├── index.html
├── api.php
├── config.example.php
├── schema.sql / migrations/
└── README.md
```

**Never commit:**

- live `config.php`
- database password
- Hostinger API key
- any participant dataset from the live database

The live deployment and repository should only be declared synchronized after an exact source comparison.
