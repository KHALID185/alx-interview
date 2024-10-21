#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
Calculates total file size and counts of HTTP status codes.
"""

import sys
import re
from typing import Dict, Union, Match


def validate_line(line: str) -> Union[Match, None]:
    """
    Validates if a line matches the expected log format using regex.
    Format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"

    Args:
        line (str): Input line to validate

    Returns:
        Match object if valid, None otherwise
    """
    pattern = (
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
        r'\[.+\] '
        r'"GET /projects/260 HTTP/1.1" '
        r'(\d{3}) '
        r'(\d+)$'
    )
    return re.match(pattern, line)


def print_statistics(total_size: int, status_codes: Dict[int, int]) -> None:
    """
    Prints the computed statistics.

    Args:
        total_size (int): Total sum of file sizes
        status_codes (dict): Dictionary with status codes and their counts
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_logs() -> None:
    """
    Main function to process logs from stdin.
    Handles the log parsing and statistics computation.
    """
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = validate_line(line)
            if match:
                status_code = int(match.group(1))
                file_size = int(match.group(2))

                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        sys.exit(0)

    print_statistics(total_size, status_codes)


if __name__ == "__main__":
    process_logs()
