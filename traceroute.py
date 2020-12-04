import socket

from modules.TerminalParser import parse_terminal_input
from modules.traceroute.Traceroute import Traceroute
from modules.traceroute.TracerouteInfo import TracerouteInfo


def main():
    args = parse_terminal_input()
    launch(args)


def launch(args):
    dest = socket.gethostbyname(args.destination)
    hops = args.max_hops
    icmp_echo = args.icmp_echo
    method = args.method
    port = args.port
    timeout = args.timeout
    pack_num = args.packet_number
    ttl = args.ttl

    traceroute_info = TracerouteInfo(dest, hops, icmp_echo, method, port,
                                     timeout, pack_num, ttl)

    router = Traceroute(traceroute_info)
    router.start()


if __name__ == '__main__':
    main()
