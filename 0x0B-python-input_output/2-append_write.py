#!/usr/bin/python3
"""
Module: 2-append_write

This module contains a function that appends
a string at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    This function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.seek(0, 2)
        num_chars = file.write(text)
    return num_chars
