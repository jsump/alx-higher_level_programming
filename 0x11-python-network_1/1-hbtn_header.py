#!/usr/bin/python3
"""
Module: 1-hbtn_header

This module contains a methos that displays the variable found
in the header of the response
"""


import sys
import urllib.request


def header_response():
    """
    This function dsiplays the value of the x-Request-Id variable
    found in the header of the response
    """
    url = sys.argv[1]

    reqst = urllib.request.Request(url)

    with urllib.request.urlopen(reqst) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == '__main__':
    header_response()
