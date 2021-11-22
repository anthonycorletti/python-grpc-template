import logging
import os
import socket
from concurrent import futures

import grpc

from python_grpc_boilerplate.protobuf import messenger_pb2, messenger_pb2_grpc


class Messenger(messenger_pb2_grpc.MessengerServicer):
    def SendMessage(
        self, request: messenger_pb2.Request, context: grpc.RpcContext
    ) -> messenger_pb2.Response:
        logging.info(f"Sending a response to {request.name}")
        return messenger_pb2.Response(message="Hello, %s!" % request.name)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=7))
    messenger_pb2_grpc.add_MessengerServicer_to_server(Messenger(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    server.start()
    server.wait_for_termination()


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
    serve()
