#!/usr/bin/python3
"""
Module: 6-peak

this module contains a methos that finds the peak in a
list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    This method finds the peak in a list of unsorted integers
    """
    n = len(list_of_integers)

    if n == 0:
        return None

    start = 0
    end = n - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]
