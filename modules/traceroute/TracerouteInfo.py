class TracerouteInfo:
    def __init__(self, dest, max_hops, icmp_echo, method, port, timeout,
                 pack_num, ttl):
        self.dest = dest
        self.max_hops = max_hops
        self.icmp_echo = icmp_echo
        self.method = method
        self.port = port
        self.timeout = timeout
        self.pack_per_hop = pack_num
        self.ttl = ttl