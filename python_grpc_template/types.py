from dataclasses import asdict, dataclass
from typing import List, Tuple


@dataclass
class GRPCServerOpts:
    max_send_message_length: int = -1
    max_receive_message_length: int = -1
    so_reuseport: int = 1
    use_local_subchannel_pool: int = 1

    def to_list(self) -> List[Tuple[str, int]]:
        return [(f"grpc.{k}", v) for k, v in asdict(self).items()]
