"""Intentionally incorrect concurrent acceptance and deletion handling."""
from support import Hooks, MemoryStore


class Service:
    def __init__(self, store=None, hooks=None):
        self.store = store if store is not None else MemoryStore()
        self.hooks = hooks if hooks is not None else Hooks()
        self.store.atomic(lambda data: data.setdefault("entities", {}))

    def apply(self, event):
        key = event["entity_id"]
        current = self.store.snapshot()["entities"].get(key)
        if current and current["version"] >= event["version"]:
            return False
        self.hooks.hit("projection_before_commit", version=event["version"])
        def commit(data):
            if event["kind"] == "delete":
                data["entities"].pop(key, None)
            else:
                data["entities"][key] = {"version": event["version"],
                                         "value": event["value"], "deleted": False}
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
