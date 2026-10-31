# From the screenshots to this framework

[Back to README](../README.md)

## The starting problem

Starting essay: 《算法面试死后，等待平庸SDE的是更残酷的降维淘汰》, supplied as screenshots in the discussion. This page summarizes its argument and the analysis that led to the framework.

The Chinese commentary supplied in the original discussion asks what engineering interviews measure when AI can complete standardized coding tasks.

It treats algorithm interviews as a proxy: a complicated engineering capability is compressed into a short, comparable task with fixed inputs and a deterministic checker. The closed world makes evaluation inexpensive. It also makes the test a suitable target for automated generation and verification.

Its argument is that losing the proxy does not eliminate the capability it was intended to measure.

## The thinking that remains

The screenshots emphasize the ability to choose state, recognize invariants, discover structure through abstraction, understand concurrency and bounds, find counterexamples, and reformulate an inadequate model.

These abilities inform data and service boundaries, idempotency, monotonicity, and checking complex code. AI can assist with them as well. The framework does not treat them as inherently human-only tasks.

## The modeling example

Cracking the Safe asks for a shortest string containing every n-character password over an alphabet of size k.

Represent length n−1 suffixes as nodes. Each n-character password is an edge from its prefix to its suffix. An Eulerian traversal covers every password once.

There are k**n passwords. A string of length L has L−n+1 windows, so the lower bound is k**n+n−1. The construction reaches it.

~~~sh
python3 examples/state_space_demo.py --n 2 --k 2
~~~

The graph node is only part of the solver state. The code also retains traversal progress, consumed outgoing edges, and a stack. The representation exposes useful structure; renaming nodes alone does not change intrinsic problem difficulty.

## From construction to falsification

The article argues that producing plausible code shifts attention toward checking assumptions against reality. Ordinary tests may miss retries, lost responses, reordering, and concurrent ownership changes.

It proposes assessment through problem formulation and adversarial verification: give a situation, let the candidate choose a useful model, permit AI, and examine how the candidate challenges and repairs a solution.

Those proposed directions belong to the Chinese commentary. The [Felix Rieseberg post](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/) supplies the opening example of one manager changing his team's interviews; it is not a complete English version of this framework.

## The intent prompt is the signal

Our discussion identifies the candidate's evolving intent prompt as the first-class artifact.

It turns a situation into directed work: selects relevant context, defines an outcome, chooses distinctions, states properties, identifies uncertainty, delegates investigation, and specifies acceptance evidence.

The signal lies in those decisions. It is not prompt length or polished wording.

The repository operationalizes this:

1. Give an executable situation with a concrete failure.
2. Capture intent before editing.
3. Allow unrestricted AI.
4. Reproduce a counterexample and repair a relevant transition.
5. Exercise an adjacent case.
6. Capture revised intent and its evidence.
7. Score the prompt and demonstrated behavior with scenario-specific anchors.

## What remains to establish

AI may help write intent, models, tests, and code. The artifacts demonstrate assisted formulation and work; they do not isolate the origin of every insight.

The included code and checks are executable. Claims about candidate differentiation and later job performance require human pilots and repeated AI-only baselines.
