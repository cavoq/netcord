"""DiscordFormatter class."""

from src.config import DiscordConfig


class DiscordFormatter:
    """Class to format text for Discord."""

    def __init__(self, config: DiscordConfig):
        self.config = config

    def format_text(self, text):
        """Format the given text for Discord."""
        return f"**```ini\n{text}```**"