#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        str = ""
        for i in range(len(row)):
            str += "{:d}".format(row[i])
            if i < (len(row)-1):
                str += " "
        print(str)
