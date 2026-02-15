#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""

import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

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
