# Durable jobs interview

You have 60 minutes with unrestricted AI. Read incident.json, job_base.py, and starter.py. Write your initial intent prompt in intent.md before editing, then revise it after evidence.

## Situation

A job worker paused, lost its lease, and later published after another worker took over. Jobs should remain recoverable when workers disappear.

Repair one ownership failure and check a related replay or recovery case. Worker computations may overlap; the guarantee concerns one authoritative published result.

## Run

~~~sh
python3 run.py
~~~

Edit starter.py. job_base.py provides queue infrastructure. Retain the API, tests, and diagnostics; record any remaining failures.

## Contract and API

- Construct Service(store, clock, hooks=None).
- submit(job_id, payload) creates one logical job. Identical replay is stable; conflicting input raises ValueError.
- claim(worker_id, request_id) returns job_id, token, expires_at, or None. Each ownership period has a distinct token. Replaying a request repeats its outcome and deadline; a fresh attempt needs a fresh ID.
- Claims expire after thirty virtual units. Equality with the deadline means expired. A stale worker does not physically stop.
- renew(job_id, token, request_id) returns an accepted flag and, on success, a new deadline. Only the current unexpired claim can renew. Replaying a renewal cannot extend it again.
- publish(job_id, token, result) returns True only for a valid new publication or exact replay of its accepted publication. A conflicting later result returns False.
- A terminal result is durable and immutable. Replay can succeed after the former lease expires.
- result(job_id) and status(job_id) expose durable outcome. Use non-None results.
- Transactions are serializable. Store data survives worker-object restart.
- Once faults cease, work is fairly scheduled and eventually a worker has enough valid authority, including renewals, to finish.
- External side effects, cancellation, deployment, and disk loss are excluded.

publication_after_persist allows a simulated crash after a committed result.

## Deliver

Initial and revised intent, a replay of the failure, a scoped repair, adjacent check output, and supported assumptions. Use rubric.md; code checks do not automatically determine intent ratings.
