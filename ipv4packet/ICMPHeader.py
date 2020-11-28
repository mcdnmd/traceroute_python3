class ICMPHeader:
    def __init__(self):
        self.type = None
        self.code = None
        self.checksum = None
        self.data = None