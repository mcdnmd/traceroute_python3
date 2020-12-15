import socket
import unittest
import ipaddress

from modules.ProtocolManager import ProtocolManager


class TestIcmpIpCreation(unittest.TestCase):

    def setUp(self):
        protocol_manager = ProtocolManager()
        self.src = ('0.0.0.0', 1337)
        self.dst = ('46.17.203.102', 32143)
        self.ttl = 1
        self.ip_header,  self.icmp_header, self.packet = \
            protocol_manager.create_icmp_ip_pack(self.src,
                                                 self.dst,
                                                 self.ttl)

    def test_ip_header_dst_addr(self):
        self.assertEqual(ipaddress.IPv4Address(self.dst[0]),
                         self.ip_header.destination_address)

    def test_ip_header_protocol(self):
        self.assertEqual(1, self.ip_header.protocol)

    def test_ip_header_ttl(self):
        self.assertEqual(self.ttl, self.ip_header.ttl)

    def test_icmp_type(self):
        self.assertEqual(8, self.icmp_header.type)

    def test_icmp_code(self):
        self.assertEqual(0, self.icmp_header.code)
