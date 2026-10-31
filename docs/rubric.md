# Intent prompt rubric

[Back to README](../README.md)

## What is scored

The repair intent and its evidence-driven revision are first-class artifacts. The candidate investigates with AI before committing to that repair instruction. Score their understanding of the core problem, choice of approach, and judgment while directing AI. Use fact notes, the investigation request, repair intent, short explanations, code, and observed behavior to locate those decisions.

Ask for concise decisions and reasons at milestones. A private thought transcript or continuous narration is unnecessary.

A concise prompt may score strongly. Generic terminology, a long checklist, eloquence, or the number of AI calls earns no points by itself. AI may help formulate the prompt.

Record functional conformance separately. A generated implementation passing all checks does not automatically establish strong problem-formulation evidence; an intelligent prompt also does not erase a known code failure.

## What to observe

Let the candidate choose the inquiry. Begin with the task and a neutral invitation such as “What would you find out first?” Answer factual questions, observe the requests they direct to AI, and follow their chosen investigation. A question can be answered by reading code or consulting the contract; unnecessary question-asking earns no extra credit.

Share broad assessment criteria. Keep the case-specific diagnosis examples out of the default candidate packet. Reserve leading mechanism questions for recorded hints after the candidate has had an opportunity to discover the issue. Public materials remain accessible; separation of packets is an administration choice, not a claim of secrecy or AI resistance.

| Probe | Evidence to record |
| --- | --- |
| What do you know, and what are you assuming? | Distinguishes requirements and observations from hypotheses; resolves the unknown that changes the design |
| What is the core problem behind this symptom? | A causal explanation tied to the supplied code and incident |
| What could you change, and why choose this approach? | A relevant alternative or trade-off, the provided guarantees it uses, and the reason for the choice |
| What should AI do first? | A specific investigation or change that follows from that explanation |
| AI proposes this patch. Why accept, revise, or reject it? | The candidate connects the proposal to the required behavior and notices unsupported assumptions |
| What would happen in this related case? | A prediction that follows from the chosen model, with an explanation or targeted observation |
| What changed your mind? | A revised instruction that addresses the underlying issue and preserves earlier requirements |

The number of passing checks determines no reasoning rating. A code walkthrough, a short execution trace, or a targeted experiment can support an explanation. Ask for a meaningful alternative when there is a consequential choice; unnecessary redesign earns no extra credit. Record actual test results and incomplete implementation separately.

## Score along the way

| Phase | Signal to observe | Dimensions informed |
| --- | --- | --- |
| Investigation | Chooses a question that resolves a consequential uncertainty; distinguishes an answer from an assumption and uses its source | Problem formulation; constraints and progress |
| Formulation | Connects the answer to a causal explanation and chooses a model or approach for a stated reason | State modeling; safety and transitions |
| AI-assisted repair | Gives a purposeful instruction and explains accepting, changing, or rejecting the resulting proposal | Safety and transitions; revision and delivery |
| Related case | Chooses or interprets a case that challenges the approach, predicts its consequence, and revises when needed | Falsification and evidence; revision and delivery |
| Handoff | Explains supported behavior and remaining uncertainty without overstating the result | Constraints and progress; revision and delivery |

Record a short evidence note when the choice happens; assign the dimension ratings after the session. Score relevance, prioritization, and use of the answer. Question count, specialist vocabulary, and an AI-generated list of questions alone do not establish understanding.

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
| 2 | Explains the core problem behind the symptom, states the outcome and non-goals, and identifies the failure to own. |
| 3 | Distinguishes plausible interpretations, prioritizes the question that changes the design, and makes the chosen contract explicit. |

## 2 State modeling

| Rating | Observable anchor |
| --- | --- |
| 0 | Conflates configurations requiring different outcomes and preserves that conflation in the final instruction. |
| 1 | Lists statuses or components without the identity, history, authority, or durability needed by the case. |
| 2 | Specifies distinctions and boundaries sufficient to reason about the relevant execution. |
| 3 | Compares a relevant alternative or trade-off, justifies the chosen distinctions, and explains which required behavior a simpler or different model must preserve. |

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
| 2 | Predicts a relevant execution and uses a walkthrough, trace, or targeted experiment to assess the explanation. |
| 3 | Chooses a case that distinguishes competing explanations or exposes a limit of the approach, and explains what its evidence establishes. |

## 6 Revision and delivery

| Rating | Observable anchor |
| --- | --- |
| 0 | Ignores decisive new evidence or delivers a claim inconsistent with the artifact. |
| 1 | Requests a patch for the observed output without revising the model or documenting remaining gaps. |
| 2 | Explains why AI's proposal is accepted or revised, updates the instruction in response to evidence, and identifies delivery gaps. |
| 3 | Revises the underlying distinction or assumption, explains the adjacent case coherently, and hands over a scoped result with precise remaining limits. |

## Evidence notes

Useful: the initial prompt treated timeout as failure; after observing a bank charge with a lost response, the revised prompt distinguishes unknown from declined, requires one stable bank identity, and directs a crash/recovery check.

Insufficient: good instincts, great prompts, senior thinking.

Factual clarification is legitimate work. Record interviewer hints that supply a diagnosis or repair. AI suggestions are allowed; capture what the candidate adopts, tests, and revises.

A second model's agreement is not a checked proof. A bounded test or model check applies to its stated model and bounds.

Use [calibration](calibration.md) to establish rating agreement and any role-specific interpretation.
