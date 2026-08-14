function read(obj, camel, snake) {
  if (obj == null) return undefined;
  return obj[camel] !== undefined ? obj[camel] : obj[snake];
}

function asBool(value) {
  return value === true || value === 1 || value === '1';
}

function finiteOrNull(value) {
  const number = Number(value);
  return Number.isFinite(number) ? number : null;
}

function ratio(numerator, denominator) {
  return denominator > 0 ? numerator / denominator : null;
}

function median(values) {
  const clean = values.filter(Number.isFinite).sort((a, b) => a - b);
  if (!clean.length) return null;
  const mid = Math.floor(clean.length / 2);
  return clean.length % 2 ? clean[mid] : (clean[mid - 1] + clean[mid]) / 2;
}

function normalizeAttempt(raw) {
  return {
    blockAttemptId: read(raw, 'blockAttemptId', 'block_attempt_id'),
    blockId: read(raw, 'blockId', 'block_id'),
    attemptNumber: Number(read(raw, 'blockAttemptNumber', 'block_attempt_number')),
    blockBudgetMs: Number(read(raw, 'blockBudgetMs', 'block_budget_ms')),
    blockTimedOut: asBool(read(raw, 'blockTimedOut', 'block_timed_out')),
    pageHiddenDuringBlock: asBool(read(raw, 'pageHiddenDuringBlock', 'page_hidden_during_block')),
    isTraining: asBool(read(raw, 'isTraining', 'is_training')),
    deviceCategory: read(raw, 'deviceCategory', 'device_category') ?? null,
  };
}

function normalizeEvent(raw) {
  return {
    blockAttemptId: read(raw, 'blockAttemptId', 'block_attempt_id'),
    blockId: read(raw, 'blockId', 'block_id'),
    attemptNumber: Number(read(raw, 'blockAttemptNumber', 'block_attempt_number')),
    pairId: read(raw, 'pairId', 'pair_id'),
    positionInBlock: Number(read(raw, 'positionInBlock', 'position_in_block')),
    pairPresented: asBool(read(raw, 'pairPresented', 'pair_presented')),
    choice: read(raw, 'choice', 'choice'),
    visualChoiceLatencyMs: finiteOrNull(read(raw, 'visualChoiceLatencyMs', 'visual_choice_latency_ms')),
    remainingBudgetAtPairStartMs: finiteOrNull(read(raw, 'remainingBudgetAtPairStartMs', 'remaining_budget_at_pair_start_ms')),
    isTraining: asBool(read(raw, 'isTraining', 'is_training')),
    deviceCategory: read(raw, 'deviceCategory', 'device_category') ?? null,
  };
}

function isChoice(event) {
  return event.choice === 'A' || event.choice === 'B';
}

function completeTelemetry(events) {
  if (events.length !== 3) return false;
  const positions = new Set(events.map(event => event.positionInBlock));
  if (positions.size !== 3 || ![1, 2, 3].every(position => positions.has(position))) return false;
  return events.every(event => event.pairId && ['A', 'B', 'timeout'].includes(event.choice));
}

function pushMetric(map, key, value) {
  if (!map.has(key)) map.set(key, []);
  map.get(key).push(value);
}

function pairSummary(pairStats) {
  return [...pairStats.entries()]
    .map(([pairId, stats]) => ({
      pairId,
      n: stats.n,
      missingCount: stats.missing,
      missingRate: ratio(stats.missing, stats.n),
      neverPresentedCount: stats.neverPresented,
      neverPresentedRate: ratio(stats.neverPresented, stats.n),
    }))
    .sort((a, b) => a.pairId.localeCompare(b.pairId));
}

function deviceSummary(deviceStats, minimumN) {
  const groups = [...deviceStats.entries()]
    .map(([deviceCategory, stats]) => ({
      deviceCategory,
      n: stats.n,
      completed: stats.completed,
      completionRate: ratio(stats.completed, stats.n),
    }))
    .sort((a, b) => a.deviceCategory.localeCompare(b.deviceCategory));

  const estimable = groups.filter(group => group.n >= minimumN);
  let completionGap = null;
  if (estimable.length >= 2) {
    const rates = estimable.map(group => group.completionRate);
    completionGap = Math.max(...rates) - Math.min(...rates);
  }
  return { groups, completionGap };
}

