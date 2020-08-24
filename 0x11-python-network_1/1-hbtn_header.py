#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of "X-Request" variable.
"""

import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as page:
        print(page.headers.get('X-Request-Id'))
