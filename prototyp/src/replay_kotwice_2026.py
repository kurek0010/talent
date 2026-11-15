"""Odtwórz cztery archiwalne kotwice TLN-PLN w katalogach tymczasowych."""
from __future__ import annotations

import csv
from datetime import date
from hashlib import sha256
import json
from pathlib import Path
import runpy
import subprocess
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[2]
REVISIONS = ("bfc9eaf", "8c682ca", "4f1cd51", "f11da70")
INPUT = "prototyp/data/first_prints_pln.json"
ANCHORS = "prototyp/data/processed/talent_anchors.csv"
PUBLISHED = "prototyp/data/processed/talent_published.json"
CODE = "prototyp/src/talent_update.py"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def replay(revision: str, workspace: Path) -> None:
    previous = revision + "^"
    today = date.fromisoformat(git("show", "-s", "--format=%aI", revision).decode()[:10])
    for relative in (INPUT, ANCHORS, PUBLISHED, CODE):
        destination = workspace / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(git("show", f"{previous}:{relative}"))
    input_data = (workspace / INPUT).read_bytes()
    if input_data != git("show", f"{revision}:{INPUT}"):
        raise RuntimeError(f"Wejścia zmieniono w commicie {revision}.")
    print(f"{revision}: {today}, SHA-256 wejścia {sha256(input_data).hexdigest()}")
    historical = runpy.run_path(str(workspace / CODE))
    calculate = historical["main"]
    original_calendar = historical["expected_anchor_month"]
    # Podaj historyczne today tej funkcji, która w zwykłym cyklu czyta zegar.
    calculate.__globals__["expected_anchor_month"] = lambda: original_calendar(today)
    calculate()

    result = list(csv.reader((workspace / ANCHORS).read_text().splitlines()))[-1]
    recorded = list(csv.reader(git("show", f"{revision}:{ANCHORS}").decode().splitlines()))[-1]
    if result != recorded:
        raise RuntimeError(f"{revision}: odtworzony wiersz {result}, oryginał {recorded}.")
    registry = json.loads((workspace / PUBLISHED).read_bytes())
    if registry != json.loads(git("show", f"{revision}:{PUBLISHED}")):
        raise RuntimeError(f"{revision}: odtworzony rejestr różni się od oryginału.")
    print(f"Zgodny wiersz: {', '.join(result)}")


if __name__ == "__main__":
    for revision in REVISIONS:
        with TemporaryDirectory() as directory:
            replay(revision, Path(directory))
