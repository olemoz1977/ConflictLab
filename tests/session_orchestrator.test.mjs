import assert from 'node:assert/strict';
import test from 'node:test';

import { FutureSessionOrchestrator } from '../src/future_session/session_orchestrator.mjs';

function plan() {
  return {
    formId: 'F2-X',
    pairs: [
      {
        pairId: 'P1',
        assetAId: 'P1-A',
        assetBId: 'P1-B',
        assetAPath: 'p1-a.png',
        assetBPath: 'p1-b.png',
        assetAPosition: 'top',
        assetBPosition: 'bottom',
      },
      {
        pairId: 'P2',
        assetAId: 'P2-A',
        assetBId: 'P2-B',
        assetAPath: 'p2-a.png',
        assetBPath: 'p2-b.png',
        assetAPosition: 'bottom',
        assetBPosition: 'top',
      },
      {
        pairId: 'P3',
        assetAId: 'P3-A',
        assetBId: 'P3-B',
        assetAPath: 'p3-a.png',
        assetBPath: 'p3-b.png',
        assetAPosition: 'top',
        assetBPosition: 'bottom',
      },
    ],
  };
}

function ids(prefix) {
  let n = 0;
  return () => `${prefix}-${++n}`;
}

test('completed primary attempt becomes reflection-ready with PRIMARY anchors', () => {
  let now = 100;
  const runner = new FutureSessionOrchestrator({
    sessionId: 'session',
    blockId: 'block',
    sessionPlan: plan(),
    blockBudgetMs: 6000,
    protocolVersion: 'future-rapid-v1',
    stimulusSetVersion: 'stimulus-set-v1',
    now: () => now,
    eventIdFactory: ids('event'),
    blockAttemptIdFactory: ids('attempt'),
  });

  runner.startAttempt();

  runner.markPairReady(now);
  now += 500;
  runner.recordChoice('A', now);

  now += 10;
  runner.markPairReady(now);
  now += 500;
  runner.recordChoice('B', now);

  now += 10;
  runner.markPairReady(now);
  now += 500;
  const result = runner.recordChoice('A', now);

  assert.equal(result.status, 'COMPLETE');
  assert.equal(runner.phase, 'REFLECTION_READY');

  const anchors = runner.reflectionAnchors();
  assert.equal(anchors.length, 3);
  assert.ok(anchors.every(anchor => anchor.anchorSource === 'PRIMARY'));

  const telemetry = runner.telemetry();
  assert.equal(telemetry.attempts.length, 1);
  assert.equal(telemetry.events.length, 3);
});

test('retry preserves plan and primary anchors remain preferred', () => {
  let now = 0;
  const runner = new FutureSessionOrchestrator({
    sessionId: 'session',
    blockId: 'block',
    sessionPlan: plan(),
    blockBudgetMs: 6000,
    protocolVersion: 'future-rapid-v1',
    stimulusSetVersion: 'stimulus-set-v1',
    now: () => now,
    eventIdFactory: ids('event'),
    blockAttemptIdFactory: ids('attempt'),
  });

  runner.startAttempt();
  runner.markPairReady(now);
  now = 500;
  runner.recordChoice('A', now);

  now = 510;
  runner.markPairReady(now);
  now = 6500;
  const timeout = runner.expire(now);
  assert.equal(timeout.phase, 'RETRY_READY');

  const retry = runner.startAttempt();
  assert.equal(retry.attemptNumber, 2);
  assert.deepEqual(
    runner.sessionPlan.pairs.map(pair => [pair.pairId, pair.assetAPosition, pair.assetBPosition]),
    plan().pairs.map(pair => [pair.pairId, pair.assetAPosition, pair.assetBPosition])
  );

  now = 7000;
  runner.markPairReady(now);
  now = 7300;
  runner.recordChoice('B', now);

  now = 7310;
  runner.markPairReady(now);
  now = 7610;
  runner.recordChoice('A', now);

  now = 7620;
  runner.markPairReady(now);
  now = 7920;
  runner.recordChoice('B', now);

  const anchors = runner.reflectionAnchors();
  assert.equal(anchors.length, 3);

  const p1 = anchors.find(anchor => anchor.pairId === 'P1');
  const p2 = anchors.find(anchor => anchor.pairId === 'P2');
  assert.equal(p1.anchorChoice, 'A');
  assert.equal(p1.anchorSource, 'PRIMARY');
  assert.equal(p2.anchorChoice, 'A');
  assert.equal(p2.anchorSource, 'FIRST_COMPLETED_RETRY');
});

test('page-hidden signal is captured without pausing the block clock', () => {
  let now = 0;
  const runner = new FutureSessionOrchestrator({
    sessionId: 'session',
    blockId: 'block',
    sessionPlan: plan(),
    blockBudgetMs: 6000,
    protocolVersion: 'future-rapid-v1',
    stimulusSetVersion: 'stimulus-set-v1',
    now: () => now,
    eventIdFactory: ids('event'),
    blockAttemptIdFactory: ids('attempt'),
  });

  runner.startAttempt();
  runner.markPairReady(now);
  runner.markPageHidden();
  now = 6000;
  runner.expire(now);

  const telemetry = runner.telemetry();
  assert.equal(telemetry.attempts[0].pageHiddenDuringBlock, true);
  assert.equal(telemetry.events[0].pageHiddenBeforeEvent, true);
});

test('pair-ready call at the deadline settles the attempt as timeout instead of leaving a dead RAPID phase', () => {
  let now = 0;
  const runner = new FutureSessionOrchestrator({
    sessionId: 'session',
    blockId: 'block',
    sessionPlan: plan(),
    blockBudgetMs: 6000,
    protocolVersion: 'future-rapid-v1',
    stimulusSetVersion: 'stimulus-set-v1',
    now: () => now,
    eventIdFactory: ids('event'),
    blockAttemptIdFactory: ids('attempt'),
  });

  runner.startAttempt();
  runner.markPairReady(now);
  now = 5999;
  const first = runner.recordChoice('A', now);
  assert.equal(first.status, 'CHOICE_RECORDED');

  now = 6000;
  const timeout = runner.markPairReady(now);
  assert.equal(timeout.status, 'TIMEOUT');
  assert.equal(timeout.phase, 'RETRY_READY');
  assert.equal(runner.phase, 'RETRY_READY');
  assert.equal(runner.telemetry().events.length, 3);
});
