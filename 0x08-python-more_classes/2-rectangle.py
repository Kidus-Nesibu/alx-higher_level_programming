#!/usr/bin/python3
"""A module that defines a rectangle """


class Rectangle:
    """class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a private attributes
        Args:
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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets a heights value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets heights value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
    
    def area(self):
        return (self.__height * self.__width)
    
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            result = 0
        result = (self.__height) * + (self.__width) * 2
        return result
