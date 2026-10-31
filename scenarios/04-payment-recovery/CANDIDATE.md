# Payment recovery interview

You have 60 minutes with unrestricted AI. Read incident.json, payment_base.py, bank_simulator.py, and starter.py. Write your initial intent prompt before editing and revise it when evidence changes your model.

## Situation

A customer was charged twice after a timeout. In another incident the bank charged, but the local service reported failure. Repair one submission or recovery failure and check the adjacent crash window.

## Run

~~~sh
python3 run.py
~~~

Edit starter.py. Prepared code provides local intents and a separate bank ledger. Retain the public API, tests, and diagnostic hooks.

## Contract and API

- Construct Service(store=store, bank=bank, hooks=None).
- submit(payment_id, payload) accepts a logical payment; payload has positive integer amount, currency, customer.
- Identical payment replay is stable; changed details for the same ID raise ValueError.
- get(payment_id) returns pending, succeeded, or declined with a matching bank_reference on success. reconcile(payment_id) recovers one; recover() scans unfinished intents.
- A payment causes at most one successful bank charge. A timeout alone is not a definitive decline.
- Bank.charge(key, payload) permanently deduplicates the same key and payload for the bounded exercise. Conflicting reuse raises ValueError.
- Bank.lookup(key) returns a terminal decision or None. Not found does not establish that an earlier request will never arrive.
- The bank and local store cannot share a transaction. The bank ledger exists independently of local state.
- Bank flags deterministically simulate unavailability, a lost committed response, and a delayed request. deliver_delayed() completes queued requests.
- Store commits survive simulated worker-object restart. Requests and responses may be delayed or lost; recovery workers can overlap.
- When faults cease, communication and providers recover and reconciliation is fairly scheduled. Accepted valid payments must eventually expose the matching success or definitive decline.
- Refunds, multiple providers, finite key retention, deployment, and disk loss are excluded.

payment_before_bank, payment_after_bank, and payment_after_persist identify the three crash boundaries. They run outside local transactions.

## Deliver

Initial and revised intent, reproduced failure, repair, adjacent evidence, guarantee, and limits. Inspect the bank ledger as well as local status. Use rubric.md.
