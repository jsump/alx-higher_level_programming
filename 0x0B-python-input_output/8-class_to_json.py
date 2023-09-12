#!/usr/bin/python3
"""
Module: 8-class_to_json

This module contains a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""


import json


def class_to_json(obj):
    """
    This function returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.
    """
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, (str, int, bool)):
        return obj
    else:
        return {attr: class_to_json(getattr(obj, attr))
                for attr in dir(obj) if not attr.startswith('__')}
