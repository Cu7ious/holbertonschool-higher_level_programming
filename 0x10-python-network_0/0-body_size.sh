#!/bin/bash
# Requests URL provided by user and displays the size of response body in bytes
curl -Is "$1" | grep "Content-Length:" | cut -d " " -f 2
