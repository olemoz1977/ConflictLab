import test from 'node:test';
import assert from 'node:assert/strict';
import {createBlockPlan,createFormOrder,createIntegratedPlans,RapidAttempt,primaryAnchors,localChoiceTrace,BLOCK_BUDGET_MS} from '../integrated_core.mjs';

const seq=(...values)=>{let i=0;return()=>values[i++%values.length]};
const uuid=(()=>{let i=0;return()=>`00000000-0000-4000-8000-${String(++i).padStart(12,'0')}`})();

test('forms are complementary',()=>{
  const order=createFormOrder(()=>0.1); assert.deepEqual(order,['F2-A','F2-B']);
  const a=createBlockPlan(order[0],1,seq(.1,.2,.3,.4,.5,.6,.7));
  const b=createBlockPlan(order[1],2,seq(.1,.2,.3,.4,.5,.6,.7));
  assert.equal(new Set([...a.pairs,...b.pairs].map(p=>p.pairId)).size,6);
  assert.deepEqual(a.pairs.map(p=>p.sessionPresentationIndex).sort(),[1,2,3]);
  assert.deepEqual(b.pairs.map(p=>p.sessionPresentationIndex).sort(),[4,5,6]);
});

test('integrated plans balance A top count across both blocks',()=>{
  const plans=createIntegratedPlans(seq(.1,.2,.3,.4,.5,.6,.7,.8,.9,.11,.22,.33,.44,.55,.66,.77));
  assert.equal(plans.length,2);
  assert.equal(plans[0].pairs.filter(p=>p.aPosition==='top').length + plans[1].pairs.filter(p=>p.aPosition==='top').length,3);
});

test('rapid attempt records actual tap latency and no_clear_choice',()=>{
  const plan=createBlockPlan('F2-A',1,seq(.1,.2,.3,.4,.5,.6));
  let now=1000; const a=new RapidAttempt({sessionId:uuid(),blockId:uuid(),blockIndex:1,formId:'F2-A',attemptNumber:1,pairs:plan.pairs,now:()=>now,uuid});
  a.markReady(now); now+=500; let r=a.recordChoice('A',now); assert.equal(r.event.visualChoiceLatencyMs,500);
  now+=50; a.markReady(now); now+=700; r=a.recordChoice('no_clear_choice',now); assert.equal(r.event.choice,'no_clear_choice'); assert.equal(r.event.visualChoiceLatencyMs,700);
  now+=50; a.markReady(now); now+=800; r=a.recordChoice('B',now); assert.equal(r.status,'COMPLETE');
  assert.equal(a.summary().blockTimedOut,false);
});

test('retry exposure number counts only prior presented exposures',()=>{
  const plan=createBlockPlan('F2-A',1,seq(.1,.2,.3,.4,.5,.6));
  let now=0;const primary=new RapidAttempt({sessionId:uuid(),blockId:uuid(),blockIndex:1,formId:'F2-A',attemptNumber:1,pairs:plan.pairs,now:()=>now,uuid});
  primary.markReady(0);now=100;primary.recordChoice('A',now);now=200;primary.markReady(now);now=BLOCK_BUDGET_MS;primary.expire(now);
  const counts={};for(const e of primary.events)if(e.pairPresented)counts[e.pairId]=(counts[e.pairId]||0)+1;
  let t=10000;const retry=new RapidAttempt({sessionId:primary.sessionId,blockId:primary.blockId,blockIndex:1,formId:'F2-A',attemptNumber:2,pairs:plan.pairs,priorExposureCounts:counts,now:()=>t,uuid});
  const ready1=retry.markReady(t);assert.equal(ready1.pairExposureNumber,2);t+=100;retry.recordChoice('A',t);t+=10;const ready2=retry.markReady(t);assert.equal(ready2.pairExposureNumber,2);t+=100;retry.recordChoice('A',t);t+=10;const ready3=retry.markReady(t);assert.equal(ready3.pairExposureNumber,1);
});

test('timeout produces three logical events and retry is not a primary Wave1 anchor',()=>{
  const plan=createBlockPlan('F2-B',1,seq(.1,.2,.3,.4,.5,.6));
  let now=0; const primary=new RapidAttempt({sessionId:uuid(),blockId:uuid(),blockIndex:1,formId:'F2-B',attemptNumber:1,pairs:plan.pairs,now:()=>now,uuid});
  primary.markReady(0); now=BLOCK_BUDGET_MS; primary.expire(now); assert.equal(primary.events.length,3);
  let t=10_000; const retry=new RapidAttempt({sessionId:primary.sessionId,blockId:primary.blockId,blockIndex:1,formId:'F2-B',attemptNumber:2,pairs:plan.pairs,now:()=>t,uuid});
  for(let i=0;i<3;i++){retry.markReady(t);t+=100;retry.recordChoice('A',t);t+=10;}
  const runs=[{attempts:[{attemptNumber:1,events:primary.events},{attemptNumber:2,events:retry.events}]}];
  assert.equal(primaryAnchors(runs).length,0);
  assert.equal(localChoiceTrace(runs).length,3);
});
