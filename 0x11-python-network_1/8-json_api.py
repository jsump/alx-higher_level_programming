#!/usr/bin/python3
"""
Module: 8-json_api

This module contains  amethos that takes a letter and
send the letter tourl as a parameter
"""


import requests
import sys


def search_api():
    """
    This method takes a letter and sends a POST request
    to a url with the letter itself as a parameter
    """
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    # first argument in cmd line

    data = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user')

    try:
        json_response = response.json()
        if json_response:
            print("{} {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    search_api()
