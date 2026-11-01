# API and data contracts

All /api routes and /events require Authorization: Bearer KEY. A read-only overlay key can access state/events only. A control key can access all routes. JSON mutations require POST and a body under 16 KiB. Unknown routes are rejected.

| Route | Method | Payload/purpose |
| --- | --- | --- |
| /health | GET | Public process health, no session data |
| /api/state | GET | Sanitized current snapshot |
| /events | GET | SSE snapshots plus heartbeat |
| /api/settings | GET | Catalog, read-only stage URL, feature flags |
| /api/export | GET | Sanitized artifact JSON |
| /api/demo/seed | POST | Empty body; demo only |
| /api/demo/message | POST | name, userId, message; demo only |
| /api/prompt | POST | prompt |
| /api/draft | POST | clusterId, optional ai=true |
| /api/semantic | POST | Request embedding assignments |
| /api/approve | POST | blueprint: title, modules[], sourceIds[] |
| /api/start | POST | Start the approved design, seed 42 |
| /api/pause | POST | Toggle pause |
| /api/step | POST | Advance one unpaused beat |
| /api/revise | POST | Return to collection |
| /api/restore | POST | id of a history entry; editable draft |
| /api/scenario | POST | scenario: 'tempest' or 'frost' |
| /api/theme/rename | POST | themeId, label |
| /api/theme/merge | POST | from, to |
| /api/move | POST | idea id, theme |
| /api/remove | POST | idea id; host removal |
| /api/reset | POST | confirm=RESET; destructive current-session reset |
| /api/twitch/auth | POST | Create one-time OAuth URL |
| /api/twitch/connect | POST | Connect saved user authorization |
| /api/twitch/disconnect | POST | Stop local live connection |
| /auth/twitch/callback | GET | OAuth callback with code/state |

## Persistent state

schema=1; id; revision; mode; phase; prompt; ideas; credits; boosts; overrides; draft; history; run; receipts; activity; metrics; createdAt.

An idea has an ID, private user ID, private display name, text, theme, source and timestamp. Provider message IDs are retained up to 5,000 entries for deduplication. History retains 30 versions. Activity retains 30 messages.

A run records seed, tick, integrity, energy, overload, pending actions, paused flag, timeline and a blueprint snapshot. The outcome is survived or overloaded. Pending viewer actions clear after each beat.

## Public snapshot

Private user IDs, raw display-name fields, credit preferences, boosts keyed by identity, receipts and overrides are removed. Names are shown as an author field only after opt-in. Viewer actions are exposed as a count, not an identity map. Contribution text is intentionally public because it was explicitly submitted for the show.

Exports use the same sanitized representation and are not importable execution bundles. There is no state-import endpoint. Do not hand-edit a state file while the process runs.

## Versioning

Restoring a historical blueprint may fail if cited contributions were removed. Rebuild with current sources rather than silently inventing attribution. The archive manifest records file hashes; it is not a code-signing certificate.
