# Intent prompt as the assessment artifact

[Back to README](../README.md)

The candidate's intent prompt is the instruction that makes a situation into directed engineering work. It selects the relevant context, an outcome, model distinctions, required properties, assumptions, delegation boundaries, and acceptance evidence.

That formulation is itself scored. Code and tool results help establish whether it is coherent and whether the candidate updates it when evidence changes.

Observe the candidate's explanation of the core problem, choice between useful approaches, and judgment about AI's suggestions. A concise decision note can show why a proposed patch fits the model, which alternative was considered, and which assumption would make the choice fail.

## Investigate before committing to a repair

Begin with AI-assisted fact-finding. The candidate can inspect code, ask factual questions, follow an execution, and run the supplied service. Record required behavior, observations, hypotheses, and material unknowns in brief notes. An investigation request can ask AI what to inspect without pretending the diagnosis is already established.

The candidate chooses the questions and the next action. Observe what they ask AI or the interviewer, why that uncertainty matters, and how the answer changes the work. Use a neutral notes sheet; leave the diagnosis-specific rubric with the interviewer. AI may suggest the question itself, so assess selection, interpretation, and follow-through rather than claiming unaided authorship.

Then capture the repair intent, before implementation edits: the core problem, chosen approach, relevant alternative or trade-off, and the instruction to AI. Capture its revision after a related case or contradictory result. Both stages fit in the same intent.md worksheet; separate polished documents are unnecessary.

Use [intent.md](../templates/intent.md). The sections are prompts for an artifact, not a requirement for long prose or disclosure of private reasoning. AI may assist throughout.

## Inspect decision content

A generic instruction such as fix the service may produce a strong implementation through delegation, but it reveals little explicit problem formulation. Record the functional result and the evidence available for each intent dimension separately.

A specific instruction can identify a state distinction, predict a failure, delegate a discriminating experiment, and define the observation required for acceptance. Its value comes from those decisions and their fit to the situation.

Passing tests supports claims about behavior. It does not establish who understood or chose the approach. Ask the candidate to explain the choice and predict a related case; record that evidence alongside the result.

Do not require a particular phrase, tool, number of calls, or opposition to AI. The scoring standard is meaningful engineering content.

## Observe revision

Capture:

**Task → AI-assisted fact-finding → problem formulation and approach choice → repair intent → implementation → related-case evidence → revised intent**

Record a prediction before the result is revealed. Inspect actual executions rather than treating an agent's claimed execution as a result. A failed first hypothesis followed by a sound revision can provide strong evidence.

Use concise milestone probes instead of continuous narration. Do not ask for an AI model's hidden reasoning or a private thought transcript.

## State the assessment claim

The artifacts demonstrate formulation and work with assistance. They do not isolate who originated every insight. Public reference repairs are available, so distribution without answers is a convenience rather than an AI-resistance guarantee.

Use [AI-only baselines](calibration.md) to test whether the exercise retains useful differentiation.
