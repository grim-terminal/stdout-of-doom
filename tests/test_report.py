from datetime import datetime, timezone

from doom.parse import Entry
from doom.report import render, summarize

T = datetime(2026, 11, 9, tzinfo=timezone.utc)


def entries(*pairs):
    return [Entry(T, level, message) for level, message in pairs]


def test_summarize_counts_levels_and_error_messages():
    levels, errors = summarize(
        entries(("INFO", "up"), ("ERROR", "db down"), ("ERROR", "db down"), ("ERROR", "disk full"))
    )
    assert levels["INFO"] == 1 and levels["ERROR"] == 3
    assert errors["db down"] == 2 and errors["disk full"] == 1


def test_render_lists_every_level_and_the_most_common_errors_first():
    levels, errors = summarize(entries(("ERROR", "a"), ("ERROR", "b"), ("ERROR", "b")))
    out = render(levels, errors).splitlines()
    assert out[0] == "levels:"
    assert out.index("errors:") > 0
    assert out[-2].endswith("b") and out[-1].endswith("a")


def test_render_without_errors_has_no_error_section():
    levels, errors = summarize(entries(("INFO", "ok")))
    assert "errors:" not in render(levels, errors)
