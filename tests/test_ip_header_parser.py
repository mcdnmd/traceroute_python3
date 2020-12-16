import unittest

import ipaddress
from ipv4packet.IP import IP


class TestIpParser(unittest.TestCase):

    def setUp(self):
        raw_data = b'E\xc0\x00D\x1c\xb5\x00\x00@\x01\xdb\x8b\xc0\xa8\x00\x01' \
                   b'\xc0\xa8\x00g\x0b\x00\xaf\xac\x00\x00\x00\x00E\x00\x00(' \
                   b'@\xcd@\x00\x01\x11~q\xc0\xa8\x00g.\x11\xcbf\x81G}\x8f' \
                   b'\x00\x14\xfd\xe6test message '

        self.ip = IP(raw_data)

    def test_ip_version(self):
        self.assertEqual(4, self.ip.header.version)

    def test_ip_header_length(self):
        self.assertEqual(5, self.ip.header.ihl)

    def test_total_length(self):
        self.assertEqual(68, self.ip.header.total_length)

    def test_id(self):
        self.assertEqual(7349, self.ip.header.id)

    def test_df_flag(self):
        self.assertEqual(0, self.ip.header.dont_fragment_flag)

    def test_mf_flag(self):
        self.assertEqual(0, self.ip.header.more_fragments_flag)

    def test_offset(self):
        self.assertEqual(0, self.ip.header.offset)

    def test_ttl(self):
        self.assertEqual(64, self.ip.header.ttl)

    def test_protocol(self):
        self.assertEqual(1, self.ip.header.protocol)

    def test_header_checksum(self):
        self.assertEqual(int('0xdb8b', 16), self.ip.header.header_checksum)

    def test_source_ip(self):
        self.assertEqual(ipaddress.IPv4Address('192.168.0.1'),
                         self.ip.header.source_address)

    def test_dest_ip(self):
        self.assertEqual(ipaddress.IPv4Address('192.168.0.103'),
                         self.ip.header.destination_address)
