#!/bin/bash
# Take in a URL, send a GET re to it, display the body of response
curl -s -o /dev/null -w "${200}" "$1"
