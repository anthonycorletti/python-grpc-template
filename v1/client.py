import logging
import os

import grpc
import messenger_pb2
import messenger_pb2_grpc


def run() -> None:
    with grpc.insecure_channel('[::]:50051') as channel:
        stub = messenger_pb2_grpc.MessengerStub(channel)
        response = stub.SendMessage(
            messenger_pb2.Request(name='username@example.com'))
    logging.info("Messenger client received: " + response.message)


if __name__ == '__main__':
    tz = "UTC"
    level = logging.INFO
    os.environ["TZ"] = tz
    logging.basicConfig(
        format=(f"[%(asctime)s.%(msecs)03d {tz}] "
                "[%(process)s] [%(pathname)s L%(lineno)d] "
                "[%(levelname)s] %(message)s"),
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S")
    run()
