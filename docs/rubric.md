# Observable rubric

[Back to README](../README.md)

## How to rate

Score the six dimensions separately. Every score needs an observed decision, artifact, or result. A proposed equal-weight profile is a starting point for piloting; no hiring cutoff has been validated.

| Rating | Meaning |
| --- | --- |
| 0 | An observed central contradiction or relevant failure remains unresolved. |
| 1 | Relevant work is present, with material gaps. |
| 2 | The main claim is supported within the exercise. |
| 3 | Evidence withstands relevant variations and the claim has precise limits. |
| N/E | The session did not elicit enough evidence. This is not zero. |

The anchors below define what those ratings mean in context. Scenario guides supply domain examples, not extra hidden scoring dimensions.

## 1 Problem formulation

| Rating | Behavioral anchor |
| --- | --- |
| 0 | Delivers behavior inconsistent with a central requirement and does not reconcile an observable discrepancy. |
| 1 | States the goal but leaves a material ambiguity unresolved or assumes an environmental guarantee that is not provided. |
| 2 | Defines a scoped contract, separates facts from assumptions, and resolves semantics relevant to the chosen design. |
| 3 | Meets 2 and prioritizes the uncertainty that would most change the design; explains alternative contracts and makes the consequential decision explicit. |

Look for a material question, its answer, and its consequence. Question count is not evidence of quality.

## 2 State modeling

| Rating | Behavioral anchor |
| --- | --- |
| 0 | The delivered representation conflates configurations that require different outcomes. |
| 1 | Represents normal behavior but omits information needed for a permitted replay, reordering, reassignment, or restart. |
| 2 | Preserves relevant identities and authoritative facts, including stale local information and external state when the claim requires it. |
| 3 | Meets 2 and explains why consequential distinctions are necessary; derives or removes redundant state without losing relevant behavior and can justify another viable representation. |

More fields and services are not automatically better. State names alone do not describe the full system model.

## 3 Safety and transitions

| Rating | Behavioral anchor |
| --- | --- |
| 0 | A permitted execution violates a claimed central guarantee and the final claim remains unchanged. |
| 1 | Names plausible properties but supports only sequential success or leaves concurrency and mutation boundaries unexplained. |
| 2 | States relevant safety conditions and connects them to the authoritative guards and mutations for competing operations and replay. |
| 3 | Meets 2 and accounts for all relevant mutation paths exercised by the scenario; detects when a proposed fix merely moves the violation elsewhere. |

The implementation must enforce the property it claims. Terminology such as transaction, idempotency, monotonicity, or fencing is insufficient by itself.

## 4 Liveness and recovery

| Rating | Behavioral anchor |
| --- | --- |
| 0 | Preserves safety by indefinitely blocking legitimate work or stranding recoverable state under the stated recovery conditions. |
| 1 | Suggests retries, cleanup, or scheduling generally while leaving the relevant progress mechanism or assumptions unresolved. |
| 2 | Shows the progress mechanism and identifies the availability, delivery, scheduling, and recovery assumptions it needs. |
| 3 | Meets 2 and investigates a repeated-retry or starvation case; distinguishes eventual progress from a bounded completion-time claim. |

Legitimate rejections can be definitive outcomes. Liveness does not imply every customer gets capacity or every payment succeeds.

## 5 Investigation and evidence

| Rating | Behavioral anchor |
| --- | --- |
| 0 | Leaves a central claim contradicted by observed evidence or reports checks as executed when they were not. |
| 1 | Runs examples or accepts generated checks that do not distinguish the relevant hypothesis or independently check the requirement. |
| 2 | Records a prediction, reproduces a valid failure, runs a repair against it, and retains evidence of a relevant regression check. |
| 3 | Meets 2 and reduces or generalizes the failure, seeks plausible disconfirming evidence, and accurately describes test or model-checking limits. |

A second model agreeing with the first is not equivalent to an executed check. A bounded replay or model check establishes a result for its specified conditions and bounds.

## 6 Adaptation and delivery

| Rating | Behavioral anchor |
| --- | --- |
| 0 | Delivers an artifact that does not support its claimed behavior and omits a known central failure from the handoff. |
| 1 | Patches one observed example while leaving a related failure unresolved, or gives an explanation inconsistent with the final artifact. |
| 2 | Revises the model or implementation in response to evidence, preserves relevant earlier behavior, and provides a reproducible result with explicit limitations. |
| 3 | Meets 2 and handles the common adjacent case through a coherent generalization; explains why the argument extends without unnecessary scope expansion. |

A larger feature extension is not needed for a score of 3 in the 60-minute format.

## Prompt and delegation evidence

A candidate prompt can encode context selection, an identity distinction, a hypothesis, a counterexample, a proposed repair, or a stopping condition. Assess whether those choices lead to supported outcomes.

Do not score wording sophistication, prompt length, number of calls, manual coding volume, constant narration, or performative disagreement with AI. Effective autonomous delegation can earn full credit.

Record interviewer hints separately from ordinary factual answers and permitted AI suggestions. A supplied diagnosis changes what was observed about discovery; it does not erase evidence of later repair and verification.

## Write defensible notes

Useful: before replay, the candidate predicted that a delayed request would cross an ownership boundary; the replay failed; the repair added an authoritative distinction and passed both that trace and committed-result replay.

Insufficient: good instincts, senior thinking, excellent prompts.

Assessors should score independently before discussing differences. Reconcile ratings against observations, retain N/E when appropriate, and do not average away a known central contract violation.

Use [calibration](calibration.md) before choosing role-specific interpretation or thresholds.
