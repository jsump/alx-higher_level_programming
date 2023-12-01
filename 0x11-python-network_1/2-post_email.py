#!/usr/bin/python3
"""
Module: 2-post_email

This module contains a function that displays the body of the response.
"""


import sys
import urllib.request
import urllib.parse


def post_email():
    """
    This method takes in a url and email
    Sends a POST to the passed url with email as a parameter
    Displays the body of the response
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')  # Make data into bytes

    reqst = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(reqst) as response:
        body = response.read()
        body_str = body.decode('utf-8')

        print(body_str)


if __name__ == '__main__':
    post_email()
