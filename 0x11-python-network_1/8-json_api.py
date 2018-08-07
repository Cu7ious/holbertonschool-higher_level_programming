#!/usr/bin/python3
""" Send a post request to an ip
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = ""
    try:
        url = "http://172.31.54.208:39995/search_user"
        data = {"q": query}
        res = requests.post(url, data=data)

        user = res.json()
        if "name" in user and "id" in user:
            print("[{}] {}".format(user["id"], user["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
