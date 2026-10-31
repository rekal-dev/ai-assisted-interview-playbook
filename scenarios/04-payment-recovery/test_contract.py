from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
import unittest
from bank_simulator import Bank
from support import Hooks, MemoryStore, SimulatedCrash

PAYLOAD = {"amount": 100, "currency": "AUD", "customer": "C"}


def build_suite(Service):
    class Contract(unittest.TestCase):
        def setUp(self):
            self.store, self.bank = MemoryStore(), Bank()
            self.service = Service(store=self.store, bank=self.bank)

        def restart(self, hooks=None):
            return Service(store=self.store, bank=self.bank, hooks=hooks)

        def test_happy_path_matches_bank(self):
            receipt = self.service.submit("P", PAYLOAD)
            self.assertEqual(receipt["status"], "succeeded")
            self.assertEqual(receipt["bank_reference"], self.bank.charges()[0]["bank_reference"])
            self.assertEqual(len(self.bank.charges()), 1)

        def test_timeout_preserves_unknown_outcome(self):
            self.bank.drop_next_response = True
            receipt = self.service.submit("P", PAYLOAD)
            self.assertEqual(len(self.bank.charges()), 1)
            self.assertEqual(receipt["status"], "pending")

        def test_client_retry_never_double_charges(self):
            self.bank.drop_next_response = True
            self.service.submit("P", PAYLOAD)
            self.service.submit("P", PAYLOAD)
            self.assertEqual(len(self.bank.charges()), 1)
            self.assertEqual(self.service.get("P")["status"], "succeeded")

        def test_recovery_after_bank_commit_before_local_write(self):
            worker = self.restart(Hooks().crash_once("payment_after_bank"))
            with self.assertRaises(SimulatedCrash):
                worker.submit("P", PAYLOAD)
            receipt = self.restart().reconcile("P")
            self.assertEqual(receipt["status"], "succeeded")
            self.assertEqual(len(self.bank.charges()), 1)
            self.assertEqual(receipt["bank_reference"], self.bank.charges()[0]["bank_reference"])

        def test_delayed_request_after_not_found(self):
            self.bank.delay_next_request = True
            self.service.submit("P", PAYLOAD)
            self.assertEqual(self.bank.charges(), [])
            self.restart().reconcile("P")
            self.bank.deliver_delayed()
            self.assertEqual(len(self.bank.charges()), 1)

        def test_committed_local_result_replays_after_response_loss(self):
            worker = self.restart(Hooks().crash_once("payment_after_persist"))
            with self.assertRaises(SimulatedCrash):
                worker.submit("P", PAYLOAD)
            recorded = self.service.get("P")
            self.assertEqual(self.restart().submit("P", PAYLOAD), recorded)
            self.assertEqual(len(self.bank.charges()), 1)

        def test_crash_before_bank_has_durable_recovery(self):
            worker = self.restart(Hooks().crash_once("payment_before_bank"))
            with self.assertRaises(SimulatedCrash):
                worker.submit("P", PAYLOAD)
            self.assertEqual(self.bank.charges(), [])
            self.assertEqual(self.restart().reconcile("P")["status"], "succeeded")
            self.assertEqual(len(self.bank.charges()), 1)

        def test_bank_outage_then_recovery(self):
            self.bank.available = False
            self.assertEqual(self.service.submit("P", PAYLOAD)["status"], "pending")
            self.bank.available = True
            results = self.restart().recover()
            self.assertEqual(results[0]["status"], "succeeded")
            self.assertEqual(len(self.bank.charges()), 1)

        def test_decline_is_terminal(self):
            declined = dict(PAYLOAD, customer="declined")
            first = self.service.submit("P", declined)
            self.assertEqual(first["status"], "declined")
            self.assertEqual(self.restart().reconcile("P"), first)
            self.assertEqual(self.bank.charges(), [])
            self.assertEqual(self.bank.operation_count(), 1)

        def test_payment_payload_is_immutable(self):
            self.service.submit("P", PAYLOAD)
            with self.assertRaises(ValueError):
                self.service.submit("P", dict(PAYLOAD, amount=200))
            self.assertEqual(len(self.bank.charges()), 1)

        def test_simultaneous_recovery_uses_one_bank_operation(self):
            self.bank.available = False
            self.service.submit("P", PAYLOAD)
            self.bank.available = True
            barrier = Barrier(2)
            hooks = Hooks({"payment_before_bank": lambda **_: barrier.wait(timeout=3)})
            a, b = self.restart(hooks), self.restart(hooks)
            with ThreadPoolExecutor(max_workers=2) as pool:
                futures = [pool.submit(worker.reconcile, "P") for worker in (a, b)]
                for future in futures:
                    self.assertEqual(future.result(timeout=5)["status"], "succeeded")
            self.assertEqual(len(self.bank.charges()), 1)
    return unittest.defaultTestLoader.loadTestsFromTestCase(Contract)
