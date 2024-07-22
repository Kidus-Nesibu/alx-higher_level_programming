#!/usr/bin/python3
"""This module contains a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Gets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates attributes of an instance"""

        if args:
            if len(args) >= 1:
                if args[0] is not None and not isinstance(args[0], int):
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None and not isinstance(value, int):
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
