"""Create a map of the given location with a circle marker and return it as an Image object."""

from discord import File
import folium
from io import BytesIO


def create_map(lat: float, lng: float, zoom: int) -> folium.Map:
    """Create a map of the given location with a circle marker."""
    map = folium.Map(location=[lat, lng], zoom_start=zoom)
    add_circle_marker(map, lat, lng)
    add_marker(map, lat, lng)
    return map


def add_circle_marker(map: folium.Map, lat: float, lng: float, radius: int, color: str) -> None:
    """Add a circle marker to the given map at the specified location."""
    folium.CircleMarker(
        location=[lat, lng],
        radius=radius/1000,
        fill=True,
        fill_opacity=0.2,
        color=color,
        fill_color=color
    ).add_to(map)


def add_marker(map: folium.Map, lat: float, lng: float) -> None:
    """Add a marker to the given map at the specified location."""
    marker = folium.Marker(location=[lat, lng])
    marker.add_to(map)


def map_location(lat: float, lng: float, zoom: int) -> File:
    """Create a map of the given location and return it as a File object."""
    map = create_map(lat, lng, zoom)
    map_bytes = map._to_png(delay=1)
    map_io = BytesIO(map_bytes)
    return File(map_io, filename='map.png')
