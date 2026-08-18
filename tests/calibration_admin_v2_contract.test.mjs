import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const release = 'deploy/conflictlab-hostinger/releases/calibration-v0.1';
const text = path => readFile(path, 'utf8');

const config = await text(`${release}/server/config.example.php`);
assert.match(config, /'collection_mode'\s*=>\s*'TECHNICAL'/);

const schema = await text(`${release}/server/schema.sql`);
assert.match(schema, /run_type VARCHAR\(16\) NOT NULL DEFAULT 'TECHNICAL'/);
assert.match(schema, /ix_cl_calibration_runs_type_clean/);

const migration = await text(`${release}/server/migration_001_run_type.sql`);
assert.match(migration, /ADD COLUMN run_type/);
assert.match(migration, /DEFAULT 'TECHNICAL'/);

const api = await text(`${release}/server/calibration_api.php`);
assert.match(api, /ALLOWED_RUN_TYPES = \['TECHNICAL', 'CALIBRATION'\]/);
assert.match(api, /\$config\['collection_mode'\]/);
assert.match(api, /run_type, form_id/);
assert.match(api, /'calibrationEligiblePrimary' => \(\$runType === 'CALIBRATION' && \$cleanPrimary\)/);
assert.doesNotMatch(api, /require_string\(\$payload, 'runType'/);

const admin = await text(`${release}/server/admin.php`);
assert.match(admin, /SERVER MODE:/);
assert.match(admin, /TECHNICAL runs never enter N\/20/);
assert.match(admin, /\$type==='TECHNICAL'/);
assert.match(admin, /\$type!=='CALIBRATION'/);
assert.match(admin, /Run #<\?=\$sid\?> detalės/);
assert.match(admin, /Pair events/);
assert.match(admin, /eligible calibration only/);

const manifest = JSON.parse(await text(`${release}/release-manifest.json`));
assert.equal(manifest.research_boundary.run_type_server_controlled, true);
assert.equal(manifest.research_boundary.technical_runs_enter_calibration_n, false);
assert.equal(manifest.storage.default_collection_mode, 'TECHNICAL');

console.log('calibration admin v2 contract: PASS');
