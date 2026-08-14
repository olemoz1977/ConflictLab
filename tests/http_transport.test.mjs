import assert from 'node:assert/strict';
import {
  blockAttemptEnvelope,
  createFutureSessionTransport,
  pairEventEnvelope,
  reflectionReasonEnvelope,
} from '../src/future_session/http_transport.mjs';

// Envelope builders preserve immutable message IDs and do not mutate source objects.
{
  const pair = { eventId: 'pair-id', choice: 'A', nested: { x: 1 } };
  const envelope = pairEventEnvelope(pair);
  assert.equal(envelope.messageId, 'pair-id');
  assert.equal(envelope.type, 'rapid_pair_event');
  envelope.payload.nested.x = 2;
  assert.equal(pair.nested.x, 1);

  const block = blockAttemptEnvelope({ blockAttemptId: 'attempt-id', blockTimedOut: false });
  assert.equal(block.messageId, 'attempt-id');
  assert.equal(block.type, 'rapid_block_attempt');

  const reason = reflectionReasonEnvelope({ eventId: 'reason-id', reasonId: 'R1' });
  assert.equal(reason.messageId, 'reason-id');
  assert.equal(reason.type, 'reflection_reason_event');
}

// Transport sends JSON to the isolated endpoint and returns status + API code.
{
  let captured;
  const send = createFutureSessionTransport({
    endpoint: '/future-session/api_v2.php',
    fetchImpl: async (url, options) => {
      captured = { url, options };
      return {
        status: 201,
        headers: { get: () => 'application/json; charset=utf-8' },
        json: async () => ({ status: 'ok', code: 'CREATED' }),
      };
    },
  });

  const result = await send({ messageId: 'm1', type: 'rapid_pair_event', payload: { x: 1 } });
  assert.deepEqual(result, { status: 201, code: 'CREATED' });
  assert.equal(captured.url, '/future-session/api_v2.php');
  assert.equal(captured.options.method, 'POST');
  assert.equal(captured.options.headers['Content-Type'], 'application/json');
  assert.equal(captured.options.credentials, 'same-origin');
  assert.equal(captured.options.cache, 'no-store');
  assert.equal(captured.options.keepalive, true);
  assert.deepEqual(JSON.parse(captured.options.body), {
    messageId: 'm1', type: 'rapid_pair_event', payload: { x: 1 },
  });
}

// 409 duplicate remains visible to the outbox classifier.
{
  const send = createFutureSessionTransport({
    endpoint: '/api_v2.php',
    fetchImpl: async () => ({
      status: 409,
      headers: { get: () => 'application/json' },
      json: async () => ({ code: 'IDEMPOTENT_DUPLICATE' }),
    }),
  });
  assert.deepEqual(
    await send({ messageId: 'm2', type: 'rapid_pair_event', payload: {} }),
    { status: 409, code: 'IDEMPOTENT_DUPLICATE' }
  );
}

// Non-JSON/error bodies never hide the HTTP status needed by retry classification.
{
  const send = createFutureSessionTransport({
    endpoint: '/api_v2.php',
    fetchImpl: async () => ({
      status: 503,
      headers: { get: () => 'text/html' },
      json: async () => { throw new Error('should not parse'); },
    }),
  });
  assert.deepEqual(
    await send({ messageId: 'm3', type: 'rapid_pair_event', payload: {} }),
    { status: 503, code: null }
  );
}

// Network failures propagate so EventOutbox can classify them as RETRY.
{
  const send = createFutureSessionTransport({
    endpoint: '/api_v2.php',
    fetchImpl: async () => { throw new TypeError('offline'); },
  });
  await assert.rejects(
    send({ messageId: 'm4', type: 'rapid_pair_event', payload: {} }),
    /offline/
  );
}

// Invalid construction fails before any network call.
{
  assert.throws(() => createFutureSessionTransport({ endpoint: '' }), /endpoint is required/);
  assert.throws(
    () => createFutureSessionTransport({ endpoint: '/x', requestTimeoutMs: 0 }),
    /requestTimeoutMs must be a positive integer/
  );
  assert.throws(() => pairEventEnvelope({}), /event.eventId is required/);
}

console.log('http_transport: all tests passed');
