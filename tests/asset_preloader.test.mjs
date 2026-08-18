import assert from 'node:assert/strict';
import test from 'node:test';

import { preloadAssetBundle, TechnicalPreloadError } from '../src/future_session/asset_preloader.mjs';

function harness({ failFetchPath = null, failDecodePath = null } = {}) {
  const fetchCalls = [];
  const revoked = [];
  let counter = 0;

  return {
    fetchCalls,
    revoked,
    async fetchFn(path) {
      fetchCalls.push(path);
      if (path === failFetchPath) throw new Error('network down');
      return {
        ok: true,
        async blob() {
          return new Blob([`bytes:${path}`], { type: 'image/png' });
        },
      };
    },
    createObjectURL(blob) {
      counter += 1;
      return `blob:test-${counter}-${blob.size}`;
    },
    revokeObjectURL(url) {
      revoked.push(url);
    },
    async decodeObjectUrl(objectUrl, { path }) {
      if (path === failDecodePath) throw new Error('decode failed');
      return { decoded: true, objectUrl, path };
    },
  };
}

test('preload returns decoded in-memory handles for all unique paths', async () => {
  const h = harness();
  const bundle = await preloadAssetBundle(['a.png', 'b.png', 'a.png'], h);
  assert.equal(bundle.status, 'READY');
  assert.deepEqual(h.fetchCalls, ['a.png', 'b.png']);
  assert.equal(bundle.handles.size, 2);
  assert.equal(bundle.get('a.png').decodedImage.decoded, true);
  assert.match(bundle.get('a.png').objectUrl, /^blob:test-/);

  bundle.release();
  assert.equal(h.revoked.length, 2);
  assert.equal(bundle.handles.size, 0);
  assert.throws(() => bundle.get('a.png'), TechnicalPreloadError);
});

test('fetch failure is a technical preload error and cleans already created object URLs', async () => {
  const h = harness({ failFetchPath: 'b.png' });
  await assert.rejects(
    () => preloadAssetBundle(['a.png', 'b.png', 'c.png'], h),
    error => error instanceof TechnicalPreloadError && error.path === 'b.png'
  );
  assert.deepEqual(h.fetchCalls, ['a.png', 'b.png']);
  assert.equal(h.revoked.length, 1);
});

test('decode failure is technical and cleans all object URLs created so far', async () => {
  const h = harness({ failDecodePath: 'b.png' });
  await assert.rejects(
    () => preloadAssetBundle(['a.png', 'b.png'], h),
    error => error instanceof TechnicalPreloadError && error.path === 'b.png'
  );
  assert.equal(h.revoked.length, 2);
});

test('missing preload path fails before any fetch', async () => {
  const h = harness();
  await assert.rejects(
    () => preloadAssetBundle(['a.png', ''], h),
    TechnicalPreloadError
  );
  assert.equal(h.fetchCalls.length, 0);
});
