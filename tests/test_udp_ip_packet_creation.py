import socket
import unittest
import ipaddress

from modules.ProtocolManager import ProtocolManager


class TestUdpIpCreation(unittest.TestCase):

    def setUp(self):
        protocol_manager = ProtocolManager()
        self.src = ('0.0.0.0', 1337)
        self.dst = ('46.17.203.102', 32143)
        self.ttl = 2
        self.message = b'Test Message 1341'
        self.ip_header, self.udp_header, self.packet = \
            protocol_manager.create_udp_ip_pack(
            self.src, self.dst, self.ttl, self.message)

    def test_ip_header_dst_addr(self):
        self.assertEqual(ipaddress.IPv4Address(self.dst[0]),
                         self.ip_header.destination_address)

    def test_ip_header_protocol(self):
        self.assertEqual(17, self.ip_header.protocol)

    def test_ip_header_ttl(self):
        self.assertEqual(self.ttl, self.ip_header.ttl)

    def test_udp_src_port(self):
        self.assertEqual(self.src[1], self.udp_header.sport)

    def test_udp_dst_port(self):
        self.assertEqual(self.dst[1], self.udp_header.dport)

    def test_udp_data(self):
        self.assertEqual(self.message, self.udp_header.data)
