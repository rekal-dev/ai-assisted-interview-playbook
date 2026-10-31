# Event projections

A service builds customer profiles from source events. Events arrive more than once and out of order. Deleted profiles have reappeared, and older updates have overwritten newer values. Repair the supplied consumer.

**60 minutes. Unrestricted AI. Python 3.10+; standard library only.**

## 1. Here is the code

Start with [starter.py](starter.py): `apply()` accepts incoming events; `get()` and `version()` expose the stored result.

Also supplied: [behavior checks](test_contract.py) and the [starting incident](incident.json).

In this candidate folder, run:

~~~sh
python3 run.py
~~~

Initial failures and exit code 1 are intentional.

Use AI to investigate first. Choose what to ask or inspect. Capture your repair instruction below before changing `starter.py`.

**API:** `apply(event)` returns an acceptance flag; `get(entity_id)` returns `{"version": ..., "value": ...}` or `None`; `version(entity_id)` returns the last accepted version or `None`.

Events have these shapes:

~~~python
{"entity_id": "E", "version": 8, "kind": "upsert", "value": {"preference": "new"}}
{"entity_id": "E", "version": 9, "kind": "delete"}
~~~

## 2. What you can and cannot change

**You can:** edit `starter.py`, add helpers, choose a compatible internal representation, and add checks in new files.

**Keep fixed:** `support.py` and `test_contract.py`, the runner, public signatures, and return shapes.

Keep `projection_before_commit(version=...)` outside and before the final acceptance transaction.

**Provided guarantees and limits:**

One source assigns increasing positive versions per entity; versions across entities are independent. Existing entity IDs never reset their versions. Events are complete snapshots or deletions; equal entity/version pairs have identical content. Arrival time is not source order.

The store supports serializable atomic changes, authoritative reads, and retained commits across restarts. Consumers may overlap; delivery may repeat, reorder, or lose acknowledgments. After faults stop, the finite event set is delivered and processed fairly. No partial updates, independent writers, cross-entity transactions, schema migration, deployment, disk loss, or record cleanup.

## 3. Expected behavior

| When | Expected result |
| --- | --- |
| Snapshot version 8 arrives, then version 7 | Keep version 8 and its value; return `False` for version 7. |
| An event is delivered again | Return `False` and leave the profile unchanged. |
| A deletion at version 9 arrives | `get()` returns `None`; `version()` still returns 9. |
| Snapshot 8 arrives after deletion 9, including after restart | Keep the profile deleted at version 9. |
| Snapshot 10 arrives after deletion 9 | Accept it and expose the new profile at version 10. |
| Consumers process versions 7 and 8 concurrently | Once version 8 is accepted, version 7 cannot overwrite it. |
| Entity A reaches version 100 and B receives version 1 | Accept B's event independently of A's version. |

Own one failure, repair it, and examine a related case. The full contract stays in force; report remaining failures.

## 4. What to hand over

1. In `intent.md`, keep the questions or instructions you chose, what you learned, and the repair instruction you gave AI before implementation edits. AI may help throughout.
2. Deliver changed code, a failure reproduction, and actual output from the checks you ran.
3. Revise your instruction after a related case or new evidence. Explain the guarantee, assumptions, and remaining gaps.

The assessment considers your understanding, approach choice, and judgment about AI output. Explain consequential decisions briefly. Passing-check count does not set this score; correctness is recorded separately.
