import assert from 'node:assert/strict';
import {
  MAX_BLOCK_ATTEMPTS,
  RapidBlockAttempt,
  deriveReflectionAnchors,
  exposureCountsFromEvents,
} from '../src/future_session/rapid_block_core.mjs';

function makePairs() {
  return [
    {
      pairId: 'P1', assetAId: 'P1-A', assetBId: 'P1-B',
      assetAPosition: 'left', assetBPosition: 'right',
    },
    {
      pairId: 'P2', assetAId: 'P2-A', assetBId: 'P2-B',
      assetAPosition: 'left', assetBPosition: 'right',
    },
    {
      pairId: 'P3', assetAId: 'P3-A', assetBId: 'P3-B',
      assetAPosition: 'left', assetBPosition: 'right',
    },
  ];
}

function makeAttempt(attemptNumber = 1, priorExposureCounts = {}) {
  let id = 0;
  return new RapidBlockAttempt({
    sessionId: 'session-1',
    blockId: 'block-1',
    blockAttemptId: `attempt-${attemptNumber}`,
    attemptNumber,
    blockBudgetMs: 6000,
    pairs: makePairs(),
    protocolVersion: 'future-session-v0.2',
    stimulusSetVersion: 'stimulus-set-test',
    priorExposureCounts,
    eventIdFactory: () => `e-${attemptNumber}-${++id}`,
  });
}

// Stable A/B identities are raw facts and are independent from screen position.
{
  const a = makeAttempt();
  a.markPairReady(0);
  const event = a.recordChoice('A', 100).event;
  assert.equal(event.assetAId, 'P1-A');
  assert.equal(event.assetBId, 'P1-B');
  assert.equal(event.assetAPosition, 'left');
  assert.equal(event.assetBPosition, 'right');
  assert.equal(event.choice, 'A');
}

// Pair definitions without stable distinct asset identities are rejected.
{
  const badPairs = makePairs();
  delete badPairs[0].assetAId;
  assert.throws(
    () => new RapidBlockAttempt({
      sessionId: 's', blockId: 'b', blockAttemptId: 'a', attemptNumber: 1,
      blockBudgetMs: 6000, pairs: badPairs, protocolVersion: 'p',
      stimulusSetVersion: 's', eventIdFactory: () => 'e',
    }),
    /stable assetAId and assetBId are required/
  );
}

// Boundary: strictly before the deadline is valid.
{
  const a = makeAttempt();
  a.markPairReady(1000);
  const result = a.recordChoice('A', 6999);
  assert.equal(result.status, 'CHOICE_RECORDED');
  assert.equal(result.event.choice, 'A');
  assert.equal(result.event.blockElapsedMsAtEvent, 5999);
}

// Full-precision clock decides validity; persisted telemetry is floored to integer ms.
{
  const a = makeAttempt();
  a.markPairReady(0.25);
  const result = a.recordChoice('A', 6000.0); // precise elapsed = 5999.75
  assert.equal(result.status, 'CHOICE_RECORDED');
  assert.equal(result.event.blockElapsedMsAtEvent, 5999);
  assert.equal(result.event.visualChoiceLatencyMs, 5999);
  assert.equal(result.event.pairReadyElapsedMs, 0);
  assert.equal(result.event.remainingBudgetAtPairStartMs, 6000);
}

// Configured block budget is an integer transport/storage contract.
{
  assert.throws(
    () => new RapidBlockAttempt({
      sessionId: 's', blockId: 'b', blockAttemptId: 'a', attemptNumber: 1,
      blockBudgetMs: 6000.5, pairs: makePairs(), protocolVersion: 'p',
      stimulusSetVersion: 's', eventIdFactory: () => 'e',
    }),
    /blockBudgetMs must be a positive integer/
  );
}

// Exactly at deadline becomes timeout, not a late A/B choice.
{
  const a = makeAttempt();
  a.markPairReady(1000);
  const result = a.recordChoice('A', 7000);
  assert.equal(result.status, 'TIMEOUT');
  assert.equal(result.events[0].choice, 'timeout');
  assert.equal(result.events[0].pairPresented, true);
  assert.equal(result.events[1].pairPresented, false);
  assert.equal(result.events[2].pairPresented, false);
}

// A scheduling bug must not be able to expire the block early.
{
  const a = makeAttempt();
  a.markPairReady(0);
  assert.throws(
    () => a.expire(5999),
    /cannot expire block before monotonic deadline/
  );
}

// If P1 was chosen and the budget expires before P2 becomes interactive,
// P2/P3 are non-exposures, not shown timeouts.
{
  const a = makeAttempt();
  a.markPairReady(0);
  a.recordChoice('A', 1000);
  const result = a.expire(6500);
  assert.equal(result.events.length, 2);
  assert.equal(result.events[0].pairId, 'P2');
  assert.equal(result.events[0].pairPresented, false);
  assert.equal(result.events[0].pairExposureNumber, null);
  assert.equal(result.events[0].pairReadyElapsedMs, null);
  assert.equal(result.events[1].pairId, 'P3');
  assert.equal(result.events[1].pairPresented, false);
}

