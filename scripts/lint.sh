#!/bin/sh -ex

mypy python_grpc_boilerplate
flake8 python_grpc_boilerplate tests --exclude python_grpc_boilerplate/protobuf
black python_grpc_boilerplate tests --check --exclude python_grpc_boilerplate/protobuf
isort python_grpc_boilerplate tests scripts --check-only --skip python_grpc_boilerplate/protobuf
