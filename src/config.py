"""Discord bot configuration."""

import json


class DiscordConfig:
    """Class to hold Discord bot configuration."""

    def __init__(self, filename):
        with open(filename) as config_file:
            self.config = json.load(config_file)

    def get_map_config(self):
        """Return the map configuration."""
        return self.config['map_location']