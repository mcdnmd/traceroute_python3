class ICMPHeader:
    def __init__(self):
        self.type = None
        self.code = None
        self.checksum = None
        self.unused = None
        self.id = None
        self.seq = None
        self.data = None

    def __str__(self):
        return f'---ICMP---\n' \
               f'  Type: {self.type}\n' \
               f'  Code: {self.code}\n' \
               f'  Checksum: {self.checksum}\n' \
               f'  Data:\n' \
               f'  {str(self.data[0])}\n' \
               f'  {str(self.data[1])}'
