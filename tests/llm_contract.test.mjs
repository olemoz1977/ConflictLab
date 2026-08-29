import assert from 'node:assert/strict';
import { NOT_ESTIMABLE } from '../src/future_session/calculation_engine.mjs';
import { buildGenerationContract } from '../src/future_session/llm_contract.mjs';

function calc(overrides = {}) {
  return {
    domain: 'CS',
    directionBalance: 0.5,
    nPos: 3,
    nNeg: 1,
    nDirectionalChoices: 4,
    nEligiblePresentations: 5,
    coverage: 0.8,
    ...overrides,
  };
}

function evidence(overrides = {}) {
  return {
    directionBalance: 0.5,
    coverage: 0.8,
    evidenceStatus: 'DESCRIPTIVE_ONLY',
    allowedClaimLevel: 1,
    flags: ['gate_e_not_passed'],
    narrativeConstraints: ['specific_pairs_only'],
    ...overrides,
  };
}

// Contract exposes only pre-computed, depersonalized evidence structure.
{
  const contract = buildGenerationContract({
    calcResult: calc(),
    evidenceResult: evidence(),
    context: {
      retryOccurred: true,
      retryDivergence: true,
      shownTimeouts: 1,
      primaryNonExposures: 1,
      timeoutByPosition: { 1: 0, 2: 1, 3: 0 },
      reflectionAnchorSources: { PRIMARY: 2, FIRST_COMPLETED_RETRY: 1 },
      // Deliberately supplied sensitive/raw fields: builder must ignore them.
      sessionId: 'SECRET_SESSION',
      eventId: 'SECRET_EVENT',
      assetAId: 'SECRET_ASSET',
      rawLatencyMs: [123, 456],
      freeText: 'SECRET_TEXT',
      intensity: 5,
    },
    reasonClassCounts: {
      DOMAIN_CONSISTENT_REASON: 2,
      OTHER_REASON: 1,
    },
  });

  assert.equal(contract.delivery_policy, 'LOCAL_ONLY_BY_DEFAULT');
  assert.equal(contract.allowed_claim_level, 1);
  assert.equal(contract.evidence_status, 'DESCRIPTIVE_ONLY');
  assert.equal(contract.domain, 'CS');
  assert.equal(contract.domain_semantics.positive_direction, 'GREATER_CLARITY');
  assert.equal(contract.domain_semantics.negative_direction, 'GREATER_AMBIGUITY');
  assert.equal(contract.observation.direction_balance, 0.5);
  assert.equal(contract.observation.coverage, 0.8);
  assert.deepEqual(contract.missingness.shown_timeout_positions, [2]);
  assert.equal(contract.reflection.anchor_sources.FIRST_COMPLETED_RETRY, 1);
  assert.equal(contract.reflection.reason_class_counts.DOMAIN_CONSISTENT_REASON, 2);
  assert.equal(contract.reflection.reason_class_counts.CROSS_DOMAIN_REASON, 0);

  const serialized = JSON.stringify(contract);
  for (const secret of [
    'SECRET_SESSION', 'SECRET_EVENT', 'SECRET_ASSET', 'SECRET_TEXT', '123', '456',
  ]) {
    assert.equal(serialized.includes(secret), false, `contract leaked ${secret}`);
  }

  // Safety instructions may legitimately contain words such as "latency". What must never
  // appear are raw input field names/values or identifying keys.
  for (const forbiddenKey of [
    'sessionId', 'eventId', 'assetAId', 'assetBId', 'rawLatencyMs', 'freeText', 'intensity',
  ]) {
    assert.equal(serialized.includes(`"${forbiddenKey}"`), false, `contract leaked key ${forbiddenKey}`);
  }
}

// No estimable direction remains a constrained observation, not an invented zero.
{
  const contract = buildGenerationContract({
    calcResult: calc({
      directionBalance: NOT_ESTIMABLE,
      nPos: 0,
      nNeg: 0,
      nDirectionalChoices: 0,
      nEligiblePresentations: 0,
      coverage: NOT_ESTIMABLE,
    }),
    evidenceResult: evidence({
      directionBalance: NOT_ESTIMABLE,
      coverage: NOT_ESTIMABLE,
      evidenceStatus: 'INSUFFICIENT',
      allowedClaimLevel: 0,
    }),
  });

  assert.equal(contract.observation.direction_balance, NOT_ESTIMABLE);
  assert.equal(contract.observation.direction_class, 'NOT_ESTIMABLE');
  assert.equal(contract.allowed_claim_level, 0);
}

// Exact zero remains balanced among observed choices; no hidden preference is invented.
{
  const contract = buildGenerationContract({
    calcResult: calc({ directionBalance: 0, nPos: 2, nNeg: 2 }),
    evidenceResult: evidence({ directionBalance: 0 }),
  });
  assert.equal(contract.observation.direction_class, 'BALANCED_AMONG_OBSERVED_CHOICES');
}

// Evidence Engine is not allowed to rewrite calculation values at the LLM boundary.
{
  assert.throws(
    () => buildGenerationContract({
      calcResult: calc(),
      evidenceResult: evidence({ directionBalance: -0.5 }),
    }),
    /must not rewrite directionBalance/
  );

  assert.throws(
    () => buildGenerationContract({
      calcResult: calc(),
      evidenceResult: evidence({ coverage: 0.4 }),
    }),
    /must not rewrite coverage/
  );
}

// Claim level 3 is forbidden without explicit REPLICATED evidence status.
{
  assert.throws(
    () => buildGenerationContract({
      calcResult: calc(),
      evidenceResult: evidence({ allowedClaimLevel: 3 }),
    }),
    /claim level 3 requires REPLICATED evidence/
  );
}

// Reflection summary accepts only the frozen interpretation classes and non-negative counts.
{
  assert.throws(
    () => buildGenerationContract({
      calcResult: calc(),
      evidenceResult: evidence(),
      reasonClassCounts: { HIDDEN_MOTIVE: 1 },
    }),
    /unknown reason class/
  );

  assert.throws(
    () => buildGenerationContract({
      calcResult: calc(),
      evidenceResult: evidence(),
      reasonClassCounts: { OTHER_REASON: -1 },
    }),
    /must be a non-negative integer/
  );
}

// CR semantics remain response directions, not traits.
{
  const contract = buildGenerationContract({
    calcResult: calc({ domain: 'CR' }),
    evidenceResult: evidence(),
  });
  assert.equal(contract.domain_semantics.positive_direction, 'GREATER_STRUCTURE');
  assert.equal(contract.domain_semantics.negative_direction, 'GREATER_FLEXIBILITY');
  assert.equal(contract.domain_semantics.interpretation_boundary, 'REACTION_DIRECTION_NOT_PERSON_TRAIT');
}

console.log('llm_contract: all tests passed');
