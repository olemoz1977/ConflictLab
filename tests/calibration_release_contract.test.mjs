import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';

const release = 'deploy/conflictlab-hostinger/releases/calibration-v0.1';
const text = path => readFile(path, 'utf8');
const bytes = path => readFile(path);

const manifest = JSON.parse(await text(`${release}/release-manifest.json`));
assert.equal(manifest.lifecycle, 'LAB');
assert.equal(manifest.public_switch.authorized, false);
assert.equal(manifest.owner_approval.status, 'PENDING');
assert.equal(manifest.research_boundary.purpose, 'MECHANICAL_TIMING_ONLY');
assert.equal(manifest.research_boundary.gate_d, 'NONE');
assert.equal(manifest.research_boundary.gate_e, 'NONE');
assert.equal(manifest.research_boundary.participant_result, 'NONE');
assert.equal(manifest.research_boundary.training_upload, false);
assert.equal(manifest.research_boundary.reflection_upload, false);
assert.equal(manifest.research_boundary.selected_a_b_identity_stored, false);
assert.equal(manifest.research_boundary.persistent_participant_id, false);
assert.equal(manifest.research_boundary.wave1_storage_reuse, false);

const exactCopies = [
  ['config/future-session/stimulus-set-v1.json', 'canonical/config/future-session/stimulus-set-v1.json'],
  ['config/future-session/rapid-presentation-v1.json', 'canonical/config/future-session/rapid-presentation-v1.json'],
  ['config/future-session/reason-map-v1.json', 'canonical/config/future-session/reason-map-v1.json'],
  ['config/future-session/training-set-v1.json', 'canonical/config/future-session/training-set-v1.json'],
  ['config/future-session/timing-calibration-v1.json', 'canonical/config/future-session/timing-calibration-v1.json'],
  ['src/future_session/presentation_plan.mjs', 'canonical/src/future_session/presentation_plan.mjs'],
  ['src/future_session/training_plan.mjs', 'canonical/src/future_session/training_plan.mjs'],
  ['src/future_session/asset_preloader.mjs', 'canonical/src/future_session/asset_preloader.mjs'],
  ['src/future_session/session_orchestrator.mjs', 'canonical/src/future_session/session_orchestrator.mjs'],
  ['src/future_session/rapid_block_core.mjs', 'canonical/src/future_session/rapid_block_core.mjs'],
  ['src/future_session/reflection_model.mjs', 'canonical/src/future_session/reflection_model.mjs'],
  ['src/future_session/reflection_ui.mjs', 'canonical/src/future_session/reflection_ui.mjs'],
  ['docs/experiments/pair-p0/images/p0-001-a.png', 'canonical/docs/experiments/pair-p0/images/p0-001-a.png'],
  ['docs/experiments/pair-p0/images/p0-001-b.png', 'canonical/docs/experiments/pair-p0/images/p0-001-b.png'],
  ['docs/experiments/pair-p0/images/p0-002-a.png', 'canonical/docs/experiments/pair-p0/images/p0-002-a.png'],
  ['docs/experiments/pair-p0/images/p0-002-b.png', 'canonical/docs/experiments/pair-p0/images/p0-002-b.png'],
  ['docs/experiments/pair-p0/images/p0-003-a.png', 'canonical/docs/experiments/pair-p0/images/p0-003-a.png'],
  ['docs/experiments/pair-p0/images/p0-003-b.png', 'canonical/docs/experiments/pair-p0/images/p0-003-b.png'],
  ['docs/experiments/stimulus-validation/assets/CS-PR-01/more-reveal.webp', 'canonical/docs/experiments/stimulus-validation/assets/CS-PR-01/more-reveal.webp'],
  ['docs/experiments/stimulus-validation/assets/CS-PR-01/less-reveal.jpg', 'canonical/docs/experiments/stimulus-validation/assets/CS-PR-01/less-reveal.jpg'],
  ['docs/experiments/stimulus-validation/assets/CS-RE-01/more-evidence.png', 'canonical/docs/experiments/stimulus-validation/assets/CS-RE-01/more-evidence.png'],
  ['docs/experiments/stimulus-validation/assets/CS-RE-01/less-evidence.png', 'canonical/docs/experiments/stimulus-validation/assets/CS-RE-01/less-evidence.png'],
  ['docs/experiments/stimulus-validation/assets/CS-CA-01/more-reference.png', 'canonical/docs/experiments/stimulus-validation/assets/CS-CA-01/more-reference.png'],
  ['docs/experiments/stimulus-validation/assets/CS-CA-01/less-reference.png', 'canonical/docs/experiments/stimulus-validation/assets/CS-CA-01/less-reference.png'],
  ['docs/experiments/stimulus-validation/assets/CR-PZ-01/no-predefined-zones.png', 'canonical/docs/experiments/stimulus-validation/assets/CR-PZ-01/no-predefined-zones.png'],
  ['docs/experiments/stimulus-validation/assets/CR-PZ-01/predefined-zones.png', 'canonical/docs/experiments/stimulus-validation/assets/CR-PZ-01/predefined-zones.png'],
  ['docs/experiments/stimulus-validation/assets/CR-FS-01/fixed-slots.png', 'canonical/docs/experiments/stimulus-validation/assets/CR-FS-01/fixed-slots.png'],
  ['docs/experiments/stimulus-validation/assets/CR-FS-01/continuous-capacity.png', 'canonical/docs/experiments/stimulus-validation/assets/CR-FS-01/continuous-capacity.png'],
  ['docs/experiments/stimulus-validation/assets/CR-PO-01/partitioned-space.png', 'canonical/docs/experiments/stimulus-validation/assets/CR-PO-01/partitioned-space.png'],
  ['docs/experiments/stimulus-validation/assets/CR-PO-01/open-space.png', 'canonical/docs/experiments/stimulus-validation/assets/CR-PO-01/open-space.png'],
];
for (const [source, copied] of exactCopies) {
  const [a,b] = await Promise.all([bytes(source), bytes(`${release}/${copied}`)]);
  assert.ok(a.equals(b), `${copied} must remain byte-identical to ${source}`);
}

