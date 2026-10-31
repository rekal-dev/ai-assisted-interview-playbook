"""One stable external operation, durable uncertainty, and reconciliation."""
from payment_base import Base, TERMINAL


class Service(Base):
    def _process(self, payment_id):
        if self.get(payment_id)["status"] in TERMINAL:
            return self.get(payment_id)
        row = self.store.snapshot()["payments"][payment_id]
        self.hooks.hit("payment_before_bank", payment_id=payment_id)
        try:
            decision = self.bank.lookup(row["bank_key"])
            if decision is None:
                decision = self.bank.charge(row["bank_key"], row["payload"])
        except TimeoutError:
            return self.get(payment_id)
        if decision["status"] not in TERMINAL:
            return self.get(payment_id)
        self.hooks.hit("payment_after_bank", payment_id=payment_id)
        return self._record(payment_id, decision)
