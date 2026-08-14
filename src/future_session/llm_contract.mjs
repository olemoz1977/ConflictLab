import { NOT_ESTIMABLE } from './calculation_engine.mjs';

const DOMAIN_SEMANTICS = Object.freeze({
  CS: Object.freeze({
    positiveDirection: 'GREATER_CLARITY',
    negativeDirection: 'GREATER_AMBIGUITY',
  }),
  CR: Object.freeze({
    positiveDirection: 'GREATER_STRUCTURE',
    negativeDirection: 'GREATER_FLEXIBILITY',
  }),
});

const REASON_CLASSES = Object.freeze([
  'DOMAIN_CONSISTENT_REASON',
  'CROSS_DOMAIN_REASON',
  'OTHER_REASON',
  'UNRESOLVED',
]);

const FORBIDDEN_OUTPUTS = Object.freeze([
  'Do NOT calculate a new CS/CR score.',
  'Do NOT describe personality traits or stable person characteristics.',
  'Do NOT interpret latency as depth, impulsivity, confidence, or signal strength.',
  'Do NOT use CONVERGENT/DIVERGENT terminology for cross-channel comparison.',
  'Do NOT infer hidden motive from a structured reason selection.',
  'Do NOT use language above allowed_claim_level.',
  'Do NOT identify or attempt to identify the participant.',
]);

const REQUIRED_OUTPUT_STRUCTURE = Object.freeze({
  observation: 'What was observed at the allowed claim level.',
  coverage_note: 'How much eligible presented evidence contained an A/B choice.',
  exceptions: 'Timeouts, non-exposure, retry divergence, or other flags when present.',
  reflection_context: 'Structured reflection context stated cautiously; no hidden-motive claim.',
  reflection_question: 'One open self-observation question.',
});

function assertNonNegativeInteger(value, name) {
  if (!Number.isInteger(value) || value < 0) {
    throw new Error(`${name} must be a non-negative integer`);
  }
}

function assertEvidenceMatchesCalculation(calcResult, evidenceResult) {
  if (evidenceResult.directionBalance !== calcResult.directionBalance) {
    throw new Error('Evidence Engine must not rewrite directionBalance');
  }
  if (evidenceResult.coverage !== calcResult.coverage) {
    throw new Error('Evidence Engine must not rewrite coverage');
  }
  if (evidenceResult.allowedClaimLevel < 0 || evidenceResult.allowedClaimLevel > 3) {
    throw new Error('allowedClaimLevel must be between 0 and 3');
  }
  if (evidenceResult.allowedClaimLevel === 3 && evidenceResult.evidenceStatus !== 'REPLICATED') {
    throw new Error('claim level 3 requires REPLICATED evidence');
  }
}

function directionClass(balance) {
  if (balance === NOT_ESTIMABLE) return 'NOT_ESTIMABLE';
  if (typeof balance !== 'number' || !Number.isFinite(balance) || balance < -1 || balance > 1) {
    throw new Error('directionBalance must be NOT_ESTIMABLE or a finite number in [-1, 1]');
  }
  if (balance > 0) return 'POSITIVE_DIRECTION_MORE_FREQUENT';
  if (balance < 0) return 'NEGATIVE_DIRECTION_MORE_FREQUENT';
  return 'BALANCED_AMONG_OBSERVED_CHOICES';
}

function normalizeReasonClassCounts(reasonClassCounts) {
  if (reasonClassCounts === null || reasonClassCounts === undefined) return null;
  if (typeof reasonClassCounts !== 'object' || Array.isArray(reasonClassCounts)) {
    throw new Error('reasonClassCounts must be an object or null');
  }

  const unknown = Object.keys(reasonClassCounts).filter(key => !REASON_CLASSES.includes(key));
  if (unknown.length > 0) {
    throw new Error(`unknown reason class: ${unknown[0]}`);
  }

  const normalized = {};
  for (const key of REASON_CLASSES) {
    const value = reasonClassCounts[key] ?? 0;
    assertNonNegativeInteger(value, `reasonClassCounts.${key}`);
    normalized[key] = value;
  }
  return normalized;
}

