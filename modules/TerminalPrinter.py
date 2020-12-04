class TerminalPrinter:
    def __init__(self):
        self.address = True

    def print_title(self, domain, ip, hops):
        print(f'traceroute to {domain} ({ip}), {hops} hops max', end='')

    def print_ttl(self, ttl):
        print(f'\n {ttl}', end='  ')
        self.address = True

    def print_ip_addr(self, ip_addr):
        if self.address:
            self.address = False
            print(ip_addr, end='  ')

    def print_time(self, time):
        print(f'{format(time * 1000, ".3f")}ms', end='  ')

    def print_noting(self):
        print('*', end=' ')

    def print_enter(self):
        print()
