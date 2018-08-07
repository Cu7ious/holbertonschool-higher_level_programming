#!/usr/bin/python3
""" This script uses Star Wars API to search for characters
    Doesn't checks for number or type of the passed arguments
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://swapi.co/api/people/"
    query = "?search="
    req = url + query + sys.argv[1]

    req = requests.get(req)

    res = req.json()

    print("Number of results: {}".format(res["count"]))
    for character in res["results"]:
        print(character["name"])
