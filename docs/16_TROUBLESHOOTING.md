# Troubleshooting

| Symptom | Action |
| --- | --- |
| Node flag/WebSocket errors | Install Node 24+, confirm node --version |
| Cannot enter dashboard | Start app, run npm run key from same directory/.env, paste exact key |
| Port already in use | Stop the other process or consistently change PORT, PUBLIC_URL and redirect URI |
| Stored session has wrong mode | Use a different DATA_DIR for demo vs Twitch; do not destroy the previous data |
| No demo contributions | Confirm demo mode and collecting phase, then Load demo ideas |
| Theme looks wrong | Move the contribution to wildcard; local mode is a keyword heuristic |
| Approve fails | Ensure 1–6 unique modules, an energy source, budget ≤12 and current source IDs |
| Restore fails | Its sources may have been removed; select a current theme and draft again |
| Storm does not advance | Resume if paused; restarted storms are intentionally paused |
| OAuth state invalid | Click Authorize again and complete within ten minutes |
| OAuth redirect error | Register exactly the configured redirect URL, including scheme/port/path |
| No Twitch chat | Confirm live mode, authorize your broadcaster account, verify user:read:chat |
| Ordinary messages absent | Expected; only documented contribution/game commands are processed |
| Model refuses/errors | Check key/model access and strict schema support; use local draft meanwhile |
| AI result discarded | Ideas/session changed during request; retry after activity settles |
| OBS blank | Paste full stage URL including #read-key, verify local server and key |
| OBS changes nothing | Expected read-only mode; use the private dashboard for controls |
| Control key exposed | Stop and rotate key, clear browser session storage, restart |
| State file damaged | Stop, back it up privately, restore a known-good copy or new DATA_DIR |

## Safe bug report

Include Node version, OS, step sequence, mode, visible error and a sanitized artifact export if appropriate. Do not include .env, .data, private keys, OAuth codes or token files.

## The demo did not fail as expected

The demonstration comparison assumes no additional viewer actions. A group can mitigate overload with !act vent. That is intended gameplay, not nondeterminism: both seed and action sequence determine a run.
