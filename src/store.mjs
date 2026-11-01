import {mkdirSync,readFileSync,writeFileSync,renameSync,existsSync} from 'node:fs';
import {join} from 'node:path';
import {randomBytes} from 'node:crypto';
import {fresh,assertState} from './engine.mjs';
export function atomic(file,value){writeFileSync(file+'.tmp',JSON.stringify(value,null,2),{mode:0o600});renameSync(file+'.tmp',file);}
export function openStore(dir,mode){mkdirSync(dir,{recursive:true,mode:0o700});const file=join(dir,'state.json');let state=existsSync(file)?assertState(JSON.parse(readFileSync(file,'utf8'))):fresh(mode);if(state.mode!==mode)throw new Error(`Stored session is ${state.mode}. Use another DATA_DIR for ${mode} mode.`);if(state.phase==='playing')state.run.paused=true;atomic(file,state);return {get:()=>state,commit(next){assertState(next);atomic(file,next);state=next;}};}
export function secret(dir,name,override){const file=join(dir,name);if(override){if(override.length<24)throw new Error(`${name} must be at least 24 characters`);return override;}if(!existsSync(file))writeFileSync(file,randomBytes(32).toString('hex'),{mode:0o600});return readFileSync(file,'utf8').trim();}
