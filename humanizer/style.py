import os
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

    for i in range(len(words)):
        w = words[i].lower()
        if w in GENZ_DICT:
            words[i] = GENZ_DICT[w][0]

    return " ".join(words)


def _formal(text: str) -> str:
    for k, v in CONTRACTIONS.items():
        text = text.replace(v, k)
    return text


def _casual(text: str) -> str:
    for k, v in CONTRACTIONS.items():
        text = text.replace(k, v)
    return text