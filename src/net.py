import os


def ping(ip_address: str):
    response = os.system("ping -c 1 " + ip_address)
    if response == 0:
        return True
    else:
        return False
