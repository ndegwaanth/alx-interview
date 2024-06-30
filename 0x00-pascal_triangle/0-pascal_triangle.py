#!/usr/bin/python3
"""
Pascal triangle formation
"""


def pascal_triangle(n):
    """
    Pascal triangle functon defination
    arg: n : This is is the positve integer being passed on
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
