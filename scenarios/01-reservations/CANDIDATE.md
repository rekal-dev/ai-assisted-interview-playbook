# Reservation service interview

You have 60 minutes and may use AI throughout. Read incident.json and the code. Before editing, write the intent prompt you would give your AI collaborator in intent.md. Revise it after new evidence.

## Situation

The service holds a seat temporarily, then confirms it. Customers retry and workers restart. An old confirmation appeared to succeed after its seat had been reassigned.

Own one failure, reproduce it, repair its transition, and check a related case. Preserve the public API and provided diagnostics.

## Run

~~~sh
python3 run.py
~~~

Failures in starter.py are intentional. Edit starter.py and rerun. Keep tests, support.py, and hooks intact. Your handoff states which failures remain.

## Contract and API

- Construct Service(store, clock, capacity=10, hooks=None).
- hold(request_id) returns a held receipt with hold_id, seat_id, expires_at, or no_capacity.
- The same request ID returns its original receipt forever in this exercise, including rejection. It cannot renew a hold. A new attempt uses a new ID.
- confirm(hold_id) returns booked, expired, or unknown. A new confirmation requires that exact hold to be valid. Equality with its thirty-unit deadline means expired.
- A successful booking permanently reserves the seat. Replaying its confirmation returns the original booking even after response loss, restart, or the former deadline.
- bookings() reports committed promises; available() reports genuinely free capacity.
- MemoryStore.atomic is serializable. Its data survives a simulated worker-object restart; local values do not.
- Clock is authoritative and monotonic. Tests advance it between atomic actions.
- Concurrent calls, pauses, duplicates, and response loss are permitted. Abandoned expired holds must not strand capacity after recovery.
- Payment, cancellations, deployment, disk loss, and garbage collection are out of scope.

The hold_before_commit and confirm_before_commit hooks are diagnostic boundaries outside the final authoritative transaction. confirmation_after_persist simulates losing a reply after a commit.

## Deliver

Your initial and revised intent, code, reproduced failure, adjacent check output, supported property, and limits. Use rubric.md. Passing checks and the quality of your intent are assessed separately.
