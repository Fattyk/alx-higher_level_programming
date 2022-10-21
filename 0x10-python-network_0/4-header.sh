#!/bin/bash
# Send a GET request to a URL with header variable X-School-User-Id and value 98
curl -sXH "X-HolbertonSchool-User-Id: 98" "${1}"
