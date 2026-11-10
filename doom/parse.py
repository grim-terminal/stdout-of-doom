"""Parse log lines of the form '2026-11-09T21:43:48Z ERROR message'."""
from dataclasses import dataclass
from datetime import datetime

LEVELS = ("DEBUG", "INFO", "WARN", "ERROR")


@dataclass(frozen=True)
class Entry:
    time: datetime
    level: str
    message: str


def parse_line(line: str) -> Entry | None:
    """Return the entry for a well-formed line, None for anything else."""
    parts = line.rstrip("\n").split(" ", 2)
    if len(parts) != 3 or parts[1] not in LEVELS:
        return None
    try:
        time = datetime.fromisoformat(parts[0])
    except ValueError:
        return None
    return Entry(time, parts[1], parts[2])


def parse_lines(lines):
    """Yield an Entry for every well-formed line."""
    for line in lines:
        entry = parse_line(line)
        if entry is not None:
            yield entry
