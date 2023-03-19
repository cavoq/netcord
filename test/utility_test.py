"""Test utility functions."""

import pytest
from src.utils import *


class TestNetUtilityFunctions:
    """Test utility functions."""

    def test_is_valid_ipv4(self):
        """Test the is_valid_ipv4 function."""
        assert is_valid_ipv4('192.168.1.1') == True
        assert is_valid_ipv4('10.0.0.1') == True
        assert is_valid_ipv4('172.16.0.1') == True
        assert is_valid_ipv4('8.8.8.8') == True
        assert is_valid_ipv4('300.300.300.300') == False
        assert is_valid_ipv4('::1') == False
        assert is_valid_ipv4('example.com') == False

    def test_is_valid_ipv6(self):
        """Test the is_valid_ipv6 function."""
        assert is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334') == True
        assert is_valid_ipv6('2001:db8:85a3:0:0:8a2e:370:7334') == True
        assert is_valid_ipv6('2001:db8:85a3::8a2e:370:7334') == True
        assert is_valid_ipv6('::1') == True
        assert is_valid_ipv6('192.168.1.1') == False
        assert is_valid_ipv6('example.com') == False

    def test_is_valid_domain(self):
        """Test the is_valid_domain function."""
        assert is_valid_domain('google.com') == True
        assert is_valid_domain('example.com') == True
        assert is_valid_domain('test1.test2.example.com') == True
        assert is_valid_domain('192.168.1.1') == False
        assert is_valid_domain('notavaliddomain') == False

    def test_resolve_address(self):
        """Test the resolve_address function."""
        assert resolve_address("8.8.8.8") == "8.8.8.8"
        assert resolve_address(
            "2001:4860:4860::8888") == "2001:4860:4860::8888"
        with pytest.raises(ValueError):
            resolve_address("invalid")
            resolve_address("non-existing-domain.com")
