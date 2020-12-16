import unittest

from ipv4packet.ICMP import ICMP
from ipv4packet.IP import IP


class TestIcmpParser(unittest.TestCase):

    def setUp(self):
        raw_data = b'E\xc0\x00D\x1c\xb5\x00\x00@\x01\xdb\x8b\xc0\xa8\x00\x01' \
                   b'\xc0\xa8\x00g\x0b\x00\xaf\xac\x00\x00\x00\x00E\x00\x00(' \
                   b'@\xcd@\x00\x01\x11~q\xc0\xa8\x00g.\x11\xcbf\x81G}\x8f' \
                   b'\x00\x14\xfd\xe6test message'

        self.ip = IP(raw_data)
        self.icmp = ICMP(self.ip.header, raw_data)

    def test_icmp_type(self):
        self.assertEqual(11, self.icmp.header.type)

    def test_icmp_code(self):
        self.assertEqual(0, self.icmp.header.code)

    def test_icmp_checksum(self):
        self.assertEqual(int('0xafac', 16), self.icmp.header.checksum)

    def test_icmp_data(self):
        self.assertFalse(self.icmp.header.data is None)

    def test_icmp_data_udp_message(self):
        self.assertEqual(b'test message', self.icmp.header.data[1].data)
