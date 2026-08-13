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

Top/Bottom is only presentation-position information. Because asset position is randomized, the primary descriptive statistics are calculated by **candidate pair + concrete asset variant**, with `no_clear_choice` reported separately. Top/Bottom choice counts are shown only as an informational position-bias diagnostic.

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
- primary pair-level statistics by concrete asset variant + `no_clear_choice`
- separate informational Top/Bottom position diagnostic
- one card per participant
- all six pair responses ordered by `presentation_index`
- Top asset / Bottom asset
- normalized Top / Bottom / No clear choice position
- actual selected asset filename
- free text
- optional intensity
- `hard_to_identify`
- latency in seconds
- CSV export with `top_asset`, `bottom_asset`, `choice_position`, and `chosen_asset`

The known v0.3 smoke-test participant is hidden by default and can be shown explicitly as `TECH / EXCLUDE`.

## Research boundary

This is a raw-data viewing/export tool, not an interpretation engine.

It must not:

- edit or delete response rows
- infer CS/CR signal polarity
- score participants
- classify free text automatically as supported/cross-load/confound
- treat Top/Bottom position as the substantive stimulus result
- change the frozen participant protocol

Post-hoc research coding remains a separate analysis layer.
