import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
with open("./cmds/setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class ping(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{ctx.message.author.mention}\nyou told me to;)')
        await ctx.send('for the real ping command, use k.trueping')
    @commands.command()
    async def trueping(self, ctx):
        embed=discord.Embed()
        embed.set_author(name=f"PONG! 'Hey! Is it {ctx.message.author} who broke my window with table tennis?'")
        embed.add_field(name="PING",value=f'{round(self.bot.latency*1000)} (ms)', inline=False)
        embed.set_footer(text="owo is op")
        await ctx.send(embed=embed)
    @commands.command()
    async def waifu(self, ctx):
        await ctx.send(jdata['waifu'])
def setup(bot):
    bot.add_cog(ping(bot))