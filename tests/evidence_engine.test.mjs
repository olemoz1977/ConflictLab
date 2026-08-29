import assert from 'node:assert/strict';
import { NOT_ESTIMABLE } from '../src/future_session/calculation_engine.mjs';
import {
  CLAIM_LEVEL,
  buildEvidenceContext,
  evaluateEvidenceStatus,
} from '../src/future_session/evidence_engine.mjs';

const gateENone = {
  aggregation_gate_version: 'gate-e-test',
  allowed_status: ['VALID', 'PENDING', 'NONE'],
  domains: {
    CS: { status: 'NONE' },
    CR: { status: 'NONE' },
  },
};

const gateEValid = {
  ...gateENone,
  domains: {
    ...gateENone.domains,
    CS: { status: 'VALID' },
  },
};

function calc({ directionBalance, nDirectionalChoices, coverage = 1 }) {
  return {
    domain: 'CS',
    directionBalance,
    nDirectionalChoices,
    coverage,
  };
}

// No directional evidence => insufficient, raw observation only.
{
  const result = evaluateEvidenceStatus({
    calcResult: calc({ directionBalance: NOT_ESTIMABLE, nDirectionalChoices: 0, coverage: NOT_ESTIMABLE }),
    gateEConfig: gateENone,
  });
  assert.equal(result.evidenceStatus, 'INSUFFICIENT');
  assert.equal(result.allowedClaimLevel, CLAIM_LEVEL.RAW_OBSERVATION);
  assert.ok(result.narrativeConstraints.includes('do_not_describe_directional_pattern'));
}

// A single directional event is not a repeated pattern, even if Gate E is VALID.
{
  const result = evaluateEvidenceStatus({
    calcResult: calc({ directionBalance: 1, nDirectionalChoices: 1 }),
    gateEConfig: gateEValid,
  });
  assert.equal(result.evidenceStatus, 'DESCRIPTIVE_ONLY');
  assert.equal(result.allowedClaimLevel, CLAIM_LEVEL.RAW_OBSERVATION);
  assert.ok(result.flags.includes('single_observation_only'));
  assert.ok(result.narrativeConstraints.includes('do_not_use_repeated_pattern_language'));
}

// Repeated pair-level evidence remains pair-specific before Gate E.
{
  const result = evaluateEvidenceStatus({
    calcResult: calc({ directionBalance: 0.5, nDirectionalChoices: 4, coverage: 0.8 }),
    gateEConfig: gateENone,
  });
  assert.equal(result.evidenceStatus, 'DESCRIPTIVE_ONLY');
  assert.equal(result.allowedClaimLevel, CLAIM_LEVEL.SPECIFIC_REPEATED_OBSERVATION);
  assert.ok(result.flags.includes('gate_e_not_passed'));
  assert.ok(result.narrativeConstraints.includes('do_not_generalize_to_domain'));
}

// Gate E VALID can authorize domain-supported language, never trait language.
{
  const result = evaluateEvidenceStatus({
    calcResult: calc({ directionBalance: -0.5, nDirectionalChoices: 4 }),
    gateEConfig: gateEValid,
  });
  assert.equal(result.evidenceStatus, 'DOMAIN_INTERPRETABLE');
  assert.equal(result.allowedClaimLevel, CLAIM_LEVEL.DOMAIN_SUPPORTED_PATTERN);
  assert.ok(result.narrativeConstraints.includes('do_not_claim_stable_person_characteristic'));
  assert.equal(result.directionBalance, -0.5);
}

// Process context creates flags/constraints but never rewrites direction.
{
  const context = buildEvidenceContext({
    events: [
      {
        eventId: 'p1', pairId: 'P1', choice: 'A', pairPresented: true,
        blockAttemptNumber: 1, positionInBlock: 1, isTraining: false,
      },
      {
        eventId: 'p2-timeout', pairId: 'P2', choice: 'timeout', pairPresented: true,
        blockAttemptNumber: 1, positionInBlock: 2, isTraining: false,
      },
      {
        eventId: 'p3-never', pairId: 'P3', choice: 'timeout', pairPresented: false,
        blockAttemptNumber: 1, positionInBlock: 3, isTraining: false,
      },
      {
        eventId: 'p1-retry', pairId: 'P1', choice: 'B', pairPresented: true,
        blockAttemptNumber: 2, positionInBlock: 1, isTraining: false,
      },
    ],
    reflectionAnchors: [
      { pairId: 'P1', anchorSource: 'PRIMARY' },
      { pairId: 'P2', anchorSource: 'FIRST_COMPLETED_RETRY' },
    ],
    positionStrategyFlag: true,
  });

  assert.equal(context.retryOccurred, true);
  assert.equal(context.retryDivergence, true);
  assert.equal(context.shownTimeouts, 1);
  assert.equal(context.primaryNonExposures, 1);
  assert.equal(context.timeoutByPosition[2], 1);
  assert.equal(context.reflectionAnchorSources.FIRST_COMPLETED_RETRY, 1);

  const result = evaluateEvidenceStatus({
    calcResult: calc({ directionBalance: 0.25, nDirectionalChoices: 4, coverage: 0.5 }),
    gateEConfig: gateEValid,
    context,
  });

  assert.equal(result.directionBalance, 0.25);
  assert.equal(result.coverage, 0.5);
  assert.ok(result.flags.includes('retry_choices_diverged_from_primary'));
  assert.ok(result.flags.includes('possible_position_strategy'));
  assert.ok(result.flags.includes('shown_timeouts_present'));
  assert.ok(result.flags.includes('primary_non_exposures_present'));
  assert.ok(result.flags.includes('some_reflections_anchored_to_retry'));
}

// Training retry events do not create research retry context.
{
  const context = buildEvidenceContext({
    events: [
      {
        eventId: 'training-retry', pairId: 'T1', choice: 'A', pairPresented: true,
        blockAttemptNumber: 2, positionInBlock: 1, isTraining: true,
      },
    ],
  });
  assert.equal(context.retryOccurred, false);
}

console.log('evidence_engine: all tests passed');
