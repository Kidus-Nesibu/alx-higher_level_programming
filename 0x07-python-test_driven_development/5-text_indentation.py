#!/usr/bin/python3
"""A module conatining  a function that prints a text in a formated way"""


def text_indentation(text):
    """A function that parses a string and prints the text accordingly
    Args:
        text: a string to be formated according to the function
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    index = 1
    length = len(text)

    while index < length:
        char = text[index]
        if char in {'.', ':', '?'}:
            print(char)
            print()
        else:
            print(char, end="")
        index += 1