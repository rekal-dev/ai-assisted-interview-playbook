# Scenario catalog

[Back to README](../README.md)

All four packets use the [60-minute process](../docs/interview-process.md), [six common dimensions](../docs/rubric.md), and [scorecard](../templates/scorecard.md).

| Packet | Candidate must reason about | Primary evidence opportunity | Readiness |
| --- | --- | --- | --- |
| [Reservations](01-reservations/README.md) | Capacity and temporary claims | Delayed confirmation after reassignment | Specification and interviewer guide |
| [Durable jobs](02-durable-jobs/README.md) | Ownership across worker failures | Stale worker attempts to publish | Specification and interviewer guide |
| [Event projections](03-event-projections/README.md) | Source order and derived state | Older events arriving after deletion | Specification and interviewer guide |
| [Payment recovery](04-payment-recovery/README.md) | An external effect with a lost response | Recovery after the bank committed | Specification and interviewer guide |

The first packet develops the original reservation example. The other three vary the modeling boundary and failure mechanism while retaining the same assessment structure.

These are documentation specifications. Runnable starters, simulators, reference repairs, and pilot results are not yet included. Prepare and validate them before administering a coding session.

An adjacent case challenges the primary repair within the published contract. Larger feature extensions are optional follow-up work. Four stories are not automatically equivalent in difficulty; use [calibration](../docs/calibration.md).
