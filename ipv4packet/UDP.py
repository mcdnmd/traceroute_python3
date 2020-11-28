import struct

from ipv4packet.UDPHeader import UDPHeader


class UDP:
    def __init__(self, ip_header, data=None):
        self.ip_header = ip_header
        if data is None:
            self.header = UDPHeader()
        else:
            self.parse(data)

    def parse(self, data):
        index = self.ip_header.ihl * 4
        raw_data = data[index:index + 8]
        udp_header = struct.unpack('!HHHH', raw_data)
        self.header = UDPHeader()
        self.header.sport = udp_header[0]
        self.header.dport = udp_header[1]
        self.header.length = udp_header[2]
        self.header.checksum = udp_header[3]

        if len(data) - index + 7 != 0:
            self.header.data = data[index + 8:]

    def create_udp_header(self, sport, dport, message=b''):
        self.header.sport = sport
        self.header.dport = dport
        self.header.length = 8 + len(message)
        self.header.data = message
        self.header.checksum = self.calculate_checksum()

    def calculate_checksum(self):
        """https://www.securitynik.com/2015/08/calculating-udp-checksum-with-taste-of.html"""
        src = int(self.ip_header.source_address)
        dst = int(self.ip_header.destination_address)
        part_1 = src >> 16
        part_2 = src & 0b1111_1111
        part_3 = dst >> 16
        part_4 = dst & 0b1111_1111

        pre_value = part_1 + part_2 + part_3 + part_4 + \
                    self.ip_header.protocol + self.ip_header.ihl + \
                    self.header.sport + self.header.dport + \
                    self.header.length + 0

        final_sum_1 = pre_value >> 16
        final_sum_2 = pre_value & 0b1111_1111_1111_1111
        return hex(pow(2, 16) - final_sum_1 - final_sum_2)

    def pack(self):
        result = struct.pack('!HHHH',
                             self.header.sport,
                             self.header.dport,
                             self.header.length,
                             int(self.header.checksum, 16))
        result += self.header.data
        return result
