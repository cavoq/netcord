import os
from src.utils import *


def ping(ip_address: str):
    if is_valid_ipv4(ip_address):
        ping_command = "ping -c 1 "
    elif is_valid_ipv6(ip_address):
        ping_command = "ping6 -c 1 "
    else:
        raise ValueError("Invalid IP address")
    response = os.system(ping_command + ip_address)
    if response != 0:
        return False
    return True
