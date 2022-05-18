#!/usr/bin/bash
docker stop $(docker ps -aq)
source init.sh