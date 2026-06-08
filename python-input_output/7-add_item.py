#!/usr/bin/python3
"""Defines a function that adds all arguments to a Python list,
    and then save them to a file."""

import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the filename to store the list
filename = "add_item.json"

# Load existing list or create a new one
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments except the script name
items.extend(sys.argv[1:])

# Save the updated list
save_to_json_file(items, filename)
