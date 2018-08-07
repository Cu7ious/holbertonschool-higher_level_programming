#!/usr/bin/python3
""" Send data to a site using requests
"""
import requests
import sys


if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    res = requests.post(sys.argv[1], data=email)

    print(res.text)
