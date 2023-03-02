from src.config import DiscordConfig


class DiscordFormatter:
    def __init__(self, config: DiscordConfig):
        self.config = config

    def format_text(self, text):
        formatted_text = f"<span style='"
        if self.config.font:
            formatted_text += f"font-family: {self.config.font}; "
        if self.config.size:
            formatted_text += f"font-size: {self.config.size}; "
        if self.config.color:
            formatted_text += f"color: {self.config.color}; "
        formatted_text += f"'>{text}</span>"
        return formatted_text
