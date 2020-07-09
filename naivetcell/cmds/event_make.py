import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
from core.classes import Cog_Extension
with open("./cmds/setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class event_make(Cog_Extension):
    @commands.command()
    async def event_make(self, ctx, title: str, info: str, time: str):
        embed=discord.Embed(title=f'new event-{title}')
        embed.add_field(name='info', value=f'{info}', inline=False)
        embed.add_field(name='time', value=time, inline=True)
        embed.set_footer(text='owo is op')
        await ctx.send(embed=embed)
        await ctx.message.delete()
        await ctx.send('@everyone')
def setup(bot):
    bot.add_cog(event_make(bot))