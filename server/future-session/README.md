# Future-session ingestion prototype

**Status: NOT DEPLOYED / NOT PRODUCTION READY**

This directory is the isolated server-side ingestion prototype for the post-Wave-1 architecture. It does not replace or modify `deploy/wave1-hostinger/api.php`.

## Responsibility boundary

The server accepts research telemetry only. It does **not** calculate participant results and does not receive personal reflection content in the v0.2 baseline.

Accepted envelope types:

```text
rapid_pair_event
rapid_block_attempt
reflection_reason_event   # explicit opt-in only
```

Explicitly rejected from payloads:

```text
participant_id / participantId
free_text / freeText
reaction_intensity / reactionIntensity
self-report fields
derived result fields
published result snapshots
absolute client timestamps
```

## Envelope

```json
{
  "messageId": "uuid-v4",
  "type": "rapid_pair_event",
  "payload": {}
}
```

The outbox uses `messageId` for immutable idempotency. Exact duplicate insertion returns HTTP `409` with code `IDEMPOTENT_DUPLICATE`; the client may treat that as acknowledged because the immutable server row already exists.

## Fail-closed config

`api_v2.php` requires a local `config.php` based on `config.example.php`.

The API must validate incoming pair identity against a versioned **RELEASED** stimulus-set JSON. A DRAFT or unknown stimulus set is rejected.

Structured reflection reason events require both:

1. a released reason-map version containing the concrete `reason_id` for that pair/anchor;
2. a consent version explicitly allow-listed in server config.

The example config allow-list is empty by default, so reflection telemetry cannot be accepted accidentally.

## Timing rule

The server stores already-decided integer telemetry. It never uses `server_received_at` to decide whether a participant beat the rapid-block deadline. Deadline authority remains the full-precision client monotonic clock under ADR-010/ADR-012.

## Abuse boundary

Session-scoped rate limits protect against accidental loops, not deliberate public-API abuse; an attacker can rotate session UUIDs. A deployment review must choose hosting/WAF-level abuse controls without introducing a persistent participant fingerprint into the research dataset.
