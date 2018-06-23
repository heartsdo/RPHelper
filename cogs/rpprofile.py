import discord
from discord.ext import commands
import sqlite3

class RpProfileCog:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def profile(self, ctx, member:discord.Member=None):
        conn = sqlite3.connect('SQLRPHelper.db')
        cursor = conn.cursor()
        if not member:
            member = ctx.author
        print(member)
        cursor.execute("""SELECT Name FROM Profile WHERE IDP=?""", (member.id,))
        fetch = [r[0] for r in cursor.fetchall()]
        print(fetch)
        name = fetch[0]
        name = str(name)
        embed = discord.Embed(name="Profile", color=0xffa233)
        embed.set_author(name="Profile de " + name, icon_url=member.avatar_url)
        embed.add_field(name="Nom: ", value=name)
        if 459855212769706015 in [y.id for y in member.roles]:
            embed.add_field(name="Clan: ", value="Phoenix de Feu")
        else:
            embed.add_field(name="Clan: ", value="Aucun")
        await ctx.send(embed=embed)
        conn.close()

def setup(bot):
    bot.add_cog(RpProfileCog(bot))