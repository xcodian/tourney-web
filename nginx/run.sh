#!/bin/env bash
docker run -it --rm -v "$(pwd)/../frontend/public:/mnt:ro" -v "$(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro" --net host nginx