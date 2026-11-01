# Product requirements

## Problem and customer

Creators ask open-ended questions but cannot convert many simultaneous suggestions into a coherent activity. Polls require predefined options. ChatAtlas provides a contribution map, a visible adoption decision, and a tangible result.

Initial customers to interview: creative variety streamers, game-development streamers, maker educators, and producers of audience co-creation events. This is a customer hypothesis, not a validated market segment.

## The central promise

“Your community can point to an idea, see how it influenced a design, and help make the next version better.”

## Journeys

Viewer: read the on-air prompt → send !idea → see it appear under a theme → optionally boost → watch the approved city → participate with !act → suggest a revision. Names remain anonymous on the stage unless the viewer opts in.

Host: configure a prompt → moderate the contributions → pick a theme → inspect a draft → adjust modules/title → approve → launch → pause if needed → interpret the result → open a revision → export the artifact.

Judge: start without credentials → run fixtures → inspect the deterministic difference between two designs → read actual Twitch instructions → inspect tests and source → distinguish tested features from proposed ones.

## Acceptance criteria

- The offline demo completes the entire creation loop without external requests.
- Ordinary chat is ignored; only documented commands are used.
- Unknown, too-large, over-budget or source-free blueprints cannot run.
- A creator approval is required before a new simulation starts.
- The same seed and actions reproduce the same result.
- A lost Twitch connection pauses an active storm.
- Read-only stage credentials cannot change state.
- An accepted idea is linked to the blueprint through actual source IDs.
- AI failures show an error and preserve local controls.
- Restarting an active session requires an explicit resume.

## Deliberate scope

One broadcaster, one local session, one city scenario, six modules, six idea themes, at most 200 contributions, five contributions per viewer, and the most recent 30 approved versions. This makes the product's boundaries inspectable. A new free-form world editor is future work, not hidden functionality.

## Success measures for a pilot

Ask whether viewers recognize their ideas, whether the creator understands why a design failed, and whether the creator wants another session. Time the setup and the idea-to-approval workflow. Record actual counts. Do not report broad engagement lifts from one small session.
