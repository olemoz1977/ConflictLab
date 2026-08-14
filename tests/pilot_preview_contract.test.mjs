import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

const source = fs.readFileSync(
  new URL('../docs/experiments/future-session-pilot-preview.html', import.meta.url),
  'utf8'
);

test('pilot preview composes training and measured future-session modules without a response-data endpoint', () => {
  for (const required of [
    'presentation_plan.mjs',
    'training_plan.mjs',
    'asset_preloader.mjs',
    'session_orchestrator.mjs',
    'reflection_model.mjs',
    'reflection_ui.mjs',
    'training-set-v1.json',
  ]) {
    assert.ok(source.includes(required), `missing preview integration: ${required}`);
  }

  for (const forbidden of ['api.php', 'api_v2.php', 'reflectionReasonEnvelope', 'createFutureSessionTransport']) {
    assert.ok(!source.includes(forbidden), `preview must stay response-write isolated: ${forbidden}`);
  }
});

test('pilot preview requires completed training before a fresh measured block', () => {
  assert.ok(source.includes("activeMode = 'TRAINING'"));
  assert.ok(source.includes('isTraining: true'));
  assert.ok(source.includes('showMeasuredIntro()'));
  assert.ok(source.includes('trainingCompleted = true'));
  assert.ok(source.includes("activeMode = 'MEASURED'"));
  assert.ok(source.includes('trainingExcludedFromCalibration: true'));
});

test('owner preview can explicitly select an unexposed form without changing the protocol config', () => {
  assert.ok(source.includes("['F2-A', 'F2-B'].includes(params.get('form'))"));
  assert.ok(source.includes('cycle.sessions.find(session => session.formId === requestedForm)'));
  assert.ok(source.includes('ownerFormOverride: requestedForm'));
  assert.ok(source.includes('staticReadOnlyFetches: true'));
});

test('pilot preview preserves rapid protocol and calibration-quality telemetry boundaries', () => {
  assert.ok(source.includes('activeRunner.recordChoice(choice.id'));
  assert.ok(source.includes('activeRunner.markPairReady(readyAt)'));
  assert.ok(source.includes("ready.status === 'TIMEOUT'"));
  assert.ok(source.includes('activeRunner?.markPageHidden()'));
  assert.ok(source.includes('allowDraft: true'));
  assert.ok(source.includes("schema: 'conflictlab.owner-ux-export.v2'"));
  assert.ok(source.includes("calibrationAssessment: 'NOT_EVALUATED_IN_UI'"));
  assert.ok(source.includes('deviceContextAtStart'));
  assert.ok(source.includes('runner?.telemetry()'));
  assert.ok(source.includes('new Blob(['));
  assert.ok(!source.includes('Nothing on this page is sent to a server.'));
  assert.ok(!source.includes('no_clear_choice'));
  assert.ok(!source.includes('interpretability_class'));
  assert.ok(!source.includes('grid-template-columns:1fr 1fr'));
  assert.ok(source.includes('scheduleDeadline(readyAt, activeBudgetMs())'));
});
