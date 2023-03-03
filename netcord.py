import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from src.config import DiscordConfig
from src.discord_formatter import DiscordFormatter
from src.net import ping

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')
config = DiscordConfig('config/format.json')
formatter = DiscordFormatter(config)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    command = message.content.split()[0][1:]
    if command == 'ping':
        ip_address = message.content.split()[1]
        reachable = ping(ip_address)
        if reachable:
            await message.channel.send(formatter.format_text(f"[{ip_address}] - Online"))
        else:
            await message.channel.send(formatter.format_text(f"[{ip_address}] - Offline"))

bot.run(TOKEN)
