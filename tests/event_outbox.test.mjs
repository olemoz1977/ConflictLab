import assert from 'node:assert/strict';
import {
  EventOutbox,
  MemoryOutboxStore,
  canonicalJson,
  classifyTransportResult,
  retryDelayMs,
} from '../src/future_session/event_outbox.mjs';

function envelope(id, payload = { pairId: 'P1', choice: 'A' }) {
  return {
    messageId: id,
    type: 'rapid_pair_event',
    payload,
  };
}

// Canonical JSON ignores object-key insertion order but preserves array order.
{
  assert.equal(
    canonicalJson({ b: 2, a: { y: 2, x: 1 } }),
    canonicalJson({ a: { x: 1, y: 2 }, b: 2 })
  );
  assert.notEqual(canonicalJson([1, 2]), canonicalJson([2, 1]));
}

// HTTP classification is explicit: successful/duplicate/retry/reject.
{
  assert.equal(classifyTransportResult({ status: 201 }).disposition, 'ACK');
  assert.equal(classifyTransportResult({ status: 409 }).disposition, 'ACK_DUPLICATE');
  assert.equal(classifyTransportResult({ status: 429 }).disposition, 'RETRY');
  assert.equal(classifyTransportResult({ status: 503 }).disposition, 'RETRY');
  assert.equal(classifyTransportResult({ status: 400 }).disposition, 'REJECT');
}

// Exponential backoff is deterministic and capped.
{
  assert.equal(retryDelayMs(1), 1000);
  assert.equal(retryDelayMs(2), 2000);
  assert.equal(retryDelayMs(7), 60000);
  assert.equal(retryDelayMs(20), 60000);
}

// Same immutable message may be re-enqueued with different key ordering without duplication.
{
  let now = 100;
  const store = new MemoryOutboxStore();
  const outbox = new EventOutbox({ store, now: () => now });

  await outbox.enqueue(envelope('e1', { a: 1, b: 2 }));
  now = 200;
  await outbox.enqueue(envelope('e1', { b: 2, a: 1 }));

  const pending = await outbox.listPending();
  assert.equal(pending.length, 1);
  assert.equal(pending[0].createdAtMs, 100);
}

// Reusing an ID with different content is a hard collision.
{
  const store = new MemoryOutboxStore();
  const outbox = new EventOutbox({ store });
  await outbox.enqueue(envelope('collision', { choice: 'A' }));
  await assert.rejects(
    outbox.enqueue(envelope('collision', { choice: 'B' })),
    /messageId collision with different payload/
  );
}

// 2xx ACK removes the durable record.
{
  const store = new MemoryOutboxStore();
  const outbox = new EventOutbox({ store });
  await outbox.enqueue(envelope('ack'));
  const result = await outbox.flush(async () => ({ status: 201 }));
  assert.deepEqual(result, { acked: 1, retried: 0, rejected: 0, skipped: 0 });
  assert.equal((await outbox.listPending()).length, 0);
}

// 409 is also an ACK because server-side primary key proves prior ingestion.
{
  const store = new MemoryOutboxStore();
  const outbox = new EventOutbox({ store });
  await outbox.enqueue(envelope('duplicate'));
  const result = await outbox.flush(async () => ({ status: 409 }));
  assert.equal(result.acked, 1);
  assert.equal((await store.list()).length, 0);
}

// Transient failure is retained with backoff and skipped before due time.
{
  let now = 10_000;
  const store = new MemoryOutboxStore();
  const outbox = new EventOutbox({ store, now: () => now });
  await outbox.enqueue(envelope('retry'));

  let calls = 0;
  let result = await outbox.flush(async () => {
    calls += 1;
    return { status: 503 };
  });
  assert.equal(result.retried, 1);

  let record = await store.get('retry');
  assert.equal(record.sendAttempts, 1);
  assert.equal(record.nextAttemptAtMs, 11_000);

  now = 10_999;
  result = await outbox.flush(async () => {
    calls += 1;
    return { status: 201 };
  });
  assert.equal(result.skipped, 1);
  assert.equal(calls, 1);

  now = 11_000;
  result = await outbox.flush(async () => {
    calls += 1;
    return { status: 503 };
  });
  assert.equal(result.retried, 1);
  record = await store.get('retry');
  assert.equal(record.sendAttempts, 2);
  assert.equal(record.nextAttemptAtMs, 13_000);
}

// A thrown network error is retryable and does not lose the message.
{
  const store = new MemoryOutboxStore();
  const outbox = new EventOutbox({ store, now: () => 1000 });
  await outbox.enqueue(envelope('network'));
  const result = await outbox.flush(async () => {
    throw new Error('offline');
  });
  assert.equal(result.retried, 1);
  assert.equal((await outbox.listPending()).length, 1);
}

// Permanent 4xx is retained as rejected for diagnostics, not retried forever.
{
  const store = new MemoryOutboxStore();
  const outbox = new EventOutbox({ store });
  await outbox.enqueue(envelope('bad'));
  const result = await outbox.flush(async () => ({ status: 422 }));
  assert.equal(result.rejected, 1);
  assert.equal((await outbox.listPending()).length, 0);
  assert.equal((await outbox.listRejected()).length, 1);
}

// Concurrent flush requests share one in-flight flush and must not double-send.
{
  const store = new MemoryOutboxStore();
  const outbox = new EventOutbox({ store });
  await outbox.enqueue(envelope('once'));

  let sends = 0;
  let release;
  const gate = new Promise(resolve => { release = resolve; });
  const send = async () => {
    sends += 1;
    await gate;
    return { status: 201 };
  };

  const first = outbox.flush(send);
  const second = outbox.flush(send);
  release();
  await Promise.all([first, second]);
  assert.equal(sends, 1);
}

console.log('event_outbox: all tests passed');
