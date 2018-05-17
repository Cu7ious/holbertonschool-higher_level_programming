#!/usr/bin/python3
from sys import argv
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""
A script that creates json file from arguments
"""


if __name__ == "__main__":
    with open("add_item.json", mode="w", encoding="utf-8") as a_file:
        a_file.write(json.dumps(argv[1:]))
