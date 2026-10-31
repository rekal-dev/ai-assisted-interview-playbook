#!/usr/bin/env python3
"""Run, verify, or export a complete interview exercise."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from support import load_module, run_contract

ROOT = Path(__file__).resolve().parent
SCENARIOS = {
    "reservations": "01-reservations",
    "jobs": "02-durable-jobs",
    "projections": "03-event-projections",
    "payments": "04-payment-recovery",
}

PACKET_RUNNER = '''#!/usr/bin/env python3
import argparse
from pathlib import Path
from support import run_contract

parser = argparse.ArgumentParser()
parser.add_argument("--implementation", default="starter.py")
args = parser.parse_args()
result, output = run_contract(Path(__file__).resolve().parent,
                              args.implementation, "candidate")
print(output, end="")
raise SystemExit(0 if result.wasSuccessful() else 1)
'''


def directory(name):
    return ROOT / "scenarios" / SCENARIOS[name]


def export_packet(name, destination):
    destination = Path(destination).resolve()
    if destination.exists():
        raise ValueError("Choose an output directory that does not exist")
    destination.mkdir(parents=True)
    source = directory(name)
    manifest = json.loads((source / "exercise.json").read_text())
    for filename in manifest["candidate_files"]:
        shutil.copy2(source / filename, destination / filename)
    shutil.copy2(ROOT / "support.py", destination / "support.py")
    shutil.copy2(ROOT / "templates" / "intent.md", destination / "intent.md")
    shutil.copy2(ROOT / "LICENSE", destination / "LICENSE")
    (destination / "README.md").write_text((source / "CANDIDATE.md").read_text())
    (destination / "run.py").write_text(PACKET_RUNNER)
    return destination


def verify():
    ok = True
    for name in SCENARIOS:
        folder = directory(name)
        manifest = json.loads((folder / "exercise.json").read_text())
        reference, output = run_contract(folder, "reference.py", name + "_reference")
        if not reference.wasSuccessful():
            ok = False
            print(output)
        starter, starter_output = run_contract(folder, "starter.py", name + "_starter")
        actual = sorted(test.id().split(".")[-1] for test, _ in starter.failures)
        expected = sorted(manifest["expected_starter_failures"])
        baseline_ok = not starter.errors and actual == expected
        if not baseline_ok:
            ok = False
            print("Unexpected starter baseline:", name, actual, "expected:", expected)
            print(starter_output)
        with tempfile.TemporaryDirectory() as temp:
            packet = export_packet(name, Path(temp) / name)
            assert not (packet / "reference.py").exists()
            assert not (packet / "interviewer-guide.md").exists()
            broken = subprocess.run(
                [sys.executable, "run.py"], cwd=packet, capture_output=True, text=True,
                timeout=30,
            )
            export_red = broken.returncode == 1 and all(
                item in broken.stdout + broken.stderr for item in expected
            )
            shutil.copy2(folder / "reference.py", packet / "starter.py")
            repaired = subprocess.run(
                [sys.executable, "run.py"], cwd=packet, capture_output=True, text=True,
                timeout=30,
            )
            export_ok = export_red and repaired.returncode == 0
            if not export_ok:
                ok = False
                print("Export failure:", name, broken.stdout, broken.stderr,
                      repaired.stdout, repaired.stderr)
        print(
            f"{name}: reference {reference.testsRun - len(reference.failures) - len(reference.errors)}"
            f"/{reference.testsRun}; starter expected failures "
            f"{len(actual)}/{len(expected)}; export {'OK' if export_ok else 'FAIL'}"
        )
    demo = load_module(ROOT / "examples" / "state_space_demo.py", "state_space_demo")
    for n in range(1, 5):
        for k in range(1, 4):
            word = demo.de_bruijn(n, k)
            windows = [word[i:i + n] for i in range(len(word) - n + 1)]
            assert len(word) == k ** n + n - 1
            assert len(set(windows)) == k ** n
    print("State-space demo: 12 bounded parameter combinations OK")
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list")
    commands.add_parser("verify")
    test = commands.add_parser("test")
    test.add_argument("scenario", choices=SCENARIOS)
    test.add_argument("--implementation", default="starter")
    export = commands.add_parser("export")
    export.add_argument("scenario", choices=SCENARIOS)
    export.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.command == "list":
        for name in SCENARIOS:
            print(name + ": " + str(directory(name).relative_to(ROOT)))
        return 0
    if args.command == "verify":
        return verify()
    if args.command == "export":
        print("Exported:", export_packet(args.scenario, args.output))
        print("In that folder run: python3 run.py")
        return 0
    implementation = args.implementation
    if implementation in ("starter", "reference"):
        implementation += ".py"
    else:
        implementation = str(Path(implementation).resolve())
    result, output = run_contract(directory(args.scenario), implementation,
                                  args.scenario + "_run")
    print(output, end="")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
