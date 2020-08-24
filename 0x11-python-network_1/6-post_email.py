#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    page = requests.post(argv[1], data={'email': argv[2]})
    print(page.text)
