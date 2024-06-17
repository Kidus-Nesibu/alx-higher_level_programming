#!/usr/bin/python3
"""This module defines A Square"""


class Square:
    """Defines a Square class"""
    def __init__(self, size):
        """Initializes the instance variable
        Args:
            size(int): the value of the instance variable
        Raise:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Returns: the value of the size instance value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size instance
        Args:
            value(int): Instance that will be changed by new value
        Raise:
            TypeError: if value is not integer
            ValueError: if value is less than 0
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns: the calculated area"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square in #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
