# ChatAtlas Foundry

**Ideas become worlds.** A Twitch co-creation studio that turns explicit audience suggestions into themes, a creator-approved floating-city blueprint, and a playable storm challenge. Keep the storm seed, revise the design, and see whether the next city survives.

This archive contains working source, a credential-free demo, optional OpenAI adapters, a local broadcaster Twitch connector, tests, and a project-specific documentation set. It is a tested local prototype, not a verified public SaaS deployment or a guarantee of a hackathon award.

## Start in two minutes

1. Install **Node.js 22 (LTS) or newer**. No runtime packages, account, or API key are needed for demo mode.
2. Extract this folder and open a terminal inside it.
3. Run:

```sh
npm run demo
```

4. Keep that terminal running. In another terminal in the same folder:

```sh
npm run key
```

5. Open **http://localhost:3000**, paste the printed control key, and enter the studio. The key is private; don't show it in a recording.

There is no compilation step. `npm ci` is optional because the app has no runtime dependencies; a lockfile is included.

## The complete demo

1. Click **Load demo ideas**. These are clearly labeled fixtures, not Twitch viewers.
2. Select **Harvest the storm**. Review its source contributions and modules.
3. Click **Approve design**, then **Run storm**.
4. Watch the storm for up to 36 seconds. The unvented collector overloads. **Advance beat** can accelerate a local rehearsal.
5. Click **Open revision**, select **Let energy escape**, approve, and launch again.
6. The same seeded storm now meets a collector/shield/discharge design and the city survives.
7. Export the artifact. Open or copy the read-only OBS stage URL.

During play, the three demo action buttons let a simulated participant store energy, strengthen the shield, or release overload. One active action per viewer per beat is retained. Multiple clicks replace that participant's action; they do not stack.

## What is implemented

- Original responsive dashboard, animated Canvas constellation, and floating-city scene.
- Bounded contribution collection, six themes including wildcard, distinct contributor counts, and per-viewer boosts.
- Local lexical grouping; optional batched embedding-based assignment to the same themes.
- Deterministic blueprint recipes; optional schema-constrained AI drafts.
- Manual module/title editing, per-module source attribution, creator theme renaming/merging, and source-linked approval.
- A 12-point construction budget, six original simulation modules, and two distinct survival scenarios ('The Great Tempest' lightning storm and 'The Frost Descent' sub-zero cryo hazard).
- Fixed-seed play, bounded viewer actions, pause, revision, history, and public artifact export.
- Atomic local state replacement and paused recovery of an interrupted run.
- Separate control and overlay keys; authenticated HTTP/SSE; source-mode isolation.
- Local Twitch OAuth code flow, token validation/refresh support, EventSub chat ingestion, retry and migration handling.
- Opt-in name attribution, !forget, host removal, and explicit demo/live labels.

## What is not implemented

Free-form game-code generation, arbitrary game types, dynamic topic discovery beyond the defined themes, multi-channel collaboration, billing, accounts for multiple customers, automated moderation-event synchronization, a hosted service, or measured revenue/retention improvements. See [roadmap](docs/15_ROADMAP.md).

## Tests

```sh
npm test
npm run check
```

Read [verification report](docs/12_VERIFICATION_REPORT.md) for exactly what was and was not tested. Optional browser automation lives in `scripts/browser-smoke.mjs`.

## Read next

Start with [documentation index](docs/00_START_HERE.md), then [Twitch setup](docs/04_TWITCH_SETUP.md), [AI setup](docs/05_AI_AND_PROMPTS.md), and [demo/submission plan](docs/10_DEMO_AND_SUBMISSION.md).

All visual assets and fixture writing in this package were created for this implementation. Licensing defaults to all rights reserved until the owner deliberately chooses a distribution license. See `LICENSE`.
