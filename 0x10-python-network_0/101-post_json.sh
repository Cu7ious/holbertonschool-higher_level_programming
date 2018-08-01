#!/bin/bash
# Sends JSON POST request to the users URL, displays the body of the response
curl -sd @"$2" -X POST "$1" -H "Content-Type: application/json"