export function evaluateTimingCalibration({ attempts = [], pairEvents = [], config }) {
  if (!config || config.scope !== 'MECHANICAL_TIMING_ONLY') {
    throw new Error('timing calibration config is required');
  }

  const normalizedAttempts = attempts.map(normalizeAttempt);
  const normalizedEvents = pairEvents.map(normalizeEvent);
  const eventsByAttempt = new Map();
  for (const event of normalizedEvents) {
    if (!eventsByAttempt.has(event.blockAttemptId)) eventsByAttempt.set(event.blockAttemptId, []);
    eventsByAttempt.get(event.blockAttemptId).push(event);
  }

  const candidatePrimary = normalizedAttempts.filter(attempt => attempt.attemptNumber === 1 && !attempt.isTraining);
  const pageHiddenCount = candidatePrimary.filter(attempt => attempt.pageHiddenDuringBlock).length;
  const excluded = {
    training: normalizedAttempts.filter(attempt => attempt.isTraining).length,
    pageHidden: pageHiddenCount,
    invalidTelemetry: 0,
    wrongBudget: 0,
  };

  const clean = [];
  for (const attempt of candidatePrimary) {
    if (attempt.pageHiddenDuringBlock) continue;
    if (attempt.blockBudgetMs !== Number(config.candidate_budget_ms)) {
      excluded.wrongBudget += 1;
      continue;
    }
    const events = (eventsByAttempt.get(attempt.blockAttemptId) || [])
      .filter(event => event.attemptNumber === 1 && !event.isTraining)
      .sort((a, b) => a.positionInBlock - b.positionInBlock);

    if (!completeTelemetry(events)) {
      excluded.invalidTelemetry += 1;
      continue;
    }

    const allChosen = events.every(isChoice);
    if (allChosen === attempt.blockTimedOut) {
      excluded.invalidTelemetry += 1;
      continue;
    }
    clean.push({ attempt, events, completed: allChosen });
  }

  const positionStats = new Map([[1, { n: 0, missing: 0, neverPresented: 0, shownTimeout: 0 }], [2, { n: 0, missing: 0, neverPresented: 0, shownTimeout: 0 }], [3, { n: 0, missing: 0, neverPresented: 0, shownTimeout: 0 }]]);
  const latencyByPosition = new Map();
  const remainingBudgetByPosition = new Map();
  const pairs = new Map();
  const devices = new Map();
  let completedBlocks = 0;

  for (const block of clean) {
    if (block.completed) completedBlocks += 1;
    const device = block.attempt.deviceCategory || block.events.find(event => event.deviceCategory)?.deviceCategory || 'unknown';
    if (!devices.has(device)) devices.set(device, { n: 0, completed: 0 });
    devices.get(device).n += 1;
    if (block.completed) devices.get(device).completed += 1;

    for (const event of block.events) {
      const stats = positionStats.get(event.positionInBlock);
      stats.n += 1;
      if (!isChoice(event)) stats.missing += 1;
      if (!event.pairPresented) stats.neverPresented += 1;
      if (event.pairPresented && !isChoice(event)) stats.shownTimeout += 1;

      if (event.visualChoiceLatencyMs !== null) pushMetric(latencyByPosition, event.positionInBlock, event.visualChoiceLatencyMs);
      if (event.remainingBudgetAtPairStartMs !== null) pushMetric(remainingBudgetByPosition, event.positionInBlock, event.remainingBudgetAtPairStartMs);

      if (!pairs.has(event.pairId)) pairs.set(event.pairId, { n: 0, missing: 0, neverPresented: 0 });
      const pair = pairs.get(event.pairId);
      pair.n += 1;
      if (!isChoice(event)) pair.missing += 1;
      if (!event.pairPresented) pair.neverPresented += 1;
    }
  }

  const cleanBlockIds = new Set(clean.map(block => block.attempt.blockId));
  const retryBlockIds = new Set(normalizedAttempts
    .filter(attempt => attempt.attemptNumber > 1 && cleanBlockIds.has(attempt.blockId))
    .map(attempt => attempt.blockId));

  const position = {};
  for (const index of [1, 2, 3]) {
    const stats = positionStats.get(index);
    position[index] = {
      n: stats.n,
      missingCount: stats.missing,
      missingRate: ratio(stats.missing, stats.n),
      neverPresentedCount: stats.neverPresented,
      neverPresentedRate: ratio(stats.neverPresented, stats.n),
      shownTimeoutCount: stats.shownTimeout,
      shownTimeoutRate: ratio(stats.shownTimeout, stats.n),
      medianLatencyMs: median(latencyByPosition.get(index) || []),
      medianRemainingBudgetAtPairStartMs: median(remainingBudgetByPosition.get(index) || []),
    };
  }

  const pairMetrics = pairSummary(pairs);
  const deviceMetrics = deviceSummary(devices, Number(config.data_floor.device_gap_min_n_per_group));
  const nClean = clean.length;
  const completionRate = ratio(completedBlocks, nClean);
  const missingGradient = nClean > 0 ? position[3].missingRate - position[1].missingRate : null;

  const metrics = {
    candidateBudgetMs: Number(config.candidate_budget_ms),
    candidatePrimaryBlocks: candidatePrimary.length,
    cleanPrimaryBlocks: nClean,
    completedPrimaryBlocks: completedBlocks,
    primaryBlockCompletionRate: completionRate,
    retryRate: ratio(retryBlockIds.size, nClean),
    pageHiddenRate: ratio(pageHiddenCount, candidatePrimary.length),
    missingRateGradientP3MinusP1: missingGradient,
    position,
    pairs: pairMetrics,
    devices: deviceMetrics,
    excluded,
  };

  if (nClean < Number(config.data_floor.min_clean_primary_blocks)) {
    return { decision: 'INSUFFICIENT_DATA', redReasons: [], greenFailures: [], metrics };
  }

  const red = config.red_thresholds;
  const green = config.green_thresholds;
  const pairMinN = Number(config.data_floor.pair_level_threshold_min_n);
  const redReasons = [];
  const greenFailures = [];

  if (completionRate < red.primary_block_completion_rate_below) redReasons.push('PRIMARY_COMPLETION_RED');
  if (position[3].neverPresentedRate > red.position3_never_presented_rate_above) redReasons.push('POSITION3_NONEXPOSURE_RED');
  if (position[3].missingRate > red.position3_missing_rate_above) redReasons.push('POSITION3_MISSING_RED');
  if (missingGradient > red.missing_rate_gradient_p3_minus_p1_above) redReasons.push('POSITION_DEPLETION_RED');
  for (const pair of pairMetrics) {
    if (pair.n >= pairMinN && pair.missingRate > red.pair_missing_rate_above) redReasons.push(`PAIR_MISSING_RED:${pair.pairId}`);
  }

  if (completionRate < green.primary_block_completion_rate_min) greenFailures.push('PRIMARY_COMPLETION_AMBER');
  if (position[3].neverPresentedRate > green.position3_never_presented_rate_max) greenFailures.push('POSITION3_NONEXPOSURE_AMBER');
  if (position[3].missingRate > green.position3_missing_rate_max) greenFailures.push('POSITION3_MISSING_AMBER');
  if (missingGradient > green.missing_rate_gradient_p3_minus_p1_max) greenFailures.push('POSITION_DEPLETION_AMBER');
  for (const pair of pairMetrics) {
    if (pair.n >= pairMinN && pair.missingRate > green.pair_missing_rate_max) greenFailures.push(`PAIR_MISSING_AMBER:${pair.pairId}`);
  }

  if (redReasons.length) return { decision: 'REJECT_6000', redReasons, greenFailures, metrics };
  if (greenFailures.length) return { decision: 'ADJUST_AND_RETEST', redReasons, greenFailures, metrics };
  return { decision: 'KEEP_6000', redReasons, greenFailures, metrics };
}
