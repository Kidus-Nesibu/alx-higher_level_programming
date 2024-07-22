#!/usr/bin/python3
"""A module that contain a Base class"""


class Base:
    """Class that count number of instances or id's"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
