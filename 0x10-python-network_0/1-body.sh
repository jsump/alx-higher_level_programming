#!/bin/bash
# Take in a URL, send a GET re to it, display the body of response
curl -s -w "$200" -o /dev/null "$1"
