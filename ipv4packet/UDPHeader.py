class UDPHeader:
    def __init__(self):
        self.sport = None
        self.dport = None
        self.length = None
        self.checksum = None
        self.data = None

    def __str__(self):
        return f'\n\t---UDP---\n' \
               f'\tSource port: {self.sport}\n' \
               f'\tDestination port: {self.dport}\n' \
               f'\tLength: {self.length}\n' \
               f'\tChecksum: {self.checksum}\n' \
               f'\tData: {self.data}'
