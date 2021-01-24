import socket


class TracerouteInfo:
    def __init__(self, dest, max_hops, method, port, timeout,
                 pack_num, ttl):
        self.raw_dest = dest
        self.dest = socket.gethostbyname(dest)
        self.max_hops = max_hops
        self.method = method
        self.port = port
        self.timeout = timeout
        self.packs_per_hop = pack_num
        self.ttl = ttl
