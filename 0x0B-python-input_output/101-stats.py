#!/usr/bin/python3
"""
Module Name: 101-stats

Description: This module reads stdin line by line and computes metrics
"""


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


if __name__ == "__main__":
    import sys

    i = 0
    total_size = 0
    status_counts = {}
    possible_status_codes = ['200', '301', '400',
                             '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if i % 10 == 0 and i != 0:
                print_statistics(total_size, status_counts)
            i += 1

            line = line.split()
            try:
                total_size += int(line[-1])
            except Exception:
                pass

            try:
                if line[-2] in possible_status_codes:
                    if status_counts.get(line[-2], -1) == -1:
                        status_counts[line[-2]] = 1
                    else:
                        status_counts[line[-2]] += 1
            except Exception:
                pass

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        raise
