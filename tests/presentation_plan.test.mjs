import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

import {
  createTwoSessionCycle,
  pairsForRetry,
  preloadPathsForSession,
  validatePresentationConfig,
} from '../src/future_session/presentation_plan.mjs';

const stimulusSet = JSON.parse(fs.readFileSync(new URL('../config/future-session/stimulus-set-v1.json', import.meta.url)));
const protocol = JSON.parse(fs.readFileSync(new URL('../config/future-session/rapid-presentation-v1.json', import.meta.url)));

function seededRng(seed = 123456789) {
  let state = seed >>> 0;
  return () => {
    state = (1664525 * state + 1013904223) >>> 0;
    return state / 0x100000000;
  };
}

test('F2 config has two disjoint three-pair forms covering all six F1 pairs', () => {
  const { forms } = validatePresentationConfig(protocol, stimulusSet);
  assert.equal(forms.length, 2);
  assert.deepEqual(forms.map(form => form.pair_ids.length), [3, 3]);
  const ids = forms.flatMap(form => form.pair_ids);
  assert.equal(new Set(ids).size, 6);
  assert.deepEqual(new Set(ids), new Set(stimulusSet.pairs.map(pair => pair.pair_id)));
});

test('first two local sessions use every pair once without repetition', () => {
  const cycle = createTwoSessionCycle({ protocol, stimulusSet, rng: seededRng(1) });
  const session1 = cycle.sessions[0].pairs.map(pair => pair.pairId);
  const session2 = cycle.sessions[1].pairs.map(pair => pair.pairId);
  assert.equal(session1.length, 3);
  assert.equal(session2.length, 3);
  assert.equal(session1.filter(id => session2.includes(id)).length, 0);
  assert.equal(new Set([...session1, ...session2]).size, 6);
});

test('A identity is top exactly three times across the two-session cycle', () => {
  for (let seed = 1; seed <= 20; seed += 1) {
    const cycle = createTwoSessionCycle({ protocol, stimulusSet, rng: seededRng(seed) });
    const counts = cycle.sessions.map(session =>
      session.pairs.filter(pair => pair.assetAPosition === 'top').length
    );
    assert.ok(counts[0] === 1 || counts[0] === 2);
    assert.ok(counts[1] === 1 || counts[1] === 2);
    assert.equal(counts[0] + counts[1], 3);

    for (const session of cycle.sessions) {
      for (const pair of session.pairs) {
        assert.ok(['top', 'bottom'].includes(pair.assetAPosition));
        assert.ok(['top', 'bottom'].includes(pair.assetBPosition));
        assert.notEqual(pair.assetAPosition, pair.assetBPosition);
      }
    }
  }
});

test('pair order is a permutation and retry reuses exact order and positions', () => {
  const cycle = createTwoSessionCycle({ protocol, stimulusSet, rng: seededRng(42) });
  const primary = cycle.sessions[0];
  const retry = pairsForRetry(primary);
  assert.deepEqual(retry, primary.pairs);
  assert.notEqual(retry, primary.pairs);
  const original = primary.pairs[0].assetAPosition;
  retry[0].assetAPosition = original === 'top' ? 'bottom' : 'top';
  assert.notEqual(retry[0].assetAPosition, primary.pairs[0].assetAPosition);
});

test('each session preloads exactly the six repository assets it will present', () => {
  const cycle = createTwoSessionCycle({ protocol, stimulusSet, rng: seededRng(7) });
  for (const session of cycle.sessions) {
    const paths = preloadPathsForSession(session);
    assert.equal(paths.length, 6);
    assert.equal(new Set(paths).size, 6);
    const expected = session.pairs.flatMap(pair => [pair.assetAPath, pair.assetBPath]);
    assert.deepEqual(paths, expected);
  }
});

test('invalid duplicate form membership fails closed', () => {
  const broken = structuredClone(protocol);
  broken.forms[1].pair_ids[0] = broken.forms[0].pair_ids[0];
  assert.throws(() => validatePresentationConfig(broken, stimulusSet), /appears in more than one form/);
});
