#!/usr/bin/python3
"""
Takes your Github credentials and uses the Github API to display your id.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    response = requests.get('https://api.github.com/user',
                            auth=(HTTPBasicAuth(argv[1], argv[2])))

    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        response = response.json()
        print(response.get('id'))
