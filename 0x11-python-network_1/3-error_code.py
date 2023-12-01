#!/usr/bin/python3
"""
Module: 3-error_code

This module contains a methos that displays the body of a response
"""


import sys
import urllib.request
import urllib.error


def error_code():
    """
    This method take in a url
    Sends a request to the url
    Displays the body of the response which is an error code
    """
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            body_str = body.decode('utf-8')
            
            print(body_str)
    except:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    error_code()
