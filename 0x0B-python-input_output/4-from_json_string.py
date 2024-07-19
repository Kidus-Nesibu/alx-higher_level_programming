#!/usr/bin/python3
"""Module that contain a funciton that decodes a json file"""
import json


def from_json_string(my_str):
    """Funciton that decodes a json file"""
    return json.loads(my_str)
