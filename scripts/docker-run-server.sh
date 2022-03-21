#!/bin/sh -ex

docker run -it --rm --network pygrpc -p 50051:50051 --name pygrpcserver pygrpcserver
