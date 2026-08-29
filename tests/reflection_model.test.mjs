import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

import {
  buildReflectionItems,
  buildReflectionReasonEvent,
  createLocalReflectionSelection,
  createReflectionController,
  validateReflectionConfigs,
} from '../src/future_session/reflection_model.mjs';

const reasonMap = JSON.parse(
  fs.readFileSync(new URL('../config/future-session/reason-map-v1.json', import.meta.url))
);
const stimulusSet = JSON.parse(
  fs.readFileSync(new URL('../config/future-session/stimulus-set-v1.json', import.meta.url))
);

const anchors = [
  {
    pairId: 'CS-RE-01',
    rapidEventId: '11111111-1111-4111-8111-111111111111',
    anchorChoice: 'A',
    anchorSource: 'PRIMARY',
  },
  {
    pairId: 'CR-PO-01',
    rapidEventId: '22222222-2222-4222-8222-222222222222',
    anchorChoice: 'B',
    anchorSource: 'FIRST_COMPLETED_RETRY',
  },
];

test('production reflection config validation fails closed on DRAFT config', () => {
  assert.throws(
    () => validateReflectionConfigs({ stimulusSet, reasonMap }),
    /stimulus set is not RELEASED/
  );

  assert.equal(
    validateReflectionConfigs({ stimulusSet, reasonMap, allowDraft: true }),
    true
  );
});

test('reflection items bind exact selected asset and hide interpretability metadata', () => {
  const draws = [0.8, 0.1, 0.6, 0.2];
  let drawIndex = 0;

  const items = buildReflectionItems({
    anchors,
    stimulusSet,
    reasonMap,
    locale: 'lt',
    allowDraft: true,
    random: () => draws[drawIndex++ % draws.length],
  });

  assert.equal(items.length, 2);
  assert.equal(items[0].assetId, 'CS-RE-01-A');
  assert.match(items[0].assetPath, /more-evidence\.png$/);
  assert.equal(items[1].assetId, 'CR-PO-01-B');
  assert.match(items[1].assetPath, /open-space\.png$/);

  for (const item of items) {
    assert.equal(item.options.length, 4);
    assert.ok(!('interpretabilityClass' in item));
    assert.ok(item.options.every(option => !('interpretability_class' in option)));
    assert.match(item.options[3].reasonId, /-R04$/);
  }
});

test('Another reason keeps free text local and other options reject it', () => {
  const [item] = buildReflectionItems({
    anchors: [anchors[0]],
    stimulusSet,
    reasonMap,
    locale: 'en',
    allowDraft: true,
    random: () => 0.4,
  });

  const other = item.options.find(option => option.allowsLocalFreeText);
  const fixed = item.options.find(option => !option.allowsLocalFreeText);

  const selection = createLocalReflectionSelection({
    item,
    reasonId: other.reasonId,
    freeText: '  my own reason  ',
  });

  assert.equal(selection.localFreeText, 'my own reason');

  assert.throws(
    () => createLocalReflectionSelection({
      item,
      reasonId: fixed.reasonId,
      freeText: 'must stay local',
    }),
    /free text is only allowed/
  );
});

test('server reflection event never contains local free text or interpretability class', () => {
  const [item] = buildReflectionItems({
    anchors: [anchors[0]],
    stimulusSet,
    reasonMap,
    allowDraft: true,
    random: () => 0.2,
  });

  const other = item.options.find(option => option.allowsLocalFreeText);
  const selection = createLocalReflectionSelection({
    item,
    reasonId: other.reasonId,
    freeText: 'private local note',
  });

  const event = buildReflectionReasonEvent({
    selection,
    sessionId: '33333333-3333-4333-8333-333333333333',
    stimulusSetVersion: stimulusSet.stimulus_set_version,
    consentVersion: 'reason-research-consent-v1',
    protocolVersion: 'future-session-v0.2',
    eventIdFactory: () => '44444444-4444-4444-8444-444444444444',
  });

  assert.equal(event.reasonId, other.reasonId);
  assert.equal(event.reflectionAnchorSource, 'PRIMARY');
  assert.ok(!('localFreeText' in event));
  assert.ok(!('freeText' in event));
  assert.ok(!('interpretabilityClass' in event));
});

test('reflection controller requires one selection per anchor before completion', () => {
  const items = buildReflectionItems({
    anchors,
    stimulusSet,
    reasonMap,
    allowDraft: true,
    random: () => 0.3,
  });

  const controller = createReflectionController(items);
  assert.equal(controller.index, 0);
  assert.equal(controller.total, 2);
  assert.equal(controller.canAdvance(), false);
  assert.throws(() => controller.next(), /select a reason/);

  controller.select(items[0].options[0].reasonId);
  assert.equal(controller.canAdvance(), true);
  assert.equal(controller.next(), true);
  controller.select(items[1].options[0].reasonId);

  assert.equal(controller.isComplete(), true);
  const selections = controller.complete();
  assert.equal(selections.length, 2);
  assert.equal(selections[0].pairId, items[0].pairId);
  assert.equal(selections[1].pairId, items[1].pairId);
});
