import unittest
from unittest import mock

from modules.SocketManager import SocketManager
from modules.traceroute.Traceroute import Traceroute
from modules.traceroute.TracerouteInfo import TracerouteInfo
from tests.PseudoNetwork import PseudoNetwork


class TestTracerouteLogic(unittest.TestCase):
    def setUp(self):
        self.dst = "222.43.54.32"
        self.icmp_echo = False
        self.max_hops = 64
        self.method = "udp"
        self.pack_num = 1
        self.port = 33443
        self.timeout = 3
        self.ttl = 1
        self.traceroute_info = TracerouteInfo(self.dst,
                                              self.max_hops,
                                              self.icmp_echo,
                                              self.method,
                                              self.port,
                                              self.timeout,
                                              self.pack_num,
                                              self.ttl)
        self.pseudo_network = PseudoNetwork()

    def test_several_hops(self):
        with mock.patch('modules.SocketManager.SocketManager.receive_icmp_message',
                        side_effect=self.pseudo_network.response.values()):
            traceroute = Traceroute(self.traceroute_info)
            traceroute.start()

