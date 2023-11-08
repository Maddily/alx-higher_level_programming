#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute the square value of each integer in a matrix"""

    # new_matrix = list(map(lambda x: list(map(lambda a: a**2, x)), matrix))

    new_matrix = [[y**2 for y in x] for x in matrix]
    return new_matrix
