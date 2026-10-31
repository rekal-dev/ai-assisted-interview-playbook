# AI Assisted Interview Playbook

When AI can complete more and more standardized coding tasks, how should an engineer demonstrate their ability? Which capabilities were algorithm interviews trying to measure, which still matter, and how do we recognize them?

## LeetCode is dead. What are we measuring now?

A company has forty-five minutes to assess an engineer. It needs interviewers with different levels of experience to evaluate thousands of candidates from different backgrounds, cheaply and consistently.

The convenient answer is an algorithm problem. Strip away business ambiguity, technical debt, and unfamiliar infrastructure. Give the candidate clear inputs, clear outputs, and a checker that can tell whether the answer works. A complicated engineering capability becomes a small, comparable test.

Then comes the arms race. Candidates learn the questions. Interviewers adapt harder competition problems. Those problems enter books and question banks. Candidates learn those too. The questions keep changing, and the preparation industry keeps catching up.

AI accelerates the same cycle. A task with fixed rules and an inexpensive automated checker is a useful target for generation, search, and verification. When a candidate can obtain a correct solution simply by handing the problem to AI, the final code tells the interviewer less about that candidate's engineering ability.

Anthropic has described this happening inside its own hiring process. In [January 2026, Tristan Hume explained](https://www.anthropic.com/research/AI-resistant-technical-evaluations) how successive Claude models overtook a performance-engineering take-home that explicitly allowed AI. Keeping the test ahead of the models pushed it toward more unusual problems, at a cost to realism. In [October 2026, engineering manager Felix Rieseberg wrote](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/) that he had stopped using traditional coding interviews and was looking for working prototypes that showed taste, empathy, and principled thinking.

Anthropic's [October 2026 study of its own workplace](https://www.anthropic.com/research/employment-at-anthropic) adds another part of the story: as agents handled more implementation, human attention became a bottleneck, and hiring assessments increasingly emphasized autonomy and judgment. These accounts make the design question concrete: how do we observe someone choosing, directing, and evaluating useful work with AI?

**The failure of a measuring tool does not mean the underlying ability has lost its value.**

Memorizing known patterns has limited value. Learning to choose a model, understand its state space, identify invariants, reason about concurrency, and find a counterexample still matters. These are the skills behind deciding what a system remembers, who owns a resource, what a retry means, and which changes must happen together.

Production adds the conditions a small coding exercise can leave out: a request is retried, a response disappears after a commit, a worker resumes after losing ownership, or an older event arrives after a deletion. A plausible implementation can pass its ordinary tests and still break a safety invariant.

As generating code becomes easier, more of the work moves from **construction to falsification**: finding where an apparently correct solution fails, identifying the assumption it violated, and repairing the model that allowed it. Challenging complex code can demand deeper understanding than writing a familiar solution from scratch.

That suggests two places to look for interview evidence: **problem formulation**, where the candidate turns an ambiguous situation into a useful model, and **adversarial verification**, where they test that model against failures and changing conditions.

This repository turns those ideas into **60-minute interviews with unrestricted AI**. Each exercise includes a runnable broken service, deterministic checks, a reference repair, a candidate packet, and an observable rubric. The purpose is to establish a reusable framework for assessing judgment, modeling, and directing work with AI, then extend it across different engineering situations. Python 3.10+ and the standard library are sufficient.

Read [why this framework](docs/why-this-framework.md).

## The intent prompt is the signal

The candidate's **intent prompt is a first-class assessment artifact**.

It expresses what the candidate thinks the problem is: which facts matter, which identities and states must be distinguished, what must remain true, what AI may assume, which trade-offs are acceptable, and what evidence would justify accepting a repair.

The candidate first uses AI to investigate: read the code, clarify the required behavior, and separate observations from assumptions. They then write a repair intent in [intent.md](templates/intent.md) before changing the implementation, and revise it after new evidence. The assessment follows their decisions: what they identify as the core problem, which approaches they consider, why they choose one, what they ask AI to do, and how they evaluate its output.

**What the candidate chooses to ask is an early signal.** Observe which uncertainty they prioritize, why the answer matters, and how they use it. AI may suggest questions; the candidate's selection and follow-through remain observable. The interviewer scores throughout, using neutral follow-ups while leaving diagnosis and approach discovery to the candidate.

Checks support that discussion. A trace, code walkthrough, or small experiment can show why an approach fits the problem. Test results are recorded separately; the number of passing tests does not set the reasoning score. A generic prompt that obtains correct code can leave the candidate's understanding unobserved.

This assesses judgment, modeling, and directing engineering work with AI. AI may help formulate the prompt too; the artifact and its consequences remain observable.

## Take a packet and use it

~~~sh
git clone https://github.com/rekal-dev/ai-assisted-interview-playbook.git
cd ai-assisted-interview-playbook

# Export a self-contained candidate packet.
python3 interview.py export reservations --output candidate-packets/reservations
cd candidate-packets/reservations
python3 run.py
~~~

The starter intentionally fails checks and returns exit code 1. The candidate repairs starter.py while retaining the API and harness. Each packet contains a concrete situation, incident, code, contract tests, deterministic failure controls, neutral intent worksheet, broad assessment criteria, and standalone run.py.

Reference repairs, case-specific rubric anchors, example prompts, and interviewer guides are omitted from exports. They are public in this repository; export is a distribution convenience, not a secrecy guarantee.

From the repository root:

~~~sh
python3 interview.py list
python3 interview.py test reservations --implementation starter
python3 interview.py test reservations --implementation reference
python3 interview.py test jobs --implementation reference
python3 interview.py test projections --implementation reference
python3 interview.py test payments --implementation reference
~~~

## Four executable exercises

| Exercise | Modeling problem | Included code and checks |
| --- | --- | --- |
| [Reservations](scenarios/01-reservations/README.md) | Capacity, claim identity, and committed-result replay | Starter, reference, 9 checks, incident, rubric |
| [Durable jobs](scenarios/02-durable-jobs/README.md) | Stale workers and temporary authority | Starter, reference, queue infrastructure, 10 checks, rubric |
| [Event projections](scenarios/03-event-projections/README.md) | Source ordering and deletion history | Starter, reference, 10 checks, delivery permutations, rubric |
| [Payment recovery](scenarios/04-payment-recovery/README.md) | Uncertain external effects and reconciliation | Starter, reference, bank simulator, 11 checks, rubric |

Each scenario opens with the code, what may change, what must stay fixed, expected behavior, and the handoff. The candidate chooses how to diagnose the problem and approach the repair.

For interviewers, `python3 interview.py verify` checks the supplied references, intentional starter failures, and exports. It is a maintenance check for the exercise materials; it does not score a candidate.

## The 60-minute interview

| Minutes | Work and observable artifact |
| --- | --- |
| 0–5 | Read the task, fixed boundaries, and expected behavior |
| 5–15 | Investigate with AI; distinguish facts, requirements, hypotheses, and unknowns |
| 15–23 | Frame the core problem, compare approaches, and write repair intent before implementation edits |
| 23–40 | Direct a repair and assess AI's proposal against the chosen model |
| 40–52 | Exercise an adjacent case and revise the intent prompt |
| 52–60 | Hand over code, evidence, revised intent, and remaining limits |

Fact-finding comes before the repair instruction. It need not resolve every uncertainty: the candidate should identify which unknowns matter and what would change the approach. One scoped repair and a related case form the practical exercise.

Use the [administration guide](docs/interview-process.md) and [scorecard](templates/scorecard.md).

## Rubric

| Dimension | Inspect in the intent prompt and its revision |
| --- | --- |
| Problem formulation | Core problem behind the symptom, intended outcome, material uncertainty, and scope |
| State modeling | Useful distinctions, plausible approaches, and the reason for the chosen model |
| Safety and transitions | Why the chosen change preserves the required promise at the relevant boundary |
| Constraints and progress | Environmental assumptions, recovery, and eventual outcomes |
| Falsification and evidence | A predicted case that distinguishes competing explanations or approaches |
| Revision and delivery | How the candidate evaluates AI output, changes direction, and explains remaining limits |

Use the [common 0–3 anchors](docs/rubric.md) and each exercise's concrete rubric and named checks. N/E means insufficient evidence. Functional check results and intent ratings are recorded separately.

Share the broad criteria with the candidate. Use diagnosis-specific anchors for observation and scoring; introducing one early is an interviewer hint and should be recorded. Useful neutral probes are “What would you find out next?”, “Why that question?”, and “What would the answer change?”

## What runs locally

MemoryStore provides serializable in-memory transactions and survives simulated worker-object restarts. Clock and Hooks make races and crash windows reproducible. The bank simulator has a separate ledger. No cloud credentials or external dependencies are required.

These environments do not model disk loss, production databases, or arbitrary network behavior. Bounded exploration supports its stated bounds. Human pilots, AI-only baseline measurements, equivalent-difficulty claims, and hiring thresholds remain unvalidated; see [calibration](docs/calibration.md).

## Extend the framework

Add runnable situations that expose different modeling decisions while retaining the process and rubric. Start with [contributing](CONTRIBUTING.md), the [scenario template](templates/scenario.md), and the [baseline record](templates/ai-baseline.md).

Further detail: [state-space rationale](docs/rationale.md), [AI interaction](docs/ai-interaction.md), [sources](docs/sources.md).

## License

[MIT](LICENSE).
