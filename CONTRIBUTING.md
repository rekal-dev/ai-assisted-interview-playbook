# Contributing

The repository develops a reusable assessment pattern. Contributions should improve the relationship between a scenario, observable engineering decisions, and supported ratings.

## Add a scenario

1. Start with the [scenario template](templates/scenario.md).
2. Give a situation with a consequential, observable failure.
3. Publish the environment guarantees, permitted failures, and required outcomes.
4. Leave representation, investigation order, and implementation strategy open.
5. Keep the [60-minute result](docs/interview-process.md) small enough to complete with prepared materials.
6. Document at least two defensible approaches and implementation-independent checks.
7. Map observations to the existing [six rubric dimensions](docs/rubric.md).
8. Record readiness and pilot status accurately.

Use one directory per scenario with a candidate README and an interviewer guide. Separating those files organizes administration; both remain public and available for AI-only baselines.

## Preserve comparison

Use common milestones, neutral probes, factual clarification rules, and an adjacent failure case selected in advance. Do not impose an extra feature as an unstated completion requirement.

Specify identities, replay behavior, time boundaries, storage guarantees, and progress assumptions wherever they affect correctness. A candidate should not need to guess an unpublished business rule.

Accept equivalent schemas and any result permitted by the contract. Difficulty should not depend on one obscure algorithm, preferred vendor, or exact field name.

## Add executable materials

Starter code should be small, deterministic, and runnable without cloud setup. A harness should expose histories and effects, support reproducible failure injection, and check published properties.

Document actual run commands and dependencies. Keep failing starter examples distinguishable from a reference repair. Mark what is checked by execution and what still depends on a model argument.

Do not claim an executable kit exists when only its specification has been written. Do not report a bounded replay as a proof about arbitrary production behavior.

## Report pilot results

Use the [scorecard](templates/scorecard.md) and [baseline record](templates/ai-baseline.md). Record versions, comparable access and resources, hint provenance, actual checks, and repeated outcomes.

Use anonymized or fictional material; do not contribute private candidate transcripts, employer incidents, credentials, or confidential code.

Describe scenario equivalence and hiring interpretation as hypotheses until supported by data. Keep previous results with their versions.

## Documentation checks

Before proposing changes, check relative links, timeline totals, rubric dimension consistency, and readiness statements. Keep canonical timing in the process guide. Scenarios should link to it rather than copy conflicting schedules.
