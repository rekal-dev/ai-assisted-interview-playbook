# Initial intent prompt

Write the instruction you would actually give your AI collaborator before editing
the implementation. You may use AI to help formulate it. Keep it specific to the
evidence and contract in front of you; length is not a scoring criterion.

## Intended outcome and scope

What should the system promise? What are you choosing to leave outside this repair?

## Working model

Which identities, state, boundaries, and transitions matter? What is still uncertain?

## Required properties and assumptions

What must always hold? What progress is required? Which guarantees may the AI rely on?

## Investigation and delegation

What should AI investigate or change first? What result would contradict your model?
What decisions require clarification rather than an invented assumption?

## Acceptance evidence

What should be executed or inspected before you accept the repair?

# Revised intent after evidence

Record the observation that changed your instruction, the revised instruction,
and which earlier guarantee still needs to hold.

# Handoff

State the supported result, actual checks run, and remaining limits.
