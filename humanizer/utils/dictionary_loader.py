import json
import os


def load_dictionary(path: str) -> dict:
    """Load a JSON dictionary from disk. Returns empty dict if file not found."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
