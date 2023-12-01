#!/usr/bin/python3
"""
Module: 0-hbtn_status

This fetches a url
"""

import urllib.request


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print('- Body response:')
print('\t- type: {}'.format(type(body)))
print('\t - content: {}'.format(body))
