import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

import { evaluateTimingCalibration } from '../src/future_session/timing_calibration.mjs';

const config = JSON.parse(fs.readFileSync(new URL('../config/future-session/timing-calibration-v1.json', import.meta.url)));
const pairIds = ['CS-PR-01', 'CS-RE-01', 'CS-CA-01', 'CR-PZ-01', 'CR-FS-01', 'CR-PO-01'];

function buildPrimaryBlock(index, { timeoutAtPosition3 = false, pageHidden = false, deviceCategory } = {}) {
  const blockAttemptId = `attempt-${index}`;
  const blockId = `block-${index}`;
  const device = deviceCategory || (index % 2 ? 'mobile' : 'desktop');
  const attempt = {
    blockAttemptId,
    blockId,
    blockAttemptNumber: 1,
    blockBudgetMs: 6000,
    blockTimedOut: timeoutAtPosition3,
    pageHiddenDuringBlock: pageHidden,
    isTraining: false,
    deviceCategory: device,
  };

  const events = [1, 2, 3].map(position => {
    const timedOut = timeoutAtPosition3 && position === 3;
    return {
      blockAttemptId,
      blockId,
      blockAttemptNumber: 1,
      pairId: pairIds[(index + position - 1) % pairIds.length],
      positionInBlock: position,
      pairPresented: true,
      choice: timedOut ? 'timeout' : (position % 2 ? 'A' : 'B'),
      visualChoiceLatencyMs: timedOut ? null : 700 + position * 100,
      remainingBudgetAtPairStartMs: 6000 - (position - 1) * 1600,
      isTraining: false,
      deviceCategory: device,
    };
  });

  return { attempt, events };
}

function dataset(count, timeoutIndexes = new Set(), hiddenIndexes = new Set()) {
  const attempts = [];
  const pairEvents = [];
  for (let index = 0; index < count; index += 1) {
    const block = buildPrimaryBlock(index, {
      timeoutAtPosition3: timeoutIndexes.has(index),
      pageHidden: hiddenIndexes.has(index),
    });
    attempts.push(block.attempt);
    pairEvents.push(...block.events);
  }
  return { attempts, pairEvents };
}

test('fewer than 20 clean primary blocks is insufficient data', () => {
  const result = evaluateTimingCalibration({ ...dataset(19), config });
  assert.equal(result.decision, 'INSUFFICIENT_DATA');
  assert.equal(result.metrics.cleanPrimaryBlocks, 19);
});

test('clean high-completion sample keeps 6000ms', () => {
  const result = evaluateTimingCalibration({ ...dataset(20), config });
  assert.equal(result.decision, 'KEEP_6000');
  assert.equal(result.metrics.primaryBlockCompletionRate, 1);
  assert.equal(result.metrics.position[3].missingRate, 0);
  assert.equal(result.metrics.devices.completionGap, 0);
});

test('moderate position-3 depletion triggers adjust and retest, not rejection', () => {
  const result = evaluateTimingCalibration({ ...dataset(20, new Set([0, 1, 2])), config });
  assert.equal(result.decision, 'ADJUST_AND_RETEST');
  assert.equal(result.metrics.primaryBlockCompletionRate, 0.85);
  assert.equal(result.metrics.position[3].missingRate, 0.15);
  assert.equal(result.metrics.missingRateGradientP3MinusP1, 0.15);
  assert.ok(result.greenFailures.includes('POSITION_DEPLETION_AMBER'));
  assert.equal(result.redReasons.length, 0);
});

test('severe depletion rejects the 6000ms candidate', () => {
  const timeoutIndexes = new Set(Array.from({ length: 9 }, (_, index) => index));
  const result = evaluateTimingCalibration({ ...dataset(20, timeoutIndexes), config });
  assert.equal(result.decision, 'REJECT_6000');
  assert.equal(result.metrics.primaryBlockCompletionRate, 0.55);
  assert.equal(result.metrics.position[3].missingRate, 0.45);
  assert.ok(result.redReasons.includes('PRIMARY_COMPLETION_RED'));
  assert.ok(result.redReasons.includes('POSITION3_MISSING_RED'));
  assert.ok(result.redReasons.includes('POSITION_DEPLETION_RED'));
});

test('page-hidden primary attempts are excluded instead of treated as timing failures', () => {
  const result = evaluateTimingCalibration({ ...dataset(21, new Set(), new Set([20])), config });
  assert.equal(result.decision, 'KEEP_6000');
  assert.equal(result.metrics.candidatePrimaryBlocks, 21);
  assert.equal(result.metrics.cleanPrimaryBlocks, 20);
  assert.equal(result.metrics.excluded.pageHidden, 1);
  assert.equal(result.metrics.pageHiddenRate, 1 / 21);
});

test('retry attempts are diagnostics only and do not enter the primary denominator', () => {
  const data = dataset(20);
  data.attempts.push({
    blockAttemptId: 'retry-0',
    blockId: 'block-0',
    blockAttemptNumber: 2,
    blockBudgetMs: 6000,
    blockTimedOut: false,
    pageHiddenDuringBlock: false,
    isTraining: false,
    deviceCategory: 'desktop',
  });
  const result = evaluateTimingCalibration({ ...data, config });
  assert.equal(result.decision, 'KEEP_6000');
  assert.equal(result.metrics.cleanPrimaryBlocks, 20);
  assert.equal(result.metrics.retryRate, 1 / 20);
});
