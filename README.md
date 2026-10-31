# AI Assisted Interview Playbook

Ready-to-use **60-minute interviews with unrestricted AI**: runnable broken services, deterministic checks, reference repairs, candidate packets, and intent-prompt rubrics. Python 3.10+ and the standard library are sufficient.

## LeetCode is dead What are we measuring now

The original screenshots open the problem this repository addresses. Algorithm interviews compress engineering into a clean, closed world with fixed inputs and a cheap verifier. As AI becomes effective at that test, the test can lose its value as a hiring signal.

**The underlying thinking still matters.** The screenshots argue that its lasting value is the ability to define state, recognize invariants, choose an abstraction, understand constraints, and falsify a plausible solution.

Their Cracking the Safe example makes the point concrete: treating passwords as nodes suggests a search problem; treating length n−1 suffixes as nodes and passwords as edges exposes an Eulerian traversal. Choosing the model changes the work.

Real engineering adds retries, crashes, stale workers, and uncertain external effects. The article therefore proposes moving assessment toward **problem formulation and adversarial verification**. Our discussion develops that argument into this practical framework.

Read the [screenshots' argument and our analysis](docs/original-argument.md), or run its [modeling example](examples/state_space_demo.py):

~~~sh
python3 examples/state_space_demo.py --n 2 --k 2
~~~

## The intent prompt is the signal

Our working thesis is that the candidate's **intent prompt is a first-class assessment artifact**.

It expresses what the candidate thinks the problem is: which facts matter, which identities and states must be distinguished, what must remain true, what AI may assume, which trade-offs are acceptable, and what evidence would justify accepting a repair.

The candidate writes [intent.md](templates/intent.md) before editing code, uses AI freely, and revises that instruction after new evidence. We score the formulation and revision against actual behavior. Fluent prose, a generic checklist, or passing test count alone does not establish a strong intent score.

This assesses judgment, modeling, and directing engineering work with AI. AI may help formulate the prompt too; the artifact and its consequences remain observable.

## Take a packet and use it

~~~sh
git clone https://github.com/rekal-dev/ai-assisted-interview-playbook.git
cd ai-assisted-interview-playbook

# Verify references, expected starter failures, exports, and the modeling demo.
python3 interview.py verify

# Export a self-contained candidate packet.
python3 interview.py export reservations --output candidate-packets/reservations
cd candidate-packets/reservations
python3 run.py
~~~

The starter intentionally fails checks and returns exit code 1. The candidate repairs starter.py while retaining the API and harness. Each packet contains a concrete situation, incident, code, contract tests, deterministic failure controls, intent worksheet, rubric, and standalone run.py.

Reference repairs and interviewer guides are omitted from exports. They are public in this repository; export is a distribution convenience, not a secrecy guarantee.

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

The verifier checks all **40 reference contract checks**, the precise intentional starter failures, and that each exported packet runs independently. It also checks the de Bruijn construction for twelve bounded parameter combinations.

## The 60-minute interview

| Minutes | Work and observable artifact |
| --- | --- |
| 0–5 | Read the situation, code, and contract |
| 5–12 | Write the initial intent prompt before editing |
| 12–22 | Ask AI to investigate; predict and reproduce one failure |
| 22–40 | Direct a repair and check its claimed property |
| 40–52 | Exercise an adjacent case and revise the intent prompt |
| 52–60 | Hand over code, evidence, revised intent, and remaining limits |

One supported repair and an adjacent check form the core exercise. A production rewrite or larger feature extension is not required.

Use the [administration guide](docs/interview-process.md) and [scorecard](templates/scorecard.md).

## Rubric

| Dimension | Inspect in the intent prompt and its revision |
| --- | --- |
| Problem formulation | Intended outcome, material uncertainty, and chosen scope |
| State modeling | Identities, authoritative state, and distinctions affecting outcomes |
| Safety and transitions | Invariants and the mutation boundary that must enforce them |
| Constraints and progress | Environmental assumptions, recovery, and eventual outcomes |
| Falsification and evidence | A counterexample, predicted result, and acceptance checks |
| Revision and delivery | Evidence that changed the instruction and what remains supported |

Use the [common 0–3 anchors](docs/rubric.md) and each exercise's concrete rubric and named checks. N/E means insufficient evidence. Functional check results and intent ratings are recorded separately.

## What runs locally

MemoryStore provides serializable in-memory transactions and survives simulated worker-object restarts. Clock and Hooks make races and crash windows reproducible. The bank simulator has a separate ledger. No cloud credentials or external dependencies are required.

These environments do not model disk loss, production databases, or arbitrary network behavior. Bounded exploration supports its stated bounds. Human pilots, AI-only baseline measurements, equivalent-difficulty claims, and hiring thresholds remain unvalidated; see [calibration](docs/calibration.md).

## Extend the framework

Add runnable situations that expose different modeling decisions while retaining the process and rubric. Start with [contributing](CONTRIBUTING.md), the [scenario template](templates/scenario.md), and the [baseline record](templates/ai-baseline.md).

Further detail: [state-space rationale](docs/rationale.md), [AI interaction](docs/ai-interaction.md), [sources](docs/sources.md).

## License

[MIT](LICENSE).
