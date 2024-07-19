#!/usr/bin/python3
"""A module containing a function that writes to a file"""


def write_file(filename="", text=""):
    """Funciton that writes a text to a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
