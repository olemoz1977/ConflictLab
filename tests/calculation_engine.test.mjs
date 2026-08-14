import assert from 'node:assert/strict';
import {
  NOT_ESTIMABLE,
  calculateDirectionalBalance,
  indexGateD,
} from '../src/future_session/calculation_engine.mjs';

const assetIds = {
  CS1: ['CS1-A', 'CS1-B'],
  CS2: ['CS2-A', 'CS2-B'],
  CR1: ['CR1-A', 'CR1-B'],
  CS_NONE: ['CSN-A', 'CSN-B'],
};

const gateD = {
  mapping_version: 'gate-d-test',
  stimulus_set_version: 'stimulus-set-test',
  allowed_domains: ['CS', 'CR'],
  allowed_mapping_status: ['VALIDATED', 'PENDING', 'NONE'],
  mappings: [
    {
      pair_id: 'CS1', asset_a_id: 'CS1-A', asset_b_id: 'CS1-B',
      domain: 'CS', mapping_status: 'VALIDATED',
      asset_a_direction: 1, asset_b_direction: -1, evidence_reference: 'test',
    },
    {
      pair_id: 'CS2', asset_a_id: 'CS2-A', asset_b_id: 'CS2-B',
      domain: 'CS', mapping_status: 'VALIDATED',
      asset_a_direction: -1, asset_b_direction: 1, evidence_reference: 'test',
    },
    {
      pair_id: 'CR1', asset_a_id: 'CR1-A', asset_b_id: 'CR1-B',
      domain: 'CR', mapping_status: 'VALIDATED',
      asset_a_direction: 1, asset_b_direction: -1, evidence_reference: 'test',
    },
    {
      pair_id: 'CS_NONE', asset_a_id: 'CSN-A', asset_b_id: 'CSN-B',
      domain: 'CS', mapping_status: 'NONE',
      asset_a_direction: null, asset_b_direction: null, evidence_reference: null,
    },
  ],
};

function event({
  id,
  pairId,
  choice,
  pairPresented = true,
  attempt = 1,
  isTraining = false,
  stimulusSetVersion = 'stimulus-set-test',
  assetAId,
  assetBId,
}) {
  const expected = assetIds[pairId] || [`${pairId}-A`, `${pairId}-B`];
  return {
    eventId: id,
    pairId,
    stimulusSetVersion,
    assetAId: assetAId ?? expected[0],
    assetBId: assetBId ?? expected[1],
    choice,
    pairPresented,
    blockAttemptNumber: attempt,
    isTraining,
  };
}

// Basic deterministic balance: +1, +1, -1 => +1/3.
{
  const result = calculateDirectionalBalance({
    domain: 'CS',
    gateDConfig: gateD,
    events: [
      event({ id: '1', pairId: 'CS1', choice: 'A' }), // +1
      event({ id: '2', pairId: 'CS2', choice: 'B' }), // +1
      event({ id: '3', pairId: 'CS1', choice: 'B' }), // -1
    ],
  });

  assert.equal(result.nPos, 2);
  assert.equal(result.nNeg, 1);
  assert.equal(result.nEligiblePresentations, 3);
  assert.equal(result.coverage, 1);
  assert.equal(result.stimulusSetVersion, 'stimulus-set-test');
  assert.ok(Math.abs(result.directionBalance - (1 / 3)) < 1e-12);
}

// Shown timeout enters coverage denominator but not direction numerator.
{
  const result = calculateDirectionalBalance({
    domain: 'CS',
    gateDConfig: gateD,
    events: [
      event({ id: '1', pairId: 'CS1', choice: 'A' }),
      event({ id: '2', pairId: 'CS2', choice: 'timeout', pairPresented: true }),
    ],
  });

  assert.equal(result.nDirectionalChoices, 1);
  assert.equal(result.nEligiblePresentations, 2);
  assert.equal(result.coverage, 0.5);
  assert.equal(result.directionBalance, 1);
}

// Never-presented timeout is not an eligible presentation.
{
  const result = calculateDirectionalBalance({
    domain: 'CS',
    gateDConfig: gateD,
    events: [
      event({ id: '1', pairId: 'CS1', choice: 'A' }),
      event({ id: '2', pairId: 'CS2', choice: 'timeout', pairPresented: false }),
    ],
  });

  assert.equal(result.nEligiblePresentations, 1);
  assert.equal(result.coverage, 1);
}

