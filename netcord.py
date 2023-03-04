#!/usr/bin/env python3

import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from src.config import DiscordConfig
from src.command_processor import CommandProcessor

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CONFIG_FILE = os.getenv('CONFIG_FILE')

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN is not set")
if CONFIG_FILE is None:
    raise ValueError("CONFIG_FILE is not set")

config = DiscordConfig(CONFIG_FILE)
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')
processor = CommandProcessor(config)


async def setup(bot: commands.Bot):
    await bot.add_cog(processor)


if __name__ == '__main__':
    asyncio.run(setup(bot))
    bot.run(TOKEN)
