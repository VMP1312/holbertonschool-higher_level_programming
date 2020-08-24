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
        jsn = page.json()
        if jsn:
            print("[{}] {}".format(jsn["id"], jsn["name"]))
        else:
            print("No result")
    except NoJSON:
        print("Not a valid JSON")
