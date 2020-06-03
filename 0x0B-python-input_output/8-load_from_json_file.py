#!/usr/bin/python3

"""
Module
"""

import json


def load_from_json_file(filename):
    """Creates an Object"""
    with open(filename, 'r') as fl:
        return json.load(fl)
