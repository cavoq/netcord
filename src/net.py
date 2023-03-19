"""Network related functions."""

import os
import subprocess
import geocoder
from src.utils import *


def ping(ip_address: str) -> bool:
    """Ping the given IP address and return True if it is reachable."""
    if is_valid_ipv4(ip_address) or is_valid_domain(ip_address):
        ping_command = "ping -c 1 "
    elif is_valid_ipv6(ip_address):
        ping_command = "ping6 -c 1 "
    else:
        raise ValueError("Invalid IP address")
    response = os.system(ping_command + ip_address + ' > /dev/null 2>&1')
    if response != 0:
        return False
    return True


def locate(ip_address: str) -> tuple or None:
    """Return the latitude and longitude of the given IP address."""
    if is_valid_domain(ip_address):
        try:
            ip_address = resolve_address(ip_address)
        except ValueError:
            return None
    if not (is_valid_ipv4(ip_address) or is_valid_ipv6(ip_address)):
        return None
    geo_location = geocoder.ip(ip_address)
    if geo_location.ok and geo_location.latlng != []:
        return geo_location.latlng
    return None


def trace(ip_address: str) -> str:
    """Return the traceroute of the given IP address."""
    if is_valid_ipv4(ip_address) or is_valid_domain(ip_address):
        trace_command = "traceroute"
    elif is_valid_ipv6(ip_address):
        trace_command = "traceroute6"
    else:
        raise ValueError("Invalid IP address")

    try:
        output = subprocess.check_output(
            [trace_command, ip_address], universal_newlines=True, timeout=10)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return "Could not trace route"

    return output
