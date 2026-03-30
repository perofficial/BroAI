import os
import re
import random
from .utils.dictionary_loader import load_dictionary

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(BASE_PATH, ".."))

GENZ_DICT = load_dictionary(
    os.path.join(ROOT_PATH, "dictionaries", "slang", "genz.json")
)

CONTRACTIONS = load_dictionary(
    os.path.join(ROOT_PATH, "dictionaries", "grammar", "contractions.json")
)

# Pre-sort keys longest-first so multi-word phrases match before substrings.
# e.g. "could have" must match before "have", "I am" before "am"
_GENZ_KEYS_SORTED = sorted(GENZ_DICT.keys(), key=len, reverse=True)
_CONTRACTION_KEYS_SORTED = sorted(CONTRACTIONS.keys(), key=len, reverse=True)


def apply_style(text: str, tone: str) -> str:
    if tone == "genz":
        return _genz(text)
    elif tone == "formal":
        return _formal(text)
    elif tone == "casual":
        return _casual(text)
    return text


def _genz(text: str) -> str:
    """
    Replace words and multi-word phrases using genz.json.
    Matches longest keys first to avoid partial substitutions.
    Case-insensitive; preserves trailing punctuation.
    """
    result = text

    for key in _GENZ_KEYS_SORTED:
        # Build a regex that matches the key as a whole phrase,
        # case-insensitive, with word boundaries.
        pattern = re.compile(
            r'(?<!\w)' + re.escape(key) + r'(?!\w)',
            re.IGNORECASE
        )

        def replacer(m, _key=key):
            replacement = random.choice(GENZ_DICT[_key])
            # Preserve original capitalisation for sentence starts
            original = m.group(0)
            if original[0].isupper():
                return replacement[0].upper() + replacement[1:]
            return replacement

        result = pattern.sub(replacer, result)

    return result


def _formal(text: str) -> str:
    """
    Expand contractions → formal full forms.
    contractions.json format: { "expanded": "contracted" }
    So we invert: replace contracted → expanded.
    Longest contracted form first to avoid partial matches.
    """
    contracted_to_expanded = {v: k for k, v in CONTRACTIONS.items()}
    keys_sorted = sorted(contracted_to_expanded.keys(), key=len, reverse=True)

    result = text
    for contracted in keys_sorted:
        expanded = contracted_to_expanded[contracted]
        pattern = re.compile(
            r'(?<!\w)' + re.escape(contracted) + r'(?!\w)',
            re.IGNORECASE
        )

        def replacer(m, exp=expanded):
            original = m.group(0)
            if original[0].isupper():
                return exp[0].upper() + exp[1:]
            return exp

        result = pattern.sub(replacer, result)

    return result


def _casual(text: str) -> str:
    """
    Apply contractions → casual short forms.
    contractions.json format: { "expanded": "contracted" }
    Longest expanded form first to avoid partial matches.
    e.g. "could have" → "could've" before "have" is touched.
    """
    result = text
    for expanded in _CONTRACTION_KEYS_SORTED:
        contracted = CONTRACTIONS[expanded]
        pattern = re.compile(
            r'(?<!\w)' + re.escape(expanded) + r'(?!\w)',
            re.IGNORECASE
        )

        def replacer(m, con=contracted):
            original = m.group(0)
            if original[0].isupper():
                return con[0].upper() + con[1:]
            return con

        result = pattern.sub(replacer, result)

    return result