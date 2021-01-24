class TerminalPrinter:
    def __init__(self):
        self.address = True

    def print_title(self, domain, ip, hops):
        print(f'traceroute to {domain} ({ip}), {hops} hops max')

    def print_ttl(self, ttl):
        print(f'{ttl: >3}', end=' ')
        self.address = True

    def print_ip_addr(self, ip_addr):
        if self.address:
            self.address = False
            print(f'{str(ip_addr): >5}', end=' ')

    def print_time(self, time):
        print(f'{format(time * 1000, ".3f"): >6}ms', end='  ')

    def print_noting(self):
        nothing = '*'
        print(f'{nothing: >3}', end=' ')

    def print_enter(self):
        print()
