import assert from 'node:assert/strict';
import { createProductReflectionController } from '../src/future_session/product_reflection_flow.mjs';

const items = [
  {
    pairId: 'P1', rapidEventId: 'E1', anchorChoice: 'A', anchorSource: 'PRIMARY',
    reasonMapVersion: 'reason-map-v1',
    options: [
      { reasonId: 'R1', text: 'One', allowsLocalFreeText: false },
      { reasonId: 'R2', text: 'Other', allowsLocalFreeText: true },
    ],
  },
  {
    pairId: 'P2', rapidEventId: 'E2', anchorChoice: 'B', anchorSource: 'PRIMARY',
    reasonMapVersion: 'reason-map-v1',
    options: [
      { reasonId: 'R3', text: 'Three', allowsLocalFreeText: false },
      { reasonId: 'R4', text: 'Other', allowsLocalFreeText: true },
    ],
  },
];

const controller = createProductReflectionController(items, { now: () => 0 });
assert.equal(controller.stage, 'REASON');
controller.markStageReady(1000);
controller.selectReason('R2', 'local words', 1650);
assert.equal(controller.stage, 'INTENSITY');
let snap = controller.snapshot();
assert.equal(snap.responses[0].reasonStatus, 'ANSWERED');
assert.equal(snap.responses[0].reasonResponseLatencyMs, 650);
assert.equal(snap.responses[0].localFreeText, 'local words');
assert.equal(snap.responses[0].intensityResponseLatencyMs, null);

controller.markStageReady(1800);
controller.selectIntensity(4, 2150);
assert.equal(controller.stage, 'REASON');
snap = controller.snapshot();
assert.equal(snap.responses[0].intensityStatus, 'ANSWERED');
assert.equal(snap.responses[0].intensity, 4);
assert.equal(snap.responses[0].intensityResponseLatencyMs, 350);

controller.markStageReady(2300);
controller.skipReason(2600);
assert.equal(controller.isComplete(), true);
snap = controller.complete();
assert.equal(snap.responses[1].reasonStatus, 'SKIPPED');
assert.equal(snap.responses[1].reasonResponseLatencyMs, null);
assert.equal(snap.responses[1].intensityStatus, 'NOT_REACHED');
assert.equal(snap.reflectionTotalElapsedMs, 1600);

assert.throws(() => createProductReflectionController([], {}), /at least one/);

console.log('product reflection flow: PASS');
