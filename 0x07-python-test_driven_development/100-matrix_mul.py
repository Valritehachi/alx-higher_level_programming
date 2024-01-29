#!/usr/bin/python3

def is_rectangle(matrix):
    last_len = 0
    for row in matrix:
        if last_len != 0 and len(row) != last_len:
            return False
        last_len = len(row)
    return True


def matrix_mul(m_a, m_b):
    if m_a is None or m_b is None:
        raise TypeError("m_a must be a list or m_b must be a list")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not is_rectangle(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not is_rectangle(m_b):
        raise TypeError("each row of m_b must be of the same size")

    m_a_cols = len(m_a[0])
    m_b_rows = len(m_b)
    if m_a_cols != m_b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    n = m_a_cols
    m = len(m_a)
    p = len(m_b[0])
    error_message1 = "m_a should contain only integers or floats"
    error_message2 = "m_b should contain only integers or floats"

    output = []
    for i in range(0, m):
        output.append([0] * p)

    for i in range(0, m):
        for j in range(0, p):
            cij = 0
            for k in range(0, n):
                if not isinstance(m_a[i][k], (int, float)):
                    raise TypeError(error_message1)
                if not isinstance(m_b[k][j], (int, float)):
                    raise TypeError(error_message2)
                cij += m_a[i][k] * m_b[k][j]
            output[i][j] = cij

    return output
