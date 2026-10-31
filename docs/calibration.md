# Pilot and calibration

[Back to README](../README.md)

## Three separate claims

Keep these questions separate:

1. Can assessors consistently describe the evidence from this session?
2. Does this scenario distinguish performance among candidates using AI?
3. Do those observations predict work that matters in the target role?

A clear rubric helps the first. It does not establish the second or third.

## Pilot the complete 60 minute experience

Use the included executable packet and first run python3 interview.py verify. Run the session with engineers representative of the role. Measure time spent on orientation, reading, reproduction, repair, verification, and handoff.

If setup or code comprehension overwhelms the session, reduce the materials or repair scope. Keep the 60-minute core: AI-assisted fact-finding, problem formulation and approach choice, repair intent before implementation edits, a scoped repair, related-case evidence, revised intent, and handoff. Do not turn a larger feature extension into an unstated pass condition.

Check that the contract is achievable with the supplied primitives and that more than one defensible representation can earn the strongest ratings.

## AI-only baseline

Run repeated autonomous attempts with:

- The same candidate brief, environment contract, broad assessment criteria, and comparable access to public materials. Record any access to worked answers or case-specific rubric anchors.
- Comparable tool access, files, wall-clock time, and resource budget.
- The same ability to obtain factual clarifications, through a consistent channel.
- The same published failure categories and evaluation standard.

Use the [baseline record](../templates/ai-baseline.md). Record model, agent, harness, and scenario versions. Distinguish a proposed result from a check actually executed.

A human asking a stakeholder for information is not comparable to an agent denied the same information. Conversely, an agent given a complete hidden answer is not a comparable baseline for a candidate given only symptoms.

Repeated runs reveal variability; a small pilot does not establish statistical validity. Do not infer a stable human advantage from one agent failure.

If the agent consistently saturates the rubric, the exercise has limited resolution for distinguishing candidates. Hiding the rubric is not a dependable repair. Improve job relevance or observation depth, or replace the exercise.

## Calibrate assessors

Have assessors independently score the same pilot evidence before discussion. For each disagreement:

1. Identify the dimension and claimed anchor.
2. Locate the timestamp, artifact, or result supporting it.
3. Separate a factual clarification, interviewer hint, AI suggestion, and candidate intervention.
4. Resolve ambiguous wording in the rubric or retain uncertainty.

Use N/E when the opportunity was not elicited. Do not translate missing observation into demonstrated failure. A supplied diagnosis may reduce evidence for discovery while leaving repair and verification fully observable.

Equal weighting is a reasonable starting proposal when there is no documented role-specific rationale for different weights. Preserve the dimension profile and any known central contract violation rather than relying only on a total.

## Compare scenarios carefully

Different stories can impose different reading burdens, prerequisite knowledge, and opportunities for evidence. An expiry race and a remote side-effect recovery problem are not automatically equivalent in difficulty.

Record which dimensions were exercised, how much assistance was supplied, and where time was spent. Calibrate alternative scenarios before treating their scores as interchangeable.

## Reassess

Re-run pilots when models, tools, starter code, environment guarantees, or scoring anchors change. Retain previous results with their versions; do not overwrite history to imply a framework was always calibrated.

Avoid a universal numerical hire threshold until role-specific evidence supports an interpretation. This repository currently contains no pilot dataset or validated predictive claim.
