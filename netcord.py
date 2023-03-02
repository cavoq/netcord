import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    command = message.content.split()[0][1:]
    if command == 'ping':
        ip_address = message.content.split()[1]
        response = os.system("ping -c 1 " + ip_address)
        if response == 0:
            await message.channel.send('True')
        else:
            await message.channel.send('False')

bot.run(TOKEN)
