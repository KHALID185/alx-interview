#!/usr/bin/python3
"""
Module that contains a function to rotate a 2D matrix 90 degrees clockwise.
The rotation is performed in-place, meaning no additional matrix is created.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    The transformation is done using the following steps:
    1. Transpose the matrix (swap elements across main diagonal)
    2. Reverse each row

    Args:
        matrix (list[list]): The n x n matrix to rotate
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
