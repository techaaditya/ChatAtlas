import http from 'node:http';
import {readFileSync,existsSync} from 'node:fs';
import {resolve,dirname,join} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {timingSafeEqual,randomBytes,randomUUID} from 'node:crypto';
import {openStore,secret} from './store.mjs';
import {fresh,view,contribute,clusters,recipe,approve,start,step,revise,validateBlueprint,CATALOG,SCENARIOS,AppError,log,text,THEMES,renameTheme,mergeThemes,moveIdea} from './engine.mjs';
import {propose,semanticThemes} from './intelligence.mjs';
import {TwitchConnection} from './twitch.mjs';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const equal=(a,b)=>typeof a==='string'&&typeof b==='string'&&Buffer.byteLength(a)===Buffer.byteLength(b)&&timingSafeEqual(Buffer.from(a),Buffer.from(b));
export function createApp({env=process.env,mode='demo'}={}){
 const dir=resolve(env.DATA_DIR||join(root,'.data'));const store=openStore(dir,mode);const key=secret(dir,'admin-key',env.ADMIN_KEY);let readKey=secret(dir,'overlay-key');const port=Number(env.PORT||3000),base=env.PUBLIC_URL||`http://localhost:${port}`;const allowedHosts=new Set([new URL(base).host,`localhost:${port}`,`127.0.0.1:${port}`]);const clients=new Set();const pendingOAuth=new Map();let twitchStatus='Disconnected',aiStatus='Local rules';let busy=false;
 const broadcast=()=>{const data=JSON.stringify({...view(store.get()),twitchStatus,aiStatus});for(const res of clients){if(res.writableLength>1000000){res.end();clients.delete(res);}else res.write(`data: ${data}\n\n`);}};
 const mutate=fn=>{const next=structuredClone(store.get());const result=fn(next);next.revision++;store.commit(next);broadcast();return result;};
 const gap=()=>{if(store.get().phase==='playing')mutate(s=>{s.run.paused=true;log(s,'Twitch disconnected. Storm paused; missed chat cannot be replayed.');});};
 const receive=event=>{if(!/^!(idea |boost |act |credit (on|off)$|forget$)/.test(event.message))return;try{mutate(s=>contribute(s,event));}catch{mutate(s=>s.metrics.rejected++);}};
 const twitch=new TwitchConnection({env:{...env,TWITCH_REDIRECT_URI:env.TWITCH_REDIRECT_URI||base+'/auth/twitch/callback'},dir,onMessage:receive,onStatus:status=>{twitchStatus=status;broadcast();},onGap:gap});
 function json(res,status,data){res.writeHead(status,{'Content-Type':'application/json'});res.end(JSON.stringify(data));}
 async function body(req){let raw='';for await(const chunk of req){raw+=chunk;if(Buffer.byteLength(raw)>16384)throw new AppError('Request too large',413);}try{return JSON.parse(raw||'{}');}catch{throw new AppError('Invalid JSON');}}
 const server=http.createServer(async(req,res)=>{res.setHeader('Cache-Control','no-store');res.setHeader('X-Content-Type-Options','nosniff');res.setHeader('Referrer-Policy','no-referrer');res.setHeader('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'");try{
  const listeningPort=server.address()?.port;const validHost=host=>allowedHosts.has(host)||host===`localhost:${listeningPort}`||host===`127.0.0.1:${listeningPort}`;
  if(!validHost(req.headers.host))throw new AppError('Unexpected Host header',403);
  const url=new URL(req.url,base);const token=req.headers.authorization?.replace(/^Bearer /,'');const admin=equal(token,key);const reader=admin||equal(token,readKey);
  if(req.method!=='GET'&&req.headers.origin&&!validHost(new URL(req.headers.origin).host))throw new AppError('Cross-origin control request refused',403);
  if(url.pathname==='/health')return json(res,200,{ok:true,app:'ChatAtlas Foundry'});
  if(url.pathname==='/auth/twitch/callback'){
   const nonce=url.searchParams.get('state'),expiry=pendingOAuth.get(nonce);pendingOAuth.delete(nonce);if(!expiry||expiry<Date.now())throw new AppError('OAuth state expired or invalid',403);if(url.searchParams.has('error'))throw new AppError('Twitch authorization declined');await twitch.exchange(text(url.searchParams.get('code'),1000));await twitch.start();res.writeHead(303,{Location:'/'});return res.end();
  }
  if(url.pathname.startsWith('/api/')||url.pathname==='/events'){
   if(!reader)throw new AppError('Enter your control key to continue',401);
   if(req.method==='GET'&&url.pathname==='/api/state')return json(res,200,{...view(store.get(),{admin}),twitchStatus,aiStatus});
   if(req.method==='GET'&&url.pathname==='/events'){if(clients.size>=100)throw new AppError('Overlay connection limit',429);res.writeHead(200,{'Content-Type':'text/event-stream','Connection':'keep-alive','X-Accel-Buffering':'no'});clients.add(res);res.write(`data: ${JSON.stringify({...view(store.get()),twitchStatus,aiStatus})}\n\n`);req.on('close',()=>clients.delete(res));return;}
   if(!admin)throw new AppError('Read-only overlay access',403);
   if(req.method==='GET'&&url.pathname==='/api/settings')return json(res,200,{catalog:CATALOG,overlayUrl:base+'/overlay#'+readKey,aiAvailable:!!env.OPENAI_API_KEY,modelConfigured:!!env.OPENAI_MODEL,mode,version:'1.0.0'});
   if(req.method==='GET'&&url.pathname==='/api/export'){res.setHeader('Content-Disposition','attachment; filename="chatatlas-artifact.json"');return json(res,200,{...view(store.get()),exportedAt:new Date().toISOString()});}
   if(req.method!=='POST')throw new AppError('Unknown endpoint',404);const b=await body(req);let result;
   switch(url.pathname){
    case '/api/demo/seed':if(mode!=='demo')throw new AppError('Fixture input is disabled in live mode',403);result=mutate(s=>{if(s.phase!=='collecting')throw new AppError('Open a revision first');for(const e of JSON.parse(readFileSync(join(root,'fixtures/ideas.json'))))contribute(s,{...e,id:'seed-'+s.id+'-'+e.userId,source:'demo'});log(s,'Loaded labeled demo contributions.');});break;
    case '/api/demo/message':if(mode!=='demo')throw new AppError('Synthetic input disabled in live mode',403);result=mutate(s=>contribute(s,{id:randomUUID(),userId:text(b.userId||'demo-host',100),name:text(b.name||'Demo viewer',40),message:text(b.message,300),source:'demo'}));break;
    case '/api/prompt':result=mutate(s=>{if(s.phase!=='collecting')throw new AppError('Open a revision first');s.prompt=text(b.prompt,200);});break;
    case '/api/draft':{const snapshot=structuredClone(store.get());if(snapshot.phase!=='collecting')throw new AppError('Open a revision first');if(b.ai){if(busy)throw new AppError('An intelligence request is already running',409);busy=true;}try{const draft=b.ai?await propose(snapshot,b.clusterId,env):{blueprint:recipe(snapshot,b.clusterId),method:'Local recipe'};if(snapshot.id!==store.get().id||snapshot.revision!==store.get().revision)throw new AppError('Ideas changed while drafting. Try again.',409);result=mutate(s=>{s.draft=draft.blueprint;log(s,draft.method);});aiStatus=draft.method;broadcast();}finally{if(b.ai)busy=false;}break;}
    case '/api/semantic':{if(busy)throw new AppError('An intelligence request is already running',409);if(store.get().phase!=='collecting')throw new AppError('Open a revision first');busy=true;try{const snapshot=structuredClone(store.get()),assignments=await semanticThemes(snapshot,env);if(snapshot.id!==store.get().id||snapshot.revision!==store.get().revision)throw new AppError('Ideas changed while grouping. Try again.',409);mutate(s=>{for(const a of assignments)s.ideas.find(i=>i.id===a.id).theme=a.theme;s.intelligence='Semantic themes';});aiStatus='Semantic themes · embeddings';broadcast();}finally{busy=false;}break;}
    case '/api/approve':result=mutate(s=>approve(s,b.blueprint));break;
    case '/api/start':result=mutate(s=>start(s,42));break;
    case '/api/pause':result=mutate(s=>{if(s.phase!=='playing')throw new AppError('No active storm');s.run.paused=!s.run.paused;});break;
    case '/api/step':result=mutate(s=>step(s));break;
    case '/api/revise':result=mutate(revise);break;
    case '/api/restore':result=mutate(s=>{if(s.phase==='playing')throw new AppError('Finish the storm first');const h=s.history.find(h=>h.id===b.id);if(!h)throw new AppError('Unknown version');s.draft=validateBlueprint(h.blueprint,s);s.phase='collecting';});break;
    case '/api/scenario':result=mutate(s=>{if(s.phase!=='collecting')throw new AppError('Open a revision first');if(!SCENARIOS[b.scenario])throw new AppError('Unknown scenario');s.scenario=b.scenario;s.prompt=SCENARIOS[b.scenario].prompt;log(s,`Switched challenge to ${SCENARIOS[b.scenario].name}`);});break;
    case '/api/theme/rename':result=mutate(s=>renameTheme(s,b.themeId,b.label));break;
    case '/api/theme/merge':result=mutate(s=>mergeThemes(s,b.from,b.to));break;
    case '/api/move':result=mutate(s=>moveIdea(s,b.id,b.theme));break;
    case '/api/remove':result=mutate(s=>{if(s.phase==='playing')throw new AppError('Finish the storm first');s.ideas=s.ideas.filter(i=>i.id!==b.id);delete s.overrides[b.id];s.draft=null;for(const h of s.history)h.blueprint.sourceIds=h.blueprint.sourceIds.filter(id=>id!==b.id);});break;
    case '/api/reset':if(b.confirm!=='RESET')throw new AppError('Type RESET to clear the session');mutate(s=>Object.assign(s,fresh(mode)));break;
    case '/api/twitch/auth':if(mode!=='twitch')throw new AppError('Start without --demo for live Twitch');if(!env.TWITCH_CLIENT_ID||!env.TWITCH_CLIENT_SECRET)throw new AppError('Configure Twitch client ID and secret');{const nonce=randomBytes(24).toString('hex');pendingOAuth.clear();pendingOAuth.set(nonce,Date.now()+600000);result={url:'https://id.twitch.tv/oauth2/authorize?'+new URLSearchParams({client_id:env.TWITCH_CLIENT_ID,redirect_uri:env.TWITCH_REDIRECT_URI||base+'/auth/twitch/callback',response_type:'code',scope:'user:read:chat',state:nonce})};}break;
    case '/api/twitch/connect':if(mode!=='twitch')throw new AppError('Live connection disabled in demo');await twitch.start();result={connected:true};break;
    case '/api/twitch/disconnect':twitch.stop();gap();twitchStatus='Disconnected';broadcast();break;
    default:throw new AppError('Unknown endpoint',404);
   }return json(res,200,{ok:true,...(result||{})});
  }
  if(req.method!=='GET')throw new AppError('Method not allowed',405);
  const assets={'/':'index.html','/overlay':'index.html','/app.js':'app.js','/styles.css':'styles.css','/icon.svg':'icon.svg'};const file=assets[url.pathname];if(!file)throw new AppError('Not found',404);res.writeHead(200,{'Content-Type':file.endsWith('.html')?'text/html; charset=utf-8':file.endsWith('.js')?'text/javascript; charset=utf-8':file.endsWith('.svg')?'image/svg+xml':'text/css; charset=utf-8'});res.end(readFileSync(join(root,'public',file)));
 }catch(error){if(!res.headersSent)json(res,error.status||500,{error:error.status?error.message:'Server operation failed; inspect local configuration and disk permissions.'});else res.end();}});
 const timer=setInterval(()=>{if(store.get().phase==='playing'&&!store.get().run.paused)try{mutate(step);}catch{twitchStatus='Storage error — storm halted';store.get().run.paused=true;broadcast();}},2000);
 const keepalive=setInterval(()=>{for(const res of clients)res.write(': heartbeat\n\n');},15000);
 return {server,store,key,get readKey(){return readKey;},close(){clearInterval(timer);clearInterval(keepalive);twitch.stop();for(const res of clients)res.end();server.close();}};
}
if(process.argv[1]&&import.meta.url===pathToFileURL(resolve(process.argv[1])).href){const mode=process.argv.includes('--demo')?'demo':'twitch';const app=createApp({mode});app.server.listen(Number(process.env.PORT||3000),process.env.HOST||'127.0.0.1',()=>{console.log(`ChatAtlas Foundry · ${mode.toUpperCase()}\nOpen ${process.env.PUBLIC_URL||'http://localhost:'+(process.env.PORT||3000)}\nControl key: run npm run key in this folder.\nDo not share .env or .data. Live Twitch must be authorized in the dashboard.`);});for(const signal of ['SIGINT','SIGTERM'])process.on(signal,()=>{app.close();setTimeout(()=>process.exit(),200).unref();});}
