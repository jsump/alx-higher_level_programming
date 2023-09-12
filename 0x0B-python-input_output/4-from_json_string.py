#!/usr/bin/python3
"""
Module: 4-from_json_string

This module contains a function that returns an object
(Python data structure) represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """
    This function that returns an object (Python data structure)
    represented by a JSON string.
    """
    return json.loads(my_str)
