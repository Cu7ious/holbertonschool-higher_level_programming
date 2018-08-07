#!/usr/bin/python3
"""
Send a post request to an ip
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    try:
        inputs = {'q': q}
        r = requests.post("http://0.0.0.0:5000/search_user", data=inputs)

        dic = r.json()
        if "name" in dic and "id" in dic:
            print("[{}] {}".format(dic["id"], dic["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
