import random


def weighted_choice(choices: list) -> str:
    """
    Select a choice based on weights.

    Args:
        choices: list of (value, weight) tuples

    Returns:
        selected value (str)
    """
    total = sum(weight for _, weight in choices)
    r = random.uniform(0, total)
    upto = 0.0
    for choice, weight in choices:
        upto += weight
        if r <= upto:
            return choice
    return choices[-1][0]
