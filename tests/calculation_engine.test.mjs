import assert from 'node:assert/strict';
import {
  NOT_ESTIMABLE,
  calculateDirectionalBalance,
  indexGateD,
} from '../src/future_session/calculation_engine.mjs';

const gateD = {
  mapping_version: 'gate-d-test',
  allowed_domains: ['CS', 'CR'],
  mappings: [
    {
      pair_id: 'CS1', domain: 'CS', mapping_status: 'VALIDATED',
      asset_a_direction: 1, asset_b_direction: -1, evidence_reference: 'test',
    },
    {
      pair_id: 'CS2', domain: 'CS', mapping_status: 'VALIDATED',
      asset_a_direction: -1, asset_b_direction: 1, evidence_reference: 'test',
    },
    {
      pair_id: 'CR1', domain: 'CR', mapping_status: 'VALIDATED',
      asset_a_direction: 1, asset_b_direction: -1, evidence_reference: 'test',
    },
    {
      pair_id: 'CS_NONE', domain: 'CS', mapping_status: 'NONE',
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
}) {
  return {
    eventId: id,
    pairId,
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

// Mapping validation rejects ambiguous or malformed source-of-truth config.
{
  assert.throws(
    () => indexGateD({
      mappings: [
        {
          pair_id: 'bad', domain: 'CS', mapping_status: 'VALIDATED',
          asset_a_direction: 1, asset_b_direction: 1,
        },
      ],
    }),
    /must be opposite/
  );

  assert.throws(
    () => indexGateD({
      mappings: [
        {
          pair_id: 'pending', domain: 'CS', mapping_status: 'PENDING',
          asset_a_direction: 1, asset_b_direction: null,
        },
      ],
    }),
    /non-VALIDATED mapping directions must be null/
  );
}

console.log('calculation_engine: all tests passed');
