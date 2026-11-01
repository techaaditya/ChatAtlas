# Verification report

## Environment

Built and tested in a Linux workspace using Node v24.22.1. No runtime dependencies were installed. The optional browser test uses a separate Playwright installation when available.

## Completed automated verification

Run `npm test` to reproduce engine, provider-mock, HTTP integration and Twitch transport-mock checks. All **31 automated tests passed**.

Verified behaviors include:
- Duplicate-event handling, per-viewer suggestion limits, distinct contributor support, and wildcard preservation.
- Creator theme renaming and theme merging with stable internal IDs.
- Per-module source attribution and validation of module-level citations.
- Multi-scenario deterministic simulation: both "The Great Tempest" (lightning storm) and "The Frost Descent" (cryo deep freeze) scenarios.
- Blueprint budgets (12-point cap) and strict rejection of invented sources.
- Pause and terminal states, action replacement within beats, opt-in attribution, and current-session deletion.
- Activity log retention: preserving session log integrity during `!forget` while scrubbing personal attribution.
- Read-only access boundaries, cross-origin rejection, failed mutation rollback, public export sanitization, persisted recovery and EventSub message normalization.

The HTTP integration test drives the real backend through a failing design, revision and successful design.

## Browser and Stage Verification

Executed `scripts/browser-smoke.mjs` against Google Chrome v156 (headless):
- Completed the full user loop: login with random key → fixture idea loading → blueprint drafting → creator approval → storm play → overload failure → revision → scenario switch to Frost Descent → per-module attribution validation → blueprint approval → storm play → survival.
- Verified OBS stage overlay URL with read-only key fragment: private host panels are hidden, canvas and stats remain readable.
- Verified mobile responsive layout at 390×844 viewport width.
- Zero page errors or uncaught exceptions observed.

## Not verified here

- Real live Twitch broadcast session with consenting audience viewers (requires broadcaster OAuth credentials on a live stream).
- Paid embedding/model requests against a real billing key.
- Production multi-tenant traffic or public cloud hosting.

## Required release rehearsal

1. Run npm test and npm run check.
2. Start a fresh demo data directory and complete the UI journey.
3. Run scripts/browser-smoke.mjs with a local Playwright installation and browser.
4. Review all screen states and mobile width manually.
5. Connect a real broadcaster account and test every documented command.
6. Record one real viewer's complete contribution-to-result path.
7. Test optional AI only if you intend to demonstrate it.
8. Confirm the archive/source repository excludes private data and keys.

## Known product limitations

The local rules are English keyword heuristics. Semantic mode assigns to fixed anchors. History is capped at 30. Provider responses can be discarded during active session edits. The app is one local operator/session, not a hosted service. Removal does not erase previous exports or video. The Canvas map has text alternatives but is not itself keyboard-navigable. Automatic Twitch moderation-event synchronization is future work.
