import discord
from discord.ext import commands
import json

with open('./config.json', 'r') as fichier:
    config = json.load(fichier)

token = config['token']
bot = commands.Bot(command_prefix='rp.')

@bot.event
async def on_ready():
    print("The Bot is started and launched !!!")
    print("Bot ID: " + str(bot.user.id))
    print("Bot Name: " + bot.user.name)

bot.run(token)