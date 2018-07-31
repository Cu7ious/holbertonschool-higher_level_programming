#!/usr/bin/env bash
# This script request the URL provided by user and displays the size
# of the body of the response in bytes
curl -Is "$1" | grep "Content-Length:" | cut -d " " -f 2
