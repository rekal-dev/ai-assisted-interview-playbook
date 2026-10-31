# Event projections

[Catalog](../README.md) · [Interviewer guide](interviewer-guide.md)

Status: executable starter, reference repair, controlled delivery, and 10 contract checks. Not hiring-piloted.

## Run and administer

From the repository root:

~~~sh
python3 interview.py test projections --implementation starter
python3 interview.py test projections --implementation reference
python3 interview.py export projections --output candidate-packets/projections
~~~

The starter intentionally fails five checks.

Use the [candidate brief](CANDIDATE.md), [intent rubric](rubric.md), [interviewer guide](interviewer-guide.md), and [example intent and revision](example-intent.md). Real code: [starter](starter.py), [reference](reference.py), and [checks](test_contract.py).

## Candidate situation

A service builds a queryable customer-profile projection from source events. Delivery is duplicated and out of order. Incidents show older preferences replacing newer ones and deleted profiles reappearing after replay.

Investigate and repair the projection's acceptance rule. Reproduce one regression, repair it, and check a related deletion or recovery case.

## Environment contract

| Area | Behavior |
| --- | --- |
| Entity identity | Each entity has a stable source ID. IDs are not reused with reset versions in this exercise. |
| Source version | A single authoritative source assigns strictly increasing versions per entity. Versions across different entities are unrelated. |
| Event content | Each event is a complete snapshot of that entity at its version, or an explicit deletion. Events are not partial deltas. |
| Duplicate consistency | The same entity and version always have identical content. Conflicting source events are outside this contract. |
| Query behavior | The projection exposes the latest accepted source version for an entity. Once it accepts version v, later reads cannot regress below v. |
| Deletion | A deletion hides the profile at its version. A later source snapshot with a higher version may recreate it. Older events cannot revive it. |
| Replay | Duplicate events cause no additional logical change. The consumer may be restarted and replay prior events. |
| Store | Serializable atomic transactions or an equivalent atomic conditional update are available. Reads are authoritative; there is no eventually consistent read replica in this exercise. |
| Time | Arrival order and wall-clock timestamps do not define source version order. |
| Failure | Out-of-order events, duplicates, lost acknowledgments, concurrent consumers, and restart are permitted. |
| Progress | After faults cease, all source events in the finite workload are eventually delivered and processing is fairly scheduled. The projection eventually reflects the highest delivered source version. |
| Retention | Ordering information survives deletion and restart for the full bounded exercise. Garbage collection is excluded. |

Cross-entity transactions, multiple independent writers, partial updates, schema migration, and deployment are excluded.

## Included environment

A small incorrect consumer, an event corpus, a query adapter, a durable store, and a deterministic scheduler for delivery order and concurrent consumers.

## Published failure categories

Duplicate and reordered snapshots; older updates after deletion; lower-version writes racing higher-version writes; acknowledgment loss; and restart before replay.

## Required result

Use the [60-minute process](../../docs/interview-process.md). Deliver a working model, a valid failing history, an acceptance-rule repair, an adjacent check, and a handoff.

Choose how to retain ordering and deletion information. The exercise does not require a particular tombstone schema.
