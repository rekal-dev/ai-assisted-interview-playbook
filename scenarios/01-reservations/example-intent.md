# Example intent and revision

This is interviewer reference material, not a required wording.

## Initial instruction

Investigate the reported old confirmation without redesigning the API. Model resource identity, a particular hold, its deadline, and a committed booking separately. A customer's live hold or booking consumes one unit; successful promises must not exceed capacity. Inspect where those facts are checked and changed.

First predict and replay A's expiry, B's acquisition, then A's confirmation. The old confirmation must fail without affecting B. Also coordinate two requests for the last seat; require one allocation. Use the supplied transaction guarantee and clock, and keep diagnostics outside the final transaction. Report the actual failing observation before proposing the smallest repair.

## Revision after adjacent evidence

The expiry guard also rejected replay of a booking already committed before response loss. Update the model to distinguish replay of a permanent result from acceptance of a new confirmation. Recognize the stored booking before applying new-confirmation expiry. Preserve stale-hold rejection. Re-run both traces, the controlled allocation race, and bounded histories. State the history bound and remaining failures.

## Scoring observation

The revision changes a consequential distinction and asks for evidence that the earlier property still holds. It earns credit through those decisions and results, not the presence of the words state or invariant.
