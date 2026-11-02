import os
import time
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:3000"
KEY = "d6e5a647c70c8be216c265433f3b26a38718825727f6e2a332a79f36a334c800"
HEADERS = {"Authorization": f"Bearer {KEY}"}

os.makedirs("screenshots", exist_ok=True)
os.makedirs("raw_recordings", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        headless=True
    )
    
    # Reset to fresh demo
    req_context = p.request.new_context()
    req_context.post(f"{BASE_URL}/api/reset", headers=HEADERS, data={"confirm": "RESET"})

    # 1. Capture Login Landing Screen
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto(BASE_URL)
    page.wait_for_timeout(1000)
    page.screenshot(path="screenshots/01_login_hero.png")
    print("Captured 01_login_hero.png", flush=True)
    page.close()

    # 2. Main Studio Session with Video Recording
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="raw_recordings",
        record_video_size={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    page.goto(BASE_URL)
    page.wait_for_timeout(800)

    # Login
    page.fill("#key", KEY)
    page.wait_for_timeout(400)
    page.click("button.primary")
    page.wait_for_selector("#app:not([hidden])")
    page.wait_for_timeout(1000)

    # Load Demo Ideas
    page.click("#seed")
    page.wait_for_timeout(1500)
    page.screenshot(path="screenshots/02_idea_constellation.png")
    print("Captured 02_idea_constellation.png", flush=True)

    # Select a Theme: "Harvest the storm"
    page.click('[data-cluster="energy"]')
    page.wait_for_timeout(1200)

    # Ensure vent module is toggled
    vent_cb = page.locator('input[data-module="vent"]')
    if not vent_cb.is_checked():
        vent_cb.check()
    page.wait_for_timeout(800)
    page.screenshot(path="screenshots/03_source_linked_blueprint.png")
    print("Captured 03_source_linked_blueprint.png", flush=True)

    # Approve design
    page.click("#approve")
    page.wait_for_timeout(1000)

    # Start storm simulation
    page.click("#start")
    page.wait_for_timeout(1200)

    # Advance beats with player actions
    for beat in range(1, 10):
        if page.locator("#demo-vent").is_visible():
            page.click("#demo-vent")
        req_context.post(f"{BASE_URL}/api/step", headers=HEADERS)
        page.wait_for_timeout(500)

    page.screenshot(path="screenshots/04_storm_simulation.png")
    print("Captured 04_storm_simulation.png", flush=True)

    # Finish storm
    for beat in range(10, 19):
        req_context.post(f"{BASE_URL}/api/step", headers=HEADERS)
        page.wait_for_timeout(350)

    page.wait_for_timeout(1200)
    page.screenshot(path="screenshots/06_revision_learning.png")
    print("Captured 06_revision_learning.png", flush=True)

    # Open revision
    page.click("#revise")
    page.wait_for_timeout(1200)

    context.close()

    # 3. OBS Broadcast Overlay Screen
    overlay_page = browser.new_page(viewport={"width": 1920, "height": 1080})
    overlay_page.goto(f"{BASE_URL}/overlay#{KEY}")
    overlay_page.wait_for_timeout(2000)
    overlay_page.screenshot(path="screenshots/05_obs_broadcast_stage.png")
    print("Captured 05_obs_broadcast_stage.png", flush=True)
    overlay_page.close()

    # 4. Mobile Responsive Screen
    mobile_page = browser.new_page(viewport={"width": 390, "height": 844})
    mobile_page.goto(BASE_URL)
    mobile_page.fill("#key", KEY)
    mobile_page.click("button.primary")
    mobile_page.wait_for_timeout(1200)
    mobile_page.screenshot(path="screenshots/07_mobile_responsive.png")
    print("Captured 07_mobile_responsive.png", flush=True)
    mobile_page.close()

    browser.close()

print("ALL_DONE", flush=True)
