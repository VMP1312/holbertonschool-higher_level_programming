#!/usr/bin/python3
"""
Takes your Github credentials and uses the Github API to display your id.
"""

import requests
import sys


if __name__ == "__main__":

    cred = (sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=cred)
    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        response = response.json()
        print(response.get('id'))