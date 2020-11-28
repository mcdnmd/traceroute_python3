import socket


class SocketManager:
    def __init__(self, timeout, icmp_echo):
        self.timeout = timeout
        self.icmp_echo = icmp_echo
        self.sender = None
        self.receiver = None
        self.init_sender_socket()

    def init_sender_socket(self):
        if self.icmp_echo:
            self.sender = socket.socket(socket.AF_INET, socket.SOCK_RAW)
        else:
            self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sender.setblocking(False)

    def init_receiver_socket(self):
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                      socket.IPPROTO_ICMP)
        self.receiver.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    def send_request(self, byte_message, ipv4, port):
        self.sender.sendto(byte_message, (ipv4, port))



