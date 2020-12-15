import os
import random
import struct
import ipaddress

from ipv4packet.IPHeader import IPHeader


class IP:
    def __init__(self, data=None):
        if data is None:
            self.header = IPHeader()
        else:
            self.parse(data)

    def parse(self, data):
        raw_header = data[:20]
        ip_header = struct.unpack('!BBHHHBBH4s4s', raw_header)
        self.header = IPHeader()
        self.header.version = ip_header[0] >> 4
        self.header.ihl = ip_header[0] & 15
        self.header.dscp = ip_header[1] >> 2
        self.header.ecn = ip_header[1] & 3
        self.header.total_length = ip_header[2]
        self.header.id = ip_header[3]
        self.header.dont_fragment_flag = (ip_header[4] >> 13) & 0b10
        self.header.more_fragments_flag = (ip_header[4] >> 13) & 1
        self.header.offset = ip_header[4] & 4096
        self.header.ttl = ip_header[5]
        self.header.protocol = ip_header[6]
        self.header.header_checksum = ip_header[7]
        self.header.source_address = ipaddress.IPv4Address(ip_header[8])
        self.header.destination_address = ipaddress.IPv4Address(ip_header[9])

    def create_ip_header(self, src, dst, ttl, protocol):
        self.header.version = 4
        self.header.ihl = 5
        self.header.dscp = 0
        self.header.ecn = 0
        self.header.id = os.getpid() & 0xFFFF0
        self.header.dont_fragment_flag = 1
        self.header.more_fragments_flag = 0
        self.header.offset = 0
        self.header.ttl = ttl
        self.header.protocol = protocol
        self.header.header_checksum = 1
        self.header.source_address = ipaddress.IPv4Address(src)
        self.header.destination_address = ipaddress.IPv4Address(dst)

    def pack(self):
        version_ihl = (self.header.version << 4) + self.header.ihl
        dscp_ecn = (self.header.dscp << 2) + self.header.ecn
        flags_offset = (self.header.zero_flag << 15) + (
                    self.header.dont_fragment_flag << 14) + (
                                   self.header.more_fragments_flag << 13) + \
                       self.header.offset

        result = struct.pack('!BBHHHBBH4s4s', version_ihl, dscp_ecn,
                             self.header.total_length, self.header.id,
                             flags_offset, self.header.ttl,
                             self.header.protocol, self.header.header_checksum,
                             int(self.header.source_address).to_bytes(4,
                                                                      'big'),
                             int(self.header.destination_address).to_bytes(4,
                                                                           'big'))
        return result
