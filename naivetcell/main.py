import discord
from discord.ext import commands
import json
import os
with open("cmds/setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix= "k.", help_command = None)
@bot.event
async def on_ready():
    print('ready')
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension}')
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension}')
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension}')
for filename in os.listdir('cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])