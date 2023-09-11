#!/usr/bin/python3
"""
Module: 0-lookup

This module contains a function that returns the list
of available attributes and methods of an object.
"""


def lookup(obj):
    """
    This function returns the list of available attributes
    and methods of an object.

    Return:
        List of attributes and methods of an object.
    """
    return dir(obj)
