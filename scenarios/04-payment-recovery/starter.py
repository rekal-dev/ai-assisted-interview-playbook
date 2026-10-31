"""Intentionally incorrect attempt identity and timeout interpretation."""
from payment_base import Base, TERMINAL


class Service(Base):
    def _process(self, payment_id):
        if self.get(payment_id)["status"] in TERMINAL:
            return self.get(payment_id)
        def next_attempt(data):
            row = data["payments"][payment_id]
            row["attempts"] += 1
            return (row["bank_key"] + "-" + str(row["attempts"]), row["payload"])
        key, payload = self.store.atomic(next_attempt)
        self.hooks.hit("payment_before_bank", payment_id=payment_id)
        try:
            decision = self.bank.charge(key, payload)
        except TimeoutError:
            self.store.atomic(
                lambda data: data["payments"][payment_id].update(status="failed")
            )
            return self.get(payment_id)
        self.hooks.hit("payment_after_bank", payment_id=payment_id)
        return self._record(payment_id, decision)
