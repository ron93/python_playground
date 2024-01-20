from part_1 import build_query, DNSHeader,  DNSQuestion

from dataclasses import dataclass
import struct
from io import BytesIO


@dataclass
class DNSRecord:
    name: bytes
    type_: int
    class_: int
    ttl: int
    data: bytes
