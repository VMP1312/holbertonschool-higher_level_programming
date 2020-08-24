#!/usr/bin/python3
"""
Takes in a letter and sends a POST request with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    page = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        data = page.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except NoJSON:
        print("Not a valid JSON")
