# Sources and competitive positioning

Checked while preparing this package, 31 October 2026. Recheck official docs during account setup because platform behavior and model availability can change.

## Primary technical references

- https://dev.twitch.tv/docs/chat/authenticating/ — choose the installed-broadcaster authorization model used here.
- https://dev.twitch.tv/docs/eventsub/handling-websocket-events/ — welcome, keepalive, reconnect, revocation and delivery gaps.
- https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/ — authorization code exchange.
- https://dev.twitch.tv/docs/authentication/validate-tokens/ — startup and hourly validation.
- https://dev.twitch.tv/docs/authentication/refresh-tokens/ — refresh token handling.
- https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types/ — channel.chat.message conditions.
- https://developers.openai.com/api/reference/resources/embeddings/methods/create — embedding requests.
- https://developers.openai.com/api/reference/resources/chat — configurable schema-constrained generation.

The code's Node HTTP server and single-directory storage are implementation choices, not requirements imposed by the hackathon.

## Official competition references

- https://twitchcon-codex.devpost.com/
- https://twitchcon-codex.devpost.com/rules
- https://twitchcon-codex.devpost.com/resources
- https://twitchcon-codex.devpost.com/updates

The researched criteria are innovation, potential impact, implementation/Codex use, and design. Submission requires the project's runnable source, description, actual Codex session ID and a short accessible video demonstrating Twitch operation and Codex use. Use the current official rules as authoritative when submitting.

## Adjacent concepts

Chat Signal already describes live chat categorization and semantic processing: https://github.com/ChatSignal/chat-signal . A moving topic map alone is not our novelty claim.

Chat Reef describes a living community overlay: https://devpost.com/software/chat-reef . Persistence and audience creatures alone are not our novelty claim.

Our proposed distinction is the full explicit contribution → source-linked approval → bounded playable creation → reproducible revision loop. That is a positioning hypothesis, not an exhaustive prior-art search or a claim that every component is unprecedented.
