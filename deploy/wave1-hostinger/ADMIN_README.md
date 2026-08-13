# Human Wave 1 — read-only admin dashboard

`admin.php` is a password-protected, read-only view for Human Wave 1 data. It does not change the participant flow, protocol version, raw responses, or stimulus assets.

## Standard

Participant presentation is **Top / Bottom**.

The MySQL schema retains legacy field/value names for v0.3 continuity:

```text
left_asset  -> Top asset
right_asset -> Bottom asset
choice=left -> Top
choice=right -> Bottom
```

The admin UI and CSV export normalize these to **Top / Bottom**. Do not rename the frozen v0.3 database fields during the pilot.

## Deployment

Upload:

```text
admin.php -> public_html/wave1/admin.php
```

Then add an admin-only password to the live server `config.php`:

```php
define('ADMIN_PASSWORD', 'YOUR_STRONG_PRIVATE_PASSWORD');
```

Never commit the real password. `config.example.php` contains only the placeholder.

Open:

```text
https://omesg360.eu/wave1/admin.php
```

## What the dashboard shows

- `wave1-v0.3` only
- participant count
- number of complete 6/6 sessions
- one card per participant
- all six pair responses ordered by `presentation_index`
- Top asset / Bottom asset
- normalized Top / Bottom / No clear choice selection
- normalized X / Y / NCC selection
- free text
- optional intensity
- `hard_to_identify`
- latency in seconds
- pair-level X / Y / NCC counts
- CSV export

The known v0.3 smoke-test participant is hidden by default and can be shown explicitly as `TECH / EXCLUDE`.

## Research boundary

This is a raw-data viewing/export tool, not an interpretation engine.

It must not:

- edit or delete response rows
- infer CS/CR signal polarity
- score participants
- classify free text automatically as supported/cross-load/confound
- change the frozen participant protocol

Post-hoc research coding remains a separate analysis layer.
