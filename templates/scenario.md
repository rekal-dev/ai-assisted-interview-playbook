# Scenario title

Describe the service, one concrete symptom, and the requested outcome in two or three sentences. Use ordinary engineering language. Leave the diagnosis and approach to the candidate.

State the time limit, allowed AI use, language version, and dependencies. The default is 60 minutes, unrestricted AI, and Python 3.10+ with the standard library.

## 1. Here is the code

Link directly to the editable starter and identify the methods to investigate. Link to the supplied checks and incident. Describe any prepared infrastructure in one sentence.

Give the actual run command and explain that initial failures are intentional. Use repository-root commands in the scenario README and standalone commands in CANDIDATE.md, which becomes the exported README.

| API to keep | Result |
| --- | --- |
| List the public constructor and methods | State return shapes and relevant errors |

Include a small input example if its shape is not obvious.

## 2. What you can and cannot change

Name the editable file, permitted helpers, and any freedom to change the internal representation. List the fixed files, API, checks, and diagnostic boundaries explicitly.

Publish the facts needed to reason about the task: identity and replay rules, authoritative state, atomicity, durability, time or ordering, permitted failures, progress assumptions, and workload bounds. State exclusions. All material facts must be available to the candidate and AI tools.

Do not prescribe a particular schema, algorithm, or repair in this section.

## 3. Expected behavior

| When | Expected result |
| --- | --- |
| Give a concrete sequence from the incident | Describe the externally observable result |
| Give a related retry, restart, or concurrency case | State which promise still holds |
| Give a legitimate outcome a narrow patch might block | State the progress or replay requirement |

Keep all evaluation cases inside the published contract. For the 60-minute session, agree one failure to own, one repair, and a related case. State that remaining failures must be reported.

## 4. What to hand over

1. Brief investigation notes: the candidate's chosen questions or requests to AI, what they learned, and what changed as a result. Keep the supplied worksheet neutral.
2. Repair intent after investigating and before implementation edits: the core problem, chosen approach, a meaningful alternative or trade-off, and the instruction to AI.
3. Changed code, a reproduction of the original failure, actual check output for the owned scope, and revised intent after evidence. Explain the guarantee, assumptions, and remaining gaps.

Use the [60-minute sequence](../docs/interview-process.md): orient, investigate, formulate repair intent, implement, challenge with a related case, and hand over. AI is available in every phase.

The [rubric](../docs/rubric.md) scores understanding, approach choice, and judgment about AI output. Tests support those claims; record functional correctness separately. A passing-check count does not set the reasoning rating.

## For interviewers

Keep administration and reference material here or in a separate guide. State readiness accurately: specification, starter available, harness checked, or piloted.

Supply starter.py, reference.py, test_contract.py, exercise.json, incident.json, CANDIDATE.md, rubric.md, interviewer-guide.md, and example-intent.md. List candidate_files and exact expected_starter_failures in exercise.json; add the slug to interview.py. Include the shared neutral intent.md worksheet in exports. Omit reference.py, rubric.md, interviewer-guide.md, and example-intent.md from candidate_files; share broad assessment criteria in the brief.

When adding or changing executable materials, use `python3 interview.py verify` to check the harness. This is an authoring check, not the candidate's rubric.

The interviewer guide should explain viable approaches and trade-offs, relevant safety and progress properties, a minimal counterexample and related case, scenario-specific observations for the six common dimensions, clarifications and recorded hints, the [60-minute process](../docs/interview-process.md), and pilot status.

Use concise probes that reveal a causal explanation, choice of approach, and evaluation of an AI proposal. Keep the rubric stable across scenarios and accept equivalent approaches supported by the contract.

Let the candidate choose the inquiry. Begin with a neutral invitation and score the relevance of the question, its priority, and use of the answer. Record diagnosis-specific prompts as hints when supplied before discovery. Observe along the way and assign final ratings after the session.
