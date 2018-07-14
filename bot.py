import json
import sys, traceback
import discord
from discord.ext import commands

with open('./config.json', 'r') as fichier:
    config = json.load(fichier)

token = config['token']

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.rp',
                      'cogs.rpprofile',
                      'cogs.botowner']

bot = commands.Bot(command_prefix='rp.')

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    game = discord.Game(name="RPHelper WIP")
    await bot.change_presence(activity=game, status=discord.Status.do_not_disturb)
    print(f'Successfully logged in and booted...!')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


bot.run(token, bot=True, reconnect=True)
