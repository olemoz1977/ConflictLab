export const PROTOCOL_VERSION = '2pair-integrated-v0.1';
export const STIMULUS_SET_VERSION = 'stimulus-set-v1';
export const TRAINING_SET_VERSION = 'training-set-v1';
export const BLOCK_BUDGET_MS = 6000;
export const MAX_ATTEMPTS = 3;

export const RESEARCH_PAIRS = Object.freeze({
  'CS-PR-01': { aId:'CS-PR-01-A', bId:'CS-PR-01-B', aFile:'more-reveal.webp', bFile:'less-reveal.jpg' },
  'CS-RE-01': { aId:'CS-RE-01-A', bId:'CS-RE-01-B', aFile:'more-evidence.png', bFile:'less-evidence.png' },
  'CS-CA-01': { aId:'CS-CA-01-A', bId:'CS-CA-01-B', aFile:'more-reference.png', bFile:'less-reference.png' },
  'CR-PZ-01': { aId:'CR-PZ-01-A', bId:'CR-PZ-01-B', aFile:'no-predefined-zones.png', bFile:'predefined-zones.png' },
  'CR-FS-01': { aId:'CR-FS-01-A', bId:'CR-FS-01-B', aFile:'fixed-slots.png', bFile:'continuous-capacity.png' },
  'CR-PO-01': { aId:'CR-PO-01-A', bId:'CR-PO-01-B', aFile:'partitioned-space.png', bFile:'open-space.png' },
});

export const FORMS = Object.freeze({
  'F2-A': ['CS-CA-01','CR-PZ-01','CR-PO-01'],
  'F2-B': ['CS-PR-01','CS-RE-01','CR-FS-01'],
});

export const TRAINING_PAIRS = Object.freeze([
  { pairId:'P0-001', aId:'P0-001-A', bId:'P0-001-B', aFile:'p0-001-a.png', bFile:'p0-001-b.png' },
  { pairId:'P0-002', aId:'P0-002-A', bId:'P0-002-B', aFile:'p0-002-a.png', bFile:'p0-002-b.png' },
  { pairId:'P0-003', aId:'P0-003-A', bId:'P0-003-B', aFile:'p0-003-a.png', bFile:'p0-003-b.png' },
]);

function assert(cond, message){ if(!cond) throw new Error(message); }
export function shuffled(values, rng=Math.random){
  const out=[...values];
  for(let i=out.length-1;i>0;i--){
    const r=rng(); assert(Number.isFinite(r)&&r>=0&&r<1,'rng must return [0,1)');
    const j=Math.floor(r*(i+1)); [out[i],out[j]]=[out[j],out[i]];
  }
  return out;
}

export function createFormOrder(rng=Math.random){
  const first = rng() < 0.5 ? 'F2-A' : 'F2-B';
  return first === 'F2-A' ? ['F2-A','F2-B'] : ['F2-B','F2-A'];
}

export function createBlockPlan(formId, blockIndex, rng=Math.random, forcedATopCount=null){
  assert(FORMS[formId], 'unknown form');
  assert(blockIndex===1||blockIndex===2,'blockIndex must be 1 or 2');
  const pairIds=shuffled(FORMS[formId], rng);
  const aTopCount=forcedATopCount===1||forcedATopCount===2?forcedATopCount:(rng()<0.5?1:2);
  const aTopPositions=new Set(shuffled([0,1,2],rng).slice(0,aTopCount));
  return {
    blockIndex, formId, blockBudgetMs:BLOCK_BUDGET_MS,
    pairs:pairIds.map((pairId,index)=>{
      const source=RESEARCH_PAIRS[pairId];
      const aTop=aTopPositions.has(index);
      return {pairId,...source,aPosition:aTop?'top':'bottom',bPosition:aTop?'bottom':'top',positionInBlock:index+1,sessionPresentationIndex:(blockIndex-1)*3+index+1};
    })
  };
}

