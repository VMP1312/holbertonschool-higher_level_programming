#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of "X-Request" variable.
"""

import requests
from sys import argv

if __name__ == "__main__":
    page = requests.get(argv[1])
    print(page.headers.get('X-Request-Id'))
