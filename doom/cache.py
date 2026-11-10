"""--cache: keep parsed entries on disk so a big log is parsed once."""
import os
import pickle


def load(path: str):
    """Return the cached entries, or None when there is no cache yet."""
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return pickle.load(f)


def save(path: str, entries) -> None:
    with open(path, "wb") as f:
        pickle.dump(list(entries), f)
