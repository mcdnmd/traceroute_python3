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

    def __str__(self):
        return f'\n\t---IP---\n' \
               f'\tVersion: {self.version}\n' \
               f'\tIHL: {self.ihl}\n' \
               f'\tDSCP: {self.dscp}\n' \
               f'\tECN: {self.ecn}\n' \
               f'\tTotal Length: {self.total_length}\n' \
               f'\tId: {self.id}\n' \
               f'\tDF: {self.dont_fragment_flag}\n' \
               f'\tMF: {self.more_fragments_flag}\n' \
               f'\tOffset: {self.offset}\n' \
               f'\tTTL: {self.ttl}\n' \
               f'\tProtocol: {self.protocol}\n' \
               f'\tHeader Checksum: {self.header_checksum}\n' \
               f'\tSource ip: {self.source_address}\n' \
               f'\tDestination ip: {self.destination_address}'
