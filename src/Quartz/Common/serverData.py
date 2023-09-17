import dns.resolver
from Quartz import DOMAIN, IP, IPTYPE

def getIPV6(domain: str, ip: str, iptype: str) -> str:
    if ip != '':
        return ip
    
    if domain != '':
        if iptype == 'IPV6':
            return dns.resolver.resolve(domain, 'AAAA')[0].to_text()
        
        else:
            return dns.resolver.resolve(domain, 'A')[0].to_text()

    
    else:
        return "localhost"

HOST = getIPV6(DOMAIN, IP, IPTYPE)
PORT = 9998


if __name__ == '__main__':
    print(HOST)
