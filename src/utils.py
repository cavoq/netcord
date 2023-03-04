"""Utility functions for the project."""

import socket
from discord import File
from io import BytesIO

import folium


def is_valid_ipv4(ip) -> bool:
    try:
        socket.inet_pton(socket.AF_INET, ip)
    except socket.error:
        return False
    return True


def is_valid_ipv6(ip) -> bool:
    try:
        socket.inet_pton(socket.AF_INET6, ip)
    except socket.error:
        return False
    return True

def map_location(lat, lng, zoom) -> File:
    map = folium.Map(location=[lat, lng], zoom_start=13)
    marker = folium.Marker(location=[lat, lng])
    marker.add_to(map)
    map_bytes = map._to_png(delay=1)
    map_io = BytesIO(map_bytes)
    return File(map_io, filename='map.png')
    