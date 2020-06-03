#!/usr/bin/python3
"""
Adds all arguments to a Python list
"""

import sys
import os.path

args = sys.argv[1:]

save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

add = []
if os.path.exists("./add_item.json"):
    add = load("add_item.json")

save(add + args, "add_item.json")
