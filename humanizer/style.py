import os
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


def apply_style(text: str, tone: str) -> str:
    if tone == "genz":
        return _genz(text)
    elif tone == "formal":
        return _formal(text)
    elif tone == "casual":
        return _casual(text)
    return text


def _genz(text: str) -> str:
    words = text.split()
    for i, word in enumerate(words):
        w = word.lower().rstrip("?.,!")
        punct = word[len(w):]
        if w in GENZ_DICT:
            replacement = random.choice(GENZ_DICT[w])  # FIX: was always [0]
            words[i] = replacement + punct
    return " ".join(words)


def _formal(text: str) -> str:
    # Expand contractions for formal tone
    for contracted, expanded in CONTRACTIONS.items():
        text = text.replace(contracted, expanded)
    return text


def _casual(text: str) -> str:
    # Apply contractions for casual tone
    for expanded, contracted in CONTRACTIONS.items():
        text = text.replace(expanded, contracted)
    return text
