import os
from playwright.sync_api import sync_playwright

os.makedirs("video_assets", exist_ok=True)

CARDS = [
    {
        "id": "card_01",
        "tag": "01 / THE CHALLENGE",
        "title": "The Twitch Creative Gap",
        "sub": "Chat ideas flash past in seconds · Standard polls limit audience agency",
        "meta": "PROBLEM ANALYSIS"
    },
    {
        "id": "card_02",
        "tag": "02 / THE SOLUTION",
        "title": "ChatAtlas Foundry",
        "sub": "Turn audience imagination into tangible, playable worlds together",
        "meta": "PRODUCT VISION"
    },
    {
        "id": "card_03",
        "tag": "03 / LIVE DISCOVERY",
        "title": "Twitch EventSub & Theme Clustering",
        "sub": "Real-time chat ingestion · Opt-in privacy (!credit on) · 6 strategic themes",
        "meta": "REAL-TIME CHAT INGESTION"
    },
    {
        "id": "card_04",
        "tag": "04 / CO-CREATION BLUEPRINT",
        "title": "Source-Linked Construction",
        "sub": "12-point budget · Modules cite exact viewer ideas that inspired them",
        "meta": "PER-MODULE ATTRIBUTION"
    },
    {
        "id": "card_05",
        "tag": "05 / DETERMINISTIC PLAY",
        "title": "The Great Tempest & OBS Broadcast Stage",
        "sub": "Live co-op actions (!act vent, !act shield) · Clean /overlay stage for stream",
        "meta": "REAL-TIME SIMULATION & OBS"
    },
    {
        "id": "card_06",
        "tag": "06 / PEDAGOGICAL REVISION",
        "title": "Fail Forward & Seed Consistency",
        "sub": "Preserved weather seed · Learn from overload · Test community revision V2",
        "meta": "DETERMINISTIC REVISION"
    },
    {
        "id": "card_07",
        "tag": "07 / CODEX COLLABORATION & VERIFICATION",
        "title": "Zero-Dependency Core & Verification",
        "sub": "Built with OpenAI Codex (Session: 4f83cf02-cd9a-4e12-9a78-3c4ffe60df8f) · 31/31 Tests Passed",
        "meta": "OPENAI CODEX × TWITCH"
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,300..600&family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  body {{
    margin: 0;
    width: 1920px;
    height: 1080px;
    background: transparent;
    overflow: hidden;
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
  }}
  .lower-third {{
    position: absolute;
    bottom: 45px;
    left: 45px;
    background: rgba(18, 24, 19, 0.92);
    border: 1px solid rgba(139, 154, 110, 0.45);
    border-left: 5px solid #8B9A6E;
    border-radius: 12px;
    padding: 16px 24px;
    max-width: 820px;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65), 0 0 20px rgba(139, 154, 110, 0.15);
    backdrop-filter: blur(14px);
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .header-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
  }}
  .tag {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #A4B685;
    text-transform: uppercase;
  }}
  .meta-badge {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    color: #EAE2D6;
    background: rgba(234, 226, 214, 0.1);
    border: 1px solid rgba(234, 226, 214, 0.2);
    border-radius: 4px;
    padding: 2px 8px;
    letter-spacing: 0.8px;
  }}
  .title {{
    font-family: 'Fraunces', Georgia, serif;
    font-size: 26px;
    font-weight: 600;
    color: #F7F2EB;
    letter-spacing: -0.02em;
    margin: 0;
  }}
  .sub {{
    font-size: 13px;
    color: #C5BCB0;
    line-height: 1.4;
    margin: 0;
  }}
</style>
</head>
<body>
  <div class="lower-third">
    <div class="header-row">
      <span class="tag">{tag}</span>
      <span class="meta-badge">{meta}</span>
    </div>
    <h2 class="title">{title}</h2>
    <p class="sub">{sub}</p>
  </div>
</body>
</html>
"""

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        headless=True
    )
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    
    for c in CARDS:
        html = HTML_TEMPLATE.format(
            tag=c["tag"],
            meta=c["meta"],
            title=c["title"],
            sub=c["sub"]
        )
        page.set_content(html)
        page.wait_for_timeout(400)
        out_path = f"video_assets/{c['id']}.png"
        page.screenshot(path=out_path, omit_background=True)
        print(f"Rendered {out_path}", flush=True)
        
    page.close()
    browser.close()

print("All overlay cards rendered successfully!", flush=True)
