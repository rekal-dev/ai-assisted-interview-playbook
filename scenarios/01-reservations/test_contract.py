"""Black-box contract checks plus bounded histories and a controlled race."""
from concurrent.futures import ThreadPoolExecutor
from itertools import product
from threading import Barrier
import unittest
from support import Clock, Hooks, MemoryStore, SimulatedCrash


def build_suite(Service):
    class Contract(unittest.TestCase):
        def setUp(self):
            self.store, self.clock = MemoryStore(), Clock()
            self.service = Service(self.store, self.clock, capacity=1)

        def test_happy_path(self):
            hold = self.service.hold("A")
            receipt = self.service.confirm(hold["hold_id"])
            self.assertEqual(receipt["status"], "booked")
            self.assertEqual(len(self.service.bookings()), 1)
            self.assertEqual(self.service.available(), 0)

        def test_hold_replay_does_not_extend_expiry(self):
            first = self.service.hold("A")
            self.clock.advance(40)
            self.assertEqual(self.service.hold("A"), first)
            self.assertEqual(self.service.available(), 1)

        def test_competing_last_seat(self):
            barrier = Barrier(2)
            hooks = Hooks({"hold_before_commit": lambda **_: barrier.wait(timeout=3)})
            left = Service(self.store, self.clock, hooks=hooks)
            right = Service(self.store, self.clock, hooks=hooks)
            with ThreadPoolExecutor(max_workers=2) as pool:
                a = pool.submit(left.hold, "A")
                b = pool.submit(right.hold, "B")
                results = [a.result(timeout=5), b.result(timeout=5)]
            self.assertEqual(sum(r["status"] == "held" for r in results), 1)

        def test_old_hold_cannot_confirm_reassigned_seat(self):
            old = self.service.hold("A")
            self.clock.advance(31)
            new = self.service.hold("B")
            self.assertEqual(self.service.confirm(old["hold_id"])["status"], "expired")
            self.assertEqual(self.service.confirm(new["hold_id"])["status"], "booked")
            self.assertEqual(len(self.service.bookings()), 1)

        def test_committed_confirmation_replays_after_expiry(self):
            hold = self.service.hold("A")
            crashing = Service(self.store, self.clock,
                               hooks=Hooks().crash_once("confirmation_after_persist"))
            with self.assertRaises(SimulatedCrash):
                crashing.confirm(hold["hold_id"])
            self.clock.advance(31)
            restarted = Service(self.store, self.clock)
            self.assertEqual(restarted.confirm(hold["hold_id"])["status"], "booked")
            self.assertEqual(len(restarted.bookings()), 1)

        def test_exact_deadline_is_expired(self):
            hold = self.service.hold("A")
            self.clock.advance(30)
            self.assertEqual(self.service.confirm(hold["hold_id"])["status"], "expired")

        def test_expired_capacity_recovers_without_cleanup(self):
            self.service.hold("A")
            self.clock.advance(31)
            restarted = Service(self.store, self.clock)
            self.assertEqual(restarted.available(), 1)
            self.assertEqual(restarted.hold("B")["status"], "held")

        def test_unknown_confirmation_is_rejected(self):
            self.assertEqual(self.service.confirm("missing")["status"], "unknown")

        def test_bounded_histories_preserve_capacity(self):
            actions = ("hold_A", "hold_B", "confirm_A", "confirm_B", "advance", "restart")
            for capacity in (1, 2):
                for history in product(actions, repeat=4):
                    store, clock = MemoryStore(), Clock()
                    service = Service(store, clock, capacity=capacity)
                    receipts = {}
                    for action in history:
                        if action.startswith("hold_"):
                            owner = action[-1]
                            receipt = service.hold(owner)
                            if receipt["status"] == "held":
                                receipts[owner] = receipt
                        elif action.startswith("confirm_"):
                            receipt = receipts.get(action[-1])
                            if receipt:
                                service.confirm(receipt["hold_id"])
                        elif action == "advance":
                            clock.advance(31)
                        else:
                            service = Service(store, clock, capacity=capacity)
                        booked = service.bookings()
                        booked_ids = {b["hold_id"] for b in booked}
                        live = [h for h in receipts.values()
                                if h["hold_id"] not in booked_ids
                                and h["expires_at"] > clock.now]
                        seats = [b["seat_id"] for b in booked] + [h["seat_id"] for h in live]
                        self.assertEqual(len(seats), len(set(seats)), history)
                        self.assertLessEqual(len(seats), capacity, history)
    return unittest.defaultTestLoader.loadTestsFromTestCase(Contract)
