# Event projection intent rubric

Rate intent and its revision. Record test results separately. 0 = unresolved contradiction; 1 = incomplete; 2 = supported formulation; 3 = challenged and refined. N/E = not observed.

| Dimension | A supported intent at level 2 | Evidence for level 3 |
| --- | --- | --- |
| Problem formulation | Checks complete snapshots, per-entity order, and deletion semantics | Separates allowed recreation from forbidden stale resurrection |
| State modeling | Retains accepted ordering even when no profile is visible | Explains why absent and deleted-at-version-v require different future behavior |
| Safety and transitions | Requires nondecreasing accepted version and atomic comparison plus mutation | Predicts a low version overwriting a higher one despite an earlier check |
| Constraints and progress | Uses source version rather than arrival time | Allows the latest delivered version and a legitimate higher-version recreation |
| Falsification and evidence | Supplies deletion followed by an older snapshot | Adds concurrency and all supplied bounded delivery permutations |
| Revision and delivery | Revises intent to preserve ordering history after deletion | Avoids an always-reject-after-delete patch and demonstrates valid recreation |

## Concrete checks

- test_deletion_retains_ordering_information and test_older_event_cannot_resurrect_deleted_entity.
- test_concurrent_lower_version_cannot_overwrite_higher.
- test_restart_retains_deletion_order.
- test_higher_version_can_recreate_entity.
- test_bounded_delivery_permutations_converge: every order of three source facts, duplicates, and restart.

Ask what the candidate's prompt tells AI to preserve when the visible value disappears, and what observation would falsify the acceptance rule.
