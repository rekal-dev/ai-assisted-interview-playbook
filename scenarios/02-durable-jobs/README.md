# Durable jobs

A worker paused while processing a job. Its claim expired, another worker took over, and the first worker then published a stale result. Repair the supplied service so only authorized work becomes the recorded result.

**60 minutes. Unrestricted AI. Python 3.10+; standard library only.**

## 1. Here is the code

Start with [starter.py](starter.py): `renew()` and `publish()` are the methods to repair.

[job_base.py](job_base.py) already provides submission, job claiming, result reads, and durable storage setup. Read it as needed; you do not need to build a queue.

Also supplied: [behavior checks](test_contract.py) and the [starting incident](incident.json).

From the repository root, run:

~~~sh
python3 interview.py test jobs --implementation starter
~~~

Initial failures and exit code 1 are intentional.

Use AI to investigate first. Choose what to ask or inspect. Capture your repair instruction below before changing `starter.py`.

**Entry points:** `submit`, `claim`, `renew`, `publish`, `result`, and `status`. Signatures and receipt fields are in the linked Python files.

## 2. What you can and cannot change

**You can:** edit `starter.py`, add helpers, choose a compatible internal representation, and add checks in new files.

**Keep fixed:** `job_base.py`, `support.py`, and `test_contract.py`, the runner, public signatures, and return shapes.

Keep `publication_after_persist` after the publication decision commits, outside its transaction.

**Provided guarantees and limits:**

The store supports serializable atomic changes and retains commits across worker restarts. One monotonic virtual clock controls 30-unit claims; equality with a deadline means expired. Workers may pause, crash, resume, or retry after lost responses. Expiry does not stop computation.

Inputs are immutable; computations may overlap but have no external side effects. Use non-`None` results. Request receipts persist throughout the exercise. After faults stop, assume fair scheduling, available storage, and a worker with enough claim time, including renewals, to finish. No cancellation, workflow dependencies, deployment, disk loss, or record cleanup.

## 3. Expected behavior

| When | Expected result |
| --- | --- |
| A job or successful claim request is repeated | Refer to the same job or return the original claim token and deadline. Replaying a claim never extends its lifetime. A fresh attempt needs a fresh request ID. |
| A claim expires before its job finishes | Another worker can claim the job with a different token. |
| A: claim at time 0; B: claim at time 31; A: publish or renew | Reject A's stale publication and renewal. B's current, unexpired claim can publish or renew. |
| An unknown token attempts to publish | Return `False`; leave the job's result unchanged. |
| A valid claim renews | Extend its deadline by 30 units from the current time. Repeating that renewal request returns the original outcome without extending it again. Expired claims cannot renew. |
| A result was accepted but its response was lost | Its exact replay returns `True`, even after restart or expiry. The recorded result stays unchanged; a conflicting later result returns `False`. |
| A job has a recorded result | It is `done` and cannot be claimed again. |

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
python3 interview.py test jobs --implementation reference
python3 interview.py export jobs --output candidate-packets/jobs
~~~

Give the exported folder to the candidate. Its README contains the same brief with standalone run instructions. It includes the code, checks, incident, and neutral intent worksheet. The [reference repair](reference.py), case-specific rubric, example intent, and interviewer guide remain outside the export.

Status: executable starter and reference; 10 contract checks. Human pilots and AI-only baseline measurements remain unperformed.
