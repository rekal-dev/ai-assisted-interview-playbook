# Event projection intent rubric

Rate intent and its revision. Record test results separately. 0 = unresolved contradiction; 1 = incomplete; 2 = supported formulation; 3 = challenged and refined. N/E = not observed.

Ask why deleting a visible profile can affect later acceptance, what information the chosen approach retains, and why the candidate accepted or revised AI's proposal. Use short explanations, a walkthrough, or targeted execution as evidence. The anchors illustrate useful decisions; equivalent approaches are welcome. Passing-check count does not set the rating.

| Dimension | A supported intent at level 2 | Evidence for level 3 |
| --- | --- | --- |
| Problem formulation | Explains how older source facts can replace newer ones and clarifies the snapshot and deletion rules | Separates allowed recreation from forbidden stale resurrection |
| State modeling | Explains why accepted ordering matters even when no profile is visible | Compares retaining only a deletion's version with keeping a deleted row, or another relevant representation, and explains the information future decisions need |
| Safety and transitions | Requires nondecreasing accepted version and atomic comparison plus mutation | Predicts a low version overwriting a higher one despite an earlier check |
| Constraints and progress | Uses source version rather than arrival time | Allows the latest delivered version and a legitimate higher-version recreation |
| Falsification and evidence | Predicts deletion followed by an older snapshot and explains the result through code or a replay | Chooses concurrent writes or newer recreation to distinguish a sound acceptance rule from a patch for one output |
| Revision and delivery | Revises intent to preserve ordering history after deletion | Avoids an always-reject-after-delete patch and demonstrates valid recreation |

## Supporting checks: record results separately

- test_deletion_retains_ordering_information and test_older_event_cannot_resurrect_deleted_entity.
- test_concurrent_lower_version_cannot_overwrite_higher.
- test_restart_retains_deletion_order.
- test_higher_version_can_recreate_entity.
- test_bounded_delivery_permutations_converge: every order of three source facts, duplicates, and restart.

Ask what the candidate's prompt tells AI to preserve when the visible value disappears, and what observation would falsify the acceptance rule.
