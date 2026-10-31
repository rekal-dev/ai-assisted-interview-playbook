# Scenario catalog

[Back to README](../README.md)

All four packets use the [60-minute process](../docs/interview-process.md), [six common dimensions](../docs/rubric.md), and [scorecard](../templates/scorecard.md).

| Packet | Candidate must reason about | Primary evidence opportunity | Readiness |
| --- | --- | --- | --- |
| [Reservations](01-reservations/README.md) | Capacity and temporary claims | Delayed confirmation after reassignment | Executable kit |
| [Durable jobs](02-durable-jobs/README.md) | Ownership across worker failures | Stale worker attempts to publish | Executable kit |
| [Event projections](03-event-projections/README.md) | Source order and derived state | Older events arriving after deletion | Executable kit |
| [Payment recovery](04-payment-recovery/README.md) | An external effect with a lost response | Recovery after the bank committed | Executable kit |

The four packets vary the modeling boundary and failure mechanism while retaining the same assessment structure.

All four packets include runnable starters, reference repairs, deterministic contract checks, incidents, intent worksheets, and scenario rubrics. Run python3 interview.py verify, then export a self-contained packet.

Human pilot and AI-only baseline results are not yet included.

An adjacent case challenges the primary repair within the published contract. Larger feature extensions are optional follow-up work. Four stories are not automatically equivalent in difficulty; use [calibration](../docs/calibration.md).
