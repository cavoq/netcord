"""Command processor for the bot."""

from src.net import *
from src.discord_formatter import DiscordFormatter
from src.map import map_location
from discord.ext import commands


class CommandProcessor(commands.Cog):
    """Class to process commands for the bot."""

    def __init__(self, config):
        self.config = config
        self.formatter = DiscordFormatter(config)

    @commands.command(name="ping")
    async def ping(self, ctx, ip_address: str):
        """Ping the given IP address and return True if it is reachable."""
        try:
            ping_output = ping(ip_address)
        except ValueError:
            await ctx.send(self.formatter.format_text("Invalid IP address"))
            return
        await ctx.send(self.formatter.format_text(ping_output))
        return

    @commands.command(name="locate")
    async def locate(self, ctx, ip_address: str):
        """Return the latitude and longitude of the given IP address."""
        location = locate(ip_address)
        if location is None:
            await ctx.send(self.formatter.format_text("Location not found"))
            return
        lat, lng = location[0], location[1]
        map_config = self.config.get_map_config()
        map_file = map_location(lat, lng, map_config)
        await ctx.send(file=map_file)

    @commands.command(name="trace")
    async def trace(self, ctx, ip_address: str):
        """Return the traceroute of the given IP address."""
        try:
            trace_output = trace(ip_address)
        except ValueError:
            await ctx.send(self.formatter.format_text("Invalid IP address"))
            return
        except Exception:
            await ctx.send(self.formatter.format_text("Could not trace route"))
            return
        await ctx.send(self.formatter.format_text(trace_output))

    @commands.command(name="commands")
    async def help(self, ctx):
        """Return the list of available commands."""
        await ctx.send(self.formatter.format_text("Available commands:\n- ping [IP address]\n- commands"))
