import time
from datetime import timedelta
from random import getrandbits

import discord
import psutil
from discord.ext import commands

process = psutil.Process()
init_cpu_time = process.cpu_percent()


class Stats(commands.Cog, name="Stats"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stats(self, ctx):
        async with ctx.channel.typing():
            """
            Returns bot statistics and technical data.
            """
            app_info = await self.client.application_info()
            total_ram = (psutil.virtual_memory().total >> 30) + 1
            embed = discord.Embed(
                title="Bot Stats",
                colour=ctx.author.colour,
                description=f"Running on a server with {total_ram}GB RAM.",
            )

            embed.add_field(name="**__General Info__**", inline=False, value="\u200b")
            embed.add_field(name="Latency", value=f"{self.client.latency*1000:.03f}ms")
            embed.add_field(name="Guild Count", value=f"{len(self.client.guilds):,}")
            embed.add_field(name="User Count", value=f"{len(self.client.users):,}")

            embed.add_field(name="**__Technical Info__**", inline=False, value="\u200b")
            embed.add_field(
                name="System CPU Usage", value=f"{psutil.cpu_percent():.02f}%"
            )
            embed.add_field(
                name="System RAM Usage",
                value=f"{psutil.virtual_memory().used/1048576:.02f} MB",
            )
            embed.add_field(
                name="System Uptime",
                value=f"{timedelta(seconds=int(time.time() - psutil.boot_time()))}",
            )
            embed.add_field(
                name="Bot CPU Usage", value=f"{process.cpu_percent():.02f}%"
            )
            embed.add_field(
                name="Bot RAM Usage",
                value=f"{process.memory_info().rss / 1048576:.02f} MB",
            )
            embed.add_field(
                name="Bot Uptime",
                value=f"{timedelta(seconds=int(time.time() - process.create_time()))}",
            )

            embed.add_field(name="**__Links__**", inline=False, value="\u200b")
            embed.add_field(
                name="Support Server",
                value="[Community Server](https://discord.gg/dKVfhV2jfn)",
            )
            embed.add_field(
                name="Invite",
                value="[Add Steve✨ to your server](https://discord.com/api/oauth2/authorize?client_id=784725037172129803&permissions=379968&scope=bot)",
            )
            embed.add_field(
                name="Top.gg page",
                value="[Steve✨](https://top.gg/bot/784725037172129803)",
            )

            embed.set_footer(
                text=f"Made by {app_info.owner}",
                icon_url=app_info.owner.avatar_url_as(size=128),
            )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Stats(client))
