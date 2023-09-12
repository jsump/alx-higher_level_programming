#!/usr/bin/python3
"""
Module: 100-append_after

This module conatins a function that inserts a line of text
to a file, after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file,
    after each line containing a specific string.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
