import assert from 'node:assert/strict';
import test from 'node:test';

import { FutureSessionOrchestrator } from '../src/future_session/session_orchestrator.mjs';

function trainingPlan() {
  return {
    formId: 'TRAINING-P0-001-003',
    isTraining: true,
    pairs: ['P0-001', 'P0-002', 'P0-003'].map((pairId, index) => ({
      pairId,
      assetAId: `${pairId}-A`,
      assetBId: `${pairId}-B`,
      assetAPath: `${pairId}-a.png`,
      assetBPath: `${pairId}-b.png`,
      assetAPosition: index === 1 ? 'bottom' : 'top',
      assetBPosition: index === 1 ? 'top' : 'bottom',
    })),
  };
}

function ids(prefix) {
  let n = 0;
  return () => `${prefix}-${++n}`;
}

function makeRunner(nowRef) {
  return new FutureSessionOrchestrator({
    sessionId: 'session',
    blockId: 'training-block',
    sessionPlan: trainingPlan(),
    blockBudgetMs: 6000,
    protocolVersion: 'training-familiarization-v1',
    stimulusSetVersion: 'training-set-v1',
    isTraining: true,
    now: () => nowRef.value,
    eventIdFactory: ids('event'),
    blockAttemptIdFactory: ids('attempt'),
  });
}

test('completed training block is COMPLETE, excluded from reflection, and marks all telemetry as training', () => {
  const now = { value: 0 };
  const runner = makeRunner(now);

  runner.startAttempt();
  for (const choice of ['A', 'B', 'A']) {
    runner.markPairReady(now.value);
    now.value += 400;
    runner.recordChoice(choice, now.value);
    now.value += 10;
  }

  assert.equal(runner.phase, 'COMPLETE');
  assert.throws(() => runner.reflectionAnchors(), /training blocks do not produce reflection anchors/);
  assert.throws(() => runner.markReflectionComplete(), /training blocks do not have reflection/);

  const telemetry = runner.telemetry();
  assert.equal(telemetry.isTraining, true);
  assert.equal(telemetry.attempts.length, 1);
  assert.ok(telemetry.attempts.every(attempt => attempt.isTraining === true));
  assert.ok(telemetry.events.every(event => event.isTraining === true));
});

test('third training timeout requires a fresh training cycle instead of entering reflection', () => {
  const now = { value: 0 };
  const runner = makeRunner(now);

  for (let attempt = 1; attempt <= 3; attempt += 1) {
    runner.startAttempt();
    runner.markPairReady(now.value);
    now.value += 6000;
    const result = runner.expire(now.value);

    if (attempt < 3) {
      assert.equal(result.phase, 'RETRY_READY');
      now.value += 100;
    } else {
      assert.equal(result.phase, 'TRAINING_RESTART_REQUIRED');
      assert.equal(runner.phase, 'TRAINING_RESTART_REQUIRED');
    }
  }

  assert.throws(() => runner.reflectionAnchors(), /training blocks do not produce reflection anchors/);
});
