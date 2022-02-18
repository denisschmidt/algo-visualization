from random import randint, choice


def spawn(x: int, y: int, choices=None):
    if choices is None:
        return randint(0, x - 1), randint(0, y - 1)
    if len(choices) == 1:
        return (-1, -1)
    return choice(choices)
