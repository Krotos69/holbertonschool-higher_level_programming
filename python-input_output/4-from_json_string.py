#!/usr/bin/python3
"""
Returns an object (Python data structure) represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """
    Return the object represent by json string
    """
    return json.loads(my_str)
