import logging
import os
import socket

import grpc

from python_grpc_boilerplate.protobuf import messenger_pb2, messenger_pb2_grpc


def run() -> None:
    with grpc.insecure_channel("pygrpcserver:50051") as channel:
        stub = messenger_pb2_grpc.MessengerStub(channel)
        response = stub.SendMessage(messenger_pb2.Request(name="name@example.com"))
    logging.info("Messenger client received: " + response.message)


if __name__ == "__main__":
    tz = "UTC"
    level = logging.INFO
    os.environ["TZ"] = tz
    logging.basicConfig(
        format=(
            f"[%(asctime)s.%(msecs)03d {tz}] [{socket.gethostname()}] "
            "[%(process)s] [%(pathname)s L%(lineno)d] "
            "[%(levelname)s] %(message)s"
        ),
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    run()
