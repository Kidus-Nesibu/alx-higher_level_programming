#!/usr/bin/python3
"""A module that contain a function that determines instance of an object"""


def is_same_class(obj, a_class):
    """Function that Checks if obj is instance of a_class
    Args:
        obj: object created
        a_class: a class to check against
    """
    if type(obj) == a_class:
        return True
    else:
        return False
