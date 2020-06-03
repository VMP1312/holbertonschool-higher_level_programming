#!/usr/bin/python3
"""
Module.
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file"""
    with open(filename, 'w') as fl:
        fl.write(json.dumps(my_obj))
