import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
from core.classes import Cog_Extension
with open("./cmds/setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class poll(Cog_Extension):

    @commands.command()
    async def poll(self, ctx, test: str):
        await ctx.message.delete()
        poll = await ctx.send(test)
        emoji = '\N{THUMBS UP SIGN}'
        await poll.add_reaction(emoji)
        emoji2 = '\N{THUMBS DOWN SIGN}'
        await poll.add_reaction(emoji2)
    @commands.command()
    async def avatar(self,ctx):
        asset = ctx.author.avatar_url_as()
        embed=discord.Embed(title=f"{ctx.author}'s avatar")
        embed.set_thumbnail(url=asset)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(poll(bot))