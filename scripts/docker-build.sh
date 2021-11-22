#!/bin/sh -ex

docker build -t pygrpcboiler-server --file Dockerfile.server .
docker build -t pygrpcboiler-client --file Dockerfile.client .
