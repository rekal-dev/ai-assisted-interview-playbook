# Run a 60 minute interview

[Back to README](../README.md)

## Prepare

~~~sh
python3 interview.py verify
python3 interview.py export reservations --output candidate-packets/reservations
~~~

Choose reservations, jobs, projections, or payments. Give the exported folder to the candidate. It includes code, tests, an incident, the contract, neutral intent.md, broad assessment criteria, and run.py. Keep the case-specific rubric, worked intent, and guide with the interviewer. No package installation or cloud account is needed.

The starter intentionally fails. Each packet starts with the code, editable and fixed parts, expected behavior, and handoff. The verifier checks the exercise materials before a session; it does not grade candidate understanding.

## Candidate instruction

Read the task, fixed boundaries, and expected behavior. First use AI to investigate: inspect the code, follow or reproduce the incident, and clarify facts that affect the design. In intent.md, briefly separate required behavior, observed facts, hypotheses, and unresolved questions. Preserve the useful investigation request without writing a second essay.

After that investigation, write the repair instruction before editing the implementation. Explain the core problem, relevant distinctions, required properties, chosen approach, and a meaningful alternative or trade-off. State any uncertainty that would change the choice. AI may help investigate and formulate the instruction. An AI assertion remains a hypothesis until supported by the code, supplied contract, clarification, or an observation.

## Let the candidate choose the questions

Start with “Here is the code, what is fixed, and the expected behavior. What would you find out first?” Let the candidate choose requests to AI, code to inspect, and clarifications to ask. Observe what they prioritize and what the answer changes.

Use neutral follow-ups: “Why that question?”, “What did you learn?”, and “What will you do with that answer?” The timeline probes below are options when a decision needs clarification, not a checklist to recite. Reserve prompts naming the missing mechanism for recorded hints.

Make brief rubric notes during the work and assign ratings afterward. Broad criteria are available to the candidate; diagnosis-specific examples guide the assessor. Asking a question AI suggested can still be useful evidence if the candidate explains its relevance and follows its consequence. A list of sophisticated questions without that connection gives little evidence.

Repair starter.py, retain the API and test facilities, execute checks, and hand over a supported result. No private thought transcript or hidden AI reasoning is required.

## Timeline

| Start | End | Activity | Common probe | Artifact |
| --- | --- | --- | --- | --- |
| 0 | 5 | Orient | What must work, and what is fixed? | Shared task and scope |
| 5 | 15 | Establish facts with AI | What is required, observed, inferred, or still unknown? | Brief fact notes and an investigated execution |
| 15 | 23 | Formulate repair intent | What is the core problem, which approach do you choose, and why? | Repair instruction and predicted consequence before implementation edits |
| 23 | 40 | Direct and assess a repair | Why accept or revise AI's proposal? Which promise does it preserve? | Decision, code, and supporting evidence |
| 40 | 52 | Challenge and revise | What changes in your instruction after this case? | Adjacent result and revised intent |
| 52 | 60 | Deliver | Which promises are supported? | Handoff and scorecard |

Candidates can use AI, read code, run the starter, and make scratch reproductions during investigation. Save implementation changes until the repair intent is captured. Record a prediction before revealing a relevant new result during the related-case challenge.

Fact-finding establishes a working account, not certainty about every execution. For payments, a timeout is an observation; the belief that the bank did not charge is an inference. Credit the candidate for keeping that distinction visible and choosing the next useful question or observation.

## Scope and observation

The core result is one supported repair and a related regression check. Agree which failure the candidate owns within the session. Record remaining failures honestly; limited repair scope and full-suite conformance are different outcomes.

Observe:

**Task → AI-assisted fact-finding → problem formulation and approach choice → repair intent → implementation → related-case evidence → revised intent**

The prompt is a first-class artifact. Code and execution corroborate whether its instructions are coherent. Do not score length, call count, typing volume, or performative disagreement with AI.

Score the explanation and decisions, including a useful approach that remains partly implemented. Use a walkthrough, short trace, or targeted execution to probe understanding. A full-suite pass is a separate functional outcome. Do not award reasoning points for green tests without evidence of the candidate's formulation and judgment.

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
