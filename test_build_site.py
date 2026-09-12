import json
from pathlib import Path


def test_events_json_exists():
    assert Path("events.json").exists()


def test_events_json_is_valid():
    with open("events.json", "r") as file:
        events = json.load(file)

    assert isinstance(events, dict)
    assert "events" in events
    assert isinstance(events["events"], list)


def test_generated_site_exists():
    assert Path("dist/index.html").exists()


def test_generated_site_contains_event():
    html = Path("dist/index.html").read_text()

    assert "<html" in html