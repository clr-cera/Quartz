import dns.resolver
from Quartz import DOMAIN

def getIPV6(domain: str) -> str:
    if domain != '':
        return dns.resolver.resolve(domain, 'AAAA')[0].to_text()
    else:
        return "localhost"

HOST = getIPV6(DOMAIN)
PORT = 9998


if __name__ == '__main__':
    print(HOST)
