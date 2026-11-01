# Security and privacy

## Intended use

This release is a single-operator local application bound to 127.0.0.1 by default. It is not hardened for public multi-tenant deployment. Do not expose the control port directly to the internet.

## Implemented protections

Random 256-bit local keys; separate read-only stage key; constant-time equal-length key comparison; bounded JSON bodies; allowlisted static routes; Host and Origin checks; security headers; no third-party frontend scripts; escaped dynamic text; bounded contribution/action stores; blueprint schema and business-rule validation; single-writer state; no arbitrary script execution; no environment values in exports.

OAuth code exchange stays on the backend. State nonces are short-lived and single use. Authorization validates client ID and chat scope. Token values never enter the public snapshot. The .gitignore excludes .env, .data and node_modules.

## Stored data

state.json contains submitted idea text, Twitch user IDs/display names, attribution preferences, recent provider event IDs, approvals and game state. twitch-tokens.json contains access and refresh tokens where applicable. admin-key and overlay-key are local capability secrets.

Directories are created with 0700 and private files with 0600 where the OS supports those modes. The app does **not** encrypt tokens or ideas at rest. Protect the operating-system account and disk. Windows permission behavior differs; keep the files private there too.

## Contributor controls

Only documented command text is collected. Display names are opt-in through !credit on and can be hidden with !credit off. !forget removes a user's current contributions, associated attribution and action/boost participation, invalidates the active draft, and removes source references from retained blueprints. It cannot erase Twitch chat, a previous export, a recording, backups or provider-retained data.

Host removal is available for an individual idea outside an active storm. Moderation actions from Twitch are not automatically synchronized in this release. A moderator must remove unwanted contributions or reset the session. Announce these limits plainly.

## AI data boundary

Optional provider calls include submitted contribution text and necessary source IDs. Embedding calls include theme anchors. Twitch user IDs/display names are not sent to the model adapters. Do not submit sensitive personal data. Configure your provider's data controls and explain the transmission before enabling AI during a stream.

## Remaining risks

Possession of the control key grants full control. Possession of the overlay URL grants read access. There is no per-person operator account, fine-grained RBAC, audit signature, distributed rate limiter, formal penetration test or automatic retention policy. A public deploy needs those decisions, TLS, encrypted credentials, proper sessions and account recovery.

To rotate locally: stop the app, move the relevant key file out of DATA_DIR, restart, and update stored keys/OBS URLs. If ADMIN_KEY is configured in .env, replace it there instead. Disconnecting the app stops its local connection; revoke app authorization in Twitch settings when removing access permanently.

## Pre-recording checklist

Do not record .env, keys, token files, API dashboards or private console data. Exported artifacts are sanitized, but still contain contributed text and opted-in names. Get permission for public attribution and footage.
