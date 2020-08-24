#!/usr/bin/python3
"""
Takes your Github credentials and uses the Github API to display your id.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':

    page = requests.get(
        "https://api.github.com/user",
        auth=(HTTPBasicAuth(argv[1], argv[2])))

    try:
        My_ID = page.json()
        print(My_ID.get('id'))

    except Exception:
        print('None')
