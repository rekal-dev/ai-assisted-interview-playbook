# Intent prompt as the assessment artifact

[Back to README](../README.md)

The candidate's intent prompt is the instruction that makes a situation into directed engineering work. It selects the relevant context, an outcome, model distinctions, required properties, assumptions, delegation boundaries, and acceptance evidence.

That formulation is itself scored. Code and tool results help establish whether it is coherent and whether the candidate updates it when evidence changes.

## Capture two artifacts

1. Initial intent, after reading the situation and before code edits.
2. Revised intent after a common adjacent case or contradictory result.

Use [intent.md](../templates/intent.md). The sections are prompts for an artifact, not a requirement for long prose or disclosure of private reasoning. AI may assist throughout.

## Inspect decision content

A generic instruction such as fix the service may produce a strong implementation through delegation, but it reveals little explicit problem formulation. Record the functional result and the evidence available for each intent dimension separately.

A specific instruction can identify a state distinction, predict a failure, delegate a discriminating experiment, and define the observation required for acceptance. Its value comes from those decisions and their fit to the situation.

Do not require a particular phrase, tool, number of calls, or opposition to AI. The scoring standard is meaningful engineering content.

## Observe revision

Capture:

**Observation → model → intent prompt → prediction → AI/tool action → evidence → revised intent**

Record a prediction before the result is revealed. Inspect actual executions rather than treating an agent's claimed execution as a result. A failed first hypothesis followed by a sound revision can provide strong evidence.

Use concise milestone probes instead of continuous narration. Do not ask for an AI model's hidden reasoning or a private thought transcript.

## State the assessment claim

The artifacts demonstrate formulation and work with assistance. They do not isolate who originated every insight. Public reference repairs are available, so distribution without answers is a convenience rather than an AI-resistance guarantee.

Use [AI-only baselines](calibration.md) to test whether the exercise retains useful differentiation.
