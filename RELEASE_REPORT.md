# Release report

Prepared 1 November 2026.

- Runtime tested: Node v22.13.1 on Windows (compatible with Node 22+ LTS and Node 24).
- Automated tests: **31 passed, 0 failed** (increased from 23).
- JavaScript syntax checks: passed across `src/`, `public/`, `scripts/`, and `test/`.
- HTTP end-to-end product journey: passed, including failed city, revision and surviving city.
- Multi-scenario challenge verified: "The Great Tempest" (lightning storm) and "The Frost Descent" (cryo deep freeze).
- Per-module source attribution verified: module-level attribution links ideas to specific modules, and missing/invented sources are rejected.
- Theme management verified: creator theme renaming and theme merging with stable internal IDs.
- Activity log retention: fixed `forget` behavior to preserve unrelated session activity logs while scrubbing contributor attribution.
- Browser/OBS interaction QA: **Completed and passed** (`scripts/browser-smoke.mjs` executed using headless Google Chrome 156.0.8078.76). Tested authentication, idea seeding, blueprint drafting, storm failure, revision, Frost Descent challenge switch, per-module source visibility, storm survival, read-only OBS overlay isolation, and 390px mobile viewport rendering with zero page errors.
- Package has zero runtime dependencies.
- Optional provider adapters: mocked success and failure paths tested.
- Twitch adapter: mocked token validation, EventSub subscription, message normalization, and revocation handling tested.
- Real Twitch broadcaster account and real paid model calls: **not tested with live credentials here** (requires channel owner authentication).
- External publication: ready for deployment.

See verification/ for reproducible test output and docs/12_VERIFICATION_REPORT.md for scope.
