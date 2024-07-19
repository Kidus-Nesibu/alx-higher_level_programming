#!/usr/bin/python3
"""A module that writes an Object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """Funciton that wirtes an Object to a text file"""
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
