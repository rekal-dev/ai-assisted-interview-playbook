# Durable jobs intent rubric

Rate intent and revision separately from functional checks. 0 = unresolved contradiction; 1 = material omissions; 2 = supported formulation; 3 = stronger evidence below. N/E = not observed.

Ask why a paused worker can still act, which approach protects the publication decision, and why the candidate accepted or revised AI's proposal. Use short explanations, a walkthrough, or targeted execution as evidence. The anchors illustrate useful decisions; equivalent approaches are welcome. Passing-check count does not set the rating.

| Dimension | A supported intent at level 2 | Evidence for level 3 |
| --- | --- | --- |
| Problem formulation | Explains how a worker can keep running after losing authority and scopes the guarantee to publication | Explicitly permits duplicate computation while preventing stale authority |
| State modeling | Distinguishes job identity, current claim, and accepted publication | Compares checking authority before computation with enforcing it at publication, and explains the consequence of the gap |
| Safety and transitions | Requires token and lease validity at the atomic publication or renewal | Explains why the same ownership rule must cover publication and renewal |
| Constraints and progress | Uses durable store, expiry, and the completion/renewal assumption | Avoids assuming an expired worker stopped and avoids promising bounded completion from fairness alone |
| Falsification and evidence | Predicts what happens when A resumes after B's claim and explains it through code or a replay | Chooses committed-publication replay to distinguish a valid retry from a new stale publication |
| Revision and delivery | Revises intent to recognize terminal publication before lease rejection | Preserves immutable result and exact replay without permitting a changed result |

## Supporting checks: record results separately

- test_stale_publication_is_rejected and test_unknown_token_cannot_publish.
- test_stale_renewal_is_rejected.
- test_publication_replay_survives_expiry_and_restart.
- test_abandoned_job_is_reclaimable.
- test_renewal_replay_does_not_extend_lease and test_completed_result_cannot_be_overwritten.

Useful prompt content identifies who is authoritative at the mutation, what survives restart, and the counterexample that would disprove the claim. The word fencing alone is not that argument.
