#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | grep -e Allow | cut -d":" -f2 | sed -e 's/^ //'
