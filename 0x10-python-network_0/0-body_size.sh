#!/bin/bash
# This script takes in URL, sends request and displays the size of body of reponse
response_size=$(curl -s -w "%{size_download}" -o /dev/null "$1")
