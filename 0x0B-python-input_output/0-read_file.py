#!/usr/bin/python3
"""A module containing a function that opens and read file"""


def read_file(filename=""):
    """Function that opens and read a file and display it"""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
