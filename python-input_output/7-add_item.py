#!/usr/bin/python3
""" script that adds all arguments to a Python list, and then save them to 
    a file """
    
import sys
import os

from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file

filename = "add_item.json"

if exists?(filename):
    items = load_from_json_file(filename)
else:
    items = []
# add all command-line arguements except the script name
items.extend(sys.argv[1:])
# Save the update list
save_to_json_file(items, filename)
