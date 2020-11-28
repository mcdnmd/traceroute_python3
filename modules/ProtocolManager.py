from ipv4packet.IP import IP
from ipv4packet.UDP import UDP
from ipv4packet.UDPHeader import UDPHeader


class ProtocolManager:
    @staticmethod
    def create_udp_ip_pack(src, dst, ttl):
        ip = IP()
        ip.create_ip_header(src[0], dst[0], ttl)

        udp = UDP(ip.header)
        udp.create_udp_header(src[1], dst[1])
        ip.header.total_length = udp.header.length + 20

        packet = ip.pack() + udp.pack()

        return {'ip': ip.header,
                'udp': udp.header,
                'packet': packet}
