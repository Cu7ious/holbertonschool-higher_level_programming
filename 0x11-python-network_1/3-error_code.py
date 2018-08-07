#!/usr/bin/python3
""" Get http error codes
"""
from urllib import error, request
from sys import argv


if __name__ == "__main__":
    body = request.Request(argv[1])

    try:
        with request.urlopen(body) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
