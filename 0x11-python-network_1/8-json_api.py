#!/usr/bin/python3
"""
Takes in a letter and sends a POST request with the letter as a parameter
"""

import requests
from sys import argv


if __name__ == "__main__":

    if len(sys.argv) == 1:
        let = ""

    else:
        let = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    value = {'q': let}

    data = requests.post(url, value)

    try:
        jsn = data.json()
        if jsn:
            print('[{}] {}'.format(jsn['id'], jsn['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
