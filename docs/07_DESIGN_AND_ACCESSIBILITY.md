# Design and accessibility

## Visual direction

Dark indigo observatory, lavender controls, mint status cues, amber construction accents, restrained linework. The city is procedural Canvas art, not a downloaded asset. The constellation links contribution themes to a shared center.

Three desktop panels separate the host's work: contribution stream, public stage, blueprint editor. Below them are connection controls and creation history. The OBS route removes private production panels and keeps public instructions, the scene and results.

## Interaction rules

- The stage should make the current phase obvious.
- Keep instructions visible: !idea during collection, !act during play.
- Always label simulated inputs and local intelligence.
- Avoid showing real names without opt-in.
- Keep sources visible beside a draft before approval.
- Use words and counts as well as color.
- Prefer a useful failure explanation over an unexplained red screen.

## Implemented accessibility foundations

Semantic buttons/forms, visible focus styling on inputs, labels for form fields, an aria-live status toast, a Canvas accessible name, readable text panels alongside graphics, responsive CSS breakpoints, and reduced-motion handling for scene animation. Native checkbox controls are used for modules.

## Manual QA still required

Test keyboard-only operation, focus retention while live ideas arrive, screen-reader order, 200% zoom, 390px mobile width, 720p stream readability, contrast values, and OBS browser audio/rendering. The constellation is not itself a fully navigable accessible visualization; the theme buttons and contribution list provide the text alternative.

Browser rendering was not visually inspected during package generation because the available browser binary could not be installed. Do not mark this checklist passed without running it. Responsive CSS is implemented, but device-level usability has not been established.

## Next polish priorities

Retain input focus during frequent snapshots, add explicit loading indicators to optional AI requests, allow theme rename/merge, and add a clearer read-only-only mode indicator. Make these improvements from observed user friction, not decorative animation alone.
