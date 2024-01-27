#!/usr/bin/python3
"""
This module divides all elements of a matrix.

Module: my_math_module

Functions:
    - add_integer(a, b=98): divides two numbers and returns the result.

"""
def matrix_divided(matrix, div):
    """
    divs two numbers and returns the result.
    Args:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of the two numbers, converted to an integer.
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix is None or len(matrix) == 0:
        raise TypeError(matrix_error)

    new_matrix = []
    last_row_size = 0
    for row in matrix:
        if row is None or (not isinstance(row, list)):
            raise TypeError(matrix_error)
        row_len = len(row)
        if last_row_size != 0 and row_len != last_row_size:
            raise TypeError("Each row of the matrix must have the same size")
        last_row_size = row_len
        new_row = []
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            item = item/div 
            new_row.append(round(item, 2))
        new_matrix.append(new_row)
    return new_matrix

