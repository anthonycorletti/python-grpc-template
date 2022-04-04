import grpc_testing
from grpc import Server
from pytest import fixture

from python_grpc_template.protobuf import messenger_pb2
from python_grpc_template.server import Messenger

servicers = {messenger_pb2.DESCRIPTOR.services_by_name["Messenger"]: Messenger()}


@fixture(scope="function")
def grpc_server() -> Server:
    return grpc_testing.server_from_dictionary(
        servicers, grpc_testing.strict_real_time()
    )
