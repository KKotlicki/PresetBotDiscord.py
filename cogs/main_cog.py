import discord
from discord.ext import commands
import urllib.request
import urllib.error
from loguru import logger


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game('$help'))
        logger.success(f"Logged in as {self.bot.user}")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def cat(self, ctx, *, question='404'):
        try:
            urllib.request.urlretrieve(
                f'https://http.cat/{question}',
                f"cat.png")
        except urllib.error.HTTPError:
            urllib.request.urlretrieve(
                f'https://http.cat/404',
                f"/cat.png")
        await ctx.send(file=discord.File(f"cat.png"))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() in\
                ["geodezja",
                 "geodezji",
                 "geodeci",
                 "gik",
                 "a co to kurwa jest",
                 "a co to kurwa jest?"
                 "a co to kurwa jest?!",
                 "a co to kurwa jest!?"]\
                and not message.author.bot:
            ctx = await self.bot.get_context(message)
            await ctx.send("A co to k*rwa jest?!")


def setup(bot):
    bot.add_cog(MainCog(bot))
