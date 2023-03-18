"""Discord bot configuration."""

import json


class DiscordConfig:
    """Class to hold Discord bot configuration."""

    def __init__(self, filename):
        with open(filename) as config_file:
            config = json.load(config_file)
