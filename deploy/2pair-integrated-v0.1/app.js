import {
  PROTOCOL_VERSION, STIMULUS_SET_VERSION, TRAINING_SET_VERSION, BLOCK_BUDGET_MS, MAX_ATTEMPTS,
  RESEARCH_PAIRS, createIntegratedPlans, createTrainingPlan, RapidAttempt, primaryAnchors, localChoiceTrace
} from './integrated_core.mjs';

const RELEASE_ID = '2pair-integrated-v0.1';
const CONSENT_VERSION = '2pair-integrated-research-consent-v0.1';
const API = './server/integrated_api.php';
const PRIVACY = '/privacy.html';
const app = document.getElementById('app');
const homeLink = document.getElementById('homeLink');
const sessionId = crypto.randomUUID();

const state = {
  lang: 'lt', mode: 'UNDECIDED', consent: false, age: false,
  deletionCode: null, deletionHash: null, trainingPlan: null,
  blockPlans: [], blockRuns: [], activeAttempt: null, activeTimer: null,
  device: deviceCategory(), reflection: [], uploadOk: false, currentBlockId: null
};

const C = {
  lt: {
    chooseLang: 'Pasirink kalbą',
    intro: 'Pirmiausia trumpai išbandysi greito pasirinkimo taisyklę. Po to bus dvi trumpos pasirinkimų serijos ir refleksija.',
    startTraining: 'Pradėti treniruotę', trainingTitle: 'Trumpa treniruotė',
    trainingText: 'Pamatysi 3 poras. Kiekvieną kartą rinkis vaizdą, kurį pasirinktum pirmiau. Visoms trims poroms skirtas vienas bendras 6 sekundžių laikas.',
    trainingOnly: 'Treniruotė lieka šiame įrenginyje ir nepatenka į analizę.',
    retry: 'Pakartoti', restart: 'Pradėti treniruotę iš naujo', trainingDone: 'Treniruotė baigta',
    consentTitle: 'Dalyvavimas tyrime',
    consentText: 'Gali tęsti su duomenų įkėlimu arba tik lokaliai. Tyrimas saugos pseudoniminį sesijos ID, vaizdų pasirinkimus, mechaninį pasirinkimo laiką ir tavo neprivalomą refleksiją. Tai nėra asmenybės diagnozė.',
    age: 'Patvirtinu, kad man yra 18 metų arba daugiau.',
    research: 'Savanoriškai sutinku, kad šie duomenys būtų naudojami 2Pair timing / UX ir stimulus validation tyrimui.',
    privacy: 'Privatumo informacija', join: 'Sutinku ir dalyvauju', local: 'Tęsti be duomenų įkėlimo',
    mainReady: 'Pagrindinė dalis',
    mainText: 'Bus dvi trumpos serijos po 3 poras. Rinkis natūraliai. Nebandyk „laimėti“ laikmačio ir neieškok teisingo atsakymo.',
    start: 'Pradėti', block: 'Serija', of: 'iš', timeout: 'Laikas baigėsi',
    retryBlock: 'Pakartok tą pačią seriją. Porų tvarka ir vaizdų pozicijos nesikeis.',
    continueNext: 'Tęsti į kitą seriją',
    rapidDoneTitle: 'Greitas etapas baigtas',
    rapidDoneText: 'Pasirinkimai užfiksuoti. Dabar gali ramiai peržiūrėti poras ir, jei nori, įvardyti pasirinkimo priežastį bei reakcijos stiprumą.',
    startReflection: 'Pereiti į refleksiją',
    reflectionTitle: 'Trumpa refleksija', reflectionPrompt: 'Kas labiausiai nulėmė tavo pasirinkimą?',
    reflectionNcc: 'Kas apsunkino pasirinkimą?', optional: 'Neprivaloma', placeholder: 'Jei nori, keli žodžiai…',
    hard: 'Sunku įvardyti priežastį', intensity: 'Reakcijos stiprumas', weak: 'Silpna', strong: 'Stipri',
    saveNext: 'Išsaugoti ir tęsti', saving: 'Išsaugoma…', saveError: 'Nepavyko išsaugoti. Patikrink ryšį ir bandyk dar kartą.',
    traceTitle: 'Tavo pasirinkimų pėdsakas', traceText: 'Tai tavo šios sesijos pasirinkimų seka. Ji nėra asmenybės rezultatas ar diagnozė.',
    noClear: 'Nėra aiškaus pasirinkimo', done: 'Baigta',
    codeTitle: 'Duomenų ištrynimo kodas', codeHelp: 'Jei dalyvavai su įkėlimu, išsisaugok kodą. Jis leidžia pašalinti šios sesijos duomenis neatskleidžiant tavo vardo.',
    restartSession: 'Pradėti iš naujo', home: 'Grįžti į 2RASI', technical: 'Techninė klaida'
  },
  en: {
    chooseLang: 'Choose language',
    intro: 'First you will practice the rapid-choice rule. Then there are two short choice blocks followed by reflection.',
    startTraining: 'Start practice', trainingTitle: 'Quick practice',
    trainingText: 'You will see 3 pairs. Each time choose the image you would pick first. All three pairs share one 6-second time window.',
    trainingOnly: 'Practice stays on this device and never enters analysis.',
    retry: 'Repeat', restart: 'Restart practice', trainingDone: 'Practice complete',
    consentTitle: 'Research participation',
    consentText: 'You can continue with data upload or locally only. The research stores a pseudonymous session ID, image choices, mechanical choice timing and your optional reflection. This is not a personality diagnosis.',
    age: 'I confirm that I am 18 years old or older.',
    research: 'I voluntarily consent to these data being used for 2Pair timing / UX and stimulus validation research.',
    privacy: 'Privacy information', join: 'I consent and participate', local: 'Continue without upload',
    mainReady: 'Main session',
    mainText: 'There will be two short series of 3 pairs. Choose naturally. Do not try to beat the timer and do not look for a correct answer.',
    start: 'Start', block: 'Block', of: 'of', timeout: 'Time ended',
    retryBlock: 'Repeat the same block. Pair order and image positions will stay unchanged.',
    continueNext: 'Continue to next block',
    rapidDoneTitle: 'Rapid stage complete',
    rapidDoneText: 'Your choices are recorded. Now you can calmly review the pairs and, if you want, name the reason and reaction intensity.',
    startReflection: 'Continue to reflection',
    reflectionTitle: 'Quick reflection', reflectionPrompt: 'What most influenced your choice?',
    reflectionNcc: 'What made the choice difficult?', optional: 'Optional', placeholder: 'If you want, a few words…',
    hard: 'Hard to identify the reason', intensity: 'Reaction intensity', weak: 'Low', strong: 'Strong',
    saveNext: 'Save and continue', saving: 'Saving…', saveError: 'Could not save. Check your connection and try again.',
    traceTitle: 'Your choice trace', traceText: 'This is the sequence of your choices in this session. It is not a personality result or diagnosis.',
    noClear: 'No clear choice', done: 'Done',
    codeTitle: 'Data deletion code', codeHelp: 'If you participated with upload, keep this code. It can be used to remove this session without revealing your name.',
    restartSession: 'Start again', home: 'Back to 2RASI', technical: 'Technical error'
  }
};
const t = k => C[state.lang][k] || k;

