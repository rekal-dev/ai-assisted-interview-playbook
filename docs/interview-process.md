# Run a 60 minute interview

[Back to README](../README.md)

## Prepare

~~~sh
python3 interview.py verify
python3 interview.py export reservations --output candidate-packets/reservations
~~~

Choose reservations, jobs, projections, or payments. Give the exported folder to the candidate. It includes code, tests, an incident, the contract, intent.md, a rubric, and run.py. No package installation or cloud account is needed.

The starter intentionally fails. The verifier checks the reference implementations, precise starter failures, and standalone exports.

## Candidate instruction

Read the situation and inspect the code. Before editing, write the intent prompt you would give an AI collaborator in intent.md. You may use AI throughout, including to help formulate that prompt.

Express the actual engineering instruction: intended outcome, relevant state and identities, required properties, assumptions, investigation plan, and acceptance evidence. Revise it when a new result changes your model.

Repair starter.py, retain the API and test facilities, execute checks, and hand over a supported result. No private thought transcript or hidden AI reasoning is required.

## Timeline

| Start | End | Activity | Common probe | Artifact |
| --- | --- | --- | --- | --- |
| 0 | 5 | Read and inspect | What situation are you taking responsibility for? | Scope and observations |
| 5 | 12 | Formulate intent | What should AI do, preserve, assume, and verify? | Initial intent before editing |
| 12 | 22 | Predict and reproduce | What result would contradict your explanation? | Prediction and failing execution |
| 22 | 40 | Repair and check | Where must the property be enforced? | Code and actual result |
| 40 | 52 | Challenge and revise | What changes in your instruction after this case? | Adjacent result and revised intent |
| 52 | 60 | Deliver | Which promises are supported? | Handoff and scorecard |

Candidates can run or inspect the starter while learning the situation. Record a prediction before revealing the relevant new result.

## Scope and observation

The core result is one supported repair and a related regression check. Agree which failure the candidate owns within the session. Record remaining failures honestly; limited repair scope and full-suite conformance are different outcomes.

Observe:

**Observation → model → intent prompt → prediction → AI/tool action → evidence → revised intent**

The prompt is a first-class artifact. Code and execution corroborate whether its instructions are coherent. Do not score length, call count, typing volume, or performative disagreement with AI.

## Common adjacent cases

- Reservations: committed confirmation replay after response loss and expiry.
- Jobs: stale-worker publication and successful-publication replay.
- Projections: old snapshot after deletion and valid newer recreation.
- Payments: bank commit before a local result and concurrent recovery.

These executions are included in test_contract.py and remain inside the public contract. Use the same case for comparable candidates.

## Hints and handoff

Factual clarification is legitimate work. Record directional, mechanism, or implementation hints when the interviewer supplies part of the assessed reasoning. AI suggestions are permitted and are not hint penalties.

The handoff identifies the property supported, actual checks run, required assumptions, remaining failures, and reproduction commands.

Use the [six dimensions](rubric.md), scenario rubric, and [scorecard](../templates/scorecard.md). Keep functional results separate from intent ratings. N/E means an opportunity was not observed.
