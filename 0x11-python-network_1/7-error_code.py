#!/usr/bin/python3
""" Prints out the error codes or the response
"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])

    if str(res.status_code)[0] == '2':
        print(res.text)
    else:
        print("Error code: {}".format(res.status_code))
