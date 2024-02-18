"""Command processor for the bot."""

from src.net import *
from src.discord_formatter import DiscordFormatter
from src.map import map_location
from discord.ext import commands


class NetcordProcessor(commands.Cog):
    """Class to process commands for the bot."""

    def __init__(self, config):
        self.config = config
        self.formatter = DiscordFormatter(config)

    @commands.command(name="ping")
    async def ping(self, ctx, ip_address: str = commands.parameter(description="IP address to ping")):
        """Ping the given IP address."""
        try:
            ping_output = ping(ip_address)
        except ValueError as e:
            await ctx.send(self.formatter.format_text(e))
            return
        await ctx.send(self.formatter.format_text(ping_output))
        return

    @commands.command(name="locate")
    async def locate(self, ctx, ip_address: str = commands.parameter(description="IP address to locate")):
        """Return the latitude and longitude of the given IP address."""
        location = locate(ip_address)
        if location is None:
            await ctx.send(self.formatter.format_text("Location not found"))
            return
        lat, lng = location[0], location[1]
        map_config = self.config.get_map_config()
        map_file = map_location(lat, lng, map_config)
        await ctx.send(file=map_file)

    @commands.command(name="traceroute")
    async def traceroute(self, ctx, ip_address: str = commands.parameter(description="IP address to trace route")):
        """Return the traceroute of the given IP address."""
        try:
            trace_output = traceroute(ip_address)
        except ValueError as e:
            await ctx.send(self.formatter.format_text(e))
            return
        except Exception:
            await ctx.send(self.formatter.format_text("Could not trace route"))
            return
        await ctx.send(self.formatter.format_text(trace_output))

    @commands.command(name="dig")
    async def dig(self, ctx, ip_address: str = commands.parameter(description="IP address to resolve DNS records")):
        """Return the DNS records of the given IP address."""
        try:
            dig_output = dig(ip_address)
        except ValueError as e:
            await ctx.send(self.formatter.format_text(e))
            return
        await ctx.send(self.formatter.format_text(dig_output))

    @commands.command(name="nslookup")
    async def nslookup(self, ctx, ip_address: str = commands.parameter(description="IP address to resolve DNS records")):
        """Return the DNS records of the given IP address."""
        try:
            nslookup_output = nslookup(ip_address)
        except ValueError as e:
            await ctx.send(self.formatter.format_text(e))
            return
        await ctx.send(self.formatter.format_text(nslookup_output))

    @commands.command(name="sslcert")
    async def sslcert(self, ctx, host: str = commands.parameter(description="Host to get SSL certificate from")):
        """Return the SSL certificate of the given host."""
        try:
            sslcert_output = sslcert(host)
        except ValueError as e:
            await ctx.send(self.formatter.format_text(e))
        except ConnectionError as e:
            await ctx.send(self.formatter.format_text(e))
            return
        await ctx.send(self.formatter.format_ssl_certificate(sslcert_output))

    @commands.command(name="commands")
    async def help(self, ctx):
        """Return the list of available commands."""
        await ctx.send(self.formatter.format_text("Available commands:\n- ping [IP address]\n- commands"))
