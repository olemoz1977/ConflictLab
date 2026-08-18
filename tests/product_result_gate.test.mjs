import assert from 'node:assert/strict';
import { deriveProductResultState } from '../src/future_session/product_result_gate.mjs';
import gateD from '../config/future-session/gate-d-v1.json' with { type: 'json' };
import gateE from '../config/future-session/gate-e-v1.json' with { type: 'json' };

const events = [{
  eventId: 'E1',
  pairId: 'CS-PR-01',
  stimulusSetVersion: 'stimulus-set-v1',
  assetAId: 'A',
  assetBId: 'B',
  choice: 'A',
  pairPresented: true,
  positionInBlock: 1,
  blockAttemptNumber: 1,
  isTraining: false,
}];

const state = deriveProductResultState({ events, gateDConfig: gateD, gateEConfig: gateE, reflectionAnchors: [] });
assert.equal(state.directionalResultAvailable, false);
assert.equal(state.resultStatus, 'NOT_ESTIMABLE');
assert.equal(state.gateDReady, false);
assert.equal(state.gateEReady, false);
assert.equal(state.domains.CS.calculation.directionBalance, 'NOT_ESTIMABLE');
assert.equal(state.domains.CR.calculation.directionBalance, 'NOT_ESTIMABLE');
assert.equal(state.domains.CS.evidence.allowedClaimLevel, 0);
assert.equal(state.domains.CR.evidence.allowedClaimLevel, 0);

console.log('product result gate: PASS');
