#!/bin/sh -ex

python -m grpc_tools.protoc -I protobuf \
--python_out=. \
--grpc_python_out=. \
--mypy_out=. \
--mypy_grpc_out=. \
protobuf/python_grpc_template/protobuf/messenger.proto
