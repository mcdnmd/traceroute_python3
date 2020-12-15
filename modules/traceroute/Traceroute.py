import time
import socket

from ipv4packet.ICMP import ICMP
from ipv4packet.IP import IP
from modules.SocketManager import SocketManager
from modules.ProtocolManager import ProtocolManager
from modules.TerminalPrinter import TerminalPrinter


class Traceroute:
    def __init__(self, traceroute_info):
        self.traceroute_info = traceroute_info
        self.src_addr = ('0.0.0.0', 33095)
        self.dst_addr = (self.traceroute_info.dest, self.traceroute_info.port)
        self.sock = SocketManager(traceroute_info.timeout,
                                  traceroute_info.icmp_echo, self.src_addr)
        self.printer = TerminalPrinter()

    def start(self):
        hop_counter = 0
        self.printer.print_title(self.dst_addr[0], self.dst_addr[0],
                                 self.traceroute_info.max_hops)
        while hop_counter < self.traceroute_info.max_hops:
            self.printer.print_ttl(self.traceroute_info.ttl)
            addr = self.make_request_to_target()
            self.traceroute_info.ttl += 1
            if str(addr) == self.traceroute_info.dest:
                self.printer.print_enter()
                break
            hop_counter += 1

    def make_request_to_target(self):
        addr = None
        for i in range(self.traceroute_info.packs_per_hop):
            if self.traceroute_info.icmp_echo:
                ip_header, icmp_header, packet = self.create_icmp_request()
            else:
                ip_header, udp_header, packet = self.create_udp_request()
            start_time = time.time()
            self.sock.send_request(packet, self.dst_addr)
            try:
                data = self.sock.receive_icmp_message()
                stop_time = time.time() - start_time
            except socket.timeout:
                self.printer.print_noting()
                continue
            addr = self.parse_reply_data(data[0], ip_header)
            self.printer.print_ip_addr(addr)
            self.printer.print_time(stop_time)

        return addr

    def create_udp_request(self):
        return ProtocolManager.create_udp_ip_pack(self.src_addr, self.dst_addr,
                                                  self.traceroute_info.ttl,
                                                  b'Hi from mcdnmd!')

    def create_icmp_request(self):
        return ProtocolManager.create_icmp_ip_pack(self.src_addr,
                                                   self.dst_addr,
                                                   self.traceroute_info.ttl)

    @staticmethod
    def parse_reply_data(raw_data, sent_ip_header):
        ip = IP(raw_data)
        icmp = ICMP(ip.header, raw_data)

        if icmp.header.type == 0 and icmp.header.code == 0:
            return ip.header.source_address

        if sent_ip_header.id == icmp.header.data[0].id:
            return ip.header.source_address
