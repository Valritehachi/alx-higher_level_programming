#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(item*item)
        new_matrix.append(new_row)
    return new_matrix
