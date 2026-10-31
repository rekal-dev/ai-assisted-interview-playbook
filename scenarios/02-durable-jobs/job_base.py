"""Prepared queue infrastructure; candidates repair publication and renewal."""
from support import Clock, Hooks, MemoryStore


class Base:
    def __init__(self, store=None, clock=None, hooks=None):
        self.store = store if store is not None else MemoryStore()
        self.clock = clock if clock is not None else Clock()
        self.hooks = hooks if hooks is not None else Hooks()
        def initialize(data):
            data.setdefault("jobs", {})
            data.setdefault("claim_receipts", {})
            data.setdefault("renew_receipts", {})
            data.setdefault("sequence", 0)
        self.store.atomic(initialize)

    def submit(self, job_id, payload):
        def commit(data):
            old = data["jobs"].get(job_id)
            if old is not None and old["payload"] != payload:
                raise ValueError("Conflicting job input")
            if old is None:
                data["jobs"][job_id] = {
                    "payload": payload, "status": "queued", "token": None,
                    "expires_at": 0, "result": None, "published_by": None,
                }
            return {"job_id": job_id, "status": "accepted"}
        return self.store.atomic(commit)

    def claim(self, worker_id, request_id):
        def commit(data):
            if request_id in data["claim_receipts"]:
                old = data["claim_receipts"][request_id]
                if old["worker_id"] != worker_id:
                    raise ValueError("Conflicting claim request")
                return old["receipt"]
            eligible = [(key, job) for key, job in sorted(data["jobs"].items())
                        if job["status"] != "done"
                        and (job["status"] == "queued"
                             or self.clock.now >= job["expires_at"])]
            receipt = None
            if eligible:
                key, job = eligible[0]
                data["sequence"] += 1
                token = "claim-" + str(data["sequence"])
                job.update(status="running", token=token,
                           expires_at=self.clock.now + 30)
                receipt = {"job_id": key, "token": token,
                           "expires_at": job["expires_at"]}
            data["claim_receipts"][request_id] = {
                "worker_id": worker_id, "receipt": receipt,
            }
            return receipt
        return self.store.atomic(commit)

    def result(self, job_id):
        job = self.store.snapshot()["jobs"].get(job_id)
        return job["result"] if job and job["status"] == "done" else None

    def status(self, job_id):
        job = self.store.snapshot()["jobs"].get(job_id)
        return job["status"] if job else None
