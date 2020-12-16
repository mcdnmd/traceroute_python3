import socket


class SocketManager:
    def __init__(self, timeout, icmp_echo, src_addr):
        self.timeout = timeout
        self.icmp_echo = icmp_echo
        self.sender = None
        self.receiver = None
        self.src_addr = src_addr
        self.init_sender_socket()
        self.init_receiver_socket()

    def init_sender_socket(self):
        if self.icmp_echo:
            self.sender = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                        socket.IPPROTO_ICMP)
        else:
            self.sender = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                        socket.IPPROTO_UDP)
        self.sender.bind(self.src_addr)
        self.sender.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        self.sender.setblocking(False)

    def init_receiver_socket(self):
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                      socket.IPPROTO_ICMP)
        self.receiver.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        self.receiver.settimeout(self.timeout)

    def send_request(self, byte_message, dst):
        self.sender.sendto(byte_message, dst)

    def receive_icmp_message(self):
        try:
            return self.receiver.recvfrom(1024)
        except socket.timeout:
            raise
