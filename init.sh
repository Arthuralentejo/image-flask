#!/bin/bash
docker build -t ocr-rest-api .
docker run -it -p 5000:5000 -d ocr-rest-api
