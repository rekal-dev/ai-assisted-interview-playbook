# Scenario title

Status: specification, starter available, harness checked, or piloted. State only what exists.

## Candidate situation

Describe the system, a concrete observed failure, and the requested outcome in business terms. Avoid prescribing the internal representation.

## Scope and 60 minute result

Define one failure to reproduce, one relevant transition to repair, one adjacent check, and a concise handoff. State explicit exclusions.

## Environment contract

| Area | Supplied guarantee or requirement |
| --- | --- |
| Identities and replay | |
| Authoritative state | |
| Storage and atomicity | |
| Time and ordering | |
| Permitted failures | |
| Progress assumptions | |
| Resource or workload bounds | |

All material facts must be available to the candidate and AI tools. Distinguish missing facts from negotiable requirements.

## Materials to prepare

List starter code, incident material, simulator facilities, public checks, and common evaluation cases. Give actual run commands only when implementations exist.

## Published failure categories

Describe permitted failure categories. Evaluation cases must remain within this contract.

## Candidate deliverables

- Working state and transition model.
- Reproducible original failure.
- Repair and checks actually executed.
- Supported guarantee, assumptions, and remaining limitations.

## Interviewer guide

Create a separate guide covering:

1. At least two viable representations or approaches.
2. Relevant safety and liveness properties.
3. A minimal counterexample and adjacent regression.
4. Domain-specific observations for the six common rubric dimensions.
5. Common clarifications and a recorded hint ladder.
6. How the [60-minute process](../docs/interview-process.md) applies.
7. Pilot and AI-only baseline status.

Keep [rubric dimensions](../docs/rubric.md) stable. Do not add a hidden required trick or tool.
