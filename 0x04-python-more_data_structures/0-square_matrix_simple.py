#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    new = [[val**2 for val in row] for row in new[:]]
    return (new)
