from modules.TerminalParser import parse_terminal_input


def main():
    args = parse_terminal_input()
    launch(args)


def launch(args):
    dest = args.destination
    hops = args.max_hops
    icmp_echo = args.icmp_echo
    method = args.method
    port = args.port
    timeout = args.timeout
    pack_num = args.packet_number
    ttl = args.ttl

    tracer = Traceroute(dest, hops, icmp_echo, method, port, timeout, pack_num,
                        ttl)
    tracer.find_route()


if __name__ == '__main__':
    main()
