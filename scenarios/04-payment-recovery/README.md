# Payment recovery

The bank charged a customer, but its response never reached the payment service. The service reported failure. When the customer retried, the bank charged again. Repair the supplied submission and recovery behavior.

**60 minutes. Unrestricted AI. Python 3.10+; standard library only.**

## 1. Here is the code

Start with [starter.py](starter.py): `_process()` is the method to repair.

[payment_base.py](payment_base.py) already stores accepted payments and provides the public API. [bank_simulator.py](bank_simulator.py) supplies a separate bank ledger and controllable failures. You do not need to build either.

Also supplied: [behavior checks](test_contract.py) and the [starting incident](incident.json).

From the repository root, run:

~~~sh
python3 interview.py test payments --implementation starter
~~~

Initial failures and exit code 1 are intentional.

Use AI to investigate first. Choose what to ask or inspect. Capture your repair instruction below before changing `starter.py`.

**Entry points:** `submit(payment_id, payload)`, `get(payment_id)`, `reconcile(payment_id)`, and `recover()`. The prepared base defines signatures and receipt fields.

Payload: `{"amount": 100, "currency": "AUD", "customer": "C"}`, with a positive integer amount. `customer="declined"` produces a bank decline. Receipt status is `pending`, `succeeded`, or `declined`.

## 2. What you can and cannot change

**You can:** edit `starter.py`, add helpers, choose a compatible internal representation, and add checks in new files.

**Keep fixed:** `payment_base.py`, `bank_simulator.py`, `support.py`, and `test_contract.py`, the runner, public signatures, and return shapes.

Keep `payment_before_bank`, `payment_after_bank`, and `payment_after_persist` at their named boundaries, outside local transactions.

**Provided guarantees and limits:**

Local transactions are serializable and commits survive worker restarts. The bank ledger is separate; it cannot share a transaction with local storage.

`bank.charge(key, payload)` permanently deduplicates identical key/details pairs; conflicting reuse raises `ValueError`. `lookup(key)` returns a decision or `None`. A missing record does not rule out a delayed request. Inspect charges with `bank.charges()`.

Use `available`, `drop_next_response`, `delay_next_request`, and `deliver_delayed()` for deterministic failures. Workers can overlap or restart using the same store and bank. After faults stop, the bank and communication recover and recovery work is fairly scheduled. No refunds, multiple providers, conversion, fraud, expiring bank records, deployment, disk loss, or record cleanup.

## 3. Expected behavior

| When | Expected result |
| --- | --- |
| A normal payment succeeds | Return `succeeded` with the bank's matching reference. One logical payment causes at most one successful charge. |
| A bank response is lost or the bank is unavailable | Return `pending` for that call. A timeout alone does not establish a decline or prove that no charge happened. |
| The client retries the same payment ID and details | Continue the same payment without another successful charge. A recorded success or definitive decline returns the original receipt. Changed details for that ID raise `ValueError`. |
| A worker crashes before the bank call, after the bank charge, or after storing the local result | A new service using the same store and bank can recover or replay the correct result. |
| Recovery sees no bank record, then an earlier delayed request arrives | The two attempts together must still produce at most one successful charge. |
| Two workers recover the same payment concurrently | They must not create duplicate successful charges or conflicting local outcomes. |
| The bank gives a definitive decline | Record `declined` with no successful charge. Treat it as a completed outcome. Once faults stop and recovery runs, each accepted valid payment eventually exposes its matching success or decline. |

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
python3 interview.py test payments --implementation reference
python3 interview.py export payments --output candidate-packets/payments
~~~

Give the exported folder to the candidate. Its README contains the same brief with standalone run instructions. It includes the code, checks, incident, and neutral intent worksheet. The [reference repair](reference.py), case-specific rubric, example intent, and interviewer guide remain outside the export.

Status: executable starter and reference; 11 contract checks. Human pilots and AI-only baseline measurements remain unperformed.
