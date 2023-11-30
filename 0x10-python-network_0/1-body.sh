#!/bin/bash
# Take in a URL, send a GET re to it, display the body of response
curl -s -o /dev/null -w "%{http_code}\n" "$url" | [ "$(cat)" == "200" ] && curl -s "$url"
