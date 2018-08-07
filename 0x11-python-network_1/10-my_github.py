#!/usr/bin/python3
""" This script takes your Github credentials (username and password)
    and uses the Github API to display your id.
    It doesn't check for valid aguments and their types (you've been worned).
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/"
    endpoint = "user"
    auth = (argv[1], argv[2])

    res = requests.get(url + endpoint, auth=auth)
    res = res.json()

    if "id" in res:
        print(res["id"])
    else:
        print("None")
