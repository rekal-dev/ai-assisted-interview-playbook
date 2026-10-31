from concurrent.futures import ThreadPoolExecutor
from itertools import permutations
from threading import Event
import unittest
from support import Hooks, MemoryStore


def snapshot(version, value=None, entity="E"):
    return {"entity_id": entity, "version": version, "kind": "upsert",
            "value": {"preference": value if value is not None else version}}


def deletion(version, entity="E"):
    return {"entity_id": entity, "version": version, "kind": "delete"}


def build_suite(Service):
    class Contract(unittest.TestCase):
        def setUp(self):
            self.store = MemoryStore()
            self.service = Service(self.store)

        def test_ordered_snapshots(self):
            self.service.apply(snapshot(1, "old"))
            self.service.apply(snapshot(2, "new"))
            self.assertEqual(self.service.get("E"), {"version": 2, "value": {"preference": "new"}})

        def test_duplicate_is_stable(self):
            event = snapshot(3)
            self.assertTrue(self.service.apply(event))
            self.assertFalse(self.service.apply(event))
            self.assertEqual(self.service.version("E"), 3)

        def test_older_snapshot_is_ignored(self):
            self.service.apply(snapshot(8))
            self.assertFalse(self.service.apply(snapshot(7)))
            self.assertEqual(self.service.version("E"), 8)

        def test_deletion_retains_ordering_information(self):
            self.service.apply(snapshot(8))
            self.service.apply(deletion(9))
            self.assertIsNone(self.service.get("E"))
            self.assertEqual(self.service.version("E"), 9)

        def test_older_event_cannot_resurrect_deleted_entity(self):
            self.service.apply(deletion(9))
            self.assertFalse(self.service.apply(snapshot(8)))
            self.assertIsNone(self.service.get("E"))

        def test_higher_version_can_recreate_entity(self):
            self.service.apply(deletion(9))
            self.assertTrue(self.service.apply(snapshot(10, "recreated")))
            self.assertEqual(self.service.get("E")["value"]["preference"], "recreated")

        def test_concurrent_lower_version_cannot_overwrite_higher(self):
            self.service.apply(snapshot(6))
            paused, release = Event(), Event()
            def pause(version):
                if version == 7:
                    paused.set()
                    if not release.wait(timeout=3):
                        raise RuntimeError("Test interleaving did not complete")
            worker = Service(self.store, Hooks({"projection_before_commit": pause}))
            with ThreadPoolExecutor(max_workers=1) as pool:
                future = pool.submit(worker.apply, snapshot(7))
                try:
                    self.assertTrue(paused.wait(timeout=3))
                    self.service.apply(snapshot(8))
                finally:
                    release.set()
                future.result(timeout=5)
            self.assertEqual(self.service.version("E"), 8)

        def test_restart_retains_deletion_order(self):
            self.service.apply(deletion(9))
            restarted = Service(self.store)
            restarted.apply(snapshot(8))
            self.assertIsNone(restarted.get("E"))
            self.assertEqual(restarted.version("E"), 9)

        def test_entity_versions_are_independent(self):
            self.service.apply(snapshot(100, entity="A"))
            self.service.apply(snapshot(1, entity="B"))
            self.assertEqual(self.service.version("B"), 1)

        def test_bounded_delivery_permutations_converge(self):
            events = (snapshot(1), deletion(2), snapshot(3))
            for ordering in permutations(events):
                store = MemoryStore()
                service = Service(store)
                latest = None
                for event in ordering:
                    service.apply(event)
                    service = Service(store)
                    service.apply(event)  # duplicate after restart
                    if latest is None or event["version"] > latest["version"]:
                        latest = event
                    self.assertEqual(service.version("E"), latest["version"], ordering)
                    if latest["kind"] == "delete":
                        self.assertIsNone(service.get("E"), ordering)
                    else:
                        self.assertEqual(service.get("E")["value"], latest["value"], ordering)
    return unittest.defaultTestLoader.loadTestsFromTestCase(Contract)
