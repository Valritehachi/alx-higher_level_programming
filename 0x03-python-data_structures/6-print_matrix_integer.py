#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        str = ""
        for n in row:
            str += "{:d} ".format(n)
        print(str)
