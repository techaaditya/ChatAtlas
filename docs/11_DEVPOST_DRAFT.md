# ChatAtlas Foundry — Devpost Submission Copy

*Ready to copy directly into your Devpost submission form.*

---

## Project Title
**ChatAtlas Foundry**

## Tagline
**Turn Twitch chat's ideas into a world your community can build, test, and improve together.**

---

## Inspiration
When a streamer asks an open-ended creative question—*"What should we build today?"* or *"How do we solve this challenge?"*—the best ideas flash past in the chat scroll and disappear forever. Standard polls only offer predefined checkboxes. 

We built **ChatAtlas Foundry** to turn audience imagination into tangible, collaborative worlds. Viewers contribute raw thoughts, watch them cluster into meaningful themes with full source attribution, see the creator approve a co-created city blueprint, and rally together during playable challenges to see if their creation survives or learns from its mistakes.

---

## What It Does
1. **Listens to Chat**: Collects explicit `!idea <thought>` contributions in real time via Twitch EventSub, rejecting spam, duplicates, and limiting inputs to 5 ideas per viewer. Names remain anonymous unless a viewer types `!credit on`.
2. **Discovers Constellations**: Organizes community ideas into 6 distinct themes (*Harvest the storm*, *Save the surplus*, *Protect the city*, *Let energy escape*, *Grow resilience*, and *Unexpected possibilities* / wildcard). Streamers can rename or merge themes on the fly.
3. **Drafts Source-Linked Blueprints**: Translates audience suggestions into a 12-point construction budget across 6 functional modules (*Sun sail*, *Storm collector*, *Storage cells*, *Cloud shield*, *Discharge route*, *Sky garden*), with per-module attribution citing the exact viewer ideas that inspired them.
4. **Plays Deterministic Challenges**:
   - **The Great Tempest**: High lightning storm hazard where unvented storm collectors overload and rupture the city, while grounding discharge routes allow survival.
   - **The Frost Descent**: Sub-zero cryo hazard where thermal heating and overload venting prevent structural freezing.
5. **Audience Co-Op Action**: Viewers type `!act store`, `!act shield`, or `!act vent` during the live 18-beat storm to assist the city in real time.
6. **Iterative Learning & Revision**: If the city fails, the host opens a revision keeping the same seed—allowing the community to see the exact consequence of their design changes!
7. **Production-Ready Broadcast Stage**: A clean OBS browser source URL (`/overlay#<key>`) with sensitive creator controls hidden, high-contrast typography, and live integrity/energy meters readable on stream.

---

## How We Built It
- **Runtime**: Pure Node.js (22+ LTS or 24+) with **zero external runtime package dependencies**.
- **Protocols & State**: Native HTTP, authenticated Server-Sent Events (SSE) for sub-second stage updates, and atomic filesystem persistence (`store.mjs`) ensuring zero data corruption.
- **Twitch Integration**: Native WebSocket client listening to Twitch EventSub (`channel.chat.message`), complete with OAuth token validation, refresh token handling, and connection drop safety (automatically pauses the storm if Twitch disconnects).
- **Frontend & Rendering**: Lightweight HTML5 Canvas drawing procedural constellations and floating cities with reduced-motion support, responsive layouts down to 390px mobile, and accessible keyboard navigation.
- **Verification**: 31 automated tests (`node:test`) and full browser interaction verification via headless Google Chrome.

---

## How We Used OpenAI Codex
Codex was our lead pair programmer and architecture collaborator throughout the entire build:
- **Architectural Scaffolding**: Designed the single-writer state store, constant-time bearer token authorization, and EventSub message normalization.
- **Deterministic Simulation Core**: Developed the hazard generation and turn resolution loop so identical seeds and actions yield 100% reproducible outcomes.
- **Per-Module Attribution & Scenario Expansion**: Implemented module-level citations linking specific viewer ideas to modules, and added "The Frost Descent" cryo challenge.
- **Bug Discovery & Fixing**: Codex identified that user deletion (`!forget`) was inadvertently wiping session activity logs, and corrected it to preserve community logs while scrubbing individual attribution.
- **End-to-End Testing**: Codex authored the 31-test TAP test suite and the automated browser smoke test script driving headless Google Chrome through the complete user journey.

**Codex Session ID:** `4f83cf02-cd9a-4e12-9a78-3c4ffe60df8f`

---

## What We Learned & Challenges
One subtle challenge was ensuring live Server-Sent Events (SSE) snapshots did not disrupt the creator during on-stream editing. Early prototypes re-rendered the blueprint form upon receiving new chat ideas, which stole focus and reset cursor position while the creator was typing a custom title. We solved this by implementing non-destructive DOM updates and cursor selection range preservation. Another key learning was making game failure pedagogical: instead of an abrupt "Game Over", the telemetry clearly shows *why* the city failed (e.g. overload exceeding 22), empowering the audience to propose the exact fix in the next revision.

---

## What Works Today
- 100% working offline demo mode (no credentials or accounts needed to test the full loop).
- Live Twitch EventSub chat connector.
- Two complete challenge scenarios with procedural canvas graphics.
- Per-module source attribution and creator theme renaming/merging.
- Full privacy compliance (`!credit on`/`off`, `!forget`, sanitized artifact export).
- 31/31 unit & integration tests passing.

---

## What's Next
- Multi-channel collaborative co-creation (two streamers co-building interconnected floating islands).
- Dynamic AI topic clustering for unconstrained open-world game modes.
- Integrated Twitch Extension panel for one-click viewer voting.

---

## Links & Submission Artifacts
- **GitHub Repository**: https://github.com/techaaditya/ChatAtlas
- **Primary Codex Session ID**: `4f83cf02-cd9a-4e12-9a78-3c4ffe60df8f`
- **Demo Video**: [Insert YouTube Unlisted Link]
- **Try it locally**: Clone repo, run `npm run demo`, and open `http://localhost:3000`.
