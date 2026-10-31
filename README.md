# AI Assisted Interview Playbook

A reusable pattern for **60-minute systems engineering interviews with unrestricted AI assistance**.

The assessment starts with a bounded situation: incomplete context, observable failures, and a precise environment. Candidates formulate the problem, choose a model, direct investigation, repair behavior, and support their conclusions with evidence.

The repository establishes the interview process, modeling rationale, observable rubrics, and a common format for adding scenarios. The scenarios make the pattern concrete; the pattern is the main contribution.

**Current status:** a documentation-first assessment framework with four scenario specifications and interviewer guides. Starter implementations, executable harnesses, pilot results, and validated hiring thresholds are future work.

## Start here

1. Read the [modeling rationale](docs/rationale.md).
2. Use the [60-minute process](docs/interview-process.md) and [observable rubric](docs/rubric.md).
3. Select a [scenario](scenarios/README.md) and prepare its required materials.
4. Record consequential decisions with the [scorecard](templates/scorecard.md).
5. Pilot with engineers and [AI-only baselines](docs/calibration.md) before using scores for selection.

## Purpose

This project develops a repeatable way to observe how engineers working with AI:

- Convert a situation into explicit requirements and assumptions.
- Choose a representation that preserves distinctions needed for correctness.
- Identify properties and connect them to actual transition boundaries.
- Investigate uncertainty through predictions, experiments, and counterexamples.
- Revise their model when evidence contradicts it.
- Deliver a result with supported guarantees and clearly stated limits.

A candidate's prompts express choices about context, goals, hypotheses, delegation, and verification. We evaluate those choices through their consequences. Prompt length, fluent narration, and specific terminology are not scoring criteria.

## Why state space and invariants

A system design contains a model of what can exist, what can change, and what behavior is acceptable. Making that model explicit exposes errors that a plausible implementation can hide.

| Concept | Question |
| --- | --- |
| State space | Which configurations can the chosen representation express? |
| Initial conditions | Which configurations may execution start from? |
| Transitions | Which changes can operations, concurrency, time, and failures cause? |
| Invariants | What must remain true in every reachable configuration? |
| Liveness | What progress must eventually occur, under which assumptions? |
| Assumptions and constraints | Which environmental guarantees, resource limits, and required outcomes apply? |

These are connected parts of a system specification. State space alone does not determine transitions or guarantee progress. Two designs can have the same status labels and preserve the same safety condition while one retries forever.

The hard modeling question is which distinctions matter. In a reservation service, a seat's identity may not distinguish an expired hold from a newer hold on that seat. Adding the right identity can expose a simple authoritative transition. Adding infrastructure without that distinction can preserve the original bug.

The invariant expresses a business obligation. Changing its representation is useful only if the externally required guarantee is preserved. See the [worked explanation and formal relationships](docs/rationale.md).

## The interview pattern

Observe a sequence of decisions:

**Observation → interpretation → model → prediction → experiment → evidence → revision**

The candidate can use AI at every step. The interviewer uses common checkpoints and evidence requests, while the candidate chooses how to investigate.

| Minutes | Activity |
| --- | --- |
| 0–5 | Understand the situation, scope, and available environment |
| 5–12 | Clarify a consequential uncertainty and propose a working model |
| 12–22 | Predict and reproduce one failure |
| 22–40 | Repair the relevant transition and check the claim |
| 40–52 | Exercise a common adjacent failure case and revise |
| 52–60 | Deliver the artifact, argument, evidence, and remaining limits |

The core deliverable is one supported repair with a relevant regression check. A larger feature extension is optional follow-up work. The [process guide](docs/interview-process.md) defines the probes, assistance rules, and scope.

## Observable rubric

The same six dimensions apply across scenarios:

| Dimension | Evidence |
| --- | --- |
| Problem formulation | Material uncertainty resolved; facts separated from assumptions |
| State modeling | Configurations requiring different outcomes remain distinguishable |
| Safety and transitions | Required properties connected to authoritative mutations |
| Liveness and recovery | Progress mechanism and necessary assumptions made explicit |
| Investigation and evidence | Prediction, discriminating experiment, actual result, and revision |
| Adaptation and delivery | Coherent repair, related regression, reproducible handoff |

Each dimension has behavioral anchors from 0 to 3, plus N/E for insufficient evidence. There is no validated numerical hiring cutoff. See the [complete anchors](docs/rubric.md) and [scorecard](templates/scorecard.md).

## Scenarios

| Scenario | Modeling focus | Status |
| --- | --- | --- |
| [Reservations](scenarios/01-reservations/README.md) | Capacity, hold identity, expiry, and committed-result replay | Specification and guide |
| [Durable jobs](scenarios/02-durable-jobs/README.md) | Lease ownership, stale workers, and one authoritative result | Specification and guide |
| [Event projections](scenarios/03-event-projections/README.md) | Ordering, versions, duplication, and deletion tombstones | Specification and guide |
| [Payment recovery](scenarios/04-payment-recovery/README.md) | External effects, uncertain outcomes, and reconciliation | Specification and guide |

Each packet includes a candidate situation, environment contract, intended evidence, and an interviewer guide with multiple valid approaches. The guides are public. Separating them from the brief helps administration; secrecy is not an assessment guarantee.

## What unrestricted AI changes

AI can propose the state space, invariants, experiments, prompts, implementation, and explanation. This framework assesses demonstrated performance **with AI**. It does not certify unaided expertise or the origin of every insight.

Effective delegation can receive full credit. If a generic agent reliably completes a scenario and saturates the rubric, that scenario has little remaining value for distinguishing candidates. Run the complete materials, including the rubric, through repeated AI-only baselines with comparable access and resources.

See [AI interaction and evidence](docs/ai-interaction.md) and [calibration](docs/calibration.md).

## Add a scenario

Use the [scenario template](templates/scenario.md) and [contribution guide](CONTRIBUTING.md). Keep the 60-minute process and six rubric dimensions stable. Add domain-specific observable examples, achievable contracts, alternative representations, and checks tied to published behavior.

Different stories are not automatically equivalent assessments. Pilot new scenarios and record where their difficulty or evidence opportunities differ.

## Next steps

- Build and validate a small deterministic starter and replay harness for reservations.
- Pilot the 60-minute format and independently score the evidence.
- Record repeated AI-only baseline results with model and harness versions.
- Prepare equivalent starter materials for the other scenarios.
- Refine the anchors from observed disagreements and job-related evidence.

Background principles and their limits are documented in [sources](docs/sources.md).

## License

[MIT](LICENSE).
