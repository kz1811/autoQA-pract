from random import choice
from string import ascii_letters


def set_random_string():
    random_string = (''.join(choice(ascii_letters) for i in range(15)))
    return random_string
