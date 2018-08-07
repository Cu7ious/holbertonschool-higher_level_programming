#!/usr/bin/python3
""" Displays the value of a header
"""
import urllib.request as req
import sys


if __name__ == "__main__":
    with req.urlopen("{}".format(sys.argv[1])) as html:
        print("{}".format(html.getheader("X-Request-Id")))
