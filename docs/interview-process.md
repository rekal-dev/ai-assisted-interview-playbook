# The 60 minute interview

[Back to README](../README.md)

## Scope

Use one prepared scenario and unrestricted AI. The required result is one reproduced failure, a supported repair of its relevant transition, an adjacent regression check, and a concise handoff.

The shorter format reduces work scope. It does not ask candidates to complete a larger exercise faster. Environment setup happens before the assessment clock. A broad feature extension is optional follow-up work.

## Prepare before the session

- Choose one [scenario](../scenarios/README.md) and document its version.
- Assemble its starter, incident material, environment contract, and replay facilities.
- Make all material facts and rubric criteria available to the candidate and their tools.
- Select the same adjacent failure case for comparable candidates.
- Verify that the environment supports at least two defensible approaches.
- Prepare common factual clarifications and a recorded hint ladder.
- Pilot the time allocation; the specifications alone are not runnable interview kits.

## Timeline

| Start | End | Activity | Common probe | Evidence |
| --- | --- | --- | --- | --- |
| 0 | 5 | Orient and scope | What is in scope, and what will you deliver? | Shared contract and environment issues |
| 5 | 12 | Clarify and model | Which uncertainty could most change your design? | Facts, assumptions, chosen distinctions |
| 12 | 22 | Predict and reproduce | What outcomes would distinguish your explanations? | Prediction and failing trace |
| 22 | 40 | Repair and check | Where is the relevant guarantee enforced? | Authoritative boundary, patch, actual result |
| 40 | 52 | Challenge and revise | Which earlier claim does this case exercise? | Adjacent case, result, revision |
| 52 | 60 | Deliver and qualify | What can the next engineer rely on? | Artifact, guarantees, limits, next check |

## Observable decision loop

Capture a few consequential sequences:

1. An observed fact or unresolved requirement.
2. A working explanation or required property.
3. A selected action that could change the next decision.
4. A prediction made before the relevant result is revealed.
5. Evidence obtained through inspection, AI, execution, or checking.
6. A comparison with the prediction.
7. A model revision, implementation revision, or justified stopping decision.

The candidate can use AI while forming predictions and deciding experiments. Capture the prediction before the result; do not infer it retrospectively from a polished explanation.

Do not demand continuous narration, a private thought transcript, or an AI model's hidden reasoning. Brief milestone summaries, prompts, changes, and execution artifacts are sufficient.

## Keep ownership of the investigation open

Candidates choose their tool use, representation, and order of investigation. Common probes elicit evidence without prescribing the model or fix.

Facts must be accessible through a consistent contract or clarification sheet. Do not reward guessing unstated requirements. Held-out traces must remain inside the published semantics and failure categories.

If a candidate fixes several issues through effective delegation, inspect the delivered evidence and award the supported score. Do not add arbitrary work just to keep them busy.

## Adjacent failure case

Choose a second case that challenges the first repair's assumptions:

- Reservations: replay a committed confirmation after response loss and expiry.
- Durable jobs: resume a stale worker after a newer claim and result.
- Event projections: replay an older update after a deletion.
- Payment recovery: crash after an external charge but before local result persistence.

See the scenario guides for exact contracts. The candidate may discover the adjacent case independently; the common checkpoint still confirms coverage.

## Clarifications and hints

| Type | Administration |
| --- | --- |
| Factual clarification | Give the same documented answer; asking for it is legitimate work. |
| Neutral checkpoint | Use the common probe without suggesting a particular fix. |
| Directional hint | Identify a relevant execution class and record that it was supplied. |
| Mechanism hint | Identify the missing distinction and record its effect on what discovery was observed. |
| Implementation hint | Supply a repair boundary and assess the remaining work on its own evidence. |

Hints do not cause a uniform deduction. A supplied diagnosis may leave formulation weakly observed while subsequent repair and verification are strongly demonstrated. AI assistance is allowed throughout and is not a hint penalty.

## Handoff

Ask for a short statement of:

- What changed and the property it supports.
- The reproduced failure and related checks actually run.
- Assumptions required for safety and progress.
- Remaining failures or unexplored behavior.
- How another engineer can reproduce the result.

No production deployment, cloud integration, or exhaustive proof is required. Claims must match the evidence obtained.

Use the [scorecard](../templates/scorecard.md), [rubric](rubric.md), and [calibration guide](calibration.md).
