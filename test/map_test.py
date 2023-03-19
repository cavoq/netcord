"""Test the map module."""

from discord import File
from src.map import map_location


def test_map_location():
    """Test the map_location function."""
    # Test a known location (New York City)
    lat = 40.730610
    lng = -73.935242
    zoom = 10
    map_file = map_location(lat, lng, zoom)
    assert isinstance(map_file, File)
    assert map_file.filename == 'map.png'
