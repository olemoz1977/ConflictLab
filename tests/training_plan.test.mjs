import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

import {
  createTrainingPlan,
  preloadPathsForTraining,
  validateTrainingSet,
} from '../src/future_session/training_plan.mjs';

const trainingSet = JSON.parse(
  fs.readFileSync(
    new URL('../config/future-session/training-set-v1.json', import.meta.url),
    'utf8'
  )
);

test('training set reuses P0-001/P0-002/P0-003 in place and fails closed for analysis', () => {
  assert.equal(validateTrainingSet(trainingSet), true);
  assert.deepEqual(
    trainingSet.pairs.map(pair => pair.pair_id),
    ['P0-001', 'P0-002', 'P0-003']
  );

  assert.equal(trainingSet.data_boundary.is_training, true);
  assert.equal(trainingSet.data_boundary.analysis_eligible, false);
  assert.equal(trainingSet.data_boundary.timing_calibration_eligible, false);
  assert.equal(trainingSet.data_boundary.server_upload, false);
  assert.equal(trainingSet.data_boundary.gate_d, 'NOT_APPLICABLE');
  assert.equal(trainingSet.data_boundary.gate_e, 'NOT_APPLICABLE');

  for (const pair of trainingSet.pairs) {
    assert.match(pair.asset_a_path, /^docs\/experiments\/pair-p0\/images\/p0-00[1-3]-a\.png$/);
    assert.match(pair.asset_b_path, /^docs\/experiments\/pair-p0\/images\/p0-00[1-3]-b\.png$/);
    assert.match(pair.asset_a_git_blob_sha, /^[0-9a-f]{40}$/);
    assert.match(pair.asset_b_git_blob_sha, /^[0-9a-f]{40}$/);
  }
});

test('training plan uses the same three-pair vertical interaction without psychological direction', () => {
  const sequence = [0.8, 0.2, 0.4, 0.6, 0.3, 0.7, 0.1, 0.9];
  let index = 0;
  const random = () => sequence[(index++) % sequence.length];

  const plan = createTrainingPlan({ trainingSet, random });

  assert.equal(plan.isTraining, true);
  assert.equal(plan.trainingSetVersion, 'training-set-v1');
  assert.equal(plan.pairs.length, 3);
  assert.equal(new Set(plan.pairs.map(pair => pair.pairId)).size, 3);

  const aTopCount = plan.pairs.filter(pair => pair.assetAPosition === 'top').length;
  assert.ok(aTopCount === 1 || aTopCount === 2);

  for (const pair of plan.pairs) {
    assert.deepEqual(
      new Set([pair.assetAPosition, pair.assetBPosition]),
      new Set(['top', 'bottom'])
    );
  }

  const paths = preloadPathsForTraining(plan);
  assert.equal(paths.length, 6);
  assert.equal(new Set(paths).size, 6);
});
