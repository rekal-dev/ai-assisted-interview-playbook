# Reservations

Customers hold a seat for 30 virtual time units before booking it. A delayed confirmation has booked a seat that was already reassigned to someone else. Repair the supplied service.

**60 minutes. Unrestricted AI. Python 3.10+; standard library only.**

## 1. Here is the code

Start with [starter.py](starter.py): `hold()` and `confirm()` contain the behavior to investigate.

Also supplied: [behavior checks](test_contract.py) and the [starting incident](incident.json).

From the repository root, run:

~~~sh
python3 interview.py test reservations --implementation starter
~~~

Initial failures and exit code 1 are intentional.

Use AI to investigate first. Choose what to ask or inspect. Capture your repair instruction below before changing `starter.py`.

**Entry points:** `hold(request_id)`, `confirm(hold_id)`, `bookings()`, and `available()`. Constructor and receipt fields are in `starter.py`.

## 2. What you can and cannot change

**You can:** edit `starter.py`, add helpers, choose a compatible internal representation, and add checks in new files.

**Keep fixed:** `support.py` and `test_contract.py`, the runner, public signatures, and return shapes.

Keep `hold_before_commit` and `confirm_before_commit` outside the final transaction, and `confirmation_after_persist` after the booking commits.

**Provided guarantees and limits:**

The store supports serializable atomic changes and retains commits across worker restarts. One monotonic virtual clock advances between atomic actions. Calls can overlap, be delayed, or repeat after lost responses.

Request IDs and outcomes persist throughout the exercise. After faults stop, workers and storage are available and work is fairly scheduled. No payments, cancellations, refunds, authentication, deployment, disk loss, or record cleanup.

## 3. Expected behavior

| When | Expected result |
| --- | --- |
| A seat is free | `hold()` reserves one seat for 30 time units. Active holds and bookings together never exceed capacity or promise the same seat to different holds. |
| Two requests compete for the last seat | Only one receives a successful hold. |
| The same hold request is repeated | Return its original receipt, including a rejection. Do not create another hold or extend its deadline. A fresh attempt needs a fresh request ID. |
| A hold reaches its deadline | It is expired, including at exact equality. Its seat can be reused without a cleanup worker. |
| A: hold at time 0; B: hold at time 31; A: confirm, with capacity 1 | A returns `expired`; B can book. A cannot use B's newer hold. |
| A booking committed but its response was lost | Repeating that confirmation returns the original booking, even after restart or the old hold deadline. A booking keeps its seat permanently. |
| The hold ID is unknown | Return `unknown` without booking a seat. |

Own one failure, repair it, and examine a related case. The full contract stays in force; report remaining failures.

## 4. What to hand over

1. In [intent.md](../../templates/intent.md), keep the questions or instructions you chose, what you learned, and the repair instruction you gave AI before implementation edits. AI may help throughout.
2. Deliver changed code, a failure reproduction, and actual output from the checks you ran.
3. Revise your instruction after a related case or new evidence. Explain the guarantee, assumptions, and remaining gaps.

The assessment considers your understanding, approach choice, and judgment about AI output. Explain consequential decisions briefly. Passing-check count does not set this score; correctness is recorded separately.

## For interviewers

Use the [60-minute process](../../docs/interview-process.md), [interviewer guide](interviewer-guide.md), [scenario rubric](rubric.md), and [example intent and revision](example-intent.md).

From the repository root:

~~~sh
python3 interview.py test reservations --implementation reference
python3 interview.py export reservations --output candidate-packets/reservations
~~~

Give the exported folder to the candidate. Its README contains the same brief with standalone run instructions. It includes the code, checks, incident, and neutral intent worksheet. The [reference repair](reference.py), case-specific rubric, example intent, and interviewer guide remain outside the export.

Status: executable starter and reference; 9 contract checks. Human pilots and AI-only baseline measurements remain unperformed.
