#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    page = requests.get(argv[1])
    if page.status_code >= 400:
        print("Error code:", page.status_code)
    else:
        print(page.text)
