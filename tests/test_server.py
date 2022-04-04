import grpc
from grpc import Server

from python_grpc_template.protobuf import messenger_pb2


def test_messenger(grpc_server: Server) -> None:
    request = messenger_pb2.Request(name="hello world")
    service = messenger_pb2.DESCRIPTOR.services_by_name["Messenger"]
    method_descriptor = service.methods_by_name["SendMessage"]
    invoke_vaex_runner = grpc_server.invoke_unary_unary(
        method_descriptor=method_descriptor,
        invocation_metadata={},
        request=request,
        timeout=1,
    )
    response, metadata, code, details = invoke_vaex_runner.termination()
    assert code == grpc.StatusCode.OK
