from random import choice

answers = ["Yes", "No", "Sorry, what?"]


def give():
    """Return random advice"""
    return choice(answers)
