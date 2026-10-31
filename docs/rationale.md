# Modeling rationale

[Back to README](../README.md)

## The model is an engineering decision

Before a system is implemented, somebody chooses what counts as an entity, what identifies an operation, what information survives a crash, and which changes must be coordinated. Those choices form a model, even when they are implicit.

The interview examines whether the candidate can make the relevant choices explicit, test them against the situation, and connect the resulting properties to an implementation. Familiarity with formal notation is optional.

## State space and behavior

A state assigns values to the variables retained in the model. The state space S contains configurations expressible by those variables and their domains. Some representable configurations should never be reachable in a correct implementation.

An initial condition Init identifies the starting states. A transition relation Next(s, s′) identifies permitted steps. An execution is a sequence of states starting in Init and following Next.

An invariant I is true in every reachable state:

    for every s in Reach(Init, Next), I(s) holds

A sufficient proof uses an inductive invariant J: Init implies J; every Next step from J preserves J; and J implies I. The desired invariant I itself may need strengthening before that induction works.

Liveness is a property of executions. For example, after failures cease, an accepted operation eventually receives a definitive result. A transition being permitted does not ensure it is eventually taken; scheduling and recovery assumptions matter.

Two systems can share the same representable states and safe states while differing in their allowed transitions or progress. A system that stays in Pending forever can preserve at-most-once effects without satisfying its completion obligation.

## Constraints are distributed across the specification

| Kind | Example | Where it belongs |
| --- | --- | --- |
| State requirement | Occupied capacity never exceeds the pool | Predicate on reachable states |
| Transition requirement | Only the current hold may be confirmed | Guard and atomic change |
| Environmental assumption | Committed records survive restart | Storage model |
| Progress assumption | An available worker is eventually scheduled | Execution or fairness model |
| Timing objective | A response completes within a stated bound | Time and workload model |
| Resource limit | Memory is bounded for a stated workload | Representation and operational model |

Some temporal properties can be represented as invariants by adding history, clocks, or monitor state. That encoding does not eliminate the distinction between a snapshot, a step, and a whole execution. Statistical objectives need additional workload or probability assumptions.

These concepts support correctness reasoning. They do not replace product judgment, security analysis, performance measurement, or operational design.

## Choose distinctions that affect outcomes

Suppose a seat is held by Alice, her hold expires, and Bob obtains a new hold on that seat. Alice's delayed confirmation arrives.

If the implementation reasons only about the seat and its current availability, it may conflate two different acquisition attempts. A useful model distinguishes a resource identity from a particular claim on that resource.

The complete reasoning model may include:

- Durable holds and confirmed bookings.
- Request identities and recorded outcomes.
- The authoritative clock.
- Worker-local values that can become stale.
- Requests and responses in flight.

The application need not store all of this in one table. The modeling boundary must nevertheless include any behavior needed for the correctness claim.

Expiry can be a derived predicate. A new status field or cleanup worker is not automatically required. A smaller representation is valuable when it preserves every distinction needed by the contract.

## Properties constrain implementation choices

For a capacity pool without cancellations, a useful condition is:

    confirmed_units + valid_unconfirmed_hold_units <= capacity

Related conditions cover request replay, ownership, and durable results. Preventing a negative available counter alone is insufficient: two customers can both receive successful promises while a lost update leaves the counter at zero.

The candidate must identify which reads, checks, and mutations together establish the property. Naming transactions, idempotency, or fencing is only a starting point.

The model must match the supplied environment. Treating a local database transaction as atomic with a remote bank call would omit a permitted failure. The [payment scenario](../scenarios/04-payment-recovery/README.md) deliberately exposes that boundary.

## Refinement preserves the promised behavior

Changing a representation can simplify the argument. It cannot silently remove a business obligation.

A candidate may replace a lock-based implementation with conditional writes, derive availability instead of maintaining a redundant counter, or preserve ordered facts instead of merging arbitrary mutations. The delivered behavior must still satisfy the agreed contract.

When requirements genuinely conflict, identifying the conflict and making an explicit contract decision is useful evidence. Rewording a failed guarantee until it becomes true is not a repair.

## Why this is useful for an interview

Modeling creates observable decisions: which uncertainty to resolve, which state to retain, which counterexample to construct, and which result would change the next action.

AI can assist with all of those decisions. The assessment captures the quality of the resulting investigation and artifacts. It does not treat modeling vocabulary as an inherently human advantage.

The scenario is a measurement environment. Choose it for the consequential choices and evidence it enables, then pilot whether its scores actually distinguish performance.

See [sources](sources.md) for the background state-based specification material.
