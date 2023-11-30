#!/bin/bash
# Take in a URL, send a GET re to it, display the body of response
curl -s -o /dev/null -w "%{http_code}\n" $1 | [ "$http_code" == "200" ] && curl -s $1
