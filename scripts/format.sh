#!/bin/sh -ex

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports python_grpc_template tests scripts --skip python_grpc_template/protobuf

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place python_grpc_template tests scripts --exclude=__init__.py,python_grpc_template/protobuf
black python_grpc_template tests scripts --exclude python_grpc_template/protobuf
isort python_grpc_template tests scripts --skip python_grpc_template/protobuf
