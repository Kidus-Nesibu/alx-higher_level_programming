#!/usr/bin/python3
"""A Module that contain a funciton that decodes a Json file"""
import json


def load_from_json_file(filename):
    """A funciton that decodes a Json file"""
    with open(filename, mode="r") as file:
        return json.load(file)
