import json


class DiscordConfig:
    def __init__(self, filename):
        with open(filename) as config_file:
            config = json.load(config_file)
