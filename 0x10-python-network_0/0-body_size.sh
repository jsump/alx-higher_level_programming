#!/usr/bin/bash
# This script takes ina a RUL, sends request o it and displays the size of body of reponse
curl -s -w "%{size_download}" -o /dev/null "$1"
