"Module for network related functions."

import os


def ping(ip_address: str):
    """
    Pings an IP address and returns the response.
    """
    response = os.system("ping -c 1 " + ip_address)
    if response == 0:
        return True
    else:
        return False
