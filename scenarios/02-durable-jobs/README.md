# Durable jobs

[Catalog](../README.md) · [Interviewer guide](interviewer-guide.md)

Status: executable starter, reference repair, queue infrastructure, and 10 contract checks. Not hiring-piloted.

## Run and administer

From the repository root:

~~~sh
python3 interview.py test jobs --implementation starter
python3 interview.py test jobs --implementation reference
python3 interview.py export jobs --output candidate-packets/jobs
~~~

The starter intentionally fails four checks.

Use the [candidate brief](CANDIDATE.md), [intent rubric](rubric.md), [interviewer guide](interviewer-guide.md), and [example intent and revision](example-intent.md). Real code: [starter](starter.py), [reference](reference.py), [queue base](job_base.py), and [checks](test_contract.py).

## Candidate situation

A service accepts jobs and assigns them to workers. A crashed worker's job should be recoverable. Incidents show a paused worker publishing after another worker has taken over, and jobs remaining unavailable after workers disappear.

Investigate and repair the core claim and result-publication behavior. Workers may compute a job more than once. The required guarantee applies to one authoritative durable result for a job.

## Environment contract

| Area | Behavior |
| --- | --- |
| Job identity | Submitting the same job ID with the same immutable input refers to one job. A conflicting input is rejected. |
| Operations | Submit a job, claim an eligible job, renew a claim, and publish a result. |
| Claim | Grants temporary authority for thirty virtual time units. A distinct claim token identifies each ownership period. |
| Renewal | Only the current unexpired claim may renew its deadline. An expired claim cannot revive itself. Replaying a renewal request returns the original outcome and cannot extend its deadline again. |
| Publication | A new result is accepted only from the current valid claim at the atomic decision point. |
| Terminal result | Once accepted, the result is durable and immutable. Replay of that successful publication returns its original acceptance even after the former lease expires. |
| Computation | Jobs have immutable inputs. Computation has no external side effects in this exercise. |
| Store | Serializable atomic transactions and durable commits are available. There is no transaction around the time spent computing. |
| Time | One authoritative monotonic virtual clock; equality with a lease deadline means expired. |
| Failure | Workers can crash, pause, resume with stale local state, lose responses, or retry requests. |
| Progress | Faults eventually cease. The store is available and work is fairly scheduled. Eventually some worker has enough valid claim time, including permitted renewals, to finish a job. |
| Retention | Job identities, successful claim requests, and publication results persist for the bounded exercise. Claim-request replay returns its original token and deadline and does not extend it. |

Arbitrary external side effects, cancellation, workflow dependencies, deployment, and garbage collection are excluded. A fresh claim attempt uses a fresh request identity.

## Included environment

A small claim service, worker simulator, deterministic clock, durable store, a recorded stale-publication incident, and controls for pausing workers around reads and writes.

## Published failure categories

Competing claims; lease expiry and reassignment; stale renewal or publication; lost successful-publication responses; and recovery of abandoned work.

## Required result

Use the [60-minute process](../../docs/interview-process.md). Reproduce one authority failure, repair the relevant transitions, verify an adjacent case, and explain the safety and progress assumptions.

Choose the representation and claim mechanism. The contract does not promise that an expired worker physically stops running.
