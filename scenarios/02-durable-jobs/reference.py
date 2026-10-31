"""A current-claim guard and durable terminal publication."""
from job_base import Base


class Service(Base):
    def renew(self, job_id, token, request_id):
        def commit(data):
            key = (job_id, token, request_id)
            if key in data["renew_receipts"]:
                return data["renew_receipts"][key]
            job = data["jobs"].get(job_id)
            valid = (job is not None and job["status"] == "running"
                     and job["token"] == token
                     and self.clock.now < job["expires_at"])
            if valid:
                job["expires_at"] = self.clock.now + 30
                receipt = {"accepted": True, "expires_at": job["expires_at"]}
            else:
                receipt = {"accepted": False}
            data["renew_receipts"][key] = receipt
            return receipt
        return self.store.atomic(commit)

    def publish(self, job_id, token, result):
        def commit(data):
            job = data["jobs"].get(job_id)
            if job is None:
                return False
            if job["status"] == "done":
                return job["published_by"] == token and job["result"] == result
            if (job["status"] != "running" or job["token"] != token
                    or self.clock.now >= job["expires_at"]):
                return False
            job.update(status="done", published_by=token, result=result)
            return True
        accepted = self.store.atomic(commit)
        self.hooks.hit("publication_after_persist", job_id=job_id)
        return accepted
