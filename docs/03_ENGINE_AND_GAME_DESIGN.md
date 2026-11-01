# Engine and game design

## Supported modules

| Module | Cost | Exact effect |
| --- | ---: | --- |
| solar | 2 | +3 energy per beat |
| collector | 3 | +8 energy and +8 overload per beat |
| battery | 2 | Capacity becomes 36 instead of 24 |
| shield | 3 | Spend 4 energy to reduce storm damage by 7 plus shield actions |
| vent | 2 | Remove 10 overload per beat |
| garden | 2 | Repair 2 integrity per beat |

Budget: 12. Each module can appear once. Every design must have solar or collector. Every design cites between 1 and 30 current contributions, with support for per-module attribution linking specific audience ideas to individual modules.

## Scenarios

### 1. The Great Tempest (Default)
High electrical storm hazard (6–10 per beat). Collector generates +8 energy and +8 overload. Overload exceeding 22 deals thermal explosion damage. Sun sails produce 3 energy. Shields absorb 7 damage. Vent modules dump 10 overload.

### 2. The Frost Descent
Sub-zero cryo hazard (7–11 per beat). Dense ice clouds reduce sun sail output to 1 energy. Collectors harvest electrostatic ice-friction (+6 energy, +6 overload). Shield creates a thermal barrier dome absorbing 8 damage. Venting overload channels excess heat into structural warmth (+3 integrity repair). Greenhouses repair 2 integrity per beat. Without thermal venting and shielding, the city suffers cold rupture and freezes.

## Turn resolution

One beat occurs every two seconds unless paused. The host can advance a beat manually for rehearsal. A storm lasts up to 18 beats. Initial energy is 12 and integrity is 100. Seed 42 is reused across designs.

1. Generate hazard from the seed and beat: an integer from 6 through 10.
2. Add module energy and up to three store actions, capped by capacity.
3. Add collector overload.
4. Remove vent-module overload and up to three viewer vent actions, two overload each.
5. Apply shield protection if enough energy exists.
6. Add overload damage when overload exceeds 22: floor((overload-22)/4).
7. Apply damage, then garden repair; clamp integrity to 0–100.
8. Clear viewer actions and record the beat.
9. End at zero integrity or after 18 beats.

Viewer influence is bounded: one active action per user per beat; changing an action replaces it. At most three actions of each kind affect a beat. This is not one-human-one-vote protection and does not prevent alternate accounts. Never advertise perfect fairness.

## Demonstration contrast

Collector + battery + shield fails under seed 42 without sufficient viewer venting. Collector + shield + vent survives. A viewer can influence an outcome, so do not promise the same result if the action sequence changes.

This is an original toy game model, not real engineering. It is designed to make tradeoffs legible. The hazard random function is deterministic, not cryptographically secure.

## Clustering

The local method tokenizes Unicode letters/numbers and uses a short English keyword vocabulary. Ties favor later, more specific themes. Unrecognized ideas enter wildcard. This is transparent lexical grouping, not embeddings or emergent topic discovery.

Optional semantic mode compares idea embeddings to five theme anchors and uses wildcard below a cosine threshold of 0.30. It retains stable theme IDs. It is semantic theme assignment, not arbitrary topic clustering. A host can move a misclassified contribution to wildcard.

## State transitions

collecting → blueprint (approve) → playing (launch) → resolved (finish). Open revision returns to collecting. Pause only changes an active run's paused flag. An unapproved draft can be edited without launching. Restoring history creates an editable draft; approval creates a new version.
