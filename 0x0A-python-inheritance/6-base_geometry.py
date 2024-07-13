#!/usr/bin/python3
"""A module that contains a BaseGeometry class"""


class BaseGeometry(object):
    """A class that defines a Geometry"""
    def area(self):
        """A funciton that raises an Exception"""
        raise Exception("area() is not implemented")
