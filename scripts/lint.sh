#!/bin/sh -ex

mypy python_grpc_template
flake8 python_grpc_template tests --exclude python_grpc_template/protobuf
black python_grpc_template tests --check --exclude python_grpc_template/protobuf
isort python_grpc_template tests scripts --check-only --skip python_grpc_template/protobuf
