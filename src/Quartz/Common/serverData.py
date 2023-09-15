import dns.resolver

def getIPV6(domain: str) -> str:
    return dns.resolver.resolve(domain, 'AAAA')[0].to_text()

DOMAIN = ''
HOST = "localhost"
PORT = 9998


if __name__ == '__main__':
    print(HOST)
