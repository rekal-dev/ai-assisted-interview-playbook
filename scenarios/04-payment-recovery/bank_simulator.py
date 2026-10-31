"""A separate durable bank ledger with deterministic network failure controls."""
from copy import deepcopy
from threading import RLock
from support import LostResponse


class Bank:
    def __init__(self):
        self.available = True
        self.drop_next_response = False
        self.delay_next_request = False
        self._operations = {}
        self._delayed = []
        self._lock = RLock()

    def lookup(self, key):
        with self._lock:
            if not self.available:
                raise TimeoutError("Bank unavailable")
            return deepcopy(self._operations.get(key))

    def charge(self, key, payload):
        with self._lock:
            if not self.available:
                raise TimeoutError("Bank unavailable")
            if self.delay_next_request:
                self.delay_next_request = False
                self._delayed.append((key, deepcopy(payload)))
                raise LostResponse("Request is still in flight")
            old = self._operations.get(key)
            if old is not None:
                if old["payload"] != payload:
                    raise ValueError("Conflicting bank key")
                decision = old
            else:
                declined = payload["customer"] == "declined"
                decision = {
                    "key": key, "payload": deepcopy(payload),
                    "status": "declined" if declined else "succeeded",
                    "bank_reference": None if declined else "bank-" + str(len(self._operations) + 1),
                }
                self._operations[key] = decision
            drop = self.drop_next_response
            self.drop_next_response = False
            result = deepcopy(decision)
        if drop:
            raise LostResponse("Bank committed but its response disappeared")
        return result

    def deliver_delayed(self):
        with self._lock:
            pending, self._delayed = self._delayed, []
        for key, payload in pending:
            self.charge(key, payload)

    def charges(self):
        with self._lock:
            return deepcopy([row for row in self._operations.values()
                             if row["status"] == "succeeded"])

    def operation_count(self):
        with self._lock:
            return len(self._operations)
