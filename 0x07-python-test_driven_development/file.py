#!/usr/bin/python3
"""This module defines a function that draws a square using a hash symbol"""
def print_square(size):
    """A function that prints a square using # symbol
    Args:
        size: number of the printed hash 
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print("")