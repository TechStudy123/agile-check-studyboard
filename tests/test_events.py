import json
from datetime import date
from pathlib import Path

EVENTS = json.loads(Path(__file__).parent.parent.joinpath("data/events.json").read_text(encoding="utf-8"))
REQUIRED = {"id", "title", "date", "place", "capacity"}


def test_required_fields():
    for e in EVENTS:
        assert REQUIRED <= e.keys(), f"足りない項目があります: {e}"


def test_date_format():
    for e in EVENTS:
        date.fromisoformat(e["date"])


def test_capacity_is_positive():
    for e in EVENTS:
        assert e["capacity"] > 0


def test_ids_are_unique():
    ids = [e["id"] for e in EVENTS]
    assert len(ids) == len(set(ids))
