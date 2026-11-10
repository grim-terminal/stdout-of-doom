from datetime import datetime, timezone

from doom.parse import Entry, parse_line, parse_lines


def test_parses_a_well_formed_line():
    entry = parse_line("2026-11-09T21:43:48Z ERROR payment gateway timeout\n")
    assert entry == Entry(
        datetime(2026, 11, 9, 21, 43, 48, tzinfo=timezone.utc), "ERROR", "payment gateway timeout"
    )


def test_skips_an_unknown_level():
    assert parse_line("2026-11-09T21:43:48Z LOUD something") is None


def test_skips_a_bad_timestamp():
    assert parse_line("yesterday ERROR something") is None


def test_skips_a_short_line():
    assert parse_line("ERROR") is None


def test_parse_lines_drops_the_bad_ones():
    lines = ["2026-11-09T21:43:48Z INFO ok", "garbage", "2026-11-09T21:43:49Z WARN slow"]
    assert [e.level for e in parse_lines(lines)] == ["INFO", "WARN"]
