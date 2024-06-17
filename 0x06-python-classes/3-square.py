#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """A class that defines a Square"""

    def __init__(self, size=0):
        """Initializes the instance size variable
        Args:
            size(int): gives the value of the square
        Raise:
            TypeError: if it is not an integer
            ValueEror: if it is less than 0
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size msut be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
