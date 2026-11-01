# Deployment and operations

## Supported release path

Run locally with Node 24+, the included frontend and one backend process. Use the OBS browser source on the same computer. Outbound access is needed only for Twitch or optional OpenAI calls.

The application uses a long-lived Twitch WebSocket, HTTP SSE and a persistent directory. An ephemeral serverless request handler is not a drop-in deployment target. No hosting provider is required for a local demo.

## Environment setup

Copy .env.example to .env. In PowerShell use Copy-Item .env.example .env; on macOS/Linux use cp .env.example .env. Keep the demo's default .data directory and a separate .data-live directory for Twitch. The app rejects cross-mode data reuse.

PORT, HOST and PUBLIC_URL must agree with the listening address and browser origin. If changing ports, change the registered OAuth redirect too. The read-only OBS URL is generated from PUBLIC_URL.

## Recovery

Stop the process normally with Ctrl+C. On restart, state is restored; an active storm is paused. Log in, reconnect Twitch if needed, inspect the latest beat and resume. A reconnect does not reconstruct missed Twitch messages.

If state parsing/schema validation fails, do not delete it casually. Stop the app, make a private backup, and inspect the error. Restore a known-good stopped backup or create a new DATA_DIR. Never run two processes against the same directory.

## Backups

For a consistent backup, stop the application first. Copy the private data directory to protected storage. Keep those files out of the deliverable archive and source repository. Backups contain personal data and secrets; set a deletion policy for them too.

## Monitoring

The dashboard shows connection health, intelligence mode, activity and simulation phase. /health reports process liveness, not Twitch health. For future public operations add structured redacted logs, metrics, error reporting, storage alerts and provider spend monitoring. Do not log Authorization headers or OAuth callback query strings.

## Hosted expansion gate

Before exposing it publicly, implement real user sessions and broadcaster ownership, encrypted secret storage, TLS, tenant isolation, per-user/account rate limits, consent and retention policies, database migrations, event delivery architecture and operational monitoring. The included installed-user adapter is not a finished cloud-bot product. Recheck the current Twitch cloud-bot grants and transport requirements.

## Submission freeze

Create a tagged source revision after your final tests and recording. Retain the exact source/video/links submitted. Continue later work separately from that submission revision and follow organizer instructions about post-deadline changes.
