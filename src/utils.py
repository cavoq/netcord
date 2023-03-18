"""Utility functions for the project."""

import socket
from discord import File
from io import BytesIO
import re
import folium


def is_valid_ipv4(ip) -> bool:
    """Check if the given IP is a valid IPv4 address."""
    try:
        socket.inet_pton(socket.AF_INET, ip)
    except socket.error:
        return False
    return True


def is_valid_ipv6(ip) -> bool:
    """Check if the given IP is a valid IPv6 address."""
    try:
        socket.inet_pton(socket.AF_INET6, ip)
    except socket.error:
        return False
    return True


def is_valid_domain(domain) -> bool:
    """Check if the given domain is valid."""
    pattern = r'^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return bool(re.match(pattern, domain))


def resolve_address(address):
    """Resolve the given address and return the IP address."""
    try:
        results = socket.getaddrinfo(address, None)
        for result in results:
            family, socktype, proto, canonname, sockaddr = result
            ip_address = sockaddr[0]
            if family == socket.AF_INET or family == socket.AF_INET6:
                return ip_address
    except socket.gaierror as e:
        print("Error resolving address:", e)
    return None


def map_location(lat, lng, zoom) -> File:
    """Create a map of the given location and return it as a File object."""
    map = folium.Map(location=[lat, lng], zoom_start=zoom)
    marker = folium.Marker(location=[lat, lng])
    marker.add_to(map)
    map_bytes = map._to_png(delay=1)
    map_io = BytesIO(map_bytes)
    return File(map_io, filename='map.png')
