"""Test the netcord module."""

import pytest
from src.net import *


class TestNetcord:
    """Test the netcord module."""

    def test_ping(self):
        """Test the ping function."""
        assert isinstance(ping('127.0.0.1'), str)
        assert isinstance(ping('::1'), str)
        with pytest.raises(ValueError):
            ping('example.invalid')
            ping('256.256.256.256')

    def test_locate(self):
        """Test the locate function."""
        assert locate('127.0.0.1') == None
        assert locate('8.8.8.8') != None
        assert locate('::1') == None
        assert locate('example.invalid') == None
        assert locate('256.256.256.256') == None

    def test_trace(self):
        """Test the trace function."""
        result = trace("8.8.8.8")
        assert isinstance(result, str)

        result = trace("2001:4860:4860::8888")
        assert isinstance(result, str)

        with pytest.raises(ValueError):
            trace("invalid")
