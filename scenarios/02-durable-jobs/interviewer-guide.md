# Durable jobs interviewer guide

[Candidate situation](README.md) · [Common rubric](../../docs/rubric.md)

## Let the candidate lead the inquiry

Use the common 60-minute sequence: orient, investigate with AI, formulate repair intent before implementation edits, repair, challenge with a related case, and hand over. Start with “What would you find out first?” Observe the candidate's chosen questions, their relevance, and use of the answers.

Answer factual questions without supplying the diagnosis. Use neutral follow-ups such as “Why that question?” and “What would the answer change?” The mechanism-specific prompts below are hints when supplied before discovery; record that assistance. Make evidence notes along the way and assign rubric ratings afterward. Case-specific anchors and this guide are interviewer materials.

## Evidence opportunities

Temporary authority and physical execution are distinct. A worker can continue computing after it loses the right to publish. The authoritative store must reject stale mutations.

Relevant properties include accepted-publication authority, an immutable terminal result, stable request replay, and eventual recovery under the stated scheduling and completion assumptions.

## Multiple viable approaches

- A durable job record with a monotonic ownership generation, deadline, and terminal result; publication and renewal use an atomic guard over the current record.
- Distinct durable claim records with a current-claim pointer, coupled transactionally with publication and replay receipts.

Unique tokens can distinguish claims without integer generations. A global lock or worker-local belief alone does not establish authority after pauses and lease expiry.

## Primary replay

Worker A obtains claim A. It pauses. A's lease expires. Worker B obtains claim B. Worker A resumes and tries to publish or renew using its old claim.

The attempt must be rejected and B's authority preserved. Even if two computations happen to produce equal values, equality of output does not establish that stale authority was correctly rejected.

Ask the candidate to point to the atomic decision, not merely the earlier ownership read.

## Common adjacent case

Worker B publishes successfully and its response disappears. B restarts and retries after the former lease deadline.

Replay returns the original accepted result. No later claim or stale publication can overwrite it.

Check abandoned work after faults cease. Fair scheduling alone does not guarantee a worker finishes within a fixed lease; the completion or renewal assumption in the contract is material.

## Map to the rubric

| Dimension | Domain observation |
| --- | --- |
| Problem formulation | Defines the publication guarantee and computation boundary |
| State modeling | Distinguishes job identity, claim identity, local beliefs, and terminal results |
| Safety and transitions | Enforces current authority atomically at renewal and publication |
| Constraints and progress | Identifies reclaimability and sufficient uninterrupted authority |
| Falsification and evidence | Predicts a stale worker's action and checks its actual rejection |
| Revision and delivery | Preserves successful-publication replay while rejecting stale attempts |

## Clarifications and hints

The contract supplies clock, replay, and storage guarantees. A directional hint can ask about a paused worker after reassignment. A mechanism hint can identify the need to distinguish ownership periods. Record assistance.

Use the [common timeline](../../docs/interview-process.md). External side effects are an optional follow-up topic requiring a new contract with the effect's receiver.

## Readiness

Run python3 interview.py verify before a session. Four starter checks fail intentionally; reference.py passes all ten. Use the [intent example](example-intent.md) and [scenario rubric](rubric.md).

job_base.py supplies durable submission and claim allocation. The reference guards renewal and publication with the current token, and recognizes an accepted terminal publication before checking the former lease. The adjacent crash check loses a response after a real store mutation.

Code and exports are checked locally. Human pilots and AI-only measurements remain unperformed.
