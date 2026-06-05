#!/usr/bin/env python3
"""
Basic JSON serialization and deserialization module.
Provides functions to save a Python dictionary to a JSON file
and load it back into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Parameters:
        data (dict): The dictionary to serialize.
        filename (str): The path to the output JSON file.
                        If the file exists, it will be replaced.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Parameters:
        filename (str): The path to the JSON file to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
