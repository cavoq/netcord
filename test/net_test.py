"""Test the netcord module."""

import pytest
from src.net import ping, locate


class TestNetcord:
    """Test the netcord module."""

    def test_ping(self):
        """Test the ping function."""
        assert ping('127.0.0.1') == True
        assert ping('google.com') == True
        assert ping('::1') == True
        assert ping('example.invalid') == False
        with pytest.raises(ValueError):
            ping('256.256.256.256')

    def test_locate(self):
        """Test the locate function."""
        assert locate('127.0.0.1') == None
        assert locate('8.8.8.8') != None
        assert locate('::1') == None
        assert locate('example.invalid') == None
        assert locate('256.256.256.256') == None