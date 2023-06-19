from random import choice

places = ["Mcdonalds", "KFC", "BurgerKing"]


def pick():
    """임의의 패스트푸드점 반환"""
    return choice(places)
