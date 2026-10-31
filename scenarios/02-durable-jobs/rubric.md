# Durable jobs intent rubric

Rate intent and revision separately from functional checks. 0 = unresolved contradiction; 1 = material omissions; 2 = supported formulation; 3 = stronger evidence below. N/E = not observed.

| Dimension | A supported intent at level 2 | Evidence for level 3 |
| --- | --- | --- |
| Problem formulation | Defines the guarantee around authoritative publication | Explicitly permits duplicate computation while preventing stale authority |
| State modeling | Distinguishes job identity, current claim, and accepted publication | Explains why a job ID or worker-local belief cannot represent changing authority |
| Safety and transitions | Requires token and lease validity at the atomic publication or renewal | Checks both stale publication and stale renewal rather than guarding only one method |
| Constraints and progress | Uses durable store, expiry, and the completion/renewal assumption | Avoids assuming an expired worker stopped and avoids promising bounded completion from fairness alone |
| Falsification and evidence | Predicts A resuming after B's claim and requires rejection | Adds committed-publication replay after restart and expiry |
| Revision and delivery | Revises intent to recognize terminal publication before lease rejection | Preserves immutable result and exact replay without permitting a changed result |

## Concrete checks

- test_stale_publication_is_rejected and test_unknown_token_cannot_publish.
- test_stale_renewal_is_rejected.
- test_publication_replay_survives_expiry_and_restart.
- test_abandoned_job_is_reclaimable.
- test_renewal_replay_does_not_extend_lease and test_completed_result_cannot_be_overwritten.

Useful prompt content identifies who is authoritative at the mutation, what survives restart, and the counterexample that would disprove the claim. The word fencing alone is not that argument.
