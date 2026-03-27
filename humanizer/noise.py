import os
import random
from .utils.dictionary_loader import load_dictionary
from .utils.random_utils import weighted_choice

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

TYPO_DICT = load_dictionary(
    os.path.join(BASE_PATH, "../dictionaries/typos/english.json")
)

FILLERS = ["uh", "um", "like", "you know"]


def inject_noise(text: str, level: float = 0.1, seed=None) -> str:
    if seed is not None:
        random.seed(seed)

    words = text.split()

    for i in range(len(words)):

        if random.random() < level:

            action = weighted_choice([
                ("typo", 0.5),
                ("filler", 0.3),
                ("drop", 0.2)
            ])

            if action == "typo":
                words[i] = apply_typo(words[i])

            elif action == "filler":
                words[i] += " " + random.choice(FILLERS)

            elif action == "drop":
                words[i] = ""

    return " ".join(filter(None, words))


def apply_typo(word: str) -> str:
    lower = word.lower()

    if lower in TYPO_DICT:
        return random.choice(TYPO_DICT[lower])

    # fallback: small swap typo
    if len(word) > 3:
        i = random.randint(0, len(word) - 2)
        word = list(word)
        word[i], word[i + 1] = word[i + 1], word[i]
        return "".join(word)

    return word