function deviceCategory() {
  const w = Math.min(innerWidth, screen.width || innerWidth);
  if (w < 700) return 'mobile';
  if (w < 1100) return 'tablet';
  return 'desktop';
}
function setRapid(v) { document.body.classList.toggle('rapid', v); }
function el(tag, cls, text) { const n = document.createElement(tag); if (cls) n.className = cls; if (text !== undefined) n.textContent = text; return n; }
function setCard(center = false) { setRapid(false); app.className = 'card' + (center ? ' center' : ''); app.replaceChildren(); }
function syncHomeLink() {
  if (!homeLink) return;
  homeLink.href = state.lang === 'lt' ? 'https://2rasi.lt/' : 'https://2rasi.com/';
  homeLink.textContent = `← ${t('home')}`;
  homeLink.hreflang = state.lang;
}
function sleepFrame() { return new Promise(r => requestAnimationFrame(() => r())); }
function randomHex(bytes = 16) { const a = new Uint8Array(bytes); crypto.getRandomValues(a); return [...a].map(x => x.toString(16).padStart(2, '0')).join(''); }
async function sha256hex(s) { const b = new TextEncoder().encode(s); const d = new Uint8Array(await crypto.subtle.digest('SHA-256', b)); return [...d].map(x => x.toString(16).padStart(2, '0')).join(''); }
function commonPayload() {
  const p = { sessionId, releaseId: RELEASE_ID, protocolVersion: PROTOCOL_VERSION, stimulusSetVersion: STIMULUS_SET_VERSION, trainingSetVersion: TRAINING_SET_VERSION, language: state.lang, deviceCategory: state.device };
  if (state.mode === 'RESEARCH') Object.assign(p, { consentVersion: CONSENT_VERSION, researchConsent: true, age18Confirmed: true, deletionTokenHash: state.deletionHash });
  return p;
}
async function post(payload) {
  const r = await fetch(API, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  let data = null; try { data = await r.json(); } catch {}
  if (!r.ok || !data?.ok) throw new Error(data?.message || `HTTP ${r.status}`);
  return data;
}

function showLanguage() {
  syncHomeLink();
  setCard(true);
  app.append(el('h1', '', t('chooseLang')), el('p', '', t('intro')));
  const g = el('div', 'lang');
  for (const lang of ['lt', 'en']) {
    const b = el('button', 'secondary', lang.toUpperCase());
    b.onclick = () => { state.lang = lang; document.documentElement.lang = lang; showLanguage(); };
    g.append(b);
  }
  app.append(g);
  const start = el('button', 'primary', t('startTraining')); start.style.marginTop = '16px'; start.onclick = showTrainingIntro; app.append(start);
}

function trainingAsset(pair, which) { return `./assets/training/${which === 'A' ? pair.aFile : pair.bFile}`; }
function researchAsset(pairId, which) { const p = RESEARCH_PAIRS[pairId]; return `./assets/research/${pairId}/${which === 'A' ? p.aFile : p.bFile}`; }
async function preload(urls) {
  await Promise.all(urls.map(url => new Promise((resolve, reject) => {
    const i = new Image();
    i.onload = async () => { try { if (i.decode) await i.decode(); } catch {} resolve(); };
    i.onerror = () => reject(new Error(`asset preload failed: ${url}`));
    i.src = url;
  })));
}

function showTrainingIntro() {
  setCard(true);
  app.append(el('h2', '', t('trainingTitle')), el('p', '', t('trainingText')), el('p', 'muted', t('trainingOnly')));
  const b = el('button', 'primary', t('startTraining')); b.onclick = beginTraining; app.append(b);
}
async function beginTraining() {
  try {
    state.trainingPlan = createTrainingPlan();
    await preload(state.trainingPlan.pairs.flatMap(p => [trainingAsset(p, 'A'), trainingAsset(p, 'B')]));
    runTrainingAttempt(1);
  } catch (e) { showError(e); }
}
function runTrainingAttempt(n) {
  runRapid({
    plan: { blockIndex: 0, formId: 'TRAINING', pairs: state.trainingPlan.pairs }, attemptNumber: n, isTraining: true,
    onTerminal: (_attempt, result) => {
      if (result.status === 'COMPLETE') { showConsent(); return; }
      if (n < MAX_ATTEMPTS) showRetry(true, () => runTrainingAttempt(n + 1));
      else showRetry(true, beginTraining, true);
    }
  });
}

function showConsent() {
  setCard();
  app.append(el('h2', '', t('consentTitle')), el('p', '', t('consentText')));
  const box = el('div', 'consent');
  const age = el('input'); age.type = 'checkbox';
  const ageLabel = el('label'); ageLabel.append(age, el('span', '', t('age')));
  const consent = el('input'); consent.type = 'checkbox';
  const cLabel = el('label'); cLabel.append(consent, el('span', '', t('research')));
  box.append(ageLabel, cLabel); app.append(box);
  const privacy = el('p', 'muted'); const a = el('a', '', t('privacy')); a.href = `${PRIVACY}?lang=${state.lang}`; a.target = '_blank'; privacy.append(a); app.append(privacy);
  const actions = el('div', 'actions');
  const join = el('button', 'primary', t('join')); join.disabled = true;
  const sync = () => join.disabled = !(age.checked && consent.checked); age.onchange = sync; consent.onchange = sync;
  join.onclick = async () => {
    state.mode = 'RESEARCH'; state.age = true; state.consent = true;
    state.deletionCode = randomHex(16); state.deletionHash = await sha256hex(state.deletionCode);
    try { localStorage.setItem(`2pair.integrated.deletion.${sessionId}`, state.deletionCode); } catch {}
    showPreUploadCode();
  };
  const local = el('button', 'secondary', t('local')); local.onclick = () => { state.mode = 'LOCAL'; prepareMeasured(); };
  actions.append(join, local); app.append(actions);
}

function showPreUploadCode() {
  setCard();
  app.append(el('h2', '', t('codeTitle')), el('p', 'muted', t('codeHelp')));
  const code = el('code'); code.textContent = state.deletionCode; code.style.wordBreak = 'break-all'; app.append(code);
  const b = el('button', 'primary', t('start')); b.style.marginTop = '16px'; b.onclick = prepareMeasured; app.append(b);
}
async function prepareMeasured() {
  try {
    state.blockPlans = createIntegratedPlans();
    await preload(state.blockPlans.flatMap(plan => plan.pairs.flatMap(p => [researchAsset(p.pairId, 'A'), researchAsset(p.pairId, 'B')])));
    setCard(true); app.append(el('h2', '', t('mainReady')), el('p', '', t('mainText')));
    const b = el('button', 'primary', t('start')); b.onclick = () => startBlock(0); app.append(b);
  } catch (e) { showError(e); }
}

function runRapid({ plan, attemptNumber, isTraining, onTerminal, priorExposureCounts = {} }) {
  const blockId = isTraining ? crypto.randomUUID() : (state.currentBlockId || crypto.randomUUID());
  if (!isTraining) state.currentBlockId = blockId;
  const attempt = new RapidAttempt({ sessionId, blockId, blockIndex: plan.blockIndex, formId: plan.formId, attemptNumber, pairs: plan.pairs, priorExposureCounts, allowNoClear: !isTraining, isTraining });
  state.activeAttempt = attempt;
  const run = { attemptNumber, summary: null, events: null };
  let firstReadyAt = null;
  const visibility = () => { if (document.hidden && state.activeAttempt === attempt) attempt.markPageHidden(); };
  document.addEventListener('visibilitychange', visibility);
  const cleanup = () => { if (state.activeTimer) clearTimeout(state.activeTimer); state.activeTimer = null; state.activeAttempt = null; document.removeEventListener('visibilitychange', visibility); };
  const terminal = result => { cleanup(); run.summary = attempt.summary(); run.events = attempt.events.map(e => ({ ...e })); onTerminal(attempt, result, run); };
  const scheduleDeadline = start => {
    firstReadyAt = start;
    const check = () => {
      if (attempt.done) return;
      const elapsed = performance.now() - firstReadyAt;
      if (elapsed >= BLOCK_BUDGET_MS) {
        let r; try { r = attempt.expire(performance.now()); } catch { state.activeTimer = setTimeout(check, 4); return; }
        terminal(r);
      } else state.activeTimer = setTimeout(check, Math.max(4, BLOCK_BUDGET_MS - elapsed + 1));
    };
    state.activeTimer = setTimeout(check, BLOCK_BUDGET_MS + 1);
  };

  const render = async () => {
    const pair = attempt.currentPair(); if (!pair) return;
    setRapid(true); app.className = 'card rapid-shell'; app.replaceChildren();
    const head = el('div', 'rapid-head');
    const left = isTraining ? `${t('trainingTitle')} ${attemptNumber}/${MAX_ATTEMPTS}` : `${t('block')} ${plan.blockIndex} ${t('of')} 2`;
    const right = isTraining ? `${pair.positionInBlock} / 3` : `${pair.sessionPresentationIndex} / 6`;
    head.append(el('span', '', left), el('span', '', right));

    const stage = el('div', isTraining ? 'pair-stage' : 'pair-stage with-ncc');
    const items = [
      { id: 'A', pos: pair.aPosition, url: isTraining ? trainingAsset(pair, 'A') : researchAsset(pair.pairId, 'A') },
      { id: 'B', pos: pair.bPosition, url: isTraining ? trainingAsset(pair, 'B') : researchAsset(pair.pairId, 'B') }
    ].sort((x, y) => x.pos === 'top' ? -1 : 1);
    let locked = false;
    const responseButtons = [];
    const choose = id => {
      if (locked) return; locked = true;
      for (const b of responseButtons) b.disabled = true;
      const r = attempt.recordChoice(id, performance.now());
      if (r.status === 'CHOICE_RECORDED') render();
      else if (r.status === 'COMPLETE' || r.status === 'TIMEOUT') terminal(r);
    };
    const makeVisual = item => {
      const b = el('button', 'visual'); b.disabled = true;
      const img = el('img'); img.src = item.url; img.alt = ''; b.append(img); b.onclick = () => choose(item.id);
      responseButtons.push(b); return b;
    };

    if (isTraining) {
      stage.append(makeVisual(items[0]), makeVisual(items[1]));
    } else {
      const ncc = el('button', 'ncc', t('noClear')); ncc.disabled = true; ncc.onclick = () => choose('no_clear_choice'); responseButtons.push(ncc);
      stage.append(makeVisual(items[0]), ncc, makeVisual(items[1]));
    }
    app.append(head, stage);

    await sleepFrame(); if (attempt.done) return;
    const readyAt = performance.now(); const ready = attempt.markReady(readyAt);
    if (ready.status === 'TIMEOUT') { terminal(ready); return; }
    for (const b of responseButtons) b.disabled = false;
    if (pair.positionInBlock === 1) scheduleDeadline(readyAt);
  };
  render().catch(showError);
  return run;
}

function showRetry(training, action, restart = false) {
  setCard(true);
  app.append(el('h2', '', training ? t('trainingTitle') : t('timeout')), el('p', '', training ? t('trainingText') : t('retryBlock')));
  const b = el('button', 'primary', restart ? t('restart') : t('retry')); b.onclick = action; app.append(b);
}
function startBlock(index) {
  const plan = state.blockPlans[index]; state.currentBlockId = crypto.randomUUID();
  const blockRun = { blockIndex: plan.blockIndex, formId: plan.formId, blockId: state.currentBlockId, messageId: crypto.randomUUID(), plan, attempts: [] };
  state.blockRuns[index] = blockRun; runBlockAttempt(index, 1);
}
function runBlockAttempt(index, n) {
  const blockRun = state.blockRuns[index]; const priorExposureCounts = {};
  for (const prior of blockRun.attempts) for (const e of prior.events) if (e.pairPresented) priorExposureCounts[e.pairId] = (priorExposureCounts[e.pairId] || 0) + 1;
  runRapid({
    plan: blockRun.plan, attemptNumber: n, isTraining: false, priorExposureCounts,
    onTerminal: async (_attempt, result, run) => {
      blockRun.attempts.push(run);
      if (result.status === 'TIMEOUT' && n < MAX_ATTEMPTS) { showRetry(false, () => runBlockAttempt(index, n + 1)); return; }
      try { if (state.mode === 'RESEARCH') await uploadBlock(blockRun); }
      catch { showUploadRetry(() => uploadBlock(blockRun).then(() => afterBlock(index))); return; }
      afterBlock(index);
    }
  });
}
function afterBlock(index) {
  if (index === 0) {
    setCard(true);
    app.append(el('h2', '', `${t('block')} 1 ${t('done')}`), el('p', '', t('continueNext')));
    const b = el('button', 'primary', t('continueNext')); b.onclick = () => startBlock(1); app.append(b);
  } else {
    setCard(true);
    app.append(el('h2', '', t('rapidDoneTitle')), el('p', '', t('rapidDoneText')));
    const b = el('button', 'primary', t('startReflection')); b.onclick = startReflection; app.append(b);
  }
}
async function uploadBlock(blockRun) {
  const attempts = blockRun.attempts.map(x => x.summary); const events = blockRun.attempts.flatMap(x => x.events);
  const result = await post({ ...commonPayload(), schema: '2pair.integrated.block.v0.1', messageId: blockRun.messageId, block: { blockId: blockRun.blockId, blockIndex: blockRun.blockIndex, formId: blockRun.formId, blockBudgetMs: BLOCK_BUDGET_MS, technicalPreloadOk: true, attempts, events } });
  state.uploadOk = true; return result;
}
function showUploadRetry(retry) {
  setCard(true); app.append(el('div', 'error', t('saveError')));
  const b = el('button', 'primary', t('retry')); b.style.marginTop = '14px';
  b.onclick = async () => { b.disabled = true; try { await retry(); } catch { b.disabled = false; } }; app.append(b);
}

function startReflection() {
  // Deliberately retains the current integrated protocol rule: primary-attempt anchors only.
  // Wave 1 sequencing / retry-anchor semantics remain a separate methodology decision.
  state.reflection = primaryAnchors(state.blockRuns);
  if (!state.reflection.length) { showTrace(); return; }
  showReflection(0);
}
function showReflection(index) {
  if (index >= state.reflection.length) { showTrace(); return; }
  const anchor = state.reflection[index]; if (!anchor.reflectionMessageId) anchor.reflectionMessageId = crypto.randomUUID();
  setCard();
  app.append(el('div', 'muted', `${index + 1} / ${state.reflection.length}`), el('h2', '', t('reflectionTitle')), el('p', '', anchor.choice === 'no_clear_choice' ? t('reflectionNcc') : t('reflectionPrompt')));
  const pics = el('div', 'reflection-pair');
  for (const which of ['A', 'B']) {
    const f = el('figure', anchor.choice === which ? 'chosen' : '');
    const im = el('img'); im.src = researchAsset(anchor.pairId, which); im.alt = ''; f.append(im); pics.append(f);
  }
  app.append(pics);
  const ta = el('textarea'); ta.placeholder = t('placeholder'); app.append(ta);
  const hard = el('button', 'secondary toggle', t('hard')); let hardOn = false;
  hard.onclick = () => { hardOn = !hardOn; hard.classList.toggle('active', hardOn); ta.disabled = hardOn; if (hardOn) ta.value = ''; };
  app.append(hard);
  let intensity = null;
  if (anchor.choice !== 'no_clear_choice') {
    app.append(el('p', 'muted', `${t('intensity')} · ${t('optional')}`));
    const scale = el('div', 'scale');
    for (let n = 1; n <= 5; n++) {
      const b = el('button', '', String(n));
      b.onclick = () => { intensity = n; for (const x of scale.children) x.classList.remove('active'); b.classList.add('active'); };
      scale.append(b);
    }
    app.append(scale);
    const labels = el('div', 'rapid-head'); labels.append(el('span', '', t('weak')), el('span', '', t('strong'))); app.append(labels);
  }
  const next = el('button', 'secondary next-action', t('saveNext')); next.style.marginTop = '16px';
  next.onclick = async () => {
    next.disabled = true; next.textContent = t('saving');
    const response = { pairId: anchor.pairId, anchorEventId: anchor.eventId, freeText: hardOn ? null : (ta.value.trim() || null), intensity: anchor.choice === 'no_clear_choice' ? null : intensity, hardToIdentify: hardOn };
    try {
      if (state.mode === 'RESEARCH') await post({ ...commonPayload(), schema: '2pair.integrated.reflection.v0.1', messageId: anchor.reflectionMessageId, ...response });
      showReflection(index + 1);
    } catch {
      next.disabled = false; next.textContent = t('saveNext');
      const old = app.querySelector('.error'); if (old) old.remove(); app.prepend(el('div', 'error', t('saveError')));
    }
  };
  app.append(next);
}

function showTrace() {
  const trace = localChoiceTrace(state.blockRuns); setCard();
  app.append(el('h2', '', t('traceTitle')), el('p', '', t('traceText')));
  const grid = el('div', 'trace');
  for (const e of trace) {
    const item = el('div', 'trace-item');
    if (e.choice === 'A' || e.choice === 'B') {
      const img = el('img'); img.src = researchAsset(e.pairId, e.choice); img.alt = ''; item.append(img);
    } else {
      item.classList.add('trace-no-clear'); item.append(el('div', 'trace-no-clear-text', t('noClear')));
    }
    grid.append(item);
  }
  app.append(grid);
  if (state.mode === 'RESEARCH' && state.deletionCode && state.uploadOk) {
    const box = el('div', 'card deletion-card'); box.style.marginTop = '16px';
    box.append(el('h2', '', t('codeTitle')), el('p', 'muted', t('codeHelp')));
    const code = el('code'); code.textContent = state.deletionCode; code.style.wordBreak = 'break-all'; box.append(code); app.append(box);
  }
  const restart = el('button', 'secondary quiet-action', t('restartSession')); restart.onclick = () => location.reload(); app.append(restart);
}
function showError(e) { console.error(e); setCard(); app.append(el('h2', '', t('technical')), el('div', 'error', String(e?.message || e))); }

showLanguage();
