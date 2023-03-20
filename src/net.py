"""Network related functions."""

import subprocess
import geocoder
from src.utils import *


def ping(ip_address: str) -> str:
    """Ping the given IP address and return the output of the ping command."""
    if is_valid_ipv4(ip_address) or is_valid_domain(ip_address):
        ping_command = "ping -c 3 "
    elif is_valid_ipv6(ip_address):
        ping_command = "ping6 -c 3 "
    else:
        raise ValueError("Invalid domain or IP address")
    result = subprocess.run(ping_command + ip_address,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return result.stdout.decode()


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


def traceroute(ip_address: str) -> str:
    """Return the traceroute of the given IP address."""
    if is_valid_ipv4(ip_address) or is_valid_domain(ip_address):
        trace_command = "traceroute"
    elif is_valid_ipv6(ip_address):
        trace_command = "traceroute6"
    else:
        raise ValueError("Invalid domain or IP address")

    try:
        output = subprocess.check_output(
            [trace_command, ip_address], universal_newlines=True, timeout=10)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return "Could not trace route"

    return output


def dig(ip_address: str) -> str:
    """Return the DNS records of the given IP address."""
    if not (is_valid_ipv4(ip_address) or is_valid_domain(ip_address) or is_valid_ipv6(ip_address)):
        raise ValueError("Invalid domain or IP address")
    try:
        output = subprocess.check_output(
            ["dig", ip_address], universal_newlines=True, timeout=10)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return "Could not resolve DNS records"

    return output


def nslookup(ip_address: str) -> str:
    """Return the DNS records of the given IP address."""
    if not (is_valid_ipv4(ip_address) or is_valid_domain(ip_address) or is_valid_ipv6(ip_address)):
        raise ValueError("Invalid domain or IP address")
    try:
        output = subprocess.check_output(
            ["nslookup", ip_address], universal_newlines=True, timeout=10)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return "Could not resolve DNS records"
    
    return output