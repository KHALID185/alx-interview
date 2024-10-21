#!/usr/bin/python3
"""
Generator script for log parsing testing.
Generates random HTTP log entries in the specified format.
"""

import random
import sys
from time import sleep
import datetime

for i in range(10000):
    # Add random delay between log entries
    sleep(random.random())

    # Generate random IP address
    ip = "{}.{}.{}.{}".format(
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255)
    )

    # Generate log entry with current timestamp
    log_entry = '{} - [{}] "GET /projects/260 HTTP/1.1" {} {}\n'.format(
        ip,
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    )

    # Write to stdout and flush
    sys.stdout.write(log_entry)
    sys.stdout.flush()
