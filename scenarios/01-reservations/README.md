# Reservations

[Catalog](../README.md) · [Interviewer guide](interviewer-guide.md)

Status: scenario specification and interviewer guide. Runnable starter and harness are planned.

## Candidate situation

A service manages a configurable pool of seats, initially ten. Customers obtain temporary holds and confirm them. During retries and worker failures, customers occasionally receive incompatible successful promises. Operations also report no availability after unconfirmed holds have expired.

Investigate a small supplied implementation and its incident material. Reproduce one failure, repair its relevant transition, check a related case, and explain the resulting guarantee. AI is available throughout.

## Environment contract

| Area | Behavior |
| --- | --- |
| Hold | A successful hold reserves one unit and returns a hold identity and deadline thirty virtual time units later. |
| Request replay | A repeated hold request ID returns its original result, including no-capacity rejection. It creates no new hold and does not extend expiry. A fresh attempt uses a fresh ID. |
| Confirmation | A new confirmation succeeds only for its identified valid hold at the atomic decision point. Equality with the deadline means expired. |
| Confirmation replay | A previously successful confirmation returns its original booking result after response loss, restart, or passage of its former hold deadline. |
| Expired hold | An unsuccessful expired hold cannot be confirmed or revived. Its capacity can be reused. |
| Capacity | Confirmed bookings and valid unconfirmed holds reserve capacity. A booking permanently consumes one unit in the base exercise. |
| Store | Serializable atomic transactions are available. Durable commits survive worker restart. |
| Time | One authoritative monotonic virtual clock; no advance inside an atomic simulator action. |
| Failure | Concurrent requests, delayed duplicates, lost responses, stale paused workers, and worker crashes are permitted. |
| Progress | After faults cease, a worker and the store are available and work is fairly scheduled. Expired holds must not indefinitely block genuinely free capacity. |
| Retention | Identities and results persist for the full bounded exercise. |

No payments, cancellations, refunds, authentication, deployment, or garbage collection are included.

## Materials to prepare

- A small incorrect service and a request history.
- Atomic store and virtual clock documentation.
- Replay controls for pause, restart, duplicate delivery, and response loss.
- A public successful booking example and property checks over observable promises.

## Published failure categories

Competition for final capacity; repeated hold requests; stale confirmations after reassignment; replay after a committed result; and expiry with no cleanup worker.

## Required result

Follow the [60-minute process](../../docs/interview-process.md). Deliver a working model, one failing replay of the original, a repair, a related regression result, and a handoff identifying assumptions and remaining uncertainty.

Representation is open. Expiry may be derived, and a stored Expired status or cleanup worker is not required.
