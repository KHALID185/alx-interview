#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    n (int): Number of rows to generate.

    Returns:
    list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    result = [[1]]
    for _ in range(1, n):
        prev_row = result[-1]
        new_row = [1]
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        new_row.append(1)
        result.append(new_row)

    return result
