import discord
from discord.ext import commands
import json
import os
from discord.ext.commands import bot
with open("cmds/setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix= "k.", help_command = None)
@bot.event
async def on_ready():
    print('ready')
@bot.command()
async def load(ctx, extension):
    author = bot.get_user(730769863378862130)
    if ctx.author == author:
        bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'Loaded {extension}')
@bot.command()
async def unload(ctx, extension):
    author = bot.get_user(730769863378862130)
    if ctx.author == author:
        bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'Unloaded {extension}')
@bot.command()
async def reload(ctx, extension):
    author = bot.get_user(730769863378862130)
    if ctx.author == author:
        bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'Loaded {extension}')
for filename in os.listdir('cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
