#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n 'H' characters.
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            # Copy All
            clipboard = current_length
            operations += 1
        
        # Paste
        current_length += clipboard
        operations += 1

    return operations if current_length == n else 0
