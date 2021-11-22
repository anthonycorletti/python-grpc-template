#!/bin/sh -ex

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports python_grpc_boilerplate tests scripts --skip python_grpc_boilerplate/protobuf

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place python_grpc_boilerplate tests scripts --exclude=__init__.py,python_grpc_boilerplate/protobuf
black python_grpc_boilerplate tests scripts --exclude python_grpc_boilerplate/protobuf
isort python_grpc_boilerplate tests scripts --skip python_grpc_boilerplate/protobuf
