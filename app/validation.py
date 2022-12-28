import ipaddress

def ip_validation(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False

def net_validation(net):
    try:
        ipaddress.ip_network(net)
        return True
    except:
        return False
