from modules.TerminalParser import parse_terminal_input
from modules.traceroute.Traceroute import Traceroute
from modules.traceroute.TracerouteInfo import TracerouteInfo


def main():
    args = parse_terminal_input()
    launch(args)


def launch(args):
    dest = args.destination
    hops = args.max_hops
    method = args.method
    port = args.port
    timeout = args.timeout
    pack_num = args.packet_number
    ttl = args.first_hop

    traceroute_info = TracerouteInfo(dest, hops, method, port,
                                     timeout, pack_num, ttl)

    router = Traceroute(traceroute_info)
    router.start()


if __name__ == '__main__':
    main()
