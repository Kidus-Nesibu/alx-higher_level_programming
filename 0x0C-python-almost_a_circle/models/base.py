#!/usr/bin/python3
"""A module that contain a Base class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = id
