#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n 'H' characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H'
    characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

        if divisor * divisor > n:
            if n > 1:
                operations += n
            break

    return operations
