import time

from modules.SocketManager import SocketManager
from modules.ProtocolManager import ProtocolManager


class Traceroute:
    def __init__(self, traceroute_info):
        self.traceroute_info = traceroute_info
        self.target = None
        self.current_address = None
        self.socket = SocketManager(traceroute_info.timeout,
                                    traceroute_info.icmp_echo)

    def start(self):
        while True:
            addr = self.make_request_to_target()

    def make_request_to_target(self):
        for i in range(self.traceroute_info.pack_per_hope):
            start_time = time.time()
            packet = ProtocolManager.create_udp_ip_pack()
            self.socket.send_request(packet,
                                     self.traceroute_info.destination,
                                     self.traceroute_info.port)
