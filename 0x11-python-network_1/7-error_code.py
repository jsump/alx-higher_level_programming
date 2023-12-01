#!/usr/bin/python3
"""
Module: 7-error_code

this module dsiplays the body of a response
"""


import requests
import sys


def requests_error():
    """
    This method displays the body of a respose,
    which is an error code.
    """
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == '__main__':
    requests_error()
