# Reservations interviewer guide

[Candidate situation](README.md) · [Common rubric](../../docs/rubric.md)

## Evidence opportunities

The important distinction is between a reusable resource and a particular temporary claim. The model must also preserve a committed booking when a response disappears.

Useful safety conditions include capacity conservation, one original outcome per hold request ID, valid ownership at confirmation, and durable committed-result replay. Progress requires usable capacity after abandoned claims expire under the published recovery assumptions.

Do not require a particular schema or terminology.

## Multiple viable approaches

- Keep explicit seats with distinct hold records and atomically couple the current claim, expiry decision, booking, and request outcome.
- Keep a capacity pool with authoritative hold and booking records; use a transaction to establish availability and the mutation consistently.

Expiry can be checked lazily when capacity is acquired. A dedicated expiration transition is another option. Both must handle stale actors and preserve completed results.

## Primary replay

Use capacity one. Alice gets hold A. Time passes beyond A's deadline. Bob gets hold B using the released capacity. Alice's delayed confirmation arrives.

The old confirmation must fail without changing B. If B is valid, the service cannot make an additional successful booking promise for A.

Observe API outcomes as well as the final counter. A counter can remain nonnegative while promises conflict.

## Common adjacent case

Confirm A while valid. The durable booking commits but its response disappears. Restart the worker and advance past the former hold deadline. Replay confirmation.

The original booking must still be returned. A repair that checks expiry before recognizing a committed terminal result may incorrectly reject a successful replay.

Also check that expired records do not block a fresh hold when no cleanup process runs. This can be a small targeted replay rather than a second large repair.

## Map to the rubric

| Dimension | Domain observation |
| --- | --- |
| Problem formulation | Resolves exact-deadline semantics and identity on replay |
| State modeling | Distinguishes hold incarnations and durable outcomes |
| Safety and transitions | Couples current-claim validation and authoritative mutation |
| Constraints and progress | Shows how abandoned capacity becomes usable |
| Falsification and evidence | Predicts and replays a stale confirmation, then inspects promises |
| Revision and delivery | Preserves terminal replay while fixing stale ownership |

## Clarifications and hints

The candidate contract contains all factual answers. If stalled, use the common hint ladder: delayed operation after reassignment; distinction between seat and hold; atomic check and mutation. Record what was supplied.

Use the [common timeline](../../docs/interview-process.md). A cancellation feature is optional follow-up work, not required for the highest core rating.

## Readiness

Run python3 interview.py verify before a session. The starter has four expected failing checks; reference.py passes all nine. Inspect the [intent example](example-intent.md) and grade with the [scenario rubric](rubric.md).

The reference moves allocation into the authoritative transaction, validates the requested hold rather than a later claim on the seat, and recognizes an existing booking before rejecting expiry. test_contract.py executes the primary, adjacent, race, and bounded-history cases.

The code is locally checked; human pilots and AI-only measurement remain to be performed.
