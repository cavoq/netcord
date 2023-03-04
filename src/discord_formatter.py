"""DiscordFormatter class."""

from src.config import DiscordConfig


class DiscordFormatter:
    def __init__(self, config: DiscordConfig):
        self.config = config

    def format_text(self, text):
        return f"**```arm\n{text}```**"
