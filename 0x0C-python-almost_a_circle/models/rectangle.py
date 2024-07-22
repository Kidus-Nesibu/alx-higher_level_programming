#!/usr/bin/python3
from models.base import Base
"""A module containing a Rectangle class that inherits from the Base class"""


class Rectangle(Base):
    """A class that defines a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        self.__width = value

    @property
    def height(self):
        """gets the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the widht"""
        self.__height = value

    @property
    def x(self):
        """gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        self.__x = value

    @property
    def y(self):
        """gets the value of y"""
        return self.__y

    @y.setter
    """sets the value of x"""
    def y(self, value):
        self.__y = value
