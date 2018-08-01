#!/bin/bash
# Takes a URL as an argument, sends a GET request to it, displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
