# 2Pair Integrated Pilot v0.1 — minimal interest telemetry

Purpose: measure whether public traffic reaches and starts the pilot before making further product/stimulus changes.

This is **operational interest telemetry**, not research evidence and not part of the 2Pair measurement model.

## Funnel events

- `page_open` — pilot entry page loaded.
- `start_click` — participant pressed Start practice / Pradėti treniruotę.
- `consent_screen` — training ended and the research/local participation screen was reached.
- `research_join` — participant chose the data-upload research path.
- `local_continue` — participant chose the local-only path.

## Privacy boundary

Stored only as daily aggregate counters in `tp_interest_daily` by:

- UTC date;
- release id;
- event name;
- coarse source label;
- language;
- device category.

Not stored:

- IP address;
- name/email;
- browser fingerprint;
- persistent visitor/user id;
- research session UUID;
- full referrer URL.

Counts are **events/page visits, not unique people**. Reloading the pilot can create another `page_open`.

## Research/timing boundary

Telemetry does not write to `tp_integrated_*` tables and is not used by timing/stimulus-validation exports.

During rapid-choice screens the telemetry script does not process visual-choice buttons. `consent_screen` detection only reacts to the page leaving rapid mode after training, so no telemetry network request is introduced into the measured research blocks.

## Source attribution

Explicit query parameters are preferred:

```text
?src=2rasi.lt
?src=2rasi.com
?src=instagram_reel
```

If no explicit source is present, only the referrer hostname is reduced to a coarse source label such as `2rasi.lt`, `2rasi.com`, `instagram`, `facebook`, `direct`, or another hostname.

## Admin

After deployment:

```text
/server/interest_admin.php
```

It uses the same admin password/session as the existing integrated admin and shows today / 7-day / all-time funnel counts plus 7-day source and device breakdowns.

## Hostinger deployment files

Deploy these release files together:

- `.htaccess`
- `index.php`
- `interest.js`
- `server/interest_event.php`
- `server/interest_admin.php`

`interest_event.php` creates the aggregate `tp_interest_daily` table with `CREATE TABLE IF NOT EXISTS` on first use. Existing `tp_integrated_*` tables are not changed.
