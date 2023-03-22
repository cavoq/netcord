"""DiscordFormatter class."""

import datetime
from src.config import DiscordConfig


class DiscordFormatter:
    """Class to format text for Discord."""

    def __init__(self, config: DiscordConfig):
        self.config = config

    def format_text(self, text):
        """Format the given text for Discord."""
        return f"**```ini\n{text}```**"

    def format_ssl_certificate(self, cert):
        """Format the given SSL certificate for Discord."""
        not_before = datetime.datetime.strptime(
            cert['notBefore'], '%b %d %H:%M:%S %Y %Z').strftime('%Y-%m-%d %H:%M:%S %Z')
        not_after = datetime.datetime.strptime(
            cert['notAfter'], '%b %d %H:%M:%S %Y %Z').strftime('%Y-%m-%d %H:%M:%S %Z')

        san_str = ', '.join(val for key, val in cert['subjectAltName'])
        if len(san_str) > 1000:
            san_str = san_str[:1000] + '...'

        cert_info = [
            f"Issuer: {', '.join(['='.join(name_val) for name_val in cert['issuer'][0]])}",
            f"Not Before: {not_before}",
            f"Not After: {not_after}",
            f"Serial Number: {cert['serialNumber']}",
            f"Subject: {', '.join(['='.join(name_val) for name_val in cert['subject'][0]])}",
            f"Subject Alternative Names: {san_str}",
            f"OCSP: {cert['OCSP'][0]}",
            f"CA Issuers: {cert['caIssuers'][0]}",
            f"Version: {cert['version']}"
        ]

        return '\n'.join(cert_info)[:2000]
