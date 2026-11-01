import {readFileSync} from 'node:fs';
import {resolve} from 'node:path';
try{console.log(process.env.ADMIN_KEY||readFileSync(resolve(process.env.DATA_DIR||'.data','admin-key'),'utf8'));}catch{console.error('Start the app first, then run npm run key. For a custom DATA_DIR load the same .env settings.');process.exitCode=1;}
