# Payment recovery

[Catalog](../README.md) · [Interviewer guide](interviewer-guide.md)

Status: scenario specification and interviewer guide. Runnable starter and bank simulator are planned.

## Candidate situation

A payment API accepts a logical payment and delegates charging to a bank. Clients retry and workers crash. Incidents show duplicate charges after a timeout and payments incorrectly marked failed when the bank actually charged successfully.

Investigate and repair the submission and recovery behavior. Keep the model small enough to reproduce one uncertain-outcome failure and a related restart case.

## Environment contract

| Area | Behavior |
| --- | --- |
| Payment identity | Within one merchant account, each payment ID binds immutable amount, currency, and customer details. Conflicting reuse is rejected. |
| Client replay | Repeating the same payment ID refers to the same logical payment. A definitive recorded outcome is stable. |
| Bank charge | The bank accepts an idempotency key and payload. The same key and payload refer to one bank operation and one stable terminal outcome. Conflicting reuse is rejected. |
| Bank retention | Idempotency and lookup records persist for the entire exercise. There is no deduplication expiry in the base contract. |
| Bank lookup | Lookup by key can return not found, pending, success, or definitive decline. Not found is an observation at that time; an earlier request may still be in flight. |
| Local store | Serializable atomic transactions and durable commits are available locally. |
| External boundary | Local database writes and bank effects cannot share an atomic transaction. |
| Failure | Requests or responses may be delayed; responses may be lost; workers may crash, resume, and retry. |
| Safety | A logical payment causes at most one successful charge. Local success requires a matching authoritative bank success. A timeout alone is not a definitive decline. |
| Progress | After faults cease, the bank and local store are available, pending bank operations eventually reach terminal outcomes, communication succeeds, and recovery work is fairly scheduled. |
| Completion | An accepted valid payment eventually exposes its matching bank success or definitive decline under those assumptions. A legitimate decline is a completed outcome. |

Refunds, multiple providers, currency conversion, fraud decisions, deployment, and garbage collection are excluded.

## Materials to prepare

A small incorrect service, a durable intent store, a bank simulator with an independent ledger, deterministic failure injection, and a recorded timeout incident.

## Published failure categories

Charge success with lost response; restart between an external effect and a local write; duplicate client requests; concurrent recovery; delayed requests after a not-found lookup; and conflicting payload reuse.

## Required result

Use the [60-minute process](../../docs/interview-process.md). Deliver an explicit boundary model, a reproduced failure, a supported submission or recovery repair, an adjacent regression check, and a statement of remaining uncertainty.

Choose the local state representation and durable recovery mechanism.