// If P2 was already interactive when budget expires, P2 is a shown timeout;
// P3 remains a non-exposure.
{
  const a = makeAttempt();
  a.markPairReady(0);
  a.recordChoice('A', 1000);
  a.markPairReady(1500);
  const result = a.expire(6200);
  assert.equal(result.events[0].pairId, 'P2');
  assert.equal(result.events[0].pairPresented, true);
  assert.equal(result.events[0].pairExposureNumber, 1);
  assert.equal(result.events[0].pairReadyElapsedMs, 1500);
  assert.equal(result.events[1].pairId, 'P3');
  assert.equal(result.events[1].pairPresented, false);
}

// Backgrounding never pauses or extends the experimental clock.
{
  const a = makeAttempt();
  a.markPairReady(100);
  a.markPageHidden();
  const result = a.recordChoice('B', 6100);
  assert.equal(result.status, 'TIMEOUT');
  assert.equal(a.getSummary().pageHiddenDuringBlock, true);
  assert.equal(a.getSummary().blockElapsedMsFinal, 6000);
}

// Pair events store only whether backgrounding had happened before that event;
// attempt summary stores whether it happened at any point during the whole block.
{
  const a = makeAttempt();
  a.markPairReady(0);
  const first = a.recordChoice('A', 500).event;
  assert.equal(first.pageHiddenBeforeEvent, false);

  a.markPairReady(700);
  a.markPageHidden();
  const second = a.recordChoice('B', 900).event;
  assert.equal(second.pageHiddenBeforeEvent, true);

  a.markPairReady(1000);
  a.recordChoice('A', 1200);
  assert.equal(a.getSummary().pageHiddenDuringBlock, true);
}

// Retry limit: attempts 1–2 can retry, attempt 3 moves to reflection.
{
  for (const n of [1, 2]) {
    const a = makeAttempt(n);
    a.markPairReady(0);
    assert.equal(a.expire(6000).next, 'RETRY');
  }
  const a3 = makeAttempt(MAX_BLOCK_ATTEMPTS);
  a3.markPairReady(0);
  assert.equal(a3.expire(6000).next, 'REFLECTION');
}

// Exposure number counts actual presentations, not attempt numbers.
{
  const first = makeAttempt(1);
  first.markPairReady(0);
  first.recordChoice('A', 500);
  first.expire(6000); // P2/P3 were never presented.

  const counts = exposureCountsFromEvents(first.events);
  assert.deepEqual(counts, { P1: 1 });

  const retry = makeAttempt(2, counts);
  retry.markPairReady(0); // P1 exposure 2
  assert.equal(retry.recordChoice('A', 300).event.pairExposureNumber, 2);
  retry.markPairReady(400); // P2 exposure 1
  assert.equal(retry.recordChoice('B', 600).event.pairExposureNumber, 1);
}

// Reflection anchor prefers primary A/B; retry is used only when primary had none.
{
  const events = [
    {
      eventId: 'p1-primary', pairId: 'P1', pairPresented: true,
      choice: 'A', blockAttemptNumber: 1, blockElapsedMsAtEvent: 100,
    },
    {
      eventId: 'p1-retry', pairId: 'P1', pairPresented: true,
      choice: 'B', blockAttemptNumber: 2, blockElapsedMsAtEvent: 90,
    },
    {
      eventId: 'p2-timeout', pairId: 'P2', pairPresented: true,
      choice: 'timeout', blockAttemptNumber: 1, blockElapsedMsAtEvent: 6000,
    },
    {
      eventId: 'p2-retry', pairId: 'P2', pairPresented: true,
      choice: 'B', blockAttemptNumber: 2, blockElapsedMsAtEvent: 200,
    },
    {
      eventId: 'p3-never', pairId: 'P3', pairPresented: false,
      choice: 'timeout', blockAttemptNumber: 1, blockElapsedMsAtEvent: 6000,
    },
  ];

  const anchors = deriveReflectionAnchors(events);
  const p1 = anchors.find(x => x.pairId === 'P1');
  const p2 = anchors.find(x => x.pairId === 'P2');
  const p3 = anchors.find(x => x.pairId === 'P3');

  assert.equal(p1.anchorSource, 'PRIMARY');
  assert.equal(p1.anchorChoice, 'A');
  assert.equal(p2.anchorSource, 'FIRST_COMPLETED_RETRY');
  assert.equal(p2.anchorChoice, 'B');
  assert.equal(p3, undefined);
}

console.log('rapid_block_core: all tests passed');
