import os
import re
import random
from .utils.dictionary_loader import load_dictionary
from .utils.random_utils import weighted_choice

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

TYPO_DICT = load_dictionary(
    os.path.join(BASE_PATH, "../dictionaries/typos/english.json")
)

# Pre-sort longest phrases first so "per favore" matches before "per"
_TYPO_KEYS_SORTED = sorted(TYPO_DICT.keys(), key=len, reverse=True)

def inject_noise(text: str, level: float = 0.1, seed: int = None) -> str:
    """
    Inject realistic noise into text.

    Strategy:
      1. First pass — replace multi-word phrases from the typo dict (e.g. "per favore" → "pls")
      2. Second pass — word-by-word: typo | drop on remaining tokens
    """
    if seed is not None:
        random.seed(seed)

    # ── Pass 1: multi-word phrase substitution ──────────────────────────────
    for key in _TYPO_KEYS_SORTED:
        if " " not in key:
            continue  # single-word keys handled in pass 2
        if random.random() < level:
            pattern = re.compile(
                r'(?<!\w)' + re.escape(key) + r'(?!\w)',
                re.IGNORECASE
            )
            replacement = random.choice(TYPO_DICT[key])
            text = pattern.sub(replacement, text, count=1)

    # ── Pass 2: word-by-word noise ──────────────────────────────────────────
    words = text.split()
    result = []

    for word in words:
        if random.random() < level:
            action = weighted_choice([
                ("typo", 0.7),
                ("drop", 0.3),
            ])
            if action == "typo":
                result.append(_apply_typo(word))
            # "drop" → word omitted intentionally
        else:
            result.append(word)

    return " ".join(result)


def _apply_typo(word: str) -> str:
    """
    Look up a single word in the typo dict.
    Falls back to a random adjacent-character swap if not found.
    Preserves trailing punctuation.
    """
    # Strip trailing punctuation
    stripped = word.rstrip("?.,!;:")
    punct = word[len(stripped):]
    lower = stripped.lower()

    if lower in TYPO_DICT:
        return random.choice(TYPO_DICT[lower]) + punct

    # Fallback: swap two adjacent characters
    if len(lower) > 3:
        i = random.randint(0, len(lower) - 2)
        chars = list(lower)
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
        return "".join(chars) + punct

    return word