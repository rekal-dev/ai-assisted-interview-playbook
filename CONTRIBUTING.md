# Contributing runnable interview situations

The original screenshots' argument and the intent-prompt thesis are the starting point. Contributions should make judgment, modeling, and problem formulation observable in a concrete executable situation.

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

## Contract and comparison

Keep the 60-minute core: initial intent, one failure, one supported repair, adjacent evidence, revised intent, and handoff. Publish identities, replay behavior, time boundaries, storage guarantees, and progress assumptions.

Preserve the six intent dimensions. Accept equivalent representations and legal outcomes. A specific schema, vendor, vocabulary, or obscure trick must not be the only path to a strong rating.

Hooks are diagnostic boundaries outside authoritative transactions. Keep their names and documented context stable so failures remain reproducible.

## Checks

Run python3 interview.py verify. It requires reference checks to pass, starter failures to match the manifest without infrastructure errors, and exported packets to run independently. Never silently accept any failing starter as a valid baseline.

Use implementation-independent observations and a meaningful counterexample. Record what bounded exploration does and does not establish.

## Pilot evidence

Executable correctness does not establish hiring validity. Use anonymized or fictional material, the scorecard, and repeated AI-only baselines. Record versions, comparable access and resources, actual checks, and rating disagreements.

No private candidate transcript, employer incident, credential, or confidential source code belongs in the repository.

Check relative links, current counts, timeline consistency, and readiness statements when changing the framework.
