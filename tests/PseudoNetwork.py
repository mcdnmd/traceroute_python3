"""
1	192.168.0.101 -> 192.168.0.1
2	192.168.0.1 -> 212.48.194.62
3	212.48.194.62 -> 213.59.212.123
                  -> 94.25.63.10
4	*
5	213.59.212.123 -> 222.43.54.32
5	94.25.63.10 -> 222.43.54.32
"""
import socket

from scapy.layers.inet import IP, ICMP

from modules.ProtocolManager import ProtocolManager


class PseudoNetwork:
    def __init__(self):
        self.response = {}
        self.dst_addr = '192.168.1.105'
        self.dst_port = 1337
        self.init_hops()

    def init_hops(self):
        self.create_icmp_ttl_exceeded('192.168.1.1', 1)
        self.create_icmp_ttl_exceeded('212.48.194.62', 2)
        self.create_icmp_ttl_exceeded('213.59.212.123', 3)
        self.create_icmp_ttl_exceeded('94.25.63.10', 3)
        self.response[4] = socket.timeout
        self.create_icmp_ttl_exceeded('222.43.54.32', 5)

    def create_icmp_ttl_exceeded(self, src_addr, ttl):
        packet = IP(dst=self.dst_addr, src=src_addr) / ICMP(type=11, code=0)
        message = b'Hi from mcdnmd!'
        request_data = ProtocolManager().create_udp_ip_pack((self.dst_addr, self.dst_port),
                                                            (src_addr, 33443),
                                                            ttl,
                                                            message)
        try:
            self.response[ttl].append([bytes(packet)+request_data[2]])
        except Exception as e:
            self.response[ttl] = [bytes(packet)+request_data[2]]
