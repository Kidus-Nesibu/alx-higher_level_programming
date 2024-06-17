#!/usr/bin/python3
"""The module defines a Square class"""


class Square:
    """Defines a Square class with getter and setter attribute"""
    def __init__(self, size=0):
        """Initializes the instances variable
        Args:
            size(int):the value wich is passed 
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
        return self.__size
    @property.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
