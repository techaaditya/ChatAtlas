import test from 'node:test';import assert from 'node:assert/strict';import {mkdtempSync,rmSync} from 'node:fs';import {tmpdir} from 'node:os';import {join} from 'node:path';import {once} from 'node:events';import {createApp} from '../src/server.mjs';import {openStore} from '../src/store.mjs';
test('HTTP product journey, privilege boundaries, and persistence',async()=>{const dir=mkdtempSync(join(tmpdir(),'chatatlas-'));const key='a'.repeat(64),app=createApp({env:{DATA_DIR:dir,PORT:'3000',ADMIN_KEY:key},mode:'demo'});app.server.listen(0,'127.0.0.1');await once(app.server,'listening');const base='http://127.0.0.1:'+app.server.address().port;const call=(path,body,token=key,extra={})=>fetch(base+path,{method:body===undefined?'GET':'POST',headers:{Host:'localhost:3000',Authorization:'Bearer '+token,...(body===undefined?{}:{'Content-Type':'application/json'}),...extra},body:body===undefined?undefined:JSON.stringify(body)});try{
 assert.equal((await call('/api/state',undefined,'wrong')).status,401);
 assert.equal((await call('/api/state',undefined,'é'.repeat(64))).status,401);
 assert.equal((await call('/api/demo/seed',{},key,{Origin:'https://attacker.example'})).status,403);
 assert.equal((await call('/api/demo/seed',{},app.readKey)).status,403);
 assert.equal((await call('/api/demo/seed',{})).status,200);
 let s=await(await call('/api/state')).json();assert.equal(s.ideas.length,8);assert.equal(s.contributors,8);
 assert.equal((await call('/api/theme/rename',{themeId:'energy',label:'Storm Harvesters'})).status,200);
 assert.equal((await call('/api/theme/merge',{from:'storage',to:'energy'})).status,200);
 s=await(await call('/api/state')).json();assert.equal(s.clusters.find(c=>c.id==='energy').label,'Storm Harvesters');
 await call('/api/draft',{clusterId:'energy'});s=await(await call('/api/state')).json();assert.equal(s.draft.modules[0],'collector');
 const revision=s.revision;assert.equal((await call('/api/approve',{blueprint:{...s.draft,modules:['code']}})).status,400);s=await(await call('/api/state')).json();assert.equal(s.revision,revision);
 await call('/api/approve',{blueprint:s.draft});await call('/api/start',{});for(let i=0;i<18;i++)await call('/api/step',{});s=await(await call('/api/state')).json();assert.equal(s.run.result,'overloaded');
 await call('/api/revise',{});await call('/api/draft',{clusterId:'grounding'});s=await(await call('/api/state')).json();await call('/api/approve',{blueprint:s.draft});await call('/api/start',{});for(let i=0;i<18;i++)await call('/api/step',{});s=await(await call('/api/export')).json();assert.equal(s.run.result,'survived');assert.equal(s.history.length,2);assert.equal(s.receipts,undefined);
 const restored=openStore(dir,'demo').get();assert.equal(restored.run.result,'survived');assert.throws(()=>openStore(dir,'twitch'),/Stored session/);
 const res=await call('/events',undefined,app.readKey);assert.equal(res.status,200);const reader=res.body.getReader();const first=await reader.read();assert.match(new TextDecoder().decode(first.value),/data: /);await reader.cancel();
 assert.equal((await call('/api/twitch/auth',{})).status,400);
 }finally{app.close();app.server.closeAllConnections();rmSync(dir,{recursive:true,force:true});}});
