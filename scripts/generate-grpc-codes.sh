#!/bin/sh -ex

python -m grpc_tools.protoc -I protobuf \
--python_out=python_grpc_template/protobuf \
--grpc_python_out=python_grpc_template/protobuf \
--mypy_out=python_grpc_template/protobuf \
--mypy_grpc_out=python_grpc_template/protobuf \
protobuf/messenger.proto
