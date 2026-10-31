# Event projections interviewer guide

[Candidate situation](README.md) · [Common rubric](../../docs/rubric.md)

## Let the candidate lead the inquiry

Use the common 60-minute sequence: orient, investigate with AI, formulate repair intent before implementation edits, repair, challenge with a related case, and hand over. Start with “What would you find out first?” Observe the candidate's chosen questions, their relevance, and use of the answers.

Answer factual questions without supplying the diagnosis. Use neutral follow-ups such as “Why that question?” and “What would the answer change?” The mechanism-specific prompts below are hints when supplied before discovery; record that assistance. Make evidence notes along the way and assign rubric ratings afterward. Case-specific anchors and this guide are interviewer materials.

## Evidence opportunities

Arrival order is distinct from source order. Absence of a visible profile is also distinct from having no record of its accepted version.

Useful properties include nondecreasing accepted version, payload matching the accepted snapshot, deletion semantics, duplicate stability, and convergence after finite delivery and processing complete.

## Multiple viable approaches

- Keep a per-entity high-water version and snapshot or deletion marker, atomically accepting only a newer version.
- Keep durable versioned source facts and derive the query view from the maximum version, with deletion treated as a versioned fact.

A physical row deletion is valid only if the ordering guard survives elsewhere. A per-entity serialization design can work if it preserves source-order rules across restart; a queue alone does not make delayed old events new.

## Primary replay

Deliver entity E version 8 with a new preference, then version 7 with an old preference. The projection must remain at version 8.

Add a concurrent variant: a consumer reads version 6, pauses, another applies version 8, and the first attempts to write version 7. A read-check-write sequence without an atomic acceptance rule can regress the projection.

## Common adjacent case

Apply deletion at version 9, restart the consumer, and replay a snapshot at version 8.

The profile stays hidden. Removing the visible row and its only ordering guard permits resurrection and violates the contract.

Finally apply a valid snapshot at version 10. Recreation is allowed by the published contract. A fix that rejects every future event after deletion prevents required convergence.

## Map to the rubric

| Dimension | Domain observation |
| --- | --- |
| Problem formulation | Checks snapshots versus deltas and the source's ordering guarantee |
| State modeling | Preserves accepted order even when the entity is not visible |
| Safety and transitions | Couples version comparison and payload mutation atomically |
| Constraints and progress | Permits eventual newest state and valid recreation |
| Falsification and evidence | Predicts regression under both reordering and a concurrent write |
| Revision and delivery | Handles deletion without permanently rejecting later valid versions |

## Clarifications and hints

All source semantics are in the candidate contract. A directional hint can ask whether physical absence proves no higher version was accepted. A mechanism hint can identify the need to retain ordering across deletion. Record assistance.

Use the [common timeline](../../docs/interview-process.md). Changing snapshots into partial deltas is optional follow-up work requiring a new merge and ordering contract.

## Readiness

Run python3 interview.py verify before a session. Five starter checks fail intentionally; reference.py passes all ten. Use the [intent example](example-intent.md) and [scenario rubric](rubric.md).

The reference retains a versioned logical deletion and compares source version in the same transaction as mutation. The concurrency check pauses a lower version before commit, applies a higher one, then resumes it. Delivery permutations check replay, restart, deletion, and recreation.

Executable checks are established. Human pilots, AI-only measurements, and difficulty equivalence remain unvalidated.
