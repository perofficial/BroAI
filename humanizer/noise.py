import os
import random
from .utils.dictionary_loader import load_dictionary
from .utils.random_utils import weighted_choice

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

TYPO_DICT = load_dictionary(
    os.path.join(BASE_PATH, "../dictionaries/typos/english.json")
)

FILLERS = ["uh", "um", "like", "you know", "i mean", "kinda"]


def inject_noise(text: str, level: float = 0.1, seed: int = None) -> str:
    if seed is not None:
        random.seed(seed)

    words = text.split()

    result = []
    for word in words:
        if random.random() < level:
            action = weighted_choice([
                ("typo",   0.5),
                ("filler", 0.3),
                ("drop",   0.2),
            ])
            if action == "typo":
                result.append(apply_typo(word))
            elif action == "filler":
                result.append(word)
                result.append(random.choice(FILLERS))
            elif action == "drop":
                pass  # word dropped intentionally
        else:
            result.append(word)

    return " ".join(result)


def apply_typo(word: str) -> str:
    lower = word.lower().rstrip("?.,!")
    punct = word[len(lower):]
    if lower in TYPO_DICT:
        return random.choice(TYPO_DICT[lower]) + punct
    # fallback: swap two adjacent characters
    if len(lower) > 3:
        i = random.randint(0, len(lower) - 2)
        chars = list(lower)
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
        return "".join(chars) + punct
    return word
