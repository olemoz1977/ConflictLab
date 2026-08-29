import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

const reasonMap = JSON.parse(fs.readFileSync(new URL('../config/future-session/reason-map-v1.json', import.meta.url)));
const stimulusSet = JSON.parse(fs.readFileSync(new URL('../config/future-session/stimulus-set-v1.json', import.meta.url)));

const ALLOWED = new Set([
  'DOMAIN_CONSISTENT_REASON',
  'CROSS_DOMAIN_REASON',
  'OTHER_REASON',
  'UNRESOLVED',
]);

const FORBIDDEN_PARTICIPANT_LANGUAGE = [
  /\btu esi\b/i,
  /\btau reikia\b/i,
  /\btu nemėgsti\b/i,
  /\btu mėgsti\b/i,
  /\byou are\b/i,
  /\byou need\b/i,
  /\byou dislike\b/i,
  /\byour personality\b/i,
  /\byour trait\b/i,
];

function itemsFor(pairId, anchorChoice) {
  return reasonMap.items.filter(item => item.pair_id === pairId && item.anchor_choice === anchorChoice);
}

test('reason-map stays DRAFT and is bound to the exact F1 stimulus set', () => {
  assert.equal(reasonMap.lifecycle, 'DRAFT');
  assert.equal(reasonMap.content_status, 'DRAFT_CONTENT_REVIEW_REQUIRED');
  assert.equal(reasonMap.stimulus_set_version, stimulusSet.stimulus_set_version);
  assert.equal(reasonMap.released_at, null);
  assert.equal(reasonMap.content_policy.gate_d_dependency, 'NONE_FOR_AUTHORING_OR_DISPLAY');
  assert.equal(reasonMap.content_policy.other_reason_free_text, 'LOCAL_ONLY_OPTIONAL');
  assert.equal(reasonMap.content_policy.server_reason_id_collection, 'EXPLICIT_RESEARCH_CONSENT_ONLY');
});

test('all six F1 pairs have A and B reason anchors with exactly four items each', () => {
  const pairIds = stimulusSet.pairs.map(pair => pair.pair_id);
  assert.equal(pairIds.length, 6);
  assert.equal(reasonMap.items.length, 48);

  for (const pairId of pairIds) {
    for (const anchorChoice of ['A', 'B']) {
      const items = itemsFor(pairId, anchorChoice);
      assert.equal(items.length, 4, `${pairId}/${anchorChoice} must have four items`);
      assert.equal(items.filter(i => i.interpretability_class === 'DOMAIN_CONSISTENT_REASON').length, 1);
      assert.equal(items.filter(i => i.interpretability_class === 'UNRESOLVED').length, 1);
      assert.equal(items.filter(i => i.allows_local_free_text === true).length, 1);
      const freeTextItem = items.find(i => i.allows_local_free_text === true);
      assert.equal(freeTextItem.interpretability_class, 'OTHER_REASON');
    }
  }
});

test('reason IDs are unique, pair-anchor specific, and all required text is present', () => {
  const ids = new Set();
  const stimulusPairIds = new Set(stimulusSet.pairs.map(pair => pair.pair_id));

  for (const item of reasonMap.items) {
    assert.ok(stimulusPairIds.has(item.pair_id));
    assert.ok(['A', 'B'].includes(item.anchor_choice));
    assert.match(item.reason_id, new RegExp(`^${item.pair_id}-${item.anchor_choice}-R\\d{2}$`));
    assert.ok(!ids.has(item.reason_id), `duplicate reason_id: ${item.reason_id}`);
    ids.add(item.reason_id);
    assert.ok(item.text_lt.trim().length > 0);
    assert.ok(item.text_en.trim().length > 0);
    assert.ok(ALLOWED.has(item.interpretability_class));
  }
});

test('participant-facing reason text contains no direct trait or need claims', () => {
  for (const item of reasonMap.items) {
    for (const text of [item.text_lt, item.text_en]) {
      for (const pattern of FORBIDDEN_PARTICIPANT_LANGUAGE) {
        assert.ok(!pattern.test(text), `${item.reason_id} contains forbidden participant claim: ${pattern}`);
      }
    }
  }
});

test('interpretability classes are metadata only and remain hidden from participant-facing UI', () => {
  assert.equal(reasonMap.content_policy.participant_facing_labels_hidden, true);
  assert.equal(reasonMap.content_policy.trait_language_forbidden, true);
  assert.equal(reasonMap.content_policy.display_order, 'RANDOMIZE_FIRST_THREE_KEEP_UNRESOLVED_LAST');
});
