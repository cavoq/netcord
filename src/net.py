"""Network related functions."""

import subprocess
import geocoder
import ssl
import socket
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


def sslcert(host: str):
    """Return the SSL certificate of the given domain."""
    if not (is_valid_ipv4(host) or is_valid_domain(host) or is_valid_ipv6(host)):
        raise ValueError("Invalid domain or IP address")

    if is_valid_ipv4(host):
        address_family = socket.AF_INET
    else:
        address_family = socket.AF_INET6

    with socket.socket(address_family, socket.SOCK_STREAM) as s:
        s.settimeout(10)
        try:
            s.connect((host, 443))
        except socket.timeout:
            return f"Error: Connection to {host} timed out."
        except socket.error as e:
            return f"Error: Could not connect to {host}: {e}"

        with ssl.create_default_context().wrap_socket(s, server_hostname=host) as sock:
            cert = sock.getpeercert()

    return (f"Certificate information for {host}:\n" #TODO: Add more information
            f"Issued to: {cert['subject'][0][0]}\n"
            f"Issued by: {cert['issuer'][0][0]}\n"
            f"Valid from: {cert['notBefore']}\n"
            f"Valid until: {cert['notAfter']}\n")
