#!/usr/bin/python3
"""
Module: 101-stats

This module contains a scrip that reads stdin line by line
and computes the metrics.
"""


import sys
from collections import defaultdict


def compute_metrics():
    """
    This function is used to calculate the metrics of stdin-read lines.
    """
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            ip, _, _, status_code, file_size = line.split()[0:5]
            total_size += int(file_size)
            status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


def print_stats(total_size, status_codes):
    """
    This function prints the metrics.
    """
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        print(f"{code}: {count}")
