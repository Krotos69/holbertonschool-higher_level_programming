#!/usr/bin/python3
"""
function that returns the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """
    Docstring for to_json_string

    :param my_obj: Description
    """
    return json.dumps(my_obj)
