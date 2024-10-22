#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""


import sys


def print_stats(size, status_codes):
    """Print accumulated metrics"""
    print("File size: {}".format(size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


def parse_line(line):
    """
    Parse a line and return the status code and file size
    Returns None if line is invalid
    """
    try:
        parts = line.split()
        if len(parts) < 2:
            return None
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (ValueError, IndexError):
        return None


if __name__ == "__main__":
    size = 0
    count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            count += 1
            parsed = parse_line(line)

            if parsed:
                status_code, file_size = parsed
                if status_code in status_codes:
                    status_codes[status_code] += 1
                size += file_size

            if count % 10 == 0:
                print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
