#!/bin/bash
# Write a Bash script that takes in a URL and also displays all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
