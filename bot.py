import discord
from discord.ext import commands
import json
import sys, traceback


with open('./config.json', 'r') as fichier:
    config = json.load(fichier)

token = config['token']

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.rp']

bot = commands.Bot(command_prefix='rp.')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    game = discord.Game(name="RPHelper WIP")
    await bot.change_presence(activity=game, status=discord.Status.do_not_disturb)
    print(f'Successfully logged in and booted...!')

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(name="Help", color=0xaf33ff)
    embed.set_author(name="RpHelper Help", icon_url=bot.user.avatar_url)
    embed.add_field(name="rp.test", value="Test Command")
    await ctx.send(embed=embed)

bot.run(token, bot=True, reconnect=True)