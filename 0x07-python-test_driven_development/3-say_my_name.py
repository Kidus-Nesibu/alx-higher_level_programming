#!/usr/bin/python3
"""module containing a function that prints a given name"""


def say_my_name(first_name, last_name=""):
    """ Concatinate and write the given argument as one
    Args:
        first_name: string argument containing first name
        last_name: string argument containing last argument
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
