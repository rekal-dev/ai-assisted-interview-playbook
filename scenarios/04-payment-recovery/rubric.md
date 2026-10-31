# Payment recovery intent rubric

Score the candidate's formulation, approach choice, and revision. 0 = unresolved contradiction; 1 = incomplete; 2 = supported formulation; 3 = challenged and refined. N/E = not observed.

Ask what a timeout actually establishes, which recovery approaches the bank contract permits, and why the candidate accepted or revised AI's proposal. Use short explanations, a walkthrough, or targeted execution as evidence. The anchors illustrate useful decisions; equivalent approaches are welcome. Passing-check count does not set the rating.

| Dimension | A supported intent at level 2 | Evidence for level 3 |
| --- | --- | --- |
| Problem formulation | Explains why the same timeout can mean no charge or a successful charge with a lost response, and owns one recovery window | Checks the provider contract before promising at-most-once charging |
| State modeling | Includes bank ledger, local intent, and an uncertain in-flight result | Explains local Pending with bank Succeeded and compares lookup-then-retry with retrying the same bank operation under the supplied contract |
| Safety and transitions | Requires a durable stable bank identity and truthful local outcomes | Applies it to simultaneous recovery and a delayed first request |
| Constraints and progress | Uses actual permanent deduplication/lookup guarantees and durable recovery work | Rejects the assumption that not-found or timeout proves no effect can occur |
| Falsification and evidence | Predicts bank commit with lost response and relates local status to the external ledger | Chooses a related crash or delayed-request case because it distinguishes the proposed approach from an unsafe retry |
| Revision and delivery | Revises intent from timeout-as-failure to durable uncertainty and reconciliation | Preserves definitive decline, exact success replay, and bounded guarantees |

## Supporting checks: record results separately

- test_timeout_preserves_unknown_outcome.
- test_client_retry_never_double_charges.
- test_recovery_after_bank_commit_before_local_write.
- test_delayed_request_after_not_found.
- test_simultaneous_recovery_uses_one_bank_operation.
- test_bank_outage_then_recovery and test_decline_is_terminal.

The instruction use idempotency is incomplete without identity scope, provider guarantees, recovery behavior, and acceptance evidence from both systems.
