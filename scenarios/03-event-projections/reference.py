"""A source-version guard retained across logical deletion."""
from support import Hooks, MemoryStore


class Service:
    def __init__(self, store=None, hooks=None):
        self.store = store if store is not None else MemoryStore()
        self.hooks = hooks if hooks is not None else Hooks()
        self.store.atomic(lambda data: data.setdefault("entities", {}))

    def apply(self, event):
        self.hooks.hit("projection_before_commit", version=event["version"])
        def commit(data):
            key = event["entity_id"]
            current = data["entities"].get(key)
            if current and current["version"] >= event["version"]:
                return False
            deleted = event["kind"] == "delete"
            data["entities"][key] = {
                "version": event["version"], "deleted": deleted,
                "value": None if deleted else event["value"],
            }
            return True
        return self.store.atomic(commit)

    def get(self, entity_id):
        row = self.store.snapshot()["entities"].get(entity_id)
        if row is None or row["deleted"]:
            return None
        return {"version": row["version"], "value": row["value"]}

    def version(self, entity_id):
        row = self.store.snapshot()["entities"].get(entity_id)
        return row["version"] if row else None
