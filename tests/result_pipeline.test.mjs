import assert from 'node:assert/strict';
import { deriveLocalResult } from '../src/future_session/result_pipeline.mjs';

const gateD = {
  mapping_version: 'gate-d-test',
  stimulus_set_version: 'stimulus-set-test',
  allowed_domains: ['CS', 'CR'],
  allowed_mapping_status: ['VALIDATED', 'PENDING', 'NONE'],
  mappings: [
    {
      pair_id: 'P1', asset_a_id: 'P1-A', asset_b_id: 'P1-B',
      domain: 'CS', mapping_status: 'VALIDATED',
      asset_a_direction: 1, asset_b_direction: -1,
    },
    {
      pair_id: 'P2', asset_a_id: 'P2-A', asset_b_id: 'P2-B',
      domain: 'CS', mapping_status: 'VALIDATED',
      asset_a_direction: -1, asset_b_direction: 1,
    },
    {
      pair_id: 'P3', asset_a_id: 'P3-A', asset_b_id: 'P3-B',
      domain: 'CS', mapping_status: 'VALIDATED',
      asset_a_direction: 1, asset_b_direction: -1,
    },
  ],
};

const gateENone = {
  aggregation_gate_version: 'gate-e-test',
  allowed_status: ['VALID', 'PENDING', 'NONE'],
  domains: { CS: { status: 'NONE' }, CR: { status: 'NONE' } },
};

const gateEValid = {
  ...gateENone,
  domains: { ...gateENone.domains, CS: { status: 'VALID' } },
};

function event({
  eventId,
  pairId,
  choice,
  attempt = 1,
  pairPresented = true,
  positionInBlock = 1,
  elapsed = 100,
}) {
  return {
    eventId,
    pairId,
    stimulusSetVersion: 'stimulus-set-test',
    assetAId: `${pairId}-A`,
    assetBId: `${pairId}-B`,
    choice,
    pairPresented,
    blockAttemptNumber: attempt,
    blockElapsedMsAtEvent: elapsed,
    positionInBlock,
    isTraining: false,
  };
}

// End-to-end: calculation -> evidence -> depersonalized generation contract.
{
  const result = deriveLocalResult({
    events: [
      event({ eventId: 'e1', pairId: 'P1', choice: 'A', positionInBlock: 1 }), // +
      event({ eventId: 'e2', pairId: 'P2', choice: 'B', positionInBlock: 2 }), // +
      event({ eventId: 'e3', pairId: 'P3', choice: 'B', positionInBlock: 3 }), // -
    ],
    gateDConfig: gateD,
    gateEConfig: gateENone,
    domain: 'CS',
  });

  assert.equal(result.calculation.nPos, 2);
  assert.equal(result.calculation.nNeg, 1);
  assert.ok(Math.abs(result.calculation.directionBalance - (1 / 3)) < 1e-12);
  assert.equal(result.evidence.evidenceStatus, 'DESCRIPTIVE_ONLY');
  assert.equal(result.evidence.allowedClaimLevel, 1);
  assert.equal(result.generationContract.allowed_claim_level, 1);
  assert.equal(result.generationContract.delivery_policy, 'LOCAL_ONLY_BY_DEFAULT');
}

// Gate E is the only layer that can authorize domain-level claim language.
{
  const events = [
    event({ eventId: 'e1', pairId: 'P1', choice: 'A' }),
    event({ eventId: 'e2', pairId: 'P2', choice: 'B' }),
  ];

  const beforeGateE = deriveLocalResult({
    events, gateDConfig: gateD, gateEConfig: gateENone, domain: 'CS',
  });
  const afterGateE = deriveLocalResult({
    events, gateDConfig: gateD, gateEConfig: gateEValid, domain: 'CS',
  });

  assert.equal(beforeGateE.calculation.directionBalance, afterGateE.calculation.directionBalance);
  assert.equal(beforeGateE.evidence.allowedClaimLevel, 1);
  assert.equal(afterGateE.evidence.allowedClaimLevel, 2);
  assert.equal(afterGateE.evidence.evidenceStatus, 'DOMAIN_INTERPRETABLE');
}

// Retry divergence and retry-anchored reflection constrain narrative but never rewrite primary direction.
{
  const result = deriveLocalResult({
    events: [
      event({ eventId: 'p1', pairId: 'P1', choice: 'A', attempt: 1, positionInBlock: 1 }),
      event({
        eventId: 'p2-timeout', pairId: 'P2', choice: 'timeout', attempt: 1,
        pairPresented: true, positionInBlock: 2, elapsed: 6000,
      }),
      event({ eventId: 'p1-r', pairId: 'P1', choice: 'B', attempt: 2, positionInBlock: 1 }),
      event({ eventId: 'p2-r', pairId: 'P2', choice: 'B', attempt: 2, positionInBlock: 2 }),
    ],
    gateDConfig: gateD,
    gateEConfig: gateEValid,
    domain: 'CS',
  });

  assert.equal(result.calculation.directionBalance, 1);
  assert.equal(result.calculation.nDirectionalChoices, 1);
  assert.equal(result.evidence.allowedClaimLevel, 0); // one primary directional observation only
  assert.equal(result.context.retryDivergence, true);
  assert.ok(result.evidence.flags.includes('retry_choices_diverged_from_primary'));

  const p2Anchor = result.reflectionAnchors.find(anchor => anchor.pairId === 'P2');
  assert.equal(p2Anchor.anchorSource, 'FIRST_COMPLETED_RETRY');
  assert.ok(result.evidence.flags.includes('some_reflections_anchored_to_retry'));
}

// Structured reflection summary cannot numerically change visual evidence.
{
  const baseArgs = {
    events: [
      event({ eventId: 'e1', pairId: 'P1', choice: 'A' }),
      event({ eventId: 'e2', pairId: 'P2', choice: 'B' }),
    ],
    gateDConfig: gateD,
    gateEConfig: gateEValid,
    domain: 'CS',
  };

  const withoutReasons = deriveLocalResult(baseArgs);
  const withReasons = deriveLocalResult({
    ...baseArgs,
    reasonClassCounts: {
      DOMAIN_CONSISTENT_REASON: 0,
      CROSS_DOMAIN_REASON: 2,
      OTHER_REASON: 0,
      UNRESOLVED: 0,
    },
  });

  assert.equal(withReasons.calculation.directionBalance, withoutReasons.calculation.directionBalance);
  assert.equal(withReasons.evidence.evidenceStatus, withoutReasons.evidence.evidenceStatus);
  assert.equal(withReasons.generationContract.reflection.reason_class_counts.CROSS_DOMAIN_REASON, 2);
}

// Raw identifiers can exist in the local pipeline result, but the LLM contract remains depersonalized.
{
  const result = deriveLocalResult({
    events: [
      event({ eventId: 'SECRET_RAW_EVENT', pairId: 'P1', choice: 'A' }),
      event({ eventId: 'e2', pairId: 'P2', choice: 'B' }),
    ],
    gateDConfig: gateD,
    gateEConfig: gateENone,
    domain: 'CS',
  });

  assert.equal(result.calculation.perPair[0].eventId, 'SECRET_RAW_EVENT');
  assert.equal(JSON.stringify(result.generationContract).includes('SECRET_RAW_EVENT'), false);
}

console.log('result_pipeline: all tests passed');
