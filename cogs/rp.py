import discord
from discord.ext import commands


class RpCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test OK ! - " + ctx.author.name + " <:des:460038817592901642>")

def setup(bot):
    bot.add_cog(RpCog(bot))