const html = await text(`${release}/index.html`);
assert.match(html, /rootPrefix\s*=\s*'\.\/canonical\/'/);
assert.match(html, /preloadPathsForTraining\(trainingPlan\)/);
assert.match(html, /preloadPathsForSession\(sessionPlan\)/);
assert.match(html, /\.\/server\/calibration_api\.php/);
assert.match(html, /responseStatus:e\.choice==='timeout'\?'timeout':'choice'/);
assert.doesNotMatch(html, /userAgent\s*:/);
assert.doesNotMatch(html, /reflectionSelections\s*:/);
assert.doesNotMatch(html, /trainingRuns\s*:/);
assert.match(html, /100dvh/);

const moduleMatch = html.match(/<script type="module">([\s\S]*?)<\/script>/);
assert.ok(moduleMatch, 'module script must exist');
const dir = await mkdtemp(join(tmpdir(), 'cl-calibration-'));
const tempModule = join(dir, 'index.mjs');
await writeFile(tempModule, moduleMatch[1]);
const check = spawnSync(process.execPath, ['--check', tempModule], { encoding:'utf8' });
await rm(dir, { recursive:true, force:true });
assert.equal(check.status, 0, check.stderr || check.stdout);

const api = await text(`${release}/server/calibration_api.php`);
assert.match(api, /conflictlab\.calibration-run\.v1/);
assert.match(api, /PAGE_HIDDEN_DURING_PRIMARY/);
assert.match(api, /SESSION_ALREADY_INGESTED/);
assert.doesNotMatch(api, /reflection_reason/i);
assert.doesNotMatch(api, /participant_id/i);

const sql = await text(`${release}/server/schema.sql`);
assert.match(sql, /cl_calibration_runs/);
assert.match(sql, /cl_calibration_attempts/);
assert.match(sql, /cl_calibration_pair_events/);
assert.doesNotMatch(sql, /\bresponses\b/i);
assert.doesNotMatch(sql, /participant_id/i);

console.log('calibration release contract: PASS');