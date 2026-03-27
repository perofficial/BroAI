import random


def weighted_choice(choices):
    """
    choices = [("typo", 0.5), ("filler", 0.3), ...]
    """

    total = sum(weight for _, weight in choices)
    r = random.uniform(0, total)
    upto = 0

    for choice, weight in choices:
        if upto + weight >= r:
            return choice
        upto += weight

    return choices[-1][0]