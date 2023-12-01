#!/usr/bin/python3
"""
Module: 0-hbtn_status

This contains a method that fetches a url's status
"""

import urllib.request


def fetch_url_status():
    """
    This methos fetches the status of a url
    """
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')

    print('- Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t - content: {}'.format(body))
    print('\t - utf8 content: {}'.format(body))


if __name__ == '__main__':
    fetch_url_status()
