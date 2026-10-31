# Why this framework

[Back to README](../README.md)

## A useful test becomes an arms race

An engineering interview faces a scaling problem: how can a company assess thousands of people with different backgrounds in a short session, using interviewers whose experience also varies?

An algorithm question makes the assessment manageable. Remove the business context, historical technical debt, and unfamiliar infrastructure. Define the inputs and outputs precisely. Supply a deterministic checker. The company can compare answers to the same bounded problem.

Preparation changes the test. Candidates learn a familiar question, interviewers adapt a harder one, and that variation eventually enters the preparation material too. More questions and harder tricks can keep the cycle going without making the task more representative of engineering work.

AI puts further pressure on this arrangement. Clear rules and cheap verification support automated attempts at a solution. As obtaining a correct answer becomes easier, that answer provides less evidence about the candidate's own judgment.

The failure of the measuring tool does not mean the underlying ability has lost its value.

## Anthropic's experience exposes the tension

In [January 2026, Tristan Hume described](https://www.anthropic.com/research/AI-resistant-technical-evaluations) a performance-engineering take-home repeatedly losing differentiation as Claude improved. His design goals included realistic work, several opportunities to demonstrate ability, and little dependence on narrow prior expertise. Making the replacement unfamiliar enough for models challenged the realism goal. The lesson for this framework is to avoid depending on one hidden insight and to measure the AI-only baseline repeatedly.

In [October 2026, Felix Rieseberg described](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/) changing his own team's approach: small coding challenges had stopped predicting the impact he cared about, and concrete prototypes offered evidence of product judgment. This framework makes the intended outcome and the reason for pursuing it part of the assessment.

Anthropic's [October 2026 workplace study](https://www.anthropic.com/research/employment-at-anthropic) reported growing emphasis on autonomy and judgment in hiring, alongside the difficulty of allocating human attention across agent output. For this playbook, choosing what to investigate and what evidence to inspect is part of the work.

These are accounts of particular teams and an internal study. Anthropic's [published candidate guidance](https://www.anthropic.com/candidate-ai-guidance) still requires explicit permission for AI during take-homes and live interviews. This repository deliberately grants that permission. Its framework and 60-minute format are design proposals that need their own pilots.

## What the questions were trying to reveal

An engineer rarely needs to implement a red-black tree from memory. But an engineer does need to decide what information a system retains, which operations are distinct, what may change together, and what must remain true after a failure.

The lasting value of algorithmic training is the habit of making those choices explicit: define a state space, recognize invariants, discover structure through abstraction, understand bounds and concurrency, and look for counterexamples.

These decisions shape service boundaries, data ownership, idempotency, monotonicity, and recovery. A useful representation can eliminate coordination that a different representation appeared to require. The representation must still preserve the business obligation.

AI can assist with these decisions too. The assessment therefore needs observable work and evidence for the resulting claims.

## A timeout makes the modeling decision concrete

A customer submits a payment. The request times out, and the customer retries.

Two different situations can produce that timeout: the request never reached the bank, or the bank charged successfully and its response was lost. Treating both situations as a definitive failure hides information needed for a safe retry.

The candidate needs to recognize the uncertainty, inspect the bank's guarantees, and choose a recovery approach that can resolve it. They might compare looking up the bank outcome before retrying with retrying the same bank operation directly. Either needs an explanation of which provider guarantee makes it safe and what survives a worker restart.

The assessment follows that decision: what did the candidate think was broken, which alternatives did they consider, why did they choose one, and how did that choice change the instruction to AI? A passing test supplies one observation about the outcome. The explanation and response to a related case provide evidence about understanding.

## Production tests the assumptions

A small algorithm exercise can fix the rules before the candidate begins. Production systems make those rules part of the engineering problem.

A database commit succeeds but its response is lost. A worker pauses, loses its lease, and later resumes. A deletion is followed by an older update. Two individually reasonable product requirements conflict under the permitted failure conditions.

The difficult bug appears where reality violates an assumption hidden in the implementation. More code or a passing happy-path test does not resolve that mismatch.

As plausible code becomes easier to generate, more attention must go to falsification: construct a failing execution, identify the violated property, and change the state or transition model so that execution is handled correctly.

## Move the assessment to formulation and verification

The interview can expose two consequential parts of this work.

**Problem formulation:** Give the candidate a concrete engineering situation with enough ambiguity to require decisions. Observe which uncertainty they resolve, which identities they distinguish, which state they treat as authoritative, and which property they choose to preserve.

**Adversarial verification:** Allow unrestricted AI, then introduce an adjacent failure within the published contract. Observe whether the candidate predicts the consequence, produces a counterexample, and directs a repair at the relevant boundary.

The exercise needs room for different useful models and firm boundaries for checking their consequences. A concrete contract, executable code, controlled failures, and observable outcomes provide those boundaries. The candidate chooses how to investigate and satisfy them.

## The intent prompt makes the thinking inspectable

The candidate first investigates with AI, separating required behavior and observed facts from hypotheses and unknowns. They then write the repair instruction before implementation edits. It captures the intended outcome, relevant context, chosen distinctions, required properties, approach choice, unresolved assumptions, and acceptance evidence.

After new evidence, the candidate revises that instruction. The revision shows whether the model changed and why.

AI may help write both versions. A polished prompt can be generated from a checklist. The assessment therefore follows the prompt into its consequences: the predicted failure, the experiment, the repair, the adjacent case, and the explanation of what remains uncertain.

Each 60-minute packet uses the same sequence:

1. Read a runnable service, contract, and incident.
2. Use AI freely to investigate; record facts, hypotheses, and material unknowns.
3. Formulate the core problem, choose an approach, and capture repair intent before implementation edits.
4. Repair a relevant transition and check its claimed property.
5. Exercise an adjacent case within the contract.
6. Capture revised intent, supporting evidence, and remaining limits.
7. Score the demonstrated decisions using common dimensions and scenario-specific anchors.

The repository supplies executable examples and a repeatable assessment structure. Human pilots and repeated AI-only baselines are still needed to establish whether its scores distinguish candidates and predict later work; see [calibration](calibration.md).
