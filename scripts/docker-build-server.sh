#!/bin/sh -ex

docker build -t pygrpcserver --file Dockerfile.server .
