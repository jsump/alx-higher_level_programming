#!/usr/bin/python3
"""
Module: 4-hbtn_status

This module contains a method that fetches a url
"""

import requests


def fetch_status():
    """
    this method fetches the status of a url
    """
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t - content: {}".format(response.text))


if __name__ == '__main__':
    fetch_status()
