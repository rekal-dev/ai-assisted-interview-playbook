"""Deterministic local test facilities. Python standard library only."""
from copy import deepcopy
import importlib.util
import io
from pathlib import Path
from threading import RLock
import sys
import unittest


class SimulatedCrash(RuntimeError):
    pass


class LostResponse(TimeoutError):
    pass


class Clock:
    def __init__(self, now=0):
        self._now = now
        self._lock = RLock()

    @property
    def now(self):
        with self._lock:
            return self._now

    def advance(self, amount):
        if amount < 0:
            raise ValueError("The clock is monotonic")
        with self._lock:
            self._now += amount
            return self._now


class MemoryStore:
    """Serializable copy-on-write transactions; committed data survives restarts."""
    def __init__(self):
        self._data = {}
        self._lock = RLock()

    def snapshot(self):
        with self._lock:
            return deepcopy(self._data)

    def atomic(self, action):
        with self._lock:
            working = deepcopy(self._data)
            result = action(working)
            self._data = deepcopy(working)
            return deepcopy(result)


class Hooks:
    """Callbacks run at documented boundaries, outside authoritative transactions."""
    def __init__(self, callbacks=None):
        self.callbacks = dict(callbacks or {})
        self._lock = RLock()

    def hit(self, name, **context):
        with self._lock:
            callback = self.callbacks.get(name)
        if callback:
            callback(**context)

    def crash_once(self, name):
        def crash(**_context):
            with self._lock:
                self.callbacks.pop(name, None)
            raise SimulatedCrash(name)
        with self._lock:
            self.callbacks[name] = crash
        return self


def load_module(path, name):
    path = Path(path).resolve()
    if str(path.parent) not in sys.path:
        sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(str(path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def run_contract(directory, implementation, namespace):
    directory = Path(directory).resolve()
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))
    implementation = Path(implementation)
    if not implementation.is_absolute():
        implementation = directory / implementation
    if not implementation.exists():
        raise FileNotFoundError(implementation)
    code = load_module(implementation, namespace + "_implementation")
    tests = load_module(directory / "test_contract.py", namespace + "_tests")
    suite = tests.build_suite(code.Service)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    return result, stream.getvalue()
