#!/usr/bin/python3
"""
Module for UTF-8 validation.
Implements a method to determine if a given data set represents UTF-8
"""


def validUTF8(data):
    """
    Determines if the given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers where each integer

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise

    UTF-8 Encoding Rules:
    - 1-byte char: 0xxxxxxx
    - 2-byte char: 110xxxxx 10xxxxxx
    - 3-byte char: 1110xxxx 10xxxxxx 10xxxxxx
    - 4-byte char: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
    """
    # Constant for checking the most significant bit
    FIRST_BIT = 1 << 7
    # Constant for checking the second most significant bit
    SECOND_BIT = 1 << 6

    pending_bytes = 0

    for byte in data:
        # Keep only the 8 least significant bits
        byte = byte & 255

        # If we're not currently in a multi-byte sequence
        if pending_bytes == 0:
            # Count how many 1s at the start to determine bytes in sequence
            mask = FIRST_BIT
            while mask & byte:
                pending_bytes += 1
                mask = mask >> 1

            # Single byte character
            if pending_bytes == 0:
                continue

            # Invalid scenarios: 1 byte or more than 4 bytes
            if pending_bytes == 1 or pending_bytes > 4:
                return False

            # Adjust count to exclude the current byte
            pending_bytes -= 1

        # Handling continuation bytes (must start with 10)
        else:
            # Check if byte starts with 10
            if not (byte & FIRST_BIT and not (byte & SECOND_BIT)):
                return False
            pending_bytes -= 1

    # All sequences must be complete
    return pending_bytes == 0
