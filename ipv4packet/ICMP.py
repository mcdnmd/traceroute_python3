import struct

from ipv4packet.ICMPHeader import ICMPHeader
from ipv4packet.IP import IP
from ipv4packet.UDP import UDP


class ICMP:
    def __init__(self, ip_header, data=None):
        self.ip_header = ip_header
        if data is None:
            self.header = ICMPHeader()
        else:
            self.parse(data)

    def parse(self, data):
        index = self.ip_header.ihl * 4
        raw_data = data[index:index+4]
        icmp_header = struct.unpack('!BBH', raw_data)
        self.header = ICMPHeader()
        self.header.type = icmp_header[0]
        self.header.code = icmp_header[1]
        self.header.checksum = icmp_header[2]

        if len(data) - index + 3 != 0:
            self.header.data = data[index+4:]
            self.parse_data(self.header.type)

    def parse_data(self, icmp_type):
        if icmp_type == 3 or icmp_type == 11:
            raw_data = self.header.data[4:]
            self.header.data = []
            ip_header = IP(raw_data).header
            self.header.data.append(ip_header)

            if ip_header.protocol == 1:
                self.header.data.append(ICMP(ip_header, raw_data).header)
            elif ip_header.protocol == 17:
                self.header.data.append(UDP(ip_header, raw_data).header)