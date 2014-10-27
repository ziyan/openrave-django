#!/bin/sh

curl -X POST -H 'Content-Type: application/zip' --data-binary @/home/ziyan/software/openrave/src/robots/pr2-beta-static.zae http://localhost:8000/api/robots/
