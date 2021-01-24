from ipv4packet.ICMP import ICMP
from ipv4packet.IP import IP
from ipv4packet.UDP import UDP


class ProtocolManager:
    @staticmethod
    def create_udp_ip_pack(src, dst, ttl, message=b'SUPERMAN!'):
        ip = IP()
        ip.create_ip_header(src[0], dst[0], ttl, 17)
        udp = UDP(ip.header)
        udp.create_udp_header(src[1], dst[1], message)
        ip.header.total_length = udp.header.length + 20

        packet = ip.pack() + udp.pack()

        return ip.header, udp.header, packet

    @staticmethod
    def create_icmp_ip_pack(src, dst, ttl):
        ip = IP()
        ip.create_ip_header(src[0], dst[0], ttl, 1)

        icmp = ICMP(ip.header)
        icmp.create_icmp_header()
        ip.header.total_length = 23

        packet = ip.pack() + icmp.pack()

        return ip.header, icmp.header, packet
