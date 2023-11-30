#!/bin/bash
# Take in URL as arg, send a GET req to it, displays the body of response
curl -s -H "$header" $1
