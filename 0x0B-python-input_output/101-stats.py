#!/usr/bin/python3
"""
Module Name: 101-stats

Description: This module reads stdin line by line and computes metrics
"""
import re
import signal
import sys
from collections import defaultdict


def print_statistics(total_size, status_counts):
    """
    Prints the statistics.

    Parameters:
    - total_size: The total file size
    - status_counts: A dict mapping status codes to their counts
    """

    print("File size:", total_size)
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")


def handle_interrupt(signum, frame):
    """
    Handles a keyboard interrupt.

    Parameters:
    - signum: Signal number that has triggered the signal handler
        (it's passed as None because it's not needed in this case)
    - frame: The current stack frame at the time the signal was received.
        (it's passed as None because it's not needed in this case)
    """
    print_statistics(total_size, status_counts)
    exit(0)


if __name__ == "__main__":
    i = 1
    total_size = 0
    status_counts = defaultdict(int)
    statistics = open("statistics.txt", "w", encoding="utf-8")
    pattern = re.compile(
        r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
    )

    signal.signal(signal.SIGINT, handle_interrupt)

    try:
        for line in sys.stdin:
            match = pattern.match(line)
            if match:
                ip_address, date, status_code, file_size = match.groups()
                total_size += int(file_size)
                status_counts[status_code] += 1

                if i % 10 == 0 and i != 0:
                    print_statistics(total_size, status_counts)

                i += 1

    except KeyboardInterrupt:
        handle_interrupt(None, None)
