#!/usr/bin/python3
"""
divides all elements of a matrix.
Elements must be a list of lists of integers or floats
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.
       Elements must be a list of lists of integers or floats
       Returns a new matrix"""

    mxc = []
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if len(matrix) == 0:
        raise TypeError(error)
    for size in matrix:
        if len(size) == 0:
            raise TypeError(error)
        else:
            mxc.append(len(size))
        for val in size:
            if type(val) is not float and type(val) is not int:
                raise TypeError(error)
    if len(set(mxc)) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) is int or type(div) is float:
        pass
    else:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    solve = [[round(val/div, 2) for val in mv2] for mv2 in matrix]
    return solve
