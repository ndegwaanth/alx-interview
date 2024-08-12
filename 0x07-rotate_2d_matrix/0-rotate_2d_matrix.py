#!/usr/bin/python3


"""0-rotate_2d_matrix.py"""


def transpose(matrix):
    """
    This function transpose the matrix given
    matrix: array: this is an array of object
    """
    for row in range(len(matrix)):
        for column in range(row + 1, len(matrix)):
            matrix[row][column], matrix[column][row] = matrix[column][row],\
                    matrix[row][column]


def rotate_2d_matrix(matrix):
    """
    This function rotate the natrix in a 90 degree
    matrix: array: this is a 2d array of object
    """
    transpose(matrix)
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix
