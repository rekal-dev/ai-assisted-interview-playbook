# Contributing runnable interview situations

Contributions should make judgment, modeling, and problem formulation observable in a concrete executable situation. Each exercise should connect the candidate's intent prompt to a consequential modeling decision, a repair, and evidence that supports it.

## Minimum exercise

Each scenario includes:

- README.md with working root commands.
- CANDIDATE.md for the standalone candidate packet.
- starter.py with a small, plausible, intentional defect.
- reference.py with a checked repair.
- test_contract.py exposing build_suite(Service).
- exercise.json listing candidate files and exact expected starter failures.
- incident.json with fictional context.
- rubric.md tying intent decisions to named checks.
- interviewer-guide.md with a reference walkthrough and adjacent case.
- Any local simulator or prepared infrastructure needed by both implementations.

Add the scenario to interview.py and the catalog. Use the existing files as an executable template. Keep dependencies in the standard library and avoid cloud setup.

Write both the scenario README and exported candidate brief in this order: code to open and run, editable and fixed parts, expected behavior, and handoff. Put administration, reference answers, and assessment guidance after the brief or in the interviewer guide. State the contract in ordinary behavior terms and leave the diagnosis and approach to the candidate.

Keep candidate worksheets neutral and omit worked prompts, references, case-specific rubric anchors, and guides from candidate_files. Share broad criteria. The candidate chooses what to ask; the assessor records why that question matters and how its answer affects the work. Diagnosis-specific prompts supplied early count as recorded hints.

## Contract and comparison

Keep the 60-minute core: AI-assisted fact-finding, problem formulation and approach choice, repair intent before implementation edits, one scoped repair, related-case evidence, revised intent, and handoff. Publish identities, replay behavior, time boundaries, storage guarantees, and progress assumptions.

Preserve the six intent dimensions. Accept equivalent representations and legal outcomes. A specific schema, vendor, vocabulary, or obscure trick must not be the only path to a strong rating.

Make core-problem understanding, approach choice, and judgment about AI output observable. Give a probe that elicits a causal explanation and a meaningful trade-off. Use checks as supporting evidence and record correctness separately; a passing-check count must not set a reasoning rating.

Hooks are diagnostic boundaries outside authoritative transactions. Keep their names and documented context stable so failures remain reproducible.

## Checks

Run python3 interview.py verify. It requires reference checks to pass, starter failures to match the manifest without infrastructure errors, and exported packets to run independently. Never silently accept any failing starter as a valid baseline.

Use implementation-independent observations and a meaningful counterexample. Record what bounded exploration does and does not establish.

## Pilot evidence

Executable correctness does not establish hiring validity. Use anonymized or fictional material, the scorecard, and repeated AI-only baselines. Record versions, comparable access and resources, actual checks, and rating disagreements.

No private candidate transcript, employer incident, credential, or confidential source code belongs in the repository.

Check relative links, current counts, timeline consistency, and readiness statements when changing the framework.
