"""Command processor for the bot."""

from src.net import *
from src.discord_formatter import DiscordFormatter
from discord.ext import commands


class CommandProcessor(commands.Cog):
    def __init__(self, config):
        self.config = config
        self.formatter = DiscordFormatter(config)

    @commands.command(name="ping")
    async def ping(self, ctx, ip_address: str):
        try:
            reachable = ping(ip_address)
        except ValueError:
            await ctx.send(self.formatter.format_text("Invalid IP address"))
            return
        if reachable:
            await ctx.send(self.formatter.format_text(f"[{ip_address}] - Online"))
            return
        await ctx.send(self.formatter.format_text(f"[{ip_address}] - Offline"))

    @commands.command(name="locate")
    async def locate(self, ctx, ip_address: str):
        location = locate(ip_address)

    @commands.command(name="commands")
    async def help(self, ctx):
        await ctx.send(self.formatter.format_text("Available commands:\n- ping [IP address]\n- commands"))
