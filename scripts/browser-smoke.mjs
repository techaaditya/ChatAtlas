// Optional QA dependency, not required to run the app.
// Install locally: npm install --no-save --package-lock=false playwright
// Then: npx playwright install chromium
// Run against a FRESH running demo: node --env-file-if-exists=.env scripts/browser-smoke.mjs
import {readFileSync,existsSync} from 'node:fs';
import {resolve} from 'node:path';
import assert from 'node:assert/strict';
const {chromium}=await import(process.env.PLAYWRIGHT_MODULE||'playwright');
const base=process.env.PUBLIC_URL||'http://localhost:3000';
const key=process.env.ADMIN_KEY||readFileSync(resolve(process.env.DATA_DIR||'.data','admin-key'),'utf8').trim();
const chromePath=process.env.CHROME_BIN||(process.platform==='win32'&&existsSync('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')?'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe':undefined);
const browser=await chromium.launch({headless:true,...(chromePath?{executablePath:chromePath}:{})});
try{
 const page=await browser.newPage({viewport:{width:1440,height:1100}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 const post=async(path,data={})=>{const r=await page.request.post(base+path,{headers:{Authorization:'Bearer '+key},data});assert.ok(r.ok(),await r.text());};
 await page.goto(base);await page.locator('#key').fill(key);await page.getByRole('button',{name:'Enter the Foundry'}).click();await page.locator('#app').waitFor({state:'visible'});
 await page.locator('#seed').click();await page.locator('[data-cluster="energy"]').click();await page.locator('#approve').click();await page.locator('#start').click();
 for(let i=0;i<18;i++)await post('/api/step');
 await page.getByRole('heading',{name:'A failure worth learning from'}).waitFor();
 await page.locator('#revise').click();
 await page.locator('#scenario-frost').click();
 await page.locator('[data-cluster="grounding"]').click();
 assert.ok(await page.locator('.module-sources').count() > 0);
 await page.locator('#approve').click();
 await page.locator('#start').click();
 for(let i=0;i<18;i++)await post('/api/step');
 await page.getByRole('heading',{name:'A city made stronger, together'}).waitFor();
 const settings=await(await page.request.get(base+'/api/settings',{headers:{Authorization:'Bearer '+key}})).json();
 const stage=await browser.newPage();await stage.goto(settings.overlayUrl);await stage.locator('#app').waitFor({state:'visible'});assert.equal(await stage.locator('.ideas-panel').isVisible(),false);
 await page.setViewportSize({width:390,height:844});assert.equal(await page.locator('#app').isVisible(),true);
 assert.deepEqual(errors,[]);console.log('Browser interaction smoke test passed. Inspect layout and accessibility manually too.');
}finally{await browser.close();}
