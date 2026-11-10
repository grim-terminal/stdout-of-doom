"""--since: keep only the entries from the last N minutes, hours or days."""
from datetime import datetime, timedelta

UNITS = {"m": 60, "h": 3600, "d": 86400}


def parse_age(text: str) -> timedelta:
    """'15m', '2h' or '1d' as a timedelta."""
    return timedelta(seconds=int(text[:-1]) * UNITS[text[-1]])


def recent(entries, age: timedelta):
    """Entries at or after now minus age."""
    cutoff = datetime.now() - age
    return [e for e in entries if e.time > cutoff]
