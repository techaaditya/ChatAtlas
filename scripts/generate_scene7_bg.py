import os
from playwright.sync_api import sync_playwright

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,300..600&family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  body {
    margin: 0;
    width: 1920px;
    height: 1080px;
    background-color: #0E1410;
    background-image: 
      radial-gradient(ellipse 90% 60% at 70% -10%, #1f2b21 0%, transparent 70%),
      radial-gradient(circle at 10% 90%, #162018 0%, transparent 60%);
    color: #F7F2EB;
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    padding: 60px 100px;
  }
  .eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    letter-spacing: 3px;
    color: #8B9A6E;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 12px;
  }
  h1 {
    font-family: 'Fraunces', Georgia, serif;
    font-size: 56px;
    margin: 0 0 20px 0;
    letter-spacing: -0.02em;
    text-align: center;
    font-weight: 500;
  }
  h1 em {
    color: #C1D39E;
    font-style: italic;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    width: 100%;
    max-width: 1400px;
    margin-top: 20px;
  }
  .card {
    background: rgba(26, 36, 28, 0.85);
    border: 1px solid #2C3A2F;
    border-radius: 14px;
    padding: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  }
  .card h3 {
    margin: 0 0 8px 0;
    font-size: 17px;
    color: #F7F2EB;
    font-weight: 600;
  }
  .card p {
    margin: 0;
    font-size: 13px;
    color: #B4C2B2;
    line-height: 1.6;
  }
  .card .stat {
    font-family: 'JetBrains Mono', monospace;
    font-size: 24px;
    color: #8B9A6E;
    font-weight: 700;
    margin-bottom: 6px;
  }
  .session-bar {
    margin-top: 36px;
    background: rgba(14, 20, 16, 0.8);
    border: 1px solid rgba(139, 154, 110, 0.4);
    border-radius: 10px;
    padding: 14px 28px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #EAE2D6;
    display: flex;
    gap: 16px;
    align-items: center;
  }
  .session-bar b {
    color: #8B9A6E;
  }
</style>
</head>
<body>
  <div class="eyebrow">OPENAI CODEX × TWITCHCON HACKATHON</div>
  <h1>Engineered for <em>Trust & Reliability</em></h1>
  
  <div class="grid">
    <div class="card">
      <div class="stat">0 Packages</div>
      <h3>Zero-Dependency Core</h3>
      <p>Pure Node.js standard library. Fast, predictable, and immune to package breakage on live broadcast day.</p>
    </div>
    <div class="card">
      <div class="stat">Native WebSocket</div>
      <h3>Twitch EventSub Ingestion</h3>
      <p>Real-time chat events, token auto-refresh, subscription revocation recovery, and safe stream disconnect pauses.</p>
    </div>
    <div class="card">
      <div class="stat">31 / 31 Passed</div>
      <h3>Deterministic Math & Tests</h3>
      <p>Identical seeds and actions produce identical results. 100% verified test suite covering all failure modes.</p>
    </div>
  </div>

  <div class="session-bar">
    <span>OpenAI Codex Lead Session: <b>4f83cf02-cd9a-4e12-9a78-3c4ffe60df8f</b></span>
    <span>•</span>
    <span>GitHub: <b>github.com/techaaditya/ChatAtlas</b></span>
  </div>
</body>
</html>
"""

os.makedirs("video_assets", exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        headless=True
    )
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.set_content(HTML)
    page.wait_for_timeout(500)
    page.screenshot(path="video_assets/scene7_bg.png")
    page.close()
    browser.close()

print("Scene 7 background generated successfully!", flush=True)
