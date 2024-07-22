#!/usr/bin/python3
""" A module containing a Rectangle class that inherits from the base class"""
from models.base import Base


class Rectangle(Base):
    """A class that defines a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

# getter functions
# ==============================================================================

    @property
    def width(self):
        """gets the value of the width"""
        return self.__width

    @property
    def height(self):
        """gets the value of the height"""
        return self.__height

    @property
    def x(self):
        """gets the value of x"""
        return self.__x

    @property
    def y(self):
        """gets the value of y"""
        return self.__y

# setter funcitons
# ====================================================================================

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """sets value of y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
