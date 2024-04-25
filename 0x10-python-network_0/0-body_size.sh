#!/bin/bash
# Use curl to fetch the response body and count its size in bytes
curl -s "$1" | wc -c
