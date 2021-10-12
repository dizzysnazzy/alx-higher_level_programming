#!/usr/bin/python3
# 3-to_json_string.py
# Dismas Kipchumba <dismaskipchumba2@gmail.com>
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
