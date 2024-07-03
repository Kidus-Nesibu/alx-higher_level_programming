#!/usr/bin/python3
"""A module that defines a rectangle """


class Rectangle:
    """class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a private attributes
        Args:
            self: it's a constant for every Instance created
            width: given value for width
            height: given height
        Raises:
            TypError: if width and height is not an integer
            ValueError: if height and widht is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets a width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets a heights value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets width value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueEror("height must be >= 0")
        self.__height = value