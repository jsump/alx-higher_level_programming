#!/usr/bin/python3
"""
Module: 0-read_file

This module contains a function that reads a text file and prints
it to stdout.
"""


def read_file(filename=""):
    """
    This function reads a text file(UTF8) and prints it
    to stdout.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
