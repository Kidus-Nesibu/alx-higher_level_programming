#!/usr/bin/python3
"""Module containing a function that divides a matrix by a given number """


def matrix_divided(matrix, div):
    """Divides elements of matrix by a given number
    Args:
        matrix: list containing 2 lists which has equal number of items
        div: Value given to divide the matrix with
    Raises:
        TypeError: if items of list are not int/float or lists are not equal
        ZeroDivisionErorr: if the value given to div is 0
    Returns: The Divided matrix result as a list within a list
    """
    result = []
    if div == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    length = len(matrix[0])
    for row in matrix:
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []

        for item in row:
            if isinstance(item, (int, float)):
                new_row.append(round(item / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
        result.append(new_row)
    return result
