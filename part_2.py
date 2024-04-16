from part_1 import build_query, DNSHeader,  DNSQuestion

from dataclasses import dataclass
import struct
from io import BytesIO


@dataclass
class DNSRecord:
    name: bytes # domain name 
    type_: int # A, AAA, MX, TXT - encoded as an interger
    class_: int # always 1
    ttl: int # how log to cache the query for 
    data: bytes # record contents - like IP address

#parse dns header
def parse_header(reader):
    items = struct.unpack("!HHHHHH",  reader.read(12))
    return DNSHeader(*items)