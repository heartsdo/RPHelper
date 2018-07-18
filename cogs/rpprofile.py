import discord
from discord.ext import commands

class RpProfileCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, member:discord.Member=None):
        if not member:
            member = ctx.author
        embed = discord.Embed(name="Profile", color=0xffa233)
        embed.set_author(name="Profile de " + member.display_name, icon_url=member.avatar_url)
        embed.add_field(name="Nom: ", value=member.display_name)
        if 459855212769706015 in [y.id for y in member.roles]:
            embed.add_field(name="Clan: ", value="Phoenix de Feu")
        else:
            embed.add_field(name="Clan: ", value="Aucun")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(RpProfileCog(bot))
