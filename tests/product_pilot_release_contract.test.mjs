import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const release = 'deploy/conflictlab-hostinger/releases/calibration-v0.1';
const text = path => readFile(path, 'utf8');
const bytes = path => readFile(path);

const html = await text(`${release}/index.html`);
assert.match(html, /Lietuvių/);
assert.match(html, /English/);
assert.match(html, /mountProductReflectionUI/);
assert.match(html, /deriveProductResultState/);
assert.match(html, /gate-d-v1\.json/);
assert.match(html, /gate-e-v1\.json/);
assert.match(html, /reflection reasons, intensity, and their response times stay local/i);
assert.match(html, /Refleksijos priežastys, intensyvumas ir jų laikai lieka lokaliai/);
assert.match(html, /NOT_ESTIMABLE/);
assert.doesNotMatch(html, /intensityResponseLatencyMs\s*:/);
assert.doesNotMatch(html, /reasonResponseLatencyMs\s*:/);

const flow = await text('src/future_session/product_reflection_flow.mjs');
assert.match(flow, /reasonResponseLatencyMs/);
assert.match(flow, /intensityResponseLatencyMs/);
assert.match(flow, /reflectionTotalElapsedMs/);
assert.match(flow, /intensity must be an integer from 1 to 5/);
assert.match(flow, /reasonStatus = 'SKIPPED'/);
assert.match(flow, /intensityStatus = 'SKIPPED'/);

const ui = await text('src/future_session/product_reflection_ui.mjs');
assert.match(ui, /Reaction intensity/);
assert.match(ui, /Reakcijos stiprumas/);
assert.match(ui, /value <= 5/);
assert.match(ui, /selectedAt = now\(\)/);

const exactCopies = [
  ['config/future-session/gate-d-v1.json', `${release}/canonical/config/future-session/gate-d-v1.json`],
  ['config/future-session/gate-e-v1.json', `${release}/canonical/config/future-session/gate-e-v1.json`],
  ['src/future_session/calculation_engine.mjs', `${release}/canonical/src/future_session/calculation_engine.mjs`],
  ['src/future_session/evidence_engine.mjs', `${release}/canonical/src/future_session/evidence_engine.mjs`],
  ['src/future_session/product_reflection_flow.mjs', `${release}/canonical/src/future_session/product_reflection_flow.mjs`],
  ['src/future_session/product_reflection_ui.mjs', `${release}/canonical/src/future_session/product_reflection_ui.mjs`],
  ['src/future_session/product_result_gate.mjs', `${release}/canonical/src/future_session/product_result_gate.mjs`],
];
for (const [source, deployed] of exactCopies) {
  const [a, b] = await Promise.all([bytes(source), bytes(deployed)]);
  assert.ok(a.equals(b), `${deployed} must be byte-identical to ${source}`);
}

for (const path of [
  `${release}/canonical/src/future_session/product_reflection_flow.js`,
  `${release}/canonical/src/future_session/product_reflection_ui.js`,
  `${release}/canonical/src/future_session/product_result_gate.js`,
  `${release}/canonical/src/future_session/evidence_engine.js`,
]) {
  assert.doesNotMatch(await text(path), /\.mjs['"]/);
}

const api = await text(`${release}/server/calibration_api.php`);
const schema = await text(`${release}/server/schema.sql`);
for (const forbidden of ['reasonResponseLatencyMs', 'intensityResponseLatencyMs', 'reaction_intensity', 'localFreeText']) {
  assert.doesNotMatch(api, new RegExp(forbidden, 'i'));
  assert.doesNotMatch(schema, new RegExp(forbidden, 'i'));
}

const gateD = JSON.parse(await text(`${release}/canonical/config/future-session/gate-d-v1.json`));
const gateE = JSON.parse(await text(`${release}/canonical/config/future-session/gate-e-v1.json`));
assert.equal(gateD.mappings.length, 0);
assert.equal(gateE.domains.CS.status, 'NONE');
assert.equal(gateE.domains.CR.status, 'NONE');

console.log('product pilot release contract: PASS');
