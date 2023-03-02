import json


class DiscordConfig:
    def __init__(self, filename):
        with open(filename) as config_file:
            config = json.load(config_file)
        self.font = config['text']['font-family']
        self.size = config['text']['font-size']
        self.color = config['text']['color']
