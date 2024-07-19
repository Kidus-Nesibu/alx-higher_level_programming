#!/usr/bin/python3
"""A module containing a function that append to a file"""


def append_write(filename="", text=""):
    """Function that append to a file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
