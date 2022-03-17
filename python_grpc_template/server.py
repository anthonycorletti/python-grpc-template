import contextlib
import multiprocessing
import os
import socket
import sys
from concurrent import futures
from typing import Generator, List, Tuple

import grpc

from python_grpc_template.logger import logger
from python_grpc_template.protobuf import messenger_pb2, messenger_pb2_grpc
from python_grpc_template.types import GRPCServerOpts


def server_num_workers() -> int:
    return int(os.getenv("NUM_WORKERS", 3))


def _server_port() -> str:
    return os.getenv("GRPC_SERVER_PORT", "50052")


def _server_host() -> str:
    return os.getenv("GRPC_SERVER_HOST", "localhost")


class Messenger(messenger_pb2_grpc.MessengerServicer):
    def SendMessage(
        self, request: messenger_pb2.Request, context: grpc.RpcContext
    ) -> messenger_pb2.Response:
        logger.info(f"Sending a response to {request.name}")
        return messenger_pb2.Response(message="Hello, %s!" % request.name)


def _run_server(listen_addr: str, server_opts: List[Tuple]) -> None:
    logger.info("Server started. Waiting for requests.")
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=1),
        options=server_opts,
    )
    messenger_pb2_grpc.add_MessengerServicer_to_server(Messenger(), server)
    server.add_insecure_port(listen_addr)
    server.start()
    server.wait_for_termination()


@contextlib.contextmanager
def _reserve_port(port: int) -> Generator:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    if sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 0:
        raise RuntimeError("Failed to set SO_REUSEPORT.")
    sock.bind(("", port))
    try:
        yield sock.getsockname()[1]
    finally:
        sock.close()


def main() -> None:
    num_workers = server_num_workers()
    logger.info(
        f"Initializing server with {num_workers} "
        f"worker{'s' if num_workers > 1 else ''}."
    )
    server_host = _server_host()
    server_port = _server_port()
    server_opts = GRPCServerOpts()
    with _reserve_port(port=int(server_port)) as port:
        listen_addr = f"{server_host}:{port}"
        logger.info(f"Binding to {listen_addr}")
        sys.stdout.flush()
        workers = []
        for _ in range(num_workers):
            worker = multiprocessing.Process(
                target=_run_server,
                kwargs={
                    "listen_addr": listen_addr,
                    "server_opts": server_opts.to_list(),
                },
            )
            worker.start()
            workers.append(worker)
        print(workers)
        for worker in workers:
            worker.join()
        logger.info("here")


if __name__ == "__main__":
    os.environ["TZ"] = "UTC"
    main()
