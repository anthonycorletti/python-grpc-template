#!/bin/sh -ex

python -m grpc_tools.protoc -I protobuf \
--python_out=python_grpc_boilerplate/protobuf \
--grpc_python_out=python_grpc_boilerplate/protobuf \
--mypy_out=python_grpc_boilerplate/protobuf \
--mypy_grpc_out=python_grpc_boilerplate/protobuf \
protobuf/messenger.proto
