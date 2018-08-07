#!/usr/bin/python3
""" This script gets the commits (last 10) of a given repository.
    It doesn't check arguments passed to the script like number or type.
    You've been warned!
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/"
    query = "{}/{}/commits".format(argv[2], argv[1])

    res = requests.get(url + query)
    res = res.json()


    for num, commit in enumerate(res):
        if num == 10:
            break

        sha = commit["sha"]
        autor = commit.get("commit").get("author").get("name")

        print(sha + ": " + autor)
