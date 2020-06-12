#!/bin/bash
# remove datains2 first
docker rm -f datains2

# start datains2 container on port 8080
docker run -d -p 8080:8080 --name datains2 datains2:dev

# create admin
docker exec -it datains2 superset fab create-admin \
               --username admin \
               --firstname Superset \
               --lastname Admin \
               --email admin@superset.com \
               --password admin

# upgrade database
docker exec -it datains2 superset db upgrade

# load examples
docker exec -it datains2 superset load_examples

# set roles
docker exec -it datains2 superset init

echo "datains2 up! service url: http://47.103.79.104:8080/login"

