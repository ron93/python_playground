from dataclasses import dataclass
import dataclasses
import struct

@dataclass
class DNSHeader:
    id: int
    flags: int
    num_questions: int = 0
    num_answers: int = 0 
    num_authorities: int = 0
    num_additionals: int = 0

@dataclass
class DNSQuestion:
    name: bytes
    # *type_ -> because type is a reseved  class
    type_: int
    class_: int

# ! before string tells python to use the byte order for computer networking
    # byte order -> big and  small endian
def header_to_bytes(header):
    fields = dataclasses.astuple(header)
    # 6 h's because there are 6 fields
    return struct.pack("!HHHHHH", *fields)

def question_to_bytes(question):
    return question.name  + struct.pack("!HH", question.type_, question.class_)

def encode_dns(domain_name):
    encode = b""
    for part in domain_name.encode("ascii").split(b"."):
        encode += bytes([len(part)]) + part
    return encode + b"\x00"
