# Event projection interview

You have 60 minutes and unrestricted AI. Read incident.json and starter.py. Capture the instruction you would give AI in intent.md before editing, then revise it after new evidence.

## Situation

A customer-profile projection receives duplicate and out-of-order source events. Deleted profiles have reappeared after replay, and concurrent consumers have sometimes regressed visible values.

Reproduce one failure, repair the acceptance transition, and check a related case.

## Run

~~~sh
python3 run.py
~~~

Edit starter.py. Preserve the API, tests, and diagnostic hook. Report remaining failures.

## Contract and API

- Construct Service(store, hooks=None).
- apply(event) accepts a newer source fact and returns True; ignored older or duplicate facts return False.
- Each event has entity_id, positive version, kind, and, for upsert, a complete value. kind is upsert or delete.
- One authoritative source assigns increasing versions per entity. Different entities have independent version orders. IDs are not reused with reset versions.
- The same entity and version always have identical content. Events are complete snapshots, not partial deltas.
- get(entity_id) returns a version and value for a visible profile, otherwise None.
- version(entity_id) reports the last accepted source version even when the profile is deleted.
- Once version v is accepted, later reads cannot regress below it. A deletion hides the profile; an older snapshot cannot revive it. A newer snapshot may recreate it.
- MemoryStore provides serializable atomic mutations and survives simulated consumer-object restart.
- Delivery order and timestamps are not source order. Concurrent calls, duplicates, reordering, lost acknowledgments, and restart are permitted.
- After faults cease and the finite event set is delivered and processed fairly, the projection converges to its highest source version.
- Partial deltas, multiple writers, cross-entity transactions, garbage collection, and deployment are excluded.

projection_before_commit is a diagnostic pause outside the final authoritative transaction.

## Deliver

Initial and revised intent, a failing history, repair, related check output, supported property, and limits. Use rubric.md.
