"""--grep: keep only the entries whose message matches a regular expression."""
import re


def grep(entries, pattern, seen=[]):
    """Return the matching entries; every match is also remembered in seen."""
    matches = []
    for entry in entries:
        if re.compile(pattern).search(entry.message):
            seen.append(entry)
            matches.append(entry)
    return matches