// Retry A/B never changes primary directional result.
{
  const primaryOnly = calculateDirectionalBalance({
    domain: 'CS',
    gateDConfig: gateD,
    events: [event({ id: 'p', pairId: 'CS1', choice: 'A', attempt: 1 })],
  });

  const withRetries = calculateDirectionalBalance({
    domain: 'CS',
    gateDConfig: gateD,
    events: [
      event({ id: 'p', pairId: 'CS1', choice: 'A', attempt: 1 }),
      event({ id: 'r1', pairId: 'CS1', choice: 'B', attempt: 2 }),
      event({ id: 'r2', pairId: 'CS2', choice: 'A', attempt: 3 }),
    ],
  });

  assert.equal(withRetries.directionBalance, primaryOnly.directionBalance);
  assert.equal(withRetries.nDirectionalChoices, 1);
}

// Training events never enter research/scoring calculation.
{
  const result = calculateDirectionalBalance({
    domain: 'CS',
    gateDConfig: gateD,
    events: [
      event({ id: 't', pairId: 'CS1', choice: 'A', isTraining: true }),
    ],
  });

  assert.equal(result.nEligiblePresentations, 0);
  assert.equal(result.directionBalance, NOT_ESTIMABLE);
  assert.equal(result.coverage, NOT_ESTIMABLE);
}

// Gate D NONE contributes neither direction nor eligible presentation.
{
  const result = calculateDirectionalBalance({
    domain: 'CS',
    gateDConfig: gateD,
    events: [event({ id: 'n', pairId: 'CS_NONE', choice: 'A' })],
  });

  assert.equal(result.nEligiblePresentations, 0);
  assert.equal(result.directionBalance, NOT_ESTIMABLE);
  assert.equal(result.coverage, NOT_ESTIMABLE);
}

// Domain separation: CR cannot leak into CS.
{
  const result = calculateDirectionalBalance({
    domain: 'CS',
    gateDConfig: gateD,
    events: [event({ id: 'cr', pairId: 'CR1', choice: 'A' })],
  });

  assert.equal(result.nEligiblePresentations, 0);
  assert.equal(result.directionBalance, NOT_ESTIMABLE);
}

// A Gate D mapping can never be silently applied to changed assets or a changed stimulus set.
{
  assert.throws(
    () => calculateDirectionalBalance({
      domain: 'CS',
      gateDConfig: gateD,
      events: [event({ id: 'bad-asset', pairId: 'CS1', choice: 'A', assetAId: 'DIFFERENT' })],
    }),
    /Gate D asset identity mismatch/
  );

  assert.throws(
    () => calculateDirectionalBalance({
      domain: 'CS',
      gateDConfig: gateD,
      events: [event({
        id: 'bad-version', pairId: 'CS1', choice: 'A', stimulusSetVersion: 'stimulus-set-v2',
      })],
    }),
    /Gate D stimulus-set mismatch/
  );
}

// Mapping validation rejects ambiguous or malformed source-of-truth config.
{
  assert.throws(
    () => indexGateD({
      stimulus_set_version: 's',
      allowed_mapping_status: ['VALIDATED', 'PENDING', 'NONE'],
      mappings: [
        {
          pair_id: 'bad', asset_a_id: 'A', asset_b_id: 'B',
          domain: 'CS', mapping_status: 'VALIDATED',
          asset_a_direction: 1, asset_b_direction: 1,
        },
      ],
    }),
    /must be opposite/
  );

  assert.throws(
    () => indexGateD({
      stimulus_set_version: 's',
      allowed_mapping_status: ['VALIDATED', 'PENDING', 'NONE'],
      mappings: [
        {
          pair_id: 'pending', asset_a_id: 'A', asset_b_id: 'B',
          domain: 'CS', mapping_status: 'PENDING',
          asset_a_direction: 1, asset_b_direction: null,
        },
      ],
    }),
    /non-VALIDATED mapping directions must be null/
  );

  assert.throws(
    () => indexGateD({
      allowed_mapping_status: ['VALIDATED'],
      mappings: [
        {
          pair_id: 'no-version', asset_a_id: 'A', asset_b_id: 'B',
          mapping_status: 'VALIDATED', asset_a_direction: 1, asset_b_direction: -1,
        },
      ],
    }),
    /stimulus_set_version is required/
  );
}

console.log('calculation_engine: all tests passed');
