import unittest
from support import Clock, Hooks, MemoryStore, SimulatedCrash


def build_suite(Service):
    class Contract(unittest.TestCase):
        def setUp(self):
            self.store, self.clock = MemoryStore(), Clock()
            self.service = Service(self.store, self.clock)
            self.service.submit("J", {"input": 1})

        def handoff(self):
            old = self.service.claim("A", "request-A")
            self.clock.advance(31)
            new = self.service.claim("B", "request-B")
            return old, new

        def test_submission_identity_and_conflict(self):
            self.assertEqual(self.service.submit("J", {"input": 1})["status"], "accepted")
            with self.assertRaises(ValueError):
                self.service.submit("J", {"input": 2})

        def test_stale_publication_is_rejected(self):
            old, new = self.handoff()
            self.assertFalse(self.service.publish("J", old["token"], "stale"))
            self.assertTrue(self.service.publish("J", new["token"], "current"))
            self.assertEqual(self.service.result("J"), "current")

        def test_stale_renewal_is_rejected(self):
            old, new = self.handoff()
            self.assertFalse(self.service.renew("J", old["token"], "renew-old")["accepted"])
            self.assertTrue(self.service.renew("J", new["token"], "renew-new")["accepted"])

        def test_unknown_token_cannot_publish(self):
            self.service.claim("A", "request-A")
            self.assertFalse(self.service.publish("J", "not-a-claim", "bad"))
            self.assertIsNone(self.service.result("J"))

        def test_publication_replay_survives_expiry_and_restart(self):
            claim = self.service.claim("A", "request-A")
            crashing = Service(self.store, self.clock,
                               hooks=Hooks().crash_once("publication_after_persist"))
            with self.assertRaises(SimulatedCrash):
                crashing.publish("J", claim["token"], "answer")
            self.clock.advance(40)
            restarted = Service(self.store, self.clock)
            self.assertTrue(restarted.publish("J", claim["token"], "answer"))
            self.assertEqual(restarted.result("J"), "answer")

        def test_abandoned_job_is_reclaimable(self):
            old, new = self.handoff()
            self.assertNotEqual(old["token"], new["token"])
            self.assertTrue(self.service.publish("J", new["token"], "answer"))

        def test_claim_replay_does_not_extend_lease(self):
            original = self.service.claim("A", "request-A")
            self.clock.advance(31)
            self.assertEqual(self.service.claim("A", "request-A"), original)
            fresh = self.service.claim("A", "fresh-request")
            self.assertNotEqual(fresh["token"], original["token"])

        def test_renewal_replay_does_not_extend_lease(self):
            claim = self.service.claim("A", "request-A")
            self.clock.advance(10)
            first = self.service.renew("J", claim["token"], "renew")
            self.clock.advance(5)
            self.assertEqual(self.service.renew("J", claim["token"], "renew"), first)
            self.assertEqual(first["expires_at"], 40)

        def test_completed_result_cannot_be_overwritten(self):
            claim = self.service.claim("A", "request-A")
            self.assertTrue(self.service.publish("J", claim["token"], "answer"))
            self.assertFalse(self.service.publish("J", claim["token"], "different"))
            self.assertEqual(self.service.result("J"), "answer")

        def test_completed_job_is_not_claimed_again(self):
            claim = self.service.claim("A", "request-A")
            self.service.publish("J", claim["token"], "answer")
            self.clock.advance(100)
            self.assertIsNone(self.service.claim("B", "fresh"))
    return unittest.defaultTestLoader.loadTestsFromTestCase(Contract)
