#!/bin/bash
# Take in URL, display all HHTP methods with request
curl -s -I -X OPTIONS $1 | grep -i 'Allow:' |cut -d' ' -f2-
