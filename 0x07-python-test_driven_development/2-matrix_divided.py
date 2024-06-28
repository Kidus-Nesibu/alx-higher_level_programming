#!/usr/bin/python3
"""Module containing a function that divides a matrix by a given number """


def matrix_divided(matrix, div):
    """Divides elements of matrix by a given number
    Args:
        matrix: list containing 2 lists which has equal number of items
        div: Value given to divide the matrix with
    Raises:
        TypeError: if type of div is not float or int
        TypeError: if type of matrix is not list
        TypeError: if type of row is not float or int
        ZeroDivisionErorr: if the value given to div is 0
    Returns: The Divided matrix result as a list within a list
    """
    result = []
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (float, int)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    length = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for item in row:
            if isinstance(item, (int, float)):
                new_row.append(round(item / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
        result.append(new_row)
    return result
