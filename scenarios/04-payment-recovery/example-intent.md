# Example intent and revision

Interviewer reference after initial investigation. The candidate chooses the inquiry and wording; this is one possible repair instruction and revision.

## Repair instruction after initial investigation

Treat logical payment identity separately from transport attempts. Model the local durable intent, bank ledger, and requests still in flight. The bank deduplicates one stable key for this exercise; our database cannot atomically include its effect.

Predict a successful bank charge with a lost response. Timeout leaves the result uncertain, not declined. Keep one durable bank key across retries and reconciliation. Inspect the bank ledger as well as local status, and ask AI to reproduce the double-charge trace before changing the processing method.

## Revision after adjacent evidence

A not-found lookup did not prove the original request was gone. Require retries to use the same key even after not found. Ask AI to deliver the delayed first request after recovery, and run simultaneous recovery with the supplied barrier. Check the before-bank, after-bank, and after-local-persist windows. Preserve definitive decline and exact success replay; state that finite provider key retention would require a new contract.
