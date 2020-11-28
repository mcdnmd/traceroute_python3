import socket
import unittest

from modules.ProtocolManager import ProtocolManager


class TestUdpIpCreation(unittest.TestCase):

    def setUp(self):
        protocol_manager = ProtocolManager()
        src = ('192.168.0.103', 33095)
        dst = ('46.17.203.102', 32143)
        ttl = 19
        self.packet = protocol_manager.create_udp_ip_pack(src, dst, 19)
