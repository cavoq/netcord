import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from src.config import DiscordConfig
from src.formatter import DiscordFormatter

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
        response = os.system("ping -c 1 " + ip_address)
        if response == 0:
            print(formatter.format_text("Online"))
            await message.channel.send(formatter.format_text("Online"))
        else:
            await message.channel.send(formatter.format_text("Offline"))

bot.run(TOKEN)
