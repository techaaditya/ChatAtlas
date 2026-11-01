# ChatAtlas Foundry — submission writing draft

**Status: edit and verify before submission. Bracketed fields must be replaced with actual evidence.**

## Tagline

Turn Twitch chat's ideas into a world your community can build, test and improve together.

## Inspiration

When a streamer asks an open-ended question, good suggestions can disappear in the scroll. We wanted an audience to do more than choose between preset options: contribute an idea, recognize it in a design and help improve what happens next.

## What it does

ChatAtlas Foundry collects explicit !idea contributions, groups them into visible themes and preserves unexpected suggestions. The host selects a theme, reviews its source contributions and approves a floating-city blueprint. Viewers then help the city through a seeded storm. The result becomes the starting point for the next revision.

The current scenario uses six bounded construction modules. A storm collector creates power but also overload; a discharge route changes how the city handles that pressure. Reusing the storm seed makes design comparisons understandable.

## How we built it

The app uses Node.js, browser Canvas, authenticated Server-Sent Events, local atomic state persistence and a broadcaster-authorized Twitch EventSub adapter. Blueprint validation limits the available modules, construction cost and contribution sources before anything runs.

[If verified and used: Optional embedding-based theme assignment and schema-constrained model proposals provide semantic interpretation while the host retains approval. State exactly which configuration you demonstrated.]

## How we used Codex

[Replace with actual details of your principal development thread. Describe the architecture work, implementation, test failures and fixes that you can show. Include the genuine session ID in the required field. Do not claim this archive itself supplies a verifiable session ID.]

## Challenges

One early integration test showed that a grounding suggestion tied with a generic energy keyword and went to the wrong theme. The local classifier was changed to prefer the more specific later theme on a nonzero tie, restoring the intended failure/revision demo. [Add your actual live testing challenge here.]

## What works today

[Verify on your machine before keeping this section.] Contribution collection, fixed-theme grouping, wildcard visibility, source-linked approval, module editing, seeded play, bounded viewer actions, revision history, export and separate control/stage access.

## What is next

Dynamic topic discovery, creator theme editing, additional original game grammars, stronger per-module attribution and creator collaboration. These are planned expansions, not implemented claims.

## Testing

Judges can run npm run demo without credentials and follow README.md for the complete loop. Live Twitch setup is documented separately. [Insert source URL, video URL, actual test results and limitations.]

## Honest claims only

Do not claim measured viewer retention, subscription demand, production-scale concurrency, worldwide novelty or fully automatic game generation without evidence. This draft is deliberately not written as a fabricated success story.