function timeoutPositions(timeoutByPosition = {}) {
  const positions = [];
  for (const position of [1, 2, 3]) {
    const count = timeoutByPosition[position] ?? timeoutByPosition[String(position)] ?? 0;
    assertNonNegativeInteger(count, `timeoutByPosition.${position}`);
    for (let i = 0; i < count; i += 1) positions.push(position);
  }
  return positions;
}

export function buildGenerationContract({
  calcResult,
  evidenceResult,
  context = {},
  reasonClassCounts = null,
  generationContractVersion = 'v0.2',
} = {}) {
  if (!calcResult || !evidenceResult) {
    throw new Error('calcResult and evidenceResult are required');
  }
  const semantics = DOMAIN_SEMANTICS[calcResult.domain];
  if (!semantics) throw new Error(`unsupported domain: ${calcResult.domain}`);
  if (evidenceResult.evidenceStatus === undefined) {
    throw new Error('evidenceResult.evidenceStatus is required');
  }

  assertEvidenceMatchesCalculation(calcResult, evidenceResult);
  assertNonNegativeInteger(calcResult.nPos, 'calcResult.nPos');
  assertNonNegativeInteger(calcResult.nNeg, 'calcResult.nNeg');
  assertNonNegativeInteger(calcResult.nEligiblePresentations, 'calcResult.nEligiblePresentations');

  const normalizedReasonCounts = normalizeReasonClassCounts(reasonClassCounts);
  const anchorSources = {
    PRIMARY: context.reflectionAnchorSources?.PRIMARY ?? 0,
    FIRST_COMPLETED_RETRY: context.reflectionAnchorSources?.FIRST_COMPLETED_RETRY ?? 0,
  };
  assertNonNegativeInteger(anchorSources.PRIMARY, 'reflectionAnchorSources.PRIMARY');
  assertNonNegativeInteger(
    anchorSources.FIRST_COMPLETED_RETRY,
    'reflectionAnchorSources.FIRST_COMPLETED_RETRY'
  );

  const shownTimeouts = context.shownTimeouts ?? 0;
  const primaryNonExposures = context.primaryNonExposures ?? 0;
  assertNonNegativeInteger(shownTimeouts, 'context.shownTimeouts');
  assertNonNegativeInteger(primaryNonExposures, 'context.primaryNonExposures');

  const contract = {
    generation_contract_version: generationContractVersion,
    delivery_policy: 'LOCAL_ONLY_BY_DEFAULT',
    allowed_claim_level: evidenceResult.allowedClaimLevel,
    evidence_status: evidenceResult.evidenceStatus,
    domain: calcResult.domain,
    domain_semantics: {
      positive_direction: semantics.positiveDirection,
      negative_direction: semantics.negativeDirection,
      interpretation_boundary: 'REACTION_DIRECTION_NOT_PERSON_TRAIT',
    },
    observation: {
      direction_balance: calcResult.directionBalance,
      direction_class: directionClass(calcResult.directionBalance),
      n_pos: calcResult.nPos,
      n_neg: calcResult.nNeg,
      eligible_presented: calcResult.nEligiblePresentations,
      coverage: calcResult.coverage,
    },
    missingness: {
      shown_timeouts: shownTimeouts,
      primary_non_exposures: primaryNonExposures,
      shown_timeout_positions: timeoutPositions(context.timeoutByPosition),
    },
    reflection: {
      anchor_sources: anchorSources,
      reason_class_counts: normalizedReasonCounts,
    },
    retry_context: {
      retry_occurred: Boolean(context.retryOccurred),
      primary_vs_retry_divergence: Boolean(context.retryDivergence),
    },
    flags: Array.isArray(evidenceResult.flags) ? [...evidenceResult.flags] : [],
    narrative_constraints: Array.isArray(evidenceResult.narrativeConstraints)
      ? [...evidenceResult.narrativeConstraints]
      : [],
    forbidden_outputs: [...FORBIDDEN_OUTPUTS],
    required_output_structure: { ...REQUIRED_OUTPUT_STRUCTURE },
  };

  return contract;
}

export { DOMAIN_SEMANTICS, FORBIDDEN_OUTPUTS, REQUIRED_OUTPUT_STRUCTURE };
