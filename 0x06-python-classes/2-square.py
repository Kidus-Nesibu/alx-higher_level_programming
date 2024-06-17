#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """A class that represnts a square """
    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represent the size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
