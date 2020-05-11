#!/bin/bash

CONTAIN_NAME="superset"
CONTARIN_PORT=8080

docker rm -vf ${CONTAIN_NAME}

current_path=$(cd "$(dirname $0)";pwd)
echo ${current_path}
#docker run -d -p ${CONTARIN_PORT}:8080 -v `pwd`/incubator-superset:/app/superset_home --name ${CONTAIN_NAME} superset:dev
docker run -d -p ${CONTARIN_PORT}:8080 -v ${current_path}:/app/superset_home --name ${CONTAIN_NAME} superset:dev

