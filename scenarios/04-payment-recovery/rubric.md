# Payment recovery intent rubric

Score intent and revision against the ledger and executed checks. 0 = unresolved contradiction; 1 = incomplete; 2 = supported formulation; 3 = challenged and refined. N/E = not observed.

| Dimension | A supported intent at level 2 | Evidence for level 3 |
| --- | --- | --- |
| Problem formulation | Distinguishes logical payment from request attempts and owns one recovery window | Checks the provider contract before promising at-most-once charging |
| State modeling | Includes bank ledger, local intent, and an uncertain in-flight result | Explains why local Pending can coexist with bank Succeeded |
| Safety and transitions | Requires a durable stable bank identity and truthful local outcomes | Applies it to simultaneous recovery and a delayed first request |
| Constraints and progress | Uses actual permanent deduplication/lookup guarantees and durable recovery work | Rejects the assumption that not-found or timeout proves no effect can occur |
| Falsification and evidence | Predicts bank commit with lost response and inspects the external ledger | Tests before-bank, after-bank, and after-local-persist crash boundaries |
| Revision and delivery | Revises intent from timeout-as-failure to durable uncertainty and reconciliation | Preserves definitive decline, exact success replay, and bounded guarantees |

## Concrete checks

- test_timeout_preserves_unknown_outcome.
- test_client_retry_never_double_charges.
- test_recovery_after_bank_commit_before_local_write.
- test_delayed_request_after_not_found.
- test_simultaneous_recovery_uses_one_bank_operation.
- test_bank_outage_then_recovery and test_decline_is_terminal.

The instruction use idempotency is incomplete without identity scope, provider guarantees, recovery behavior, and acceptance evidence from both systems.
