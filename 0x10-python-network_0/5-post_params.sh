#!/bin/bash
# Send POST req, send with var email ans subject
curl -s -X POST -d "email=$email&subject=$subject" $1
