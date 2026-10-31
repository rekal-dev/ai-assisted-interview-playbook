"""Prepared durable intent storage and public API."""
from bank_simulator import Bank
from support import Hooks, MemoryStore

TERMINAL = ("succeeded", "declined")


class Base:
    def __init__(self, store=None, bank=None, hooks=None):
        self.store = store if store is not None else MemoryStore()
        self.bank = bank if bank is not None else Bank()
        self.hooks = hooks if hooks is not None else Hooks()
        self.store.atomic(lambda data: data.setdefault("payments", {}))

    def _ensure(self, payment_id, payload):
        if (not isinstance(payload.get("amount"), int) or payload["amount"] <= 0
                or not payload.get("currency") or not payload.get("customer")):
            raise ValueError("Positive integer amount, currency, and customer required")
        def commit(data):
            old = data["payments"].get(payment_id)
            if old is not None and old["payload"] != payload:
                raise ValueError("Conflicting payment details")
            if old is None:
                data["payments"][payment_id] = {
                    "payload": payload, "status": "pending", "bank_reference": None,
                    "bank_key": "payment-" + payment_id, "attempts": 0,
                }
        self.store.atomic(commit)

    def submit(self, payment_id, payload):
        self._ensure(payment_id, payload)
        return self._process(payment_id)

    def reconcile(self, payment_id):
        if self.get(payment_id) is None:
            raise ValueError("Unknown payment")
        return self._process(payment_id)

    def recover(self):
        ids = [key for key, row in self.store.snapshot()["payments"].items()
               if row["status"] not in TERMINAL]
        return [self.reconcile(key) for key in ids]

    def get(self, payment_id):
        row = self.store.snapshot()["payments"].get(payment_id)
        if row is None:
            return None
        return {"payment_id": payment_id, "status": row["status"],
                "bank_reference": row["bank_reference"]}

    def _record(self, payment_id, decision):
        def commit(data):
            row = data["payments"][payment_id]
            if row["status"] not in TERMINAL:
                row["status"] = decision["status"]
                row["bank_reference"] = decision["bank_reference"]
        self.store.atomic(commit)
        result = self.get(payment_id)
        self.hooks.hit("payment_after_persist", payment_id=payment_id)
        return result
