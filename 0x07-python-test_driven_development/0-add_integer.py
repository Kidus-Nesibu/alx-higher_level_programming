#!/usr/bin/python3


"""A module That a function to add integers"""


def add_integer(a, b=98):
    """Return the sum of integers
    Args:
        a: first argument
        b: second argument

    Return:
        sum of the two arguments

    Raise:
        TyepError: if either of the arguments not an integer or a float

    """
    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
