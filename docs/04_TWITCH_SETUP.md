# Real Twitch setup

This adapter uses the **installed broadcaster** model, not a cloud bot serving many channels. It listens as the authorized broadcaster to that broadcaster's own channel. No writing scope, Bits, Channel Points, raid event or Affiliate feature is required.

## Configure

1. Complete your Twitch developer account prerequisites and register an application at https://dev.twitch.tv/console.
2. Register the exact OAuth redirect URL: http://localhost:3000/auth/twitch/callback.
3. Copy .env.example to .env. Set TWITCH_CLIENT_ID and TWITCH_CLIENT_SECRET.
4. Set DATA_DIR=.data-live so live state is separate from the demo. Keep PUBLIC_URL=http://localhost:3000 and the matching redirect URI.
5. Stop the demo server. Run npm start, then npm run key in another terminal.
6. Enter the dashboard with that live directory's control key.
7. Click Authorize Twitch and approve **user:read:chat** for your broadcaster account.
8. Confirm that the dashboard reports Connected to your account name.
9. Add the read-only stage URL as an OBS Browser Source. Start with 1280×900 or 1920×1080; preview the layout.
10. Ask a consenting viewer to send !idea harvest lightning. Confirm a TWITCH-tagged contribution appears.

The OAuth state nonce expires after ten minutes and is single use. Tokens are kept on the local machine with restrictive file permissions. For this prototype they are not encrypted at rest; do not place this directory on shared hosting or commit it.

## Token alternative

A user access token may be supplied in TWITCH_USER_TOKEN for testing. It must belong to the configured app, include user:read:chat, and identify your broadcaster account. Its scope and client ID are validated. An environment-only token without a refresh token requires reauthorization when it expires. The dashboard OAuth flow is preferred.

## Commands

| Command | Effect |
| --- | --- |
| !idea your thought | Submit up to five ideas in this session |
| !boost energy | Support one existing theme; another boost replaces it |
| !act store | Add a bounded energy action during a storm |
| !act shield | Add a bounded protection action |
| !act vent | Release a bounded amount of overload |
| !credit on | Permit display of your Twitch display name |
| !credit off | Hide your name on future snapshots |
| !forget | Remove your current-session contributions and attribution |

Theme IDs: energy, storage, shield, grounding, life, wildcard. Boost only works if that theme already has contributions. Ordinary messages are ignored. Host commands are not exposed in chat.

## Broadcast notice

“ChatAtlas is collecting !idea contributions for our shared city. Contributions appear on stream. Names stay hidden unless you type !credit on. Use !forget to remove your contributions from the current session. If semantic/AI mode is enabled, submitted ideas may be sent to the configured model provider.”

Ask participants to acknowledge the activity before recording. Their messages already exist in Twitch chat independently of this app; !forget does not erase Twitch chat or a stream recording.

## Reliability

The connector handles welcome, keepalive, subscription, reconnect migration, close and revocation. A lost connection pauses the storm. The host resumes after checking connection health. Twitch does not replay events missed during a disconnection. Token validation runs at startup and hourly while connected. Refresh uses OAuth refresh tokens where available.

On restart, click Connect saved account. Automatic unattended live reconnection on process startup is intentionally not enabled.

## Required live rehearsal

Verify real message → theme → approval → storm → revision, a ten-minute connection, disconnect and resume, contributor removal, and read-only OBS access. None of these live account checks was performed with user credentials during package generation. A mocked integration test is not live certification.
