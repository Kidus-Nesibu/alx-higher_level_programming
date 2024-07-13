#!/usr/bin/python3
"""Module that contain a class called Mylist"""


class MyList(list):
    """A class that has a sort functionalit"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
