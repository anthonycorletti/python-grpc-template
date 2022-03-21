#!/bin/sh -ex

docker run -it --rm --network pygrpc --name pygrpcclient pygrpcclient
