#!/usr/bin/python3
"""
Module: 1-write_file

This module contains a function that writes a string to a text file
(UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file
    (UTF8) and returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars
