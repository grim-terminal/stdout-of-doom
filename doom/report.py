"""Count entries and render the summary."""
from collections import Counter

from doom.parse import LEVELS


def summarize(entries):
    """Return (entries per level, ERROR entries per message)."""
    levels = Counter()
    errors = Counter()
    for entry in entries:
        levels[entry.level] += 1
        if entry.level == "ERROR":
            errors[entry.message] += 1
    return levels, errors


def render(levels, errors, top=None) -> str:
    lines = ["levels:"]
    for level in LEVELS:
        lines.append(f"  {level:<5} {levels[level]}")
    if errors:
        lines.append("errors:")
        for message, count in errors.most_common(top):
            lines.append(f"  {count:>4}  {message}")
    return "\n".join(lines)
