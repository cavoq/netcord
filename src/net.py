"""Network related functions."""

import os
import geocoder
from src.utils import *


def ping(ip_address: str):
    if is_valid_ipv4(ip_address):
        ping_command = "ping -c 1 "
    elif is_valid_ipv6(ip_address):
        ping_command = "ping6 -c 1 "
    else:
        raise ValueError("Invalid IP address")
    response = os.system(ping_command + ip_address + ' > /dev/null 2>&1')
    if response != 0:
        return False
    return True


def locate(ip_address: str):
    if not is_valid_ipv4(ip_address) and not is_valid_ipv6(ip_address):
        return None
    try:
        geo_location = geocoder.ip(ip_address)
        return geo_location.latlng
    except Exception:
        return None


def trace(ip_address: str):
    pass