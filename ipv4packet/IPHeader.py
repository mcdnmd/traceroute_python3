class IPHeader:
    def __init__(self):
        self.version = None
        self.ihl = None
        self.dscp = None
        self.ecn = None
        self.total_length = None
        self.id = None
        self.zero_flag = 0
        self.dont_fragment_flag = None
        self.more_fragments_flag = None
        self.offset = None
        self.ttl = None
        self.protocol = None
        self.header_checksum = None
        self.source_address = None
        self.destination_address = None