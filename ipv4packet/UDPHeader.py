class UDPHeader:
    def __init__(self):
        self.sport = None
        self.dport = None
        self.length = None
        self.checksum = None
        self.data = None