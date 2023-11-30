#!/bin/bash
# Take in URL, display all HHTP methods with request
curl -s -I -X OPTIONS $1 | grep 'Allow:' | awk '{print $2}'
