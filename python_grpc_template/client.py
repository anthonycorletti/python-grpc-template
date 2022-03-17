import os

import grpc

from python_grpc_template.logger import logger
from python_grpc_template.protobuf import messenger_pb2, messenger_pb2_grpc


def run() -> None:
    with grpc.insecure_channel("pygrpcserver:50052") as channel:
        stub = messenger_pb2_grpc.MessengerStub(channel)
        response = stub.SendMessage(messenger_pb2.Request(name="name@example.com"))
    logger.info("Messenger client received: " + response.message)


if __name__ == "__main__":
    os.environ["TZ"] = "UTC"
    run()
