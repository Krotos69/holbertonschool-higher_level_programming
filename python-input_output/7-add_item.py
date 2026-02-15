#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file """

import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

#Load existing list or create a new one
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []
# add all command-line arguements except the script name
items.extend(sys.argv[1:])
# Save the update list
save_to_json_file(items, filename)
