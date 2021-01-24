import os
import socket
import struct
import time

from ipv4packet.IP import IP
from ipv4packet.UDP import UDP


class ICMPHeader:
    def __init__(self):
        self.type = None
        self.code = None
        self.checksum = None
        self.unused = None
        self.id = None
        self.seq = None
        self.data = None

    def __str__(self):
        return f'---ICMP---\n' \
               f'  Type: {self.type}\n' \
               f'  Code: {self.code}\n' \
               f'  Checksum: {self.checksum}\n' \
               f'  Data:\n' \
               f'  {str(self.data[0])}\n' \
               f'  {str(self.data[1])}'


def icmp_checksum(source_string):
    countTo = (int(len(source_string) / 2)) * 2
    sum = 0
    count = 0

    while count < countTo:
        loByte = source_string[count]
        hiByte = source_string[count + 1]
        sum = sum + (hiByte * 256 + loByte)
        count += 2

    if countTo < len(source_string):
        loByte = source_string[len(source_string) - 1]
        sum += loByte

    sum &= 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum += (sum >> 16)
    answer = ~sum & 0xffff
    answer = socket.htons(answer)

    return answer


class ICMP:
    def __init__(self, ip_header, data=None):
        self.ip_header = ip_header
        if data is None:
            self.header = ICMPHeader()
        else:
            self.parse(data)

    def parse(self, data):
        index = self.ip_header.ihl * 4
        raw_data = data[index:index + 8]
        icmp_header = struct.unpack('!BBH4s', raw_data)
        self.header = ICMPHeader()
        self.header.type = icmp_header[0]
        self.header.code = icmp_header[1]
        self.header.checksum = icmp_header[2]
        self.header.unused = icmp_header[3]

        if len(data) - index - 8 != 0:
            self.header.data = data[index + 8:]
            self.parse_data(self.header.type)

    def parse_data(self, icmp_type):
        if icmp_type == 3 or icmp_type == 11:
            raw_data = self.header.data
            self.header.data = []
            ip_header = IP(raw_data).header
            self.header.data.append(ip_header)

            if ip_header.protocol == 1:
                self.header.data.append(ICMP(ip_header, raw_data).header)
            elif ip_header.protocol == 17:
                self.header.data.append(UDP(ip_header, raw_data).header)

    def create_icmp_header(self):
        self.header.type = 8
        self.header.code = 0
        self.header.checksum = 0
        self.header.id = os.getpid() & 0xFFFF0
        self.header.seq = 0
        self.header.data = struct.pack("d", time.time())

        header = struct.pack('!BBHHh', self.header.type, self.header.code,
                             self.header.checksum, self.header.id,
                             self.header.seq)

        self.header.checksum = icmp_checksum(header + self.header.data)

    def pack(self):
        result = struct.pack('!BBHHh', self.header.type, self.header.code,
                             self.header.checksum, self.header.id,
                             self.header.seq)
        result += self.header.data
        return result
