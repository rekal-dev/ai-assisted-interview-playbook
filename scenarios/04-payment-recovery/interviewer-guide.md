# Payment recovery interviewer guide

[Candidate situation](README.md) · [Common rubric](../../docs/rubric.md)

## Let the candidate lead the inquiry

Use the common 60-minute sequence: orient, investigate with AI, formulate repair intent before implementation edits, repair, challenge with a related case, and hand over. Start with “What would you find out first?” Observe the candidate's chosen questions, their relevance, and use of the answers.

Answer factual questions without supplying the diagnosis. Use neutral follow-ups such as “Why that question?” and “What would the answer change?” The mechanism-specific prompts below are hints when supplied before discovery; record that assistance. Make evidence notes along the way and assign rubric ratings afterward. Case-specific anchors and this guide are interviewer materials.

## Evidence opportunities

The model must account for a bank effect that exists without a local terminal record. A timeout does not reveal whether a request failed to arrive or succeeded with a lost response.

Relevant properties include one successful charge per logical payment, immutable payload binding, truthful local outcomes, durable recovery intent, and eventual reconciliation under the published assumptions.

## Multiple viable approaches

- A durable payment intent and recovery state machine using one stable bank key, lookup, and retry of the same operation.
- A transactionally recorded intent and outbox, with a recovery dispatcher that uses the same stable bank identity and reconciles terminal results.

An outbox does not make delivery exactly once or atomically include the bank. The provider's idempotency contract and the recovery protocol are material to the guarantee.

## Primary replay

The bank successfully charges payment P. Its response is lost. A worker retries after assuming the timeout meant failure.

If a fresh bank key is used, the simulator can charge again. Check the independent bank ledger, not only the local payment row.

Ask the candidate to identify which identity is stable across attempts and where it becomes durable.

## Common adjacent case

The bank charges P, the worker crashes before persisting local success, and recovery finds only a pending local intent.

Recovery must locate or retry the same logical bank operation and eventually persist the matching terminal result. A not-found lookup cannot justify declaring that an earlier in-flight request will never charge.

Include simultaneous recovery attempts and replay of an already recorded success. The provider contract can make repeated same-key requests safe; local state must also converge without conflicting outcomes.

## Map to the rubric

| Dimension | Domain observation |
| --- | --- |
| Problem formulation | Resolves the bank's actual idempotency and lookup guarantees |
| State modeling | Includes external ledger, in-flight messages, and durable local intent |
| Safety and transitions | Keeps a stable operation identity and records truthful terminal outcomes |
| Constraints and progress | Schedules durable reconciliation and states eventual bank and communication assumptions |
| Falsification and evidence | Reproduces the bank-committed/local-pending window and inspects both sides |
| Revision and delivery | Handles restart and simultaneous recovery without new charge identities |

## Clarifications and hints

The base provider guarantees are deliberately sufficient for the stated outcome. A directional hint can distinguish a lost request from a lost response. A mechanism hint can identify bank-side operation identity. Record assistance.

Use the [common timeline](../../docs/interview-process.md). Finite provider deduplication retention is optional follow-up work. Supply a new contract before introducing it. With unbounded delayed requests and inadequate provider guarantees, an explicit impossibility or weakened-guarantee argument may be the correct response.

## Readiness

Run python3 interview.py verify before a session. Six starter checks fail intentionally; reference.py passes all eleven. Use the [intent example](example-intent.md) and [scenario rubric](rubric.md).

payment_base.py supplies durable intents. bank_simulator.py has its own ledger and controls for lost responses, delayed requests, and unavailability. The reference reuses one stable bank key, retains pending on timeout, and reconciles before publishing a terminal local result.

Checks exercise all three crash boundaries and simultaneous recovery. The simulator is checked locally; human pilots and AI-only measurements remain unperformed.
