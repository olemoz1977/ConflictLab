import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

import { mountReflectionUI } from '../src/future_session/reflection_ui.mjs';

const source = fs.readFileSync(
  new URL('../src/future_session/reflection_ui.mjs', import.meta.url),
  'utf8'
);

test('reflection UI keeps internal interpretation metadata out of participant DOM code', () => {
  assert.ok(!source.includes('interpretability_class'));
  assert.ok(!source.includes('interpretabilityClass'));
  assert.ok(!source.includes('innerHTML'));
  assert.ok(source.includes('textContent'));
});

test('reflection UI requires an explicit root and never performs implicit global mounting', () => {
  assert.throws(
    () => mountReflectionUI({ root: null, items: [{}] }),
    /root DOM element is required/
  );
});
