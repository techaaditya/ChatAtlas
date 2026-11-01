# Architecture

## Runtime

Node 24 provides HTTP, fetch, a WebSocket client, filesystem operations, test runner and crypto. Browser code uses Canvas, fetch streaming, and plain DOM APIs. There are no runtime package dependencies and no build pipeline.

`src/server.mjs` owns the HTTP server, routing, authentication, SSE fan-out and single state writer. `engine.mjs` owns contribution rules, blueprints and the simulation. `store.mjs` owns atomic file replacement and private local keys. `twitch.mjs` owns the Twitch connection. `intelligence.mjs` owns bounded optional provider requests. `public/app.js` renders the dashboard and stage.

## Event order

1. Twitch delivers a documented command or a host sends an authorized request.
2. The server clones the current state.
3. The engine validates and applies the operation.
4. The store writes a temporary file and renames it over state.json.
5. The in-memory state changes only after that write succeeds.
6. A public snapshot is emitted to SSE subscribers.

This is a single-process atomic replacement design, not a relational transaction or a multi-worker consensus system. A power outage may still lose filesystem buffers. Back up stopped application data for important sessions.

## Trust boundaries

Native Twitch identity is trusted only after app/token validation and the authorized channel subscription. Viewer text is untrusted. A model draft is untrusted until validated. The overlay key permits reading only. The control key permits publishing, export and destructive actions. Filesystem access is an operator-level privilege.

## Public transport

GET /events is an authenticated Server-Sent Events feed. It sends an initial complete snapshot, subsequent complete snapshots, and periodic heartbeats. Clients reconnect and receive the latest state. There is no need to replay every intermediate UI change.

The feed uses fetch streaming so its bearer key is sent in a header. The OBS URL contains a read-only key in its fragment; JavaScript reads it locally. The fragment is not part of the HTTP request, and Referrer-Policy is no-referrer. Anyone possessing that URL can read the stage's session data.

## Bounded concurrency

Engine operations are synchronous and serialized by Node's event loop. Provider requests happen outside the state writer. Their results are discarded if the session ID or revision changed while awaiting a response. That prevents a stale model response from overwriting a new session or edited ideas. In very active chat this can require retrying after contribution activity settles.

## Persistence and recovery

State includes idea records, approvals, seed, timeline and phase. OAuth tokens live in a separate private file. A recovered active storm is paused. An unexpected schema or mismatched demo/live mode stops startup rather than silently overwriting data. Data migration and hosted multi-user storage are future work.
