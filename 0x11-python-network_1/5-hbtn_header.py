#!/usr/bin/python3
"""
Module: 5-hbtn_header.py

this module contains a method that displays the value of the resonse header
"""


import sys
import requests


def response_request():
    """
    This method takes in a url,
    sends a request to  the url and
    displays the value of the variable s-requesr-id in the response header
    """
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)


if __name__ == '__main__':
    response_request()
