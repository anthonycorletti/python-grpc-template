import os

import grpc

from python_grpc_template.logger import logger
from python_grpc_template.protobuf import messenger_pb2, messenger_pb2_grpc
from python_grpc_template.server import _server_port


def _server_svc_endpoint() -> str:
    return os.getenv("GRPC_SERVER_SVC_NAME", "pygrpcserver")


def run() -> None:
    with grpc.insecure_channel(f"{_server_svc_endpoint()}:{_server_port()}") as channel:
        stub = messenger_pb2_grpc.MessengerStub(channel)
        response = stub.SendMessage(messenger_pb2.Request(name="name@example.com"))
    logger.info("Messenger client received: " + response.message)


if __name__ == "__main__":
    os.environ["TZ"] = "UTC"  # pragma: no cover
    run()  # pragma: no cover
