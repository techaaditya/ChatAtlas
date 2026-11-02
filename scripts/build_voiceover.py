import asyncio
import os
import subprocess
import edge_tts

VOICE = "en-US-ChristopherNeural"
RATE = "+5%"  # Natural energetic cadence that brings the total runtime safely to ~2:45

SCENES = [
    {
        "id": "scene1_hook",
        "title": "The Problem & Hook",
        "text": "Live streaming on Twitch has a creative gap. When a broadcaster asks the community 'What should we build?', great suggestions flash past in chat and vanish within seconds. Channel polls only offer three or four checkboxes. Viewers want to co-create, and creators want tools that turn chat ideas into tangible, playable experiences."
    },
    {
        "id": "scene2_pitch",
        "title": "Introducing ChatAtlas Foundry",
        "text": "This is ChatAtlas Foundry: a live co-creation studio built for Twitch streams. Viewers submit ideas in chat. The engine groups them into thematic constellations with exact source attribution. The broadcaster approves a community blueprint, and everyone coordinates live to help the city weather fierce storm challenges."
    },
    {
        "id": "scene3_ingestion",
        "title": "Idea Ingestion & Constellations",
        "text": "In the Idea Stream, viewers submit ideas using the idea command. The system deduplicates spam, normalizes text, and caps submissions at five per viewer. Privacy is opt-in: viewer names remain anonymous until they type credit on. On the central stage, ideas cluster into six strategic themes like Harvest the storm, Save the surplus, or Protect the city. Broadcasters can rename or merge clusters in real time without losing attribution."
    },
    {
        "id": "scene4_blueprint",
        "title": "Source-Linked Blueprints",
        "text": "Selecting a theme turns community suggestions into a blueprint. Each structure has a cost against a strict twelve-point construction budget. Sun sails, storm collectors, storage cells, and cloud shields balance energy intake and protection. Most importantly, ChatAtlas Foundry features genuine per-module attribution: every component cites the exact viewer messages that inspired it."
    },
    {
        "id": "scene5_simulation",
        "title": "Storm Simulation & OBS Overlay",
        "text": "Once the creator approves the blueprint, the storm begins. Over eighteen simulated beats, the floating city balances energy, integrity, and overload. Viewers participate live using chat commands like act store, act shield, and act vent. For the broadcast, ChatAtlas Foundry includes a dedicated OBS overlay. It hides broadcaster controls and delivers high-contrast, broadcast-ready telemetry that pops on stream."
    },
    {
        "id": "scene6_revision",
        "title": "Pedagogical Revision & Learning",
        "text": "If the city overloads, failure is educational rather than punishing. The telemetry shows exactly where the weakness occurred. The host reopens revision mode with the identical storm seed, allowing the community to debate changes and prove that their new design can survive."
    },
    {
        "id": "scene7_architecture",
        "title": "Architecture & Codex Wrap-up",
        "text": "ChatAtlas Foundry is built with zero external runtime dependencies on native Node.js and Twitch EventSub WebSockets. OpenAI Codex served as our lead engineering collaborator, architecting the deterministic simulation core, privacy enforcement, and end-to-end test suite. The complete project is open source and ready for Twitch communities everywhere."
    }
]

os.makedirs("audio", exist_ok=True)

async def main():
    total_duration = 0.0
    for scene in SCENES:
        out_path = f"audio/{scene['id']}.mp3"
        communicate = edge_tts.Communicate(scene['text'], VOICE, rate=RATE)
        await communicate.save(out_path)
        
        # Get duration using ffprobe
        res = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", out_path],
            capture_output=True, text=True
        )
        duration = float(res.stdout.strip())
        scene["duration"] = duration
        total_duration += duration
        print(f"{scene['id']}: {duration:.2f}s | {scene['title']}")
        
    print(f"\nTotal Voiceover Duration: {total_duration:.2f}s ({total_duration/60:.2f} minutes)")

if __name__ == "__main__":
    asyncio.run(main())
