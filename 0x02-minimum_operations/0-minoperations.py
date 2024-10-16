#!/usr/bin/python3
"""
This module defines a method to calculate the fewest number of
operations needed to achieve exactly n 'H' characters in the file.
The available operations are 'Copy All' and 'Paste'.
"""

def min_operations(target_count: int) -> int:
    """
    Calculate the minimum number of operations needed to get exactly target_count 'H' characters.

    Args:
        target_count (int): The number of 'H' characters required.

    Returns:
        int: The minimum number of operations, or 0 if impossible.
    """
    if target_count < 2:
        return 0

    total_operations = 0
    current_factor = 2

    while target_count > 1:
        while target_count % current_factor == 0:
            total_operations += current_factor
            target_count //= current_factor
        current_factor += 1

    return total_operations
