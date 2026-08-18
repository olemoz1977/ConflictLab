import { calculateDirectionalBalance } from './calculation_engine.mjs';
import { buildEvidenceContext, evaluateEvidenceStatus } from './evidence_engine.mjs';
import { buildGenerationContract } from './llm_contract.mjs';
import { deriveReflectionAnchors } from './rapid_block_core.mjs';

export function deriveLocalResult({
  events,
  gateDConfig,
  gateEConfig,
  domain,
  reflectionAnchors = null,
  reasonClassCounts = null,
  positionStrategyFlag = false,
} = {}) {
  if (!Array.isArray(events)) throw new Error('events must be an array');

  const anchors = reflectionAnchors === null
    ? deriveReflectionAnchors(events)
    : reflectionAnchors;

  if (!Array.isArray(anchors)) throw new Error('reflectionAnchors must be an array or null');

  const calculation = calculateDirectionalBalance({
    events,
    gateDConfig,
    domain,
  });

  const context = buildEvidenceContext({
    events,
    reflectionAnchors: anchors,
    positionStrategyFlag,
  });

  const evidence = evaluateEvidenceStatus({
    calcResult: calculation,
    gateEConfig,
    context,
  });

  const generationContract = buildGenerationContract({
    calcResult: calculation,
    evidenceResult: evidence,
    context,
    reasonClassCounts,
  });

  return {
    calculation,
    context,
    evidence,
    reflectionAnchors: anchors.map(anchor => ({ ...anchor })),
    generationContract,
  };
}
