#!/usr/bin/python3
"""
Module: 10-my_github

This module contains a methos that displays one's GitHub id
"""


import requests
import sys


def github_id():
    """
    This method takes one's GitHub credemtials and uses GitHub API
    to diplay your id
    """
    url = "https://api.github.com/user"

    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_id = response.json()['id']
        print(user_id)
    else:
        print("Status code: ", response.status_code)


if __name__ == '__main__':
    github_id()
