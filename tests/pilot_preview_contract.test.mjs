import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

const source = fs.readFileSync(
  new URL('../docs/experiments/future-session-pilot-preview.html', import.meta.url),
  'utf8'
);

test('pilot preview composes the actual future-session modules without a server endpoint', () => {
  for (const required of [
    'presentation_plan.mjs',
    'asset_preloader.mjs',
    'session_orchestrator.mjs',
    'reflection_model.mjs',
    'reflection_ui.mjs',
  ]) {
    assert.ok(source.includes(required), `missing preview integration: ${required}`);
  }

  for (const forbidden of ['api.php', 'api_v2.php', 'reflectionReasonEnvelope', 'createFutureSessionTransport']) {
    assert.ok(!source.includes(forbidden), `preview must stay server-isolated: ${forbidden}`);
  }
});

test('pilot preview preserves rapid protocol boundaries', () => {
  assert.ok(source.includes("runner.recordChoice(choice.id"));
  assert.ok(source.includes('runner.markPairReady(readyAt)'));
  assert.ok(source.includes("ready.status === 'TIMEOUT'"));
  assert.ok(source.includes('runner?.markPageHidden()'));
  assert.ok(source.includes('allowDraft: true'));
  assert.ok(!source.includes('no_clear_choice'));
  assert.ok(!source.includes('interpretability_class'));
  assert.ok(!source.includes('grid-template-columns:1fr 1fr'));
  assert.ok(source.includes('scheduleDeadline(readyAt, rapidProtocol.timing.block_budget_ms)'));
});
