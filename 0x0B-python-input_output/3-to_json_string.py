#!/usr/bin/python3
"""A module that contain a function that convert string to json"""
import json


def to_json_string(my_obj):
    """Funciton that return an a json string """
    return json.dumps(my_obj)