export function createIntegratedPlans(rng=Math.random){
  const order=createFormOrder(rng);
  const firstATopCount=rng()<0.5?1:2;
  const secondATopCount=3-firstATopCount;
  return [
    createBlockPlan(order[0],1,rng,firstATopCount),
    createBlockPlan(order[1],2,rng,secondATopCount),
  ];
}

export function createTrainingPlan(rng=Math.random){
  const pairs=shuffled(TRAINING_PAIRS,rng);
  const aTopCount=rng()<0.5?1:2;
  const aTopPositions=new Set(shuffled([0,1,2],rng).slice(0,aTopCount));
  return {blockBudgetMs:BLOCK_BUDGET_MS,pairs:pairs.map((p,index)=>({
    ...p,aPosition:aTopPositions.has(index)?'top':'bottom',bPosition:aTopPositions.has(index)?'bottom':'top',positionInBlock:index+1
  }))};
}

export class RapidAttempt {
  constructor({sessionId,blockId,blockIndex,formId,attemptNumber,pairs,priorExposureCounts={},now=()=>performance.now(),uuid=()=>crypto.randomUUID(),allowNoClear=true,isTraining=false}){
    assert(typeof sessionId==='string'&&sessionId,'sessionId required');
    assert(typeof blockId==='string'&&blockId,'blockId required');
    assert(attemptNumber>=1&&attemptNumber<=MAX_ATTEMPTS,'bad attemptNumber');
    assert(Array.isArray(pairs)&&pairs.length===3,'three pairs required');
    this.sessionId=sessionId; this.blockId=blockId; this.blockIndex=blockIndex; this.formId=formId;
    this.attemptNumber=attemptNumber; this.pairs=pairs.map(p=>({...p})); this.now=now; this.uuid=uuid;
    this.allowNoClear=allowNoClear; this.isTraining=isTraining; this.startMs=null; this.currentReadyMs=null; this.currentExposureNumber=null; this.exposureCounts={...priorExposureCounts}; this.currentIndex=0;
    this.events=[]; this.done=false; this.timedOut=false; this.pageHidden=false; this.finalElapsedMs=null;
  }
  currentPair(){return this.done?null:this.pairs[this.currentIndex];}
  markPageHidden(){this.pageHidden=true;}
  markReady(at=this.now()){
    assert(!this.done,'attempt done'); assert(this.currentReadyMs===null,'already ready');
    if(this.startMs===null)this.startMs=at;
    if(at-this.startMs>=BLOCK_BUDGET_MS)return this.expire(at);
    this.currentReadyMs=at;
    const pair=this.currentPair();
    this.currentExposureNumber=(this.exposureCounts[pair.pairId]||0)+1;
    this.exposureCounts[pair.pairId]=this.currentExposureNumber;
    return {status:'READY',pairExposureNumber:this.currentExposureNumber,remainingBudgetMs:Math.max(0,Math.floor(BLOCK_BUDGET_MS-(at-this.startMs)))};
  }
  recordChoice(choice,at=this.now()){
    assert(!this.done,'attempt done'); assert(this.currentReadyMs!==null,'pair not ready');
    const valid=this.allowNoClear?['A','B','no_clear_choice']:['A','B']; assert(valid.includes(choice),'invalid choice');
    if(at-this.startMs>=BLOCK_BUDGET_MS)return this.expire(at);
    const pair=this.currentPair();
    const event=this.#event(pair,choice,true,this.currentExposureNumber,Math.floor(at-this.currentReadyMs),Math.floor(this.currentReadyMs-this.startMs),Math.floor(at-this.startMs));
    this.events.push(event); this.currentIndex++; this.currentReadyMs=null; this.currentExposureNumber=null;
    if(this.currentIndex===3){this.done=true;this.finalElapsedMs=Math.floor(at-this.startMs);return{status:'COMPLETE',event};}
    return{status:'CHOICE_RECORDED',event};
  }
  expire(at=this.now()){
    assert(!this.done,'attempt done'); assert(this.startMs!==null,'not started'); assert(at-this.startMs>=BLOCK_BUDGET_MS,'too early');
    for(let i=this.currentIndex;i<3;i++){
      const pair=this.pairs[i]; const presented=(i===this.currentIndex&&this.currentReadyMs!==null);
      const readyElapsed=presented?Math.floor(this.currentReadyMs-this.startMs):null;
      this.events.push(this.#event(pair,'timeout',presented,presented?this.currentExposureNumber:null,null,readyElapsed,BLOCK_BUDGET_MS));
    }
    this.done=true;this.timedOut=true;this.finalElapsedMs=BLOCK_BUDGET_MS;this.currentReadyMs=null;this.currentExposureNumber=null;
    return{status:'TIMEOUT',next:this.attemptNumber<MAX_ATTEMPTS?'RETRY':'TERMINAL'};
  }
  summary(){assert(this.done,'attempt not done');return{
    blockAttemptId:this.attemptId,blockAttemptNumber:this.attemptNumber,blockBudgetMs:BLOCK_BUDGET_MS,blockElapsedMsFinal:this.finalElapsedMs,
    blockTimedOut:this.timedOut,pageHiddenDuringBlock:this.pageHidden,isTraining:this.isTraining,protocolVersion:PROTOCOL_VERSION,stimulusSetVersion:STIMULUS_SET_VERSION
  };}
  get attemptId(){if(!this._attemptId)this._attemptId=this.uuid();return this._attemptId;}
  #event(pair,choice,presented,exposureNumber,latency,readyElapsed,eventElapsed){
    const remaining=presented&&readyElapsed!==null?Math.max(0,BLOCK_BUDGET_MS-readyElapsed):null;
    return {eventId:this.uuid(),sessionId:this.sessionId,blockId:this.blockId,blockIndex:this.blockIndex,formId:this.formId,blockAttemptId:this.attemptId,
      blockAttemptNumber:this.attemptNumber,pairId:pair.pairId,positionInBlock:pair.positionInBlock,sessionPresentationIndex:pair.sessionPresentationIndex??null,
      assetAId:pair.aId,assetBId:pair.bId,assetAPosition:pair.aPosition,assetBPosition:pair.bPosition,pairPresented:presented,pairExposureNumber:exposureNumber,
      pairReadyElapsedMs:readyElapsed,choice,visualChoiceLatencyMs:latency,blockElapsedMsAtEvent:eventElapsed,remainingBudgetAtPairStartMs:remaining,
      pageHiddenBeforeEvent:this.pageHidden,isTraining:this.isTraining,protocolVersion:PROTOCOL_VERSION,stimulusSetVersion:STIMULUS_SET_VERSION};
  }
}

export function primaryAnchors(blockRuns){
  const out=[];
  for(const block of blockRuns){
    const primary=block.attempts.find(a=>a.attemptNumber===1);
    if(!primary)continue;
    for(const e of primary.events){
      if(e.choice==='A'||e.choice==='B'||e.choice==='no_clear_choice') out.push({...e,anchorSource:'PRIMARY'});
    }
  }
  return out.sort((a,b)=>(a.sessionPresentationIndex??999)-(b.sessionPresentationIndex??999));
}

export function localChoiceTrace(blockRuns){
  const byPair=new Map();
  for(const block of blockRuns){
    for(const attempt of block.attempts){
      for(const e of attempt.events){
        if(byPair.has(e.pairId))continue;
        if(e.choice==='A'||e.choice==='B'||e.choice==='no_clear_choice') byPair.set(e.pairId,{...e,anchorSource:attempt.attemptNumber===1?'PRIMARY':'RETRY'});
      }
    }
  }
  return [...byPair.values()].sort((a,b)=>(a.sessionPresentationIndex??999)-(b.sessionPresentationIndex??999));
}
