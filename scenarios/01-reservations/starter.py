"""Intentionally incorrect reservation service. Repair this file."""
from support import Clock, Hooks, MemoryStore


class Service:
    def __init__(self, store=None, clock=None, capacity=10, hooks=None):
        self.store = store if store is not None else MemoryStore()
        self.clock = clock if clock is not None else Clock()
        self.hooks = hooks if hooks is not None else Hooks()
        def initialize(data):
            data.setdefault("capacity", capacity)
            data.setdefault("sequence", 0)
            data.setdefault("holds", {})
            data.setdefault("requests", {})
            data.setdefault("bookings", {})
        self.store.atomic(initialize)

    @staticmethod
    def _used(data, now):
        return ({item["seat_id"] for item in data["bookings"].values()}
                | {item["seat_id"] for item in data["holds"].values()
                   if item["status"] == "held" and item["expires_at"] > now})

    def hold(self, request_id):
        snapshot = self.store.snapshot()
        if request_id in snapshot["requests"]:
            return snapshot["requests"][request_id]
        free = set(range(snapshot["capacity"])) - self._used(snapshot, self.clock.now)
        chosen = min(free) if free else None
        self.hooks.hit("hold_before_commit", request_id=request_id)
        def commit(data):
            if request_id in data["requests"]:
                return data["requests"][request_id]
            if chosen is None:
                receipt = {"request_id": request_id, "status": "no_capacity"}
            else:
                data["sequence"] += 1
                token = "hold-" + str(data["sequence"])
                receipt = {"request_id": request_id, "status": "held",
                           "hold_id": token, "seat_id": chosen,
                           "expires_at": self.clock.now + 30}
                data["holds"][token] = dict(receipt, sequence=data["sequence"])
            data["requests"][request_id] = receipt
            return receipt
        return self.store.atomic(commit)

    def confirm(self, hold_id):
        snapshot = self.store.snapshot()
        original = snapshot["holds"].get(hold_id)
        if original is None:
            return {"status": "unknown"}
        same_seat = [h for h in snapshot["holds"].values()
                     if h["seat_id"] == original["seat_id"]]
        current = max(same_seat, key=lambda h: h["sequence"])
        if self.clock.now >= current["expires_at"]:
            return {"status": "expired"}
        self.hooks.hit("confirm_before_commit", hold_id=hold_id)
        def commit(data):
            if hold_id in data["bookings"]:
                return data["bookings"][hold_id]
            receipt = {"status": "booked", "booking_id": "booking-" + hold_id,
                       "hold_id": hold_id, "seat_id": original["seat_id"]}
            data["holds"][hold_id]["status"] = "booked"
            data["bookings"][hold_id] = receipt
            return receipt
        receipt = self.store.atomic(commit)
        self.hooks.hit("confirmation_after_persist", hold_id=hold_id)
        return receipt

    def bookings(self):
        return list(self.store.snapshot()["bookings"].values())

    def available(self):
        data = self.store.snapshot()
        return data["capacity"] - len(self._used(data, self.clock.now))
