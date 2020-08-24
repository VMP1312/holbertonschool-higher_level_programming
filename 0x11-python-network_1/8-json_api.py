#!/usr/bin/python3
"""
Takes in a letter and sends a POST request with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    page = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        data = page.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except NoJSON:
        print("Not a valid JSON")
