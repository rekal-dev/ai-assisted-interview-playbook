# Intent prompt rubric

[Back to README](../README.md)

## What is scored

The initial intent prompt and its evidence-driven revision are first-class artifacts. Evaluate the engineering decisions they express, then use code, execution, and the handoff to check coherence.

A concise prompt may score strongly. Generic terminology, a long checklist, eloquence, or the number of AI calls earns no points by itself. AI may help formulate the prompt.

Record functional conformance separately. A generated implementation passing all checks does not automatically establish strong problem-formulation evidence; an intelligent prompt also does not erase a known code failure.

## Rating scale

| Rating | Meaning |
| --- | --- |
| 0 | Observed instruction or final claim conflicts with a central requirement and remains unreconciled. |
| 1 | Relevant intent is present but material decisions are missing. |
| 2 | Intent is specific, coherent, and supported in the owned scope. |
| 3 | The formulation withstands a relevant challenge and is revised with precise limits. |
| N/E | The session did not elicit enough evidence. This is not zero. |

Use the six dimensions below and the scenario's rubric.md. Quote the relevant instruction or revision and link the resulting evidence. Equal weighting is a pilot starting point; no universal hiring threshold is supplied.

## 1 Problem formulation

| Rating | Observable anchor |
| --- | --- |
| 0 | Directs behavior inconsistent with a core requirement and leaves the conflict unresolved. |
| 1 | Requests a fix or improvement without defining the relevant outcome, scope, or uncertainty. |
| 2 | States the outcome and non-goals, resolves a consequential fact, and identifies the failure to own. |
| 3 | Distinguishes plausible interpretations, prioritizes the question that changes the design, and makes the chosen contract explicit. |

## 2 State modeling

| Rating | Observable anchor |
| --- | --- |
| 0 | Conflates configurations requiring different outcomes and preserves that conflation in the final instruction. |
| 1 | Lists statuses or components without the identity, history, authority, or durability needed by the case. |
| 2 | Specifies distinctions and boundaries sufficient to reason about the relevant execution. |
| 3 | Justifies why those distinctions are necessary and simplifies or revises the representation without losing a required behavior. |

## 3 Safety and transitions

| Rating | Observable anchor |
| --- | --- |
| 0 | Silently weakens a business guarantee or accepts a known violation. |
| 1 | Asks for correctness, thread safety, or idempotency without a concrete property. |
| 2 | States the relevant invariant and directs attention to the authoritative guard and mutation. |
| 3 | Connects the property to initialization and relevant mutation paths, including the adjacent case or restart. |

## 4 Constraints and progress

| Rating | Observable anchor |
| --- | --- |
| 0 | Relies on an unavailable guarantee or preserves safety by permanently blocking required work. |
| 1 | Requests retries, cleanup, or performance generally without the assumptions they require. |
| 2 | States the material environmental guarantees and the mechanism for progress after recovery. |
| 3 | Separates assumptions from requirements, detects a starvation or repeated-retry risk, and distinguishes eventual progress from a bounded-time claim. |

## 5 Falsification and evidence

| Rating | Observable anchor |
| --- | --- |
| 0 | Accepts a central claim contradicted by observed results or reports checks as executed when they were not. |
| 1 | Asks for tests or review without specifying a relevant counterexample or acceptance observation. |
| 2 | Gives a predicted failing history and acceptance check, then executes or inspects the resulting evidence. |
| 3 | Seeks a plausible disconfirming case, reduces or generalizes the failure, and states the bounds of the checks. |

## 6 Revision and delivery

| Rating | Observable anchor |
| --- | --- |
| 0 | Ignores decisive new evidence or delivers a claim inconsistent with the artifact. |
| 1 | Requests a patch for the observed output without revising the model or documenting remaining gaps. |
| 2 | Updates the instruction because of evidence, preserves the earlier property, and hands over a reproducible scoped result. |
| 3 | Repairs the underlying distinction or assumption, handles the adjacent case coherently, and states what remains unverified. |

## Evidence notes

Useful: the initial prompt treated timeout as failure; after observing a bank charge with a lost response, the revised prompt distinguishes unknown from declined, requires one stable bank identity, and directs a crash/recovery check.

Insufficient: good instincts, great prompts, senior thinking.

Factual clarification is legitimate work. Record interviewer hints that supply a diagnosis or repair. AI suggestions are allowed; capture what the candidate adopts, tests, and revises.

A second model's agreement is not a checked proof. A bounded test or model check applies to its stated model and bounds.

Use [calibration](calibration.md) to establish rating agreement and any role-specific interpretation.
