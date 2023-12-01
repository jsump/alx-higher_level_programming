#!/usr/bin/python3
"""
Module: 6-post_email

this modulecontains a methos that displays the body of a response
"""


import requests
import sys


def requests_email():
    """
    this method takes ina url and an email address
    sends a POST request to the passed URL with the emai
    as parameter, and displays the body of response
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)
    # see this one doesn't need the data to be in bytes
    print(response.text)


if __name__ == '__main__':
    requests_email